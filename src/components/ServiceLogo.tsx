import React, { useState } from 'react';

interface ServiceLogoProps {
  slug: string;
  name: string;
  color?: string;
  size?: 'sm' | 'md' | 'lg' | 'xl';
  className?: string;
}

const SERVICE_DOMAINS: Record<string, string> = {
  // Музыка
  spotify: 'spotify.com',
  'apple-music': 'music.apple.com',
  soundcloud: 'soundcloud.com',
  deezer: 'deezer.com',
  tidal: 'tidal.com',
  splice: 'splice.com',
  'youtube-music': 'music.youtube.com',

  // Видео
  'youtube-premium': 'youtube.com',
  netflix: 'netflix.com',
  crunchyroll: 'crunchyroll.com',
  'disney-plus': 'disneyplus.com',
  'max-hbo': 'max.com',
  'apple-tv': 'tv.apple.com',

  // ИИ
  'chatgpt-plus': 'chatgpt.com',
  'claude-pro': 'claude.ai',
  'gemini-advanced': 'gemini.google.com',
  'perplexity-pro': 'perplexity.ai',
  'cursor-pro': 'cursor.com',
  'grok-x-premium': 'x.com',
  'github-copilot': 'github.com',
  midjourney: 'midjourney.com',
  elevenlabs: 'elevenlabs.io',
  'deepl-pro': 'deepl.com',

  // Дизайн
  'adobe-creative-cloud': 'adobe.com',
  'canva-pro': 'canva.com',
  'figma-pro': 'figma.com',

  // Продуктивность
  'microsoft-365': 'microsoft.com',
  'notion-plus': 'notion.so',
  'zoom-pro': 'zoom.us',
  'duolingo-super': 'duolingo.com',
  tradingview: 'tradingview.com',

  // Игры
  'playstation-plus': 'playstation.com',
  'xbox-game-pass': 'xbox.com',
  'steam-ea-play': 'store.steampowered.com',
  steam: 'store.steampowered.com',
  'nintendo-switch-online': 'nintendo.com',
  'roblox-premium': 'roblox.com',

  // Софт & VPN
  'telegram-premium': 'telegram.org',
  'discord-nitro': 'discord.com',
  'icloud-plus': 'apple.com',
  nordvpn: 'nordvpn.com',
  'surfshark-vpn': 'surfshark.com',
  'proton-unlimited': 'proton.me',
  'jetbrains-all-products': 'jetbrains.com',
  '1password': '1password.com',
  'tinder-gold': 'tinder.com',
};

// Прямые высококачественные иконки для некоторых сервисов
const DIRECT_ICONS: Record<string, string> = {
  spotify: 'https://storage.googleapis.com/pr-newsroom-wp/1/2023/05/Spotify_Primary_Logo_RGB_Green.png',
  netflix: 'https://assets.nflxext.com/us/ffe/siteui/common/icons/nficon2023.ico',
  'youtube-premium': 'https://www.youtube.com/s/desktop/f7ba0534/img/favicon_144x144.png',
  'chatgpt-plus': 'https://oaistatic-cdn.azureedge.net/chatgpt/favicon.ico',
  'discord-nitro': 'https://assets-global.website-files.com/6257adef93867e50d84d30e2/636e0a6a49cf127bf92de1e2_icon_clyde_blurple_RGB.png',
  'telegram-premium': 'https://telegram.org/img/t_logo.png',
  'apple-music': 'https://music.apple.com/assets/favicon/favicon-180.png',
};

export const ServiceLogo: React.FC<ServiceLogoProps> = ({
  slug,
  name,
  color = '#38bdf8',
  size = 'md',
  className = '',
}) => {
  const [failed, setFailed] = useState(false);

  const sizeClasses = {
    sm: 'w-6 h-6 p-0.5',
    md: 'w-9 h-9 p-1',
    lg: 'w-11 h-11 p-1.5',
    xl: 'w-14 h-14 p-2',
  }[size];

  const domain = SERVICE_DOMAINS[slug] || `${slug.replace(/-/g, '')}.com`;
  // Google Favicon API отдает качественную цветную официальную иконку 128x128
  const iconUrl = DIRECT_ICONS[slug] || `https://www.google.com/s2/favicons?domain=${domain}&sz=128`;

  return (
    <div
      className={`relative rounded-xl flex items-center justify-center bg-[#131b28] border border-slate-700/80 shadow-md overflow-hidden shrink-0 transition-transform duration-200 group-hover:scale-105 ${sizeClasses} ${className}`}
      style={{
        boxShadow: `0 3px 12px ${color}20`,
      }}
      title={name}
    >
      {!failed ? (
        <img
          src={iconUrl}
          alt={name}
          loading="lazy"
          onError={() => setFailed(true)}
          className="w-full h-full object-contain rounded-lg drop-shadow-sm select-none"
        />
      ) : (
        <div
          className="w-full h-full rounded-lg flex items-center justify-center font-bold text-white text-xs font-mono"
          style={{ backgroundColor: color }}
        >
          {name.substring(0, 2).toUpperCase()}
        </div>
      )}
    </div>
  );
};

export default ServiceLogo;
