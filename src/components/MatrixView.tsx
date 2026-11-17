import React, { useEffect, useState } from 'react';
import type { MatrixRow } from '../types';
import { ServiceLogo } from './ServiceLogo';
import { Flag } from './Flag';
import { RefreshCw } from 'lucide-react';

interface MatrixViewProps {
  currency: string;
  currencySymbol: string;
  onSelectService: (serviceId: string) => void;
}

const MATRIX_COUNTRIES = [
  { code: 'TR', name: 'Турция', flag: '🇹🇷' },
  { code: 'NG', name: 'Нигерия', flag: '🇳🇬' },
  { code: 'IN', name: 'Индия', flag: '🇮🇳' },
  { code: 'KZ', name: 'Казахстан', flag: '🇰🇿' },
  { code: 'UA', name: 'Украина', flag: '🇺🇦' },
  { code: 'AR', name: 'Аргентина', flag: '🇦🇷' },
  { code: 'PL', name: 'Польша', flag: '🇵🇱' },
  { code: 'US', name: 'США (База)', flag: '🇺🇸' },
];

export const MatrixView: React.FC<MatrixViewProps> = ({
  currency,
  currencySymbol,
  onSelectService,
}) => {
  const [rows, setRows] = useState<MatrixRow[]>([]);
  const [loading, setLoading] = useState(true);
  const [syncing, setSyncing] = useState(false);

  const fetchMatrix = () => {
    setLoading(true);
    fetch(`/api/matrix?currency=${currency}`)
      .then((res) => res.json())
      .then((data: MatrixRow[]) => {
        setRows(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error('Failed to load matrix:', err);
        setLoading(false);
      });
  };

  useEffect(() => {
    fetchMatrix();
  }, [currency]);

  const handleSyncNow = async () => {
    setSyncing(true);
    try {
      await fetch('/api/sync', { method: 'POST' });
      setTimeout(() => {
        fetchMatrix();
        setSyncing(false);
      }, 1500);
    } catch {
      setSyncing(false);
    }
  };

  if (loading) {
    return (
      <div className="py-24 flex flex-col items-center justify-center space-y-3">
        <div className="w-8 h-8 border-4 border-sky-500 border-t-transparent rounded-full animate-spin"></div>
        <p className="text-sm text-slate-400">Формирование матрицы цен...</p>
      </div>
    );
  }

  return (
    <div className="space-y-4">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 bg-[#17202e] p-4 rounded-xl border border-slate-800 shadow-md">
        <div>
          <h2 className="text-base font-bold text-white flex items-center gap-2">
            <span>🌐 Матрица региональных цен</span>
            <span className="px-2 py-0.5 rounded text-xs bg-sky-950 text-sky-400 border border-sky-800">
              Live Matrix
            </span>
          </h2>
          <p className="text-xs text-slate-400 mt-0.5">
            Сводное сравнение базовых тарифов. Зеленым выделена лучшая мировая цена.
          </p>
        </div>

        <div className="flex items-center gap-3">
          <button
            onClick={handleSyncNow}
            disabled={syncing}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white border border-slate-700 transition"
          >
            <RefreshCw className={`w-3.5 h-3.5 ${syncing ? 'animate-spin text-sky-400' : ''}`} />
            <span>{syncing ? 'Синхронизация...' : 'Обновить цены'}</span>
          </button>

          <div className="text-xs text-slate-400">
            Валюта: <strong className="text-sky-400">{currency} ({currencySymbol})</strong>
          </div>
        </div>
      </div>

      <div className="overflow-x-auto rounded-xl border border-slate-800 bg-[#0f141e] shadow-xl">
        <table className="w-full text-left text-sm">
          <thead>
            <tr className="border-b border-slate-800 bg-[#151c28] text-xs font-semibold text-slate-400">
              <th className="py-3 px-4 min-w-[200px]">Сервис</th>
              {MATRIX_COUNTRIES.map((c) => (
                <th key={c.code} className="py-3 px-3 text-center whitespace-nowrap">
                  <div className="flex items-center justify-center gap-1.5">
                    <Flag emoji={c.flag} code={c.code} />
                    <span>{c.code}</span>
                  </div>
                  <div className="text-[10px] text-slate-400 font-normal">{c.name}</div>
                </th>
              ))}
              <th className="py-3 px-4 text-center">Макс. выгода</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-800/60 font-mono text-xs">
            {rows.map((row) => (
              <tr
                key={row.service_id}
                onClick={() => onSelectService(row.service_id)}
                className="hover:bg-slate-800/50 cursor-pointer transition group"
              >
                <td className="py-3 px-4 font-sans font-medium text-slate-200">
                  <div className="flex items-center gap-2.5">
                    <ServiceLogo slug={row.service_id} name={row.service_name} size="sm" />
                    <div>
                      <div className="font-semibold text-white group-hover:text-sky-400 transition">
                        {row.service_name}
                      </div>
                      <span className="text-[10px] text-slate-400">
                        {row.category}
                      </span>
                    </div>
                  </div>
                </td>

                {MATRIX_COUNTRIES.map((c) => {
                  const price = row.prices?.[c.code];
                  const status = row.statuses?.[c.code];
                  const isBest = row.best_country === c.code && status === 'available';

                  if (status === 'not_available' || price === undefined) {
                    return (
                      <td key={c.code} className="py-3 px-3 text-center">
                        <span className="inline-block px-1.5 py-0.5 rounded text-[10px] font-sans font-medium bg-slate-900/80 text-slate-500 border border-slate-800">
                          Не запущен
                        </span>
                      </td>
                    );
                  }

                  if (status === 'global_usd') {
                    return (
                      <td key={c.code} className="py-3 px-3 text-center whitespace-nowrap">
                        <div className="flex flex-col items-center">
                          <span className="font-semibold text-indigo-300">
                            {price.toFixed(2)} {currencySymbol}
                          </span>
                          <span className="text-[9px] font-sans px-1 rounded bg-indigo-950/70 text-indigo-400 border border-indigo-800/40 mt-0.5">
                            Global $
                          </span>
                        </div>
                      </td>
                    );
                  }

                  if (status === 'suspended') {
                    return (
                      <td key={c.code} className="py-3 px-3 text-center">
                        <span className="inline-block px-1.5 py-0.5 rounded text-[10px] font-sans font-medium bg-rose-950/60 text-rose-400 border border-rose-800/50">
                          Приостановлен
                        </span>
                      </td>
                    );
                  }

                  return (
                    <td
                      key={c.code}
                      className={`py-3 px-3 text-center whitespace-nowrap transition ${
                        isBest ? 'bg-emerald-950/40 text-emerald-300 font-bold' : 'text-slate-300'
                      }`}
                    >
                      {price.toFixed(2)} {currencySymbol}
                    </td>
                  );
                })}

                <td className="py-3 px-4 text-center whitespace-nowrap">
                  {row.max_discount > 0 ? (
                    <span className="inline-flex items-center px-2 py-0.5 rounded font-mono font-bold text-xs bg-[#5c7e10] text-[#a4d007] border border-[#759e14]">
                      -{row.max_discount.toFixed(0)}%
                    </span>
                  ) : (
                    <span className="text-slate-500 text-xs">0%</span>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
