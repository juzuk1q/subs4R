import React, { useState } from 'react';
import { X, Send, CheckCircle2 } from 'lucide-react';
import type { ServiceSummary } from '../types';

interface SuggestModalProps {
  services: ServiceSummary[];
  onClose: () => void;
}

export const SuggestModal: React.FC<SuggestModalProps> = ({ services, onClose }) => {
  const [serviceId, setServiceId] = useState(services[0]?.id || '');
  const [countryCode, setCountryCode] = useState('TR');
  const [planName, setPlanName] = useState('Individual');
  const [price, setPrice] = useState('');
  const [currency, setCurrency] = useState('TRY');
  const [notes, setNotes] = useState('');
  const [contact, setContact] = useState('');
  const [status, setStatus] = useState<'idle' | 'submitting' | 'success'>('idle');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!price || isNaN(Number(price))) return;

    setStatus('submitting');
    try {
      const res = await fetch('/api/suggest', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          service_id: serviceId,
          country_code: countryCode,
          plan_name: planName,
          proposed_price: parseFloat(price),
          currency,
          notes,
          user_contact: contact,
        }),
      });

      if (res.ok) {
        setStatus('success');
        setTimeout(() => {
          onClose();
        }, 1800);
      } else {
        setStatus('idle');
      }
    } catch (err) {
      console.error(err);
      setStatus('idle');
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm animate-in fade-in">
      <div className="relative w-full max-w-lg rounded-xl border border-slate-700 bg-[#151c28] p-6 shadow-2xl text-slate-200">
        <button
          onClick={onClose}
          className="absolute right-4 top-4 p-1 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800"
        >
          <X className="w-5 h-5" />
        </button>

        <h3 className="text-lg font-bold text-white mb-1 flex items-center gap-2">
          <span>📝 Предложить актуальную цену</span>
        </h3>
        <p className="text-xs text-slate-400 mb-5">
          Заметили изменение тарифа или знаете новый выгодный регион? Поделитесь с сообществом!
        </p>

        {status === 'success' ? (
          <div className="py-8 text-center space-y-2">
            <CheckCircle2 className="w-12 h-12 text-emerald-400 mx-auto" />
            <h4 className="text-base font-bold text-white">Спасибо!</h4>
            <p className="text-xs text-slate-300">
              Ваше предложение отправлено на верификацию и скоро появится в базе.
            </p>
          </div>
        ) : (
          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="block text-xs font-semibold text-slate-300 mb-1">Сервис</label>
              <select
                value={serviceId}
                onChange={(e) => setServiceId(e.target.value)}
                className="w-full bg-[#0d121c] border border-slate-700 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-sky-500"
              >
                {services.map((s) => (
                  <option key={s.id} value={s.id}>
                    {s.name}
                  </option>
                ))}
              </select>
            </div>

            <div className="grid grid-cols-2 gap-3">
              <div>
                <label className="block text-xs font-semibold text-slate-300 mb-1">Страна</label>
                <select
                  value={countryCode}
                  onChange={(e) => setCountryCode(e.target.value)}
                  className="w-full bg-[#0d121c] border border-slate-700 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-sky-500"
                >
                  <option value="TR">🇹🇷 Турция</option>
                  <option value="NG">🇳🇬 Нигерия</option>
                  <option value="AR">🇦🇷 Аргентина</option>
                  <option value="IN">🇮🇳 Индия</option>
                  <option value="KZ">🇰🇿 Казахстан</option>
                  <option value="UA">🇺🇦 Украина</option>
                  <option value="EG">🇪🇬 Египет</option>
                  <option value="PH">🇵🇭 Филиппины</option>
                  <option value="BR">🇧🇷 Бразилия</option>
                  <option value="PL">🇵🇱 Польша</option>
                </select>
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-300 mb-1">Тарифный план</label>
                <input
                  type="text"
                  value={planName}
                  onChange={(e) => setPlanName(e.target.value)}
                  placeholder="Individual / Family"
                  className="w-full bg-[#0d121c] border border-slate-700 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-sky-500"
                  required
                />
              </div>
            </div>

            <div className="grid grid-cols-2 gap-3">
              <div>
                <label className="block text-xs font-semibold text-slate-300 mb-1">Цена</label>
                <input
                  type="number"
                  step="any"
                  value={price}
                  onChange={(e) => setPrice(e.target.value)}
                  placeholder="Например: 79.99"
                  className="w-full bg-[#0d121c] border border-slate-700 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-sky-500"
                  required
                />
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-300 mb-1">Валюта</label>
                <select
                  value={currency}
                  onChange={(e) => setCurrency(e.target.value)}
                  className="w-full bg-[#0d121c] border border-slate-700 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-sky-500"
                >
                  <option value="TRY">TRY (₺)</option>
                  <option value="NGN">NGN (₦)</option>
                  <option value="ARS">ARS ($)</option>
                  <option value="INR">INR (₹)</option>
                  <option value="KZT">KZT (₸)</option>
                  <option value="UAH">UAH (₴)</option>
                  <option value="USD">USD ($)</option>
                  <option value="EUR">EUR (€)</option>
                  <option value="EGP">EGP (E£)</option>
                </select>
              </div>
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-300 mb-1">
                Заметки по оплате (какие карты работают)
              </label>
              <textarea
                value={notes}
                onChange={(e) => setNotes(e.target.value)}
                rows={2}
                placeholder="Работает через Ininal, требуется VPN..."
                className="w-full bg-[#0d121c] border border-slate-700 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-sky-500 resize-none"
              />
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-300 mb-1">
                Ваш контакт (Telegram или Email, опционально)
              </label>
              <input
                type="text"
                value={contact}
                onChange={(e) => setContact(e.target.value)}
                placeholder="@username"
                className="w-full bg-[#0d121c] border border-slate-700 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-sky-500"
              />
            </div>

            <div className="pt-2 flex justify-end gap-2">
              <button
                type="button"
                onClick={onClose}
                className="px-4 py-2 rounded-lg text-sm text-slate-400 hover:text-white hover:bg-slate-800"
              >
                Отмена
              </button>
              <button
                type="submit"
                disabled={status === 'submitting'}
                className="flex items-center gap-1.5 px-4 py-2 rounded-lg text-sm font-semibold bg-sky-600 hover:bg-sky-500 text-white shadow-lg transition"
              >
                <Send className="w-4 h-4" />
                <span>{status === 'submitting' ? 'Отправка...' : 'Отправить'}</span>
              </button>
            </div>
          </form>
        )}
      </div>
    </div>
  );
};
