import React from 'react';
import { Database, Grid, Table, Calculator, PlusCircle, Coins } from 'lucide-react';

interface NavbarProps {
  activeTab: 'table' | 'matrix' | 'calc';
  setActiveTab: (tab: 'table' | 'matrix' | 'calc') => void;
  currency: string;
  setCurrency: (c: string) => void;
  onOpenSuggest: () => void;
}

export const CURRENCIES = [
  { code: 'USD', symbol: '$', label: 'USD ($)' },
  { code: 'RUB', symbol: '₽', label: 'RUB (₽)' },
  { code: 'EUR', symbol: '€', label: 'EUR (€)' },
  { code: 'KZT', symbol: '₸', label: 'KZT (₸)' },
  { code: 'TRY', symbol: '₺', label: 'TRY (₺)' },
  { code: 'UAH', symbol: '₴', label: 'UAH (₴)' },
  { code: 'PLN', symbol: 'zł', label: 'PLN (zł)' },
  { code: 'GBP', symbol: '£', label: 'GBP (£)' },
];

export const Navbar: React.FC<NavbarProps> = ({
  activeTab,
  setActiveTab,
  currency,
  setCurrency,
  onOpenSuggest,
}) => {
  return (
    <header className="sticky top-0 z-40 w-full border-b border-slate-800 bg-[#101722]/95 backdrop-blur-md">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <div className="flex items-center gap-6">
            <div 
              onClick={() => setActiveTab('table')}
              className="flex items-center gap-2.5 cursor-pointer group"
            >
              <div className="w-9 h-9 rounded-lg bg-gradient-to-tr from-sky-600 to-cyan-400 flex items-center justify-center text-white shadow-lg shadow-sky-600/25 group-hover:scale-105 transition">
                <Database className="w-5 h-5" />
              </div>
              <div className="flex flex-col">
                <span className="font-black text-lg text-white tracking-wider font-mono flex items-center gap-1">
                  SUB<span className="text-sky-400">DB</span>
                  <span className="text-[10px] text-slate-400 font-sans font-bold px-1.5 py-0.5 rounded bg-slate-800 border border-slate-700">
                    .INFO
                  </span>
                </span>
                <span className="text-[10px] text-slate-400 uppercase tracking-widest -mt-1 font-semibold">
                  Global Service Prices
                </span>
              </div>
            </div>

            {/* Navigation Tabs */}
            <nav className="hidden md:flex items-center gap-1 bg-[#17212f] p-1 rounded-lg border border-slate-800">
              <button
                onClick={() => setActiveTab('table')}
                className={`flex items-center gap-2 px-3.5 py-1.5 rounded-md text-xs font-semibold transition ${
                  activeTab === 'table'
                    ? 'bg-sky-600 text-white shadow-md'
                    : 'text-slate-400 hover:text-white hover:bg-slate-800/60'
                }`}
              >
                <Table className="w-3.5 h-3.5" />
                <span>Все сервисы</span>
              </button>

              <button
                onClick={() => setActiveTab('matrix')}
                className={`flex items-center gap-2 px-3.5 py-1.5 rounded-md text-xs font-semibold transition ${
                  activeTab === 'matrix'
                    ? 'bg-sky-600 text-white shadow-md'
                    : 'text-slate-400 hover:text-white hover:bg-slate-800/60'
                }`}
              >
                <Grid className="w-3.5 h-3.5" />
                <span>Матрица стран</span>
              </button>

              <button
                onClick={() => setActiveTab('calc')}
                className={`flex items-center gap-2 px-3.5 py-1.5 rounded-md text-xs font-semibold transition ${
                  activeTab === 'calc'
                    ? 'bg-sky-600 text-white shadow-md'
                    : 'text-slate-400 hover:text-white hover:bg-slate-800/60'
                }`}
              >
                <Calculator className="w-3.5 h-3.5" />
                <span>Калькулятор</span>
              </button>
            </nav>
          </div>

          {/* Right Controls */}
          <div className="flex items-center gap-3">
            {/* Currency Selector */}
            <div className="flex items-center gap-1.5 bg-[#17212f] px-2.5 py-1.5 rounded-lg border border-slate-800">
              <Coins className="w-3.5 h-3.5 text-amber-400" />
              <select
                value={currency}
                onChange={(e) => setCurrency(e.target.value)}
                className="bg-transparent text-xs font-bold text-slate-200 focus:outline-none cursor-pointer"
              >
                {CURRENCIES.map((c) => (
                  <option key={c.code} value={c.code} className="bg-[#17212f] text-white">
                    {c.label}
                  </option>
                ))}
              </select>
            </div>

            {/* Suggest Price Button */}
            <button
              onClick={onOpenSuggest}
              className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold bg-emerald-600/20 hover:bg-emerald-600/30 text-emerald-300 border border-emerald-600/40 transition shadow-sm"
            >
              <PlusCircle className="w-3.5 h-3.5" />
              <span className="hidden sm:inline">Предложить цену</span>
            </button>
          </div>
        </div>

        {/* Mobile Navigation bar */}
        <div className="flex md:hidden items-center justify-around py-2 border-t border-slate-800/60">
          <button
            onClick={() => setActiveTab('table')}
            className={`flex items-center gap-1.5 text-xs font-medium py-1 px-2.5 rounded ${
              activeTab === 'table' ? 'text-sky-400 font-bold' : 'text-slate-400'
            }`}
          >
            <Table className="w-3.5 h-3.5" />
            <span>Сервисы</span>
          </button>
          <button
            onClick={() => setActiveTab('matrix')}
            className={`flex items-center gap-1.5 text-xs font-medium py-1 px-2.5 rounded ${
              activeTab === 'matrix' ? 'text-sky-400 font-bold' : 'text-slate-400'
            }`}
          >
            <Grid className="w-3.5 h-3.5" />
            <span>Матрица</span>
          </button>
          <button
            onClick={() => setActiveTab('calc')}
            className={`flex items-center gap-1.5 text-xs font-medium py-1 px-2.5 rounded ${
              activeTab === 'calc' ? 'text-sky-400 font-bold' : 'text-slate-400'
            }`}
          >
            <Calculator className="w-3.5 h-3.5" />
            <span>Калькулятор</span>
          </button>
        </div>
      </div>
    </header>
  );
};
