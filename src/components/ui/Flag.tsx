import React, { useState } from 'react';

interface FlagProps {
  /** Флаг-эмодзи вида 🇹🇷 (пара региональных индикаторов) */
  emoji?: string;
  /** Двухбуквенный ISO-код страны вида "TR", "US", "KZ" */
  code?: string;
  className?: string;
}

/** 🇹🇷 → "TR". Возвращает null, если строка не похожа на флаг-эмодзи. */
function emojiToCountryCode(emoji?: string): string | null {
  if (!emoji) return null;
  const points = Array.from(emoji).map((ch) => ch.codePointAt(0) ?? 0);
  if (points.length !== 2 || points.some((p) => p < 0x1f1e6 || p > 0x1f1ff)) return null;
  return points.map((p) => String.fromCharCode(p - 0x1f1e6 + 65)).join('');
}

/**
 * Windows (Chrome / Edge) не рисует флаги-эмодзи — вместо 🇹🇷 показываются буквы «TR».
 * Поэтому флаг выводится картинкой. Если картинка не загрузилась — откат на эмодзи.
 * Источник: flagcdn.com.
 */
export const Flag: React.FC<FlagProps> = ({ emoji, code: directCode, className = '' }) => {
  const [failed, setFailed] = useState(false);
  const code = directCode || emojiToCountryCode(emoji);

  if (!code || failed) {
    return <span className={`text-lg leading-none ${className}`}>{emoji || directCode}</span>;
  }

  const lower = code.toLowerCase();
  return (
    <img
      src={`https://flagcdn.com/24x18/${lower}.png`}
      srcSet={`https://flagcdn.com/48x36/${lower}.png 2x`}
      width={24}
      height={18}
      alt={code}
      loading="lazy"
      onError={() => setFailed(true)}
      className={`inline-block rounded-[3px] object-cover ring-1 ring-white/10 ${className}`}
    />
  );
};

export default Flag;
