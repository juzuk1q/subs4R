import React, { useState } from 'react';
import type { ServiceSummary } from '../types';
import { Calculator, Check } from 'lucide-react';
import { ServiceLogo } from './ServiceLogo';

interface CalculatorViewProps {
  services: ServiceSummary[];
  currency: string;
  currencySymbol: string;
}

export const CalculatorView: React.FC<CalculatorViewProps> = ({
  services,
  currencySymbol,
}) => {
  const [selectedIds, setSelectedIds] = useState<string[]>([
    'youtube-premium',
    'spotify',
    'chatgpt-plus',
    'netflix',
  ]);

  const toggleService = (id: string) => {
    setSelectedIds((prev) =>
      prev.includes(id) ? prev.filter((item) => item !== id) : [...prev, id]
    );
  };

  const selectedServices = services.filter((s) => selectedIds.includes(s.id));

  // Суммируем базовые цены в США и цены в самых выгодных регионах
  const totalUS = selectedServices.reduce((acc, s) => acc + s.us_price, 0);
  const totalCheapest = selectedServices.reduce((acc, s) => acc + s.cheapest_price, 0);
  const monthlySavings = Math.max(0, totalUS - totalCheapest);
  const yearlySavings = monthlySavings * 12;
  const overallDiscount = totalUS > 0 ? ((monthlySavings / totalUS) * 100).toFixed(0) : 0;

  return (
    <div className="space-y-6">
      {/* Top Banner */}
      <div className="rounded-xl border border-sky-800/40 bg-gradient-to-r from-[#17202e] to-[#121824] p-6 shadow-xl">
        <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
          <div className="space-y-2 max-w-xl">
            <div className="flex items-center gap-2">
              <span className="p-2 rounded-lg bg-sky-500/10 text-sky-400 border border-sky-500/20">
                <Calculator className="w-5 h-5" />
              </span>
              <h2 className="text-xl font-bold text-white">Калькулятор подписочной выгоды</h2>
            </div>
            <p className="text-sm text-slate-300">
              Отметьте подписки, которыми вы пользуетесь регулярно, и узнайте, сколько денег вы сбережете за год, оформив их по региональным ценам.
            </p>
          </div>

          {/* Result Card */}
          <div className="w-full md:w-auto flex flex-col sm:flex-row items-center gap-4 bg-[#0d121c] p-4 rounded-xl border border-slate-700/80 shadow-lg">
            <div className="text-center sm:text-left">
              <div className="text-xs text-slate-400 uppercase tracking-wider font-semibold">
                Годовая экономия
              </div>
              <div className="text-2xl sm:text-3xl font-extrabold text-[#a4d007] font-mono">
                +{yearlySavings.toFixed(2)} {currencySymbol}
              </div>
              <div className="text-xs text-slate-400 mt-0.5">
                Скидка <strong className="text-emerald-400">~{overallDiscount}%</strong> от базовой стоимости
              </div>
            </div>

            <div className="hidden sm:block h-12 w-px bg-slate-800" />

            <div className="text-center sm:text-left text-xs space-y-1">
              <div className="text-slate-400">
                В США: <span className="line-through text-slate-500">{totalUS.toFixed(2)} {currencySymbol}/мес</span>
              </div>
              <div className="text-emerald-300 font-bold">
                В регионах: {totalCheapest.toFixed(2)} {currencySymbol}/мес
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Grid of Selectable Services */}
      <div>
        <div className="flex items-center justify-between mb-3">
          <h3 className="text-sm font-semibold text-slate-200">
            Выберите ваши сервисы ({selectedIds.length} выбрано):
          </h3>
          <div className="space-x-2">
            <button
              onClick={() => setSelectedIds(services.map((s) => s.id))}
              className="text-xs text-sky-400 hover:underline"
            >
              Выбрать все
            </button>
            <span className="text-slate-600">|</span>
            <button
              onClick={() => setSelectedIds([])}
              className="text-xs text-slate-400 hover:underline"
            >
              Снять все
            </button>
          </div>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3">
          {services.map((s) => {
            const isSelected = selectedIds.includes(s.id);
            return (
              <div
                key={s.id}
                onClick={() => toggleService(s.id)}
                className={`relative p-4 rounded-xl border cursor-pointer transition-all ${
                  isSelected
                    ? 'bg-[#1b2536] border-sky-500/80 shadow-lg shadow-sky-950/40'
                    : 'bg-[#121824] border-slate-800/80 hover:border-slate-700 opacity-70 hover:opacity-100'
                }`}
              >
                <div className="flex items-start justify-between">
                  <div className="flex items-center gap-2.5">
                    <ServiceLogo slug={s.slug} color={s.color} name={s.name} size="sm" />
                    <div>
                      <div className="text-sm font-bold text-white leading-snug">{s.name}</div>
                      <div className="text-[11px] text-slate-400">{s.category}</div>
                    </div>
                  </div>

                  <div
                    className={`w-5 h-5 rounded flex items-center justify-center border transition ${
                      isSelected
                        ? 'bg-sky-500 border-sky-400 text-white'
                        : 'border-slate-600 bg-slate-800'
                    }`}
                  >
                    {isSelected && <Check className="w-3.5 h-3.5 stroke-[3]" />}
                  </div>
                </div>

                <div className="mt-4 pt-3 border-t border-slate-800/60 flex items-center justify-between text-xs">
                  <div>
                    <span className="text-slate-500 line-through">
                      {s.us_price.toFixed(2)}
                    </span>
                    <span className="text-emerald-400 font-bold font-mono ml-1.5">
                      {s.cheapest_price.toFixed(2)} {currencySymbol}
                    </span>
                  </div>
                  <span className="font-mono text-[#a4d007] font-bold text-[11px] bg-[#3a4f0b] px-1.5 py-0.5 rounded">
                    -{s.max_discount.toFixed(0)}%
                  </span>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};
