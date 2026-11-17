import React from 'react';

interface SparklineProps {
  data: number[];
  width?: number;
  height?: number;
  color?: string;
}

export const Sparkline: React.FC<SparklineProps> = ({
  data,
  width = 64,
  height = 20,
  color = '#38bdf8',
}) => {
  if (!data || data.length < 2) {
    return <span className="text-slate-600 text-[10px] font-mono">—</span>;
  }

  const min = Math.min(...data);
  const max = Math.max(...data);
  const range = max - min || 1;

  // Формируем координаты точек
  const points = data
    .map((val, idx) => {
      const x = (idx / (data.length - 1)) * (width - 4) + 2;
      const y = height - ((val - min) / range) * (height - 6) - 3;
      return `${x.toFixed(1)},${y.toFixed(1)}`;
    })
    .join(' ');

  const isUp = data[data.length - 1] > data[0];
  const strokeColor = isUp ? '#f43f5e' : '#10b981'; // если подорожало — красное, если подешевело — зеленое

  return (
    <div className="inline-flex items-center gap-1" title={`История цен: ${data.map(v => '$' + v).join(' → ')}`}>
      <svg width={width} height={height} className="overflow-visible">
        <polyline
          fill="none"
          stroke={strokeColor || color}
          strokeWidth="1.8"
          strokeLinecap="round"
          strokeLinejoin="round"
          points={points}
        />
        {/* Последняя точка */}
        {data.length > 0 && (
          <circle
            cx={(width - 2)}
            cy={height - ((data[data.length - 1] - min) / range) * (height - 6) - 3}
            r="2"
            fill={strokeColor}
          />
        )}
      </svg>
    </div>
  );
};
