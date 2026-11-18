import React, { useState, useEffect } from 'react';
import { X, ExternalLink, ShieldAlert, CheckCircle2, AlertTriangle, TrendingDown, Info, Activity } from 'lucide-react';
import { ServiceLogo } from '../ui/ServiceLogo';
import { Sparkline } from '../ui/Sparkline';
import { Flag } from '../ui/Flag';
import type { ServiceDetail, ServicePlan, PlanPrice } from '../../types';

interface ServiceDetailModalProps {
  serviceId: string | null;
  currency: string;
  currencySymbol: string;
  onClose: () => void;
}

export const ServiceDetailModal: React.FC<ServiceDetailModalProps> = ({
  serviceId,
  currency,
  currencySymbol,
  onClose,
}) => {
  const [detail, setDetail] = useState<ServiceDetail | null>(null);
  const [loading, setLoading] = useState(true);
  const [selectedPlanId, setSelectedPlanId] = useState<string>('');

  useEffect(() => {
    if (!serviceId) return;
    setLoading(true);
    fetch(`/api/services/${serviceId}?currency=${currency}`)
      .then((res) => res.json())
      .then((data: ServiceDetail) => {
        setDetail(data);
        if (data.plans && data.plans.length > 0) {
          setSelectedPlanId(data.plans[0].id);
        }
        setLoading(false);
      })
      .catch((err) => {
        console.error('Failed to load service detail:', err);
        setLoading(false);
      });
  }, [serviceId, currency]);

  if (!serviceId) return null;

  const currentPlan: ServicePlan | undefined = detail?.plans?.find(
    (p) => p.id === selectedPlanId
  ) || detail?.plans?.[0];

  const getDifficultyBadge = (difficulty: PlanPrice['payment_difficulty']) => {
    switch (difficulty) {
      case 'easy':
        return (
          <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded text-xs font-semibold bg-emerald-950/80 text-emerald-400 border border-emerald-800/60">
            <CheckCircle2 className="w-3 h-3" /> Легко (карты СНГ/мир)
          </span>
        );
      case 'medium':
        return (
          <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded text-xs font-semibold bg-amber-950/80 text-amber-300 border border-amber-800/60">
            <AlertTriangle className="w-3 h-3" /> Средне (виртуальные карты)
          </span>
        );
      case 'hard':
        return (
          <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded text-xs font-semibold bg-rose-950/80 text-rose-400 border border-rose-800/60">
            <ShieldAlert className="w-3 h-3" /> Сложно (местный ID/SMS)
          </span>
        );
      default:
        return null;
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm animate-in fade-in duration-200">
      <div 
        className="relative w-full max-w-5xl max-h-[92vh] flex flex-col rounded-xl border border-slate-700/80 bg-[#151c28] shadow-2xl overflow-hidden text-slate-200"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div className="flex items-center justify-between border-b border-slate-700/60 px-6 py-4 bg-[#1b2434]">
          <div className="flex items-center gap-3">
            <ServiceLogo
              slug={detail?.slug || ''}
              color={detail?.color || '#3b82f6'}
              name={detail?.name || 'Service'}
              size="lg"
            />
            <div>
              <div className="flex items-center gap-2">
                <h2 className="text-xl font-bold text-white tracking-wide">{detail?.name || 'Загрузка...'}</h2>
                <span className="px-2 py-0.5 rounded text-xs bg-slate-800 text-sky-400 border border-slate-700">
                  {detail?.category}
                </span>
              </div>
              <p className="text-xs text-slate-400 mt-0.5">{detail?.description}</p>
            </div>
          </div>

          <div className="flex items-center gap-2">
            {detail?.official_url && (
              <a
                href={detail.official_url}
                target="_blank"
                rel="noreferrer"
                className="hidden sm:flex items-center gap-1.5 px-3 py-1.5 rounded-md text-xs font-medium text-slate-300 bg-slate-800/80 hover:bg-slate-700 border border-slate-700 hover:text-white transition"
              >
                <span>Оф. сайт</span>
                <ExternalLink className="w-3.5 h-3.5" />
              </a>
            )}
            <button
              onClick={onClose}
              className="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition"
              title="Закрыть"
            >
              <X className="w-5 h-5" />
            </button>
          </div>
        </div>

        {/* Content Body */}
        <div className="overflow-y-auto flex-1 p-6 space-y-6">
          {loading ? (
            <div className="py-20 flex flex-col items-center justify-center space-y-3">
              <div className="w-8 h-8 border-4 border-sky-500 border-t-transparent rounded-full animate-spin"></div>
              <p className="text-sm text-slate-400">Получение региональных тарифов...</p>
            </div>
          ) : detail && (
            <>
              {/* Plan Tabs */}
              {detail.plans && detail.plans.length > 1 && (
                <div>
                  <div className="text-xs uppercase tracking-wider text-slate-400 font-semibold mb-2">
                    Выберите тарифный план:
                  </div>
                  <div className="flex flex-wrap gap-2">
                    {detail.plans.map((plan) => (
                      <button
                        key={plan.id}
                        onClick={() => setSelectedPlanId(plan.id)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition border ${
                          selectedPlanId === plan.id
                            ? 'bg-sky-600 text-white border-sky-500 shadow-lg shadow-sky-600/30'
                            : 'bg-slate-800/70 text-slate-300 border-slate-700 hover:bg-slate-800 hover:text-white'
                        }`}
                      >
                        {plan.name}
                        {plan.period && (
                          <span className="ml-1.5 text-xs opacity-75">
                            ({plan.period === 'month' ? '/мес' : '/год'})
                          </span>
                        )}
                      </button>
                    ))}
                  </div>
                  {currentPlan?.description && (
                    <p className="text-xs text-slate-400 mt-2 italic bg-slate-900/60 p-2.5 rounded border border-slate-800">
                      ℹ️ {currentPlan.description}
                    </p>
                  )}
                </div>
              )}

              {/* SteamDB-style Price Table */}
              <div>
                <div className="flex items-center justify-between mb-3">
                  <h3 className="text-sm font-semibold text-slate-200 flex items-center gap-1.5">
                    <TrendingDown className="w-4 h-4 text-emerald-400" />
                    <span>Цены по регионам мира</span>
                  </h3>
                  <span className="text-xs text-slate-400">
                    Пересчет в <strong className="text-sky-400">{currency} ({currencySymbol})</strong>
                  </span>
                </div>

                <div className="overflow-x-auto rounded-lg border border-slate-800 bg-[#0f141e]">
                  <table className="w-full text-left text-sm">
                    <thead>
                      <tr className="border-b border-slate-800 bg-[#18202d] text-xs font-semibold text-slate-400 uppercase tracking-wider">
                        <th className="py-3 px-4">Страна</th>
                        <th className="py-3 px-4">Статус</th>
                        <th className="py-3 px-4">Источник</th>
                        <th className="py-3 px-4">Оригинал</th>
                        <th className="py-3 px-4">В {currency}</th>
                        <th className="py-3 px-4">Выгода</th>
                        <th className="py-3 px-4 text-center">Тренд (6 мес)</th>
                        <th className="py-3 px-4">Оплата</th>
                        <th className="py-3 px-4">Заметки</th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-slate-800/60 font-sans text-xs">
                      {currentPlan?.prices.map((p, idx) => {
                        const isCheapest = idx === 0 && (p.status === 'available' || p.status === 'global_usd') && p.available !== false;
                        const isUS = p.country_code === 'US';
                        const isNotAvail = p.status === 'not_available' || p.available === false;
                        const isSuspended = p.status === 'suspended';
                        const isGlobal = p.status === 'global_usd';

                        const renderSourcePill = () => {
                          const tag = (() => {
                            switch (p.source) {
                              case 'official':
                                return <span className="px-1.5 py-0.5 rounded text-[10px] bg-emerald-950/80 text-emerald-300 border border-emerald-800/60">✓ Official</span>;
                              case 'store':
                                return <span className="px-1.5 py-0.5 rounded text-[10px] bg-sky-950/80 text-sky-300 border border-sky-800/60">🛒 Store</span>;
                              case 'usd_flat':
                                return <span className="px-1.5 py-0.5 rounded text-[10px] bg-indigo-950/80 text-indigo-300 border border-indigo-800/60">🌐 USD Flat</span>;
                              case 'community':
                                return <span className="px-1.5 py-0.5 rounded text-[10px] bg-amber-950/80 text-amber-300 border border-amber-800/60">👥 Community</span>;
                              case 'archive':
                                return <span className="px-1.5 py-0.5 rounded text-[10px] bg-slate-800 text-slate-300 border border-slate-700">📜 Archive</span>;
                              case 'estimated':
                                return <span className="px-1.5 py-0.5 rounded text-[10px] bg-purple-950/80 text-purple-300 border border-purple-800/60">📊 Estimated</span>;
                              default:
                                return <span className="px-1.5 py-0.5 rounded text-[10px] bg-slate-800 text-slate-400">{p.source || 'Curated'}</span>;
                            }
                          })();

                          if (p.source_url) {
                            return (
                              <a
                                href={p.source_url}
                                target="_blank"
                                rel="noreferrer"
                                title={`Источник: ${p.source_url} (Дата: ${p.source_date || 'н/д'})`}
                                className="inline-flex items-center gap-1 hover:opacity-80 transition"
                              >
                                {tag}
                                <ExternalLink className="w-2.5 h-2.5 text-slate-500" />
                              </a>
                            );
                          }
                          return tag;
                        };

                        return (
                          <tr
                            key={p.country_code}
                            className={`hover:bg-slate-800/40 transition ${
                              isCheapest ? 'bg-emerald-950/20' : ''
                            }`}
                          >
                            <td className="py-3 px-4 whitespace-nowrap">
                              <div className="flex items-center gap-2.5">
                                <Flag emoji={p.flag} code={p.country_code} />
                                <span className="font-medium text-slate-200">
                                  {p.country_name}
                                </span>
                                {isCheapest && (
                                  <span className="px-1.5 py-0.5 text-[9px] uppercase font-bold tracking-wider rounded bg-emerald-500/20 text-emerald-400 border border-emerald-500/40">
                                    Лучшая
                                  </span>
                                )}
                              </div>
                            </td>

                            <td className="py-3 px-4 whitespace-nowrap">
                              {isSuspended ? (
                                <span className="px-2 py-0.5 rounded text-[10px] font-semibold bg-rose-950/80 text-rose-300 border border-rose-800/50">
                                  🔒 {p.status_label || 'Приостановлен'}
                                </span>
                              ) : isNotAvail ? (
                                <span className="px-2 py-0.5 rounded text-[10px] font-semibold bg-slate-800 text-slate-400 border border-slate-700">
                                  🚫 {p.status_label || 'Не запущен'}
                                </span>
                              ) : isGlobal ? (
                                <span className="px-2 py-0.5 rounded text-[10px] font-semibold bg-indigo-950/80 text-indigo-300 border border-indigo-800/50">
                                  🌐 Global $
                                </span>
                              ) : (
                                <span className="px-2 py-0.5 rounded text-[10px] font-semibold bg-emerald-950/60 text-emerald-300 border border-emerald-800/40">
                                  ✓ Доступен
                                </span>
                              )}
                            </td>

                            <td className="py-3 px-4 whitespace-nowrap">
                              {renderSourcePill()}
                            </td>

                            <td className="py-3 px-4 font-mono text-slate-300 whitespace-nowrap">
                              <span className={isSuspended ? 'line-through text-slate-500' : ''}>
                                {p.original_price.toLocaleString()} {p.symbol}
                              </span>
                            </td>

                            <td className="py-3 px-4 whitespace-nowrap">
                              <div>
                                <span className={`font-mono font-bold text-sm ${isSuspended ? 'line-through text-slate-500' : 'text-white'}`}>
                                  {p.target_price.toFixed(2)} {currencySymbol}
                                </span>
                                <span className="text-[11px] text-slate-400 ml-1 font-mono">
                                  (~${p.converted_price_usd.toFixed(2)})
                                </span>
                              </div>
                            </td>

                            <td className="py-3 px-4 whitespace-nowrap">
                              {isUS ? (
                                <span className="text-slate-400 font-mono">База (0%)</span>
                              ) : p.discount_percent > 0 ? (
                                <span className="inline-flex items-center px-2 py-0.5 rounded font-mono font-bold text-xs bg-[#5c7e10] text-[#a4d007] border border-[#759e14]">
                                  -{p.discount_percent.toFixed(0)}%
                                </span>
                              ) : (
                                <span className="text-rose-400 font-mono">
                                  +{(Math.abs(p.discount_percent)).toFixed(0)}%
                                </span>
                              )}
                            </td>

                            <td className="py-3 px-4 text-center whitespace-nowrap">
                              <Sparkline data={p.price_history} />
                            </td>

                            <td className="py-3 px-4 whitespace-nowrap">
                              {getDifficultyBadge(p.payment_difficulty)}
                            </td>

                            <td className="py-3 px-4 text-[11px] text-slate-400 max-w-xs">
                              {p.payment_notes}
                            </td>
                          </tr>
                        );
                      })}
                    </tbody>
                  </table>
                </div>
              </div>

              {/* Guide / Tips */}
              {detail.guide && (
                <div className="rounded-xl border border-sky-900/50 bg-sky-950/20 p-4">
                  <div className="flex items-start gap-3">
                    <Info className="w-5 h-5 text-sky-400 shrink-0 mt-0.5" />
                    <div>
                      <h4 className="text-sm font-semibold text-sky-300">
                        Гайд и особенности подключения {detail.name}
                      </h4>
                      <p className="text-xs text-slate-300 mt-1 leading-relaxed">
                        {detail.guide}
                      </p>
                    </div>
                  </div>
                </div>
              )}
            </>
          )}
        </div>

        {/* Footer */}
        <div className="border-t border-slate-700/60 px-6 py-3.5 bg-[#1b2434] flex flex-col sm:flex-row items-center justify-between gap-2 text-xs text-slate-400">
          <div className="flex items-center gap-2">
            <Activity className="w-4 h-4 text-emerald-400" />
            <span>Цены валидируются с официальных витрин магазинов (Microsoft Store, Steam, Apple)</span>
          </div>
          <button
            onClick={onClose}
            className="px-4 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 font-medium transition"
          >
            Закрыть
          </button>
        </div>
      </div>
    </div>
  );
};
