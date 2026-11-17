import { useState, useEffect } from 'react';
import {
  Search,
  ArrowUpDown,
  TrendingDown,
  Sparkles,
  ChevronRight,
} from 'lucide-react';
import { Navbar, CURRENCIES } from './components/layout/Navbar';
import { ServiceDetailModal } from './components/modals/ServiceDetailModal';
import { SuggestModal } from './components/modals/SuggestModal';
import { MatrixView } from './views/MatrixView';
import { CalculatorView } from './views/CalculatorView';
import { ServiceLogo } from './components/ui/ServiceLogo';
import { Flag } from './components/ui/Flag';
import type { ServiceSummary } from './types';

const COUNTRY_NAME_TO_CODE: Record<string, string> = {
  Nigeria: 'NG',
  Turkey: 'TR',
  Argentina: 'AR',
  India: 'IN',
  Kazakhstan: 'KZ',
  Ukraine: 'UA',
  Brazil: 'BR',
  Poland: 'PL',
  'United States': 'US',
  Eurozone: 'EU',
  'United Kingdom': 'GB',
  Egypt: 'EG',
  Philippines: 'PH',
  Japan: 'JP',
  Russia: 'RU',
};

const CATEGORIES = [
  { id: 'all', label: 'Все категории' },
  { id: 'AI & Software', label: '🤖 AI & Нейросети' },
  { id: 'Music', label: '🎵 Музыка' },
  { id: 'Design', label: '🎨 Дизайн' },
  { id: 'Productivity', label: '💼 Для работы' },
  { id: 'Streaming Video', label: '🎬 Видео' },
  { id: 'Gaming', label: '🎮 Игры' },
  { id: 'Software & Tools', label: '🛠 Софт & Утилиты' },
];

export function App() {
  const [activeTab, setActiveTab] = useState<'table' | 'matrix' | 'calc'>('table');
  const [currency, setCurrency] = useState<string>('USD');
  const [search, setSearch] = useState<string>('');
  const [category, setCategory] = useState<string>('all');
  const [sortBy, setSortBy] = useState<string>('discount'); // discount, price_asc, popularity, name

  const [services, setServices] = useState<ServiceSummary[]>([]);
  const [loading, setLoading] = useState<boolean>(true);

  const [selectedServiceId, setSelectedServiceId] = useState<string | null>(null);
  const [isSuggestOpen, setIsSuggestOpen] = useState<boolean>(false);

  const currentCurrencySymbol =
    CURRENCIES.find((c) => c.code === currency)?.symbol || '$';

  const fetchServices = () => {
    setLoading(true);
    const query = new URLSearchParams({
      currency,
      category,
      search,
      sort: sortBy,
    });

    fetch(`/api/services?${query.toString()}`)
      .then((res) => res.json())
      .then((data: ServiceSummary[]) => {
        setServices(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error('Error fetching services:', err);
        setLoading(false);
      });
  };

  useEffect(() => {
    fetchServices();
  }, [currency, category, sortBy]);

  // Debounced search
  useEffect(() => {
    const timer = setTimeout(() => {
      fetchServices();
    }, 250);
    return () => clearTimeout(timer);
  }, [search]);

  return (
    <div className="min-h-screen bg-[#0d121a] text-slate-200 flex flex-col font-sans selection:bg-sky-500 selection:text-white">
      {/* Top Navigation */}
      <Navbar
        activeTab={activeTab}
        setActiveTab={setActiveTab}
        currency={currency}
        setCurrency={setCurrency}
        onOpenSuggest={() => setIsSuggestOpen(true)}
      />

      {/* Main Container */}
      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6 space-y-6">
        {/* SteamDB-style Banner */}
        <div className="relative overflow-hidden rounded-2xl border border-slate-800 bg-gradient-to-b from-[#1b2536] via-[#141b27] to-[#0f141e] p-6 shadow-2xl">
          <div className="relative z-10 flex flex-col lg:flex-row items-start lg:items-center justify-between gap-6">
            <div className="space-y-2 max-w-2xl">
              <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider bg-sky-500/10 text-sky-400 border border-sky-500/20">
                <Sparkles className="w-3.5 h-3.5" />
                <span>База региональных цен подписок & сервисов</span>
              </div>
              <h1 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
                Где дешевле: YouTube, Spotify, ChatGPT, Netflix и игры
              </h1>
              <p className="text-sm text-slate-300 leading-relaxed">
                Сравнение официальных цен в Турции 🇹🇷, Нигерии 🇳🇬, Аргентине 🇦🇷, Индии 🇮🇳, Казахстане 🇰🇿 и других странах с конвертацией в реальном времени.
              </p>
            </div>

            {/* Quick Stat Pill Widgets */}
            <div className="grid grid-cols-2 sm:grid-cols-3 gap-3 w-full lg:w-auto">
              <div className="bg-[#0f1521] border border-slate-800/80 p-3.5 rounded-xl">
                <div className="text-[11px] text-slate-400 uppercase font-semibold">Макс. выгода</div>
                <div className="text-xl font-extrabold text-[#a4d007] font-mono mt-0.5">до -92%</div>
                <div className="text-[10px] text-slate-500">в Турции / Нигерии</div>
              </div>

              <div className="bg-[#0f1521] border border-slate-800/80 p-3.5 rounded-xl">
                <div className="text-[11px] text-slate-400 uppercase font-semibold">Сервисов</div>
                <div className="text-xl font-extrabold text-sky-400 font-mono mt-0.5">{services.length || 12} шт</div>
                <div className="text-[10px] text-slate-500">проверено вручную</div>
              </div>

              <div className="bg-[#0f1521] border border-slate-800/80 p-3.5 rounded-xl col-span-2 sm:col-span-1">
                <div className="text-[11px] text-slate-400 uppercase font-semibold">Валюта</div>
                <div className="text-xl font-extrabold text-amber-400 font-mono mt-0.5">{currency}</div>
                <div className="text-[10px] text-slate-500">живая конвертация</div>
              </div>
            </div>
          </div>
        </div>

        {/* Tab: Table View */}
        {activeTab === 'table' && (
          <div className="space-y-4">
            {/* Filter & Search Bar */}
            <div className="flex flex-col md:flex-row gap-3 items-stretch md:items-center justify-between bg-[#121926] p-3 rounded-xl border border-slate-800">
              {/* Categories */}
              <div className="flex items-center gap-1.5 overflow-x-auto pb-1 md:pb-0 scrollbar-none">
                {CATEGORIES.map((cat) => (
                  <button
                    key={cat.id}
                    onClick={() => setCategory(cat.id)}
                    className={`px-3 py-1.5 rounded-lg text-xs font-semibold whitespace-nowrap transition ${
                      category === cat.id
                        ? 'bg-sky-600 text-white shadow-md'
                        : 'bg-[#182130] text-slate-400 hover:text-white hover:bg-slate-800'
                    }`}
                  >
                    {cat.label}
                  </button>
                ))}
              </div>

              {/* Search & Sort */}
              <div className="flex items-center gap-2">
                <div className="relative flex-1 md:w-64">
                  <Search className="w-4 h-4 text-slate-500 absolute left-3 top-2.5" />
                  <input
                    type="text"
                    value={search}
                    onChange={(e) => setSearch(e.target.value)}
                    placeholder="Поиск сервиса..."
                    className="w-full bg-[#0a0e16] border border-slate-700/80 rounded-lg pl-9 pr-3 py-1.5 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-sky-500"
                  />
                  {search && (
                    <button
                      onClick={() => setSearch('')}
                      className="absolute right-2.5 top-2 text-xs text-slate-400 hover:text-white"
                    >
                      ✕
                    </button>
                  )}
                </div>

                <div className="flex items-center gap-1.5 bg-[#0a0e16] border border-slate-700/80 px-2 py-1.5 rounded-lg">
                  <ArrowUpDown className="w-3.5 h-3.5 text-slate-400" />
                  <select
                    value={sortBy}
                    onChange={(e) => setSortBy(e.target.value)}
                    className="bg-transparent text-xs text-slate-300 font-medium focus:outline-none cursor-pointer"
                  >
                    <option value="discount" className="bg-[#17212f]">
                      Сначала с макс. выгодой
                    </option>
                    <option value="price_asc" className="bg-[#17212f]">
                      Сначала дешевые
                    </option>
                    <option value="popularity" className="bg-[#17212f]">
                      По популярности
                    </option>
                    <option value="name" className="bg-[#17212f]">
                      По алфавиту
                    </option>
                  </select>
                </div>
              </div>
            </div>

            {/* SteamDB-style Services Table */}
            <div className="overflow-hidden rounded-xl border border-slate-800 bg-[#0f141e] shadow-xl">
              <div className="overflow-x-auto">
                <table className="w-full text-left text-sm">
                  <thead>
                    <tr className="border-b border-slate-800 bg-[#151c28] text-xs font-semibold text-slate-400 uppercase tracking-wider">
                      <th className="py-3 px-4 w-12 text-center">#</th>
                      <th className="py-3 px-4">Сервис</th>
                      <th className="py-3 px-4">Тариф</th>
                      <th className="py-3 px-4">Самая дешевая страна</th>
                      <th className="py-3 px-4">В {currency}</th>
                      <th className="py-3 px-4">В США</th>
                      <th className="py-3 px-4 text-center">Скидка / Выгода</th>
                      <th className="py-3 px-4 text-right">Детали</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-800/60">
                    {loading ? (
                      <tr>
                        <td colSpan={8} className="py-16 text-center text-slate-500">
                          <div className="flex flex-col items-center justify-center space-y-2">
                            <div className="w-7 h-7 border-3 border-sky-500 border-t-transparent rounded-full animate-spin"></div>
                            <span className="text-xs">Загрузка цен...</span>
                          </div>
                        </td>
                      </tr>
                    ) : services.length === 0 ? (
                      <tr>
                        <td colSpan={8} className="py-12 text-center text-slate-500 text-xs">
                          Ничего не найдено по запросу «{search}».
                        </td>
                      </tr>
                    ) : (
                      services.map((s, idx) => (
                        <tr
                          key={s.id}
                          onClick={() => setSelectedServiceId(s.id)}
                          className="hover:bg-slate-800/40 cursor-pointer transition group"
                        >
                          <td className="py-3.5 px-4 text-center font-mono text-xs text-slate-500">
                            {idx + 1}
                          </td>

                          <td className="py-3.5 px-4 whitespace-nowrap">
                            <div className="flex items-center gap-3">
                              <ServiceLogo slug={s.slug} color={s.color} name={s.name} size="md" />
                              <div>
                                <div className="font-bold text-white group-hover:text-sky-400 transition flex items-center gap-1.5">
                                  <span>{s.name}</span>
                                </div>
                                <div className="text-[11px] text-slate-400">{s.category}</div>
                              </div>
                            </div>
                          </td>

                          <td className="py-3.5 px-4 whitespace-nowrap text-xs text-slate-300 font-medium">
                            <span className="px-2 py-0.5 rounded bg-slate-800/80 border border-slate-700/60">
                              {s.default_plan_name}
                            </span>
                          </td>

                          <td className="py-3.5 px-4 whitespace-nowrap">
                            <div className="flex items-center gap-2">
                              <Flag
                                emoji={s.cheapest_flag}
                                code={COUNTRY_NAME_TO_CODE[s.cheapest_country] || 'US'}
                              />
                              <span className="font-semibold text-slate-200 text-xs">
                                {s.cheapest_country}
                              </span>
                            </div>
                          </td>

                          <td className="py-3.5 px-4 whitespace-nowrap">
                            <span className="font-mono font-bold text-emerald-400 text-base">
                              {s.cheapest_price.toFixed(2)} {currentCurrencySymbol}
                            </span>
                            <span className="text-[11px] text-slate-500 ml-1">/мес</span>
                          </td>

                          <td className="py-3.5 px-4 whitespace-nowrap font-mono text-xs text-slate-400">
                            {s.us_price.toFixed(2)} {currentCurrencySymbol}
                          </td>

                          <td className="py-3.5 px-4 text-center whitespace-nowrap">
                            {s.max_discount > 0 ? (
                              <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded font-mono font-bold text-xs bg-[#5c7e10] text-[#a4d007] border border-[#759e14] shadow-sm">
                                <TrendingDown className="w-3 h-3" />
                                -{s.max_discount.toFixed(0)}%
                              </span>
                            ) : (
                              <span className="text-xs text-slate-500">—</span>
                            )}
                          </td>

                          <td className="py-3.5 px-4 text-right whitespace-nowrap">
                            <button
                              onClick={(e) => {
                                e.stopPropagation();
                                setSelectedServiceId(s.id);
                              }}
                              className="inline-flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 hover:bg-sky-600 text-slate-300 hover:text-white border border-slate-700 hover:border-sky-500 transition shadow-sm"
                            >
                              <span>Сравнить</span>
                              <ChevronRight className="w-3.5 h-3.5" />
                            </button>
                          </td>
                        </tr>
                      ))
                    )}
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        )}

        {/* Tab: Matrix View */}
        {activeTab === 'matrix' && (
          <MatrixView
            currency={currency}
            currencySymbol={currentCurrencySymbol}
            onSelectService={(id) => setSelectedServiceId(id)}
          />
        )}

        {/* Tab: Calculator View */}
        {activeTab === 'calc' && (
          <CalculatorView
            services={services}
            currency={currency}
            currencySymbol={currentCurrencySymbol}
          />
        )}
      </main>

      {/* Footer */}
      <footer className="border-t border-slate-800/80 bg-[#0b0f17] py-6 mt-12 text-center text-xs text-slate-500">
        <div className="max-w-7xl mx-auto px-4 space-y-2">
          <p className="font-semibold text-slate-400">
            SubDB.info — Независимая база региональных цен сервисов и подписок. Вдохновлено SteamDB.
          </p>
          <p className="text-[11px] text-slate-600">
            Все товарные знаки и логотипы являются собственностью их владельцев. Цены носят информационный характер.
          </p>
        </div>
      </footer>

      {/* Modal: Service Detail */}
      <ServiceDetailModal
        serviceId={selectedServiceId}
        currency={currency}
        currencySymbol={currentCurrencySymbol}
        onClose={() => setSelectedServiceId(null)}
      />

      {/* Modal: Suggest Price */}
      {isSuggestOpen && (
        <SuggestModal
          services={services}
          onClose={() => setIsSuggestOpen(false)}
        />
      )}
    </div>
  );
}

export default App;
