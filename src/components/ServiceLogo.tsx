import React from 'react';

interface ServiceLogoProps {
  slug: string;
  name: string;
  color?: string;
  size?: 'sm' | 'md' | 'lg' | 'xl';
  className?: string;
}

export const ServiceLogo: React.FC<ServiceLogoProps> = ({
  slug,
  name,
  color = '#38bdf8',
  size = 'md',
  className = '',
}) => {
  const sizeClasses = {
    sm: 'w-6 h-6 p-1 text-xs',
    md: 'w-9 h-9 p-1.5 text-sm',
    lg: 'w-11 h-11 p-2 text-base',
    xl: 'w-14 h-14 p-2.5 text-xl',
  }[size];

  const iconSize = {
    sm: 16,
    md: 22,
    lg: 26,
    xl: 34,
  }[size];

  // SVG Paths for official brands
  const renderBrandIcon = () => {
    switch (slug) {
      case 'spotify':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 2C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10S17.523 2 12 2zm4.586 14.424c-.18.295-.563.387-.857.207-2.35-1.436-5.308-1.76-8.792-.963-.335.077-.67-.133-.746-.469-.077-.335.132-.67.468-.747 3.808-.871 7.077-.506 9.72 1.115.294.18.387.563.207.857zm1.226-2.724c-.226.367-.707.482-1.074.256-2.69-1.654-6.79-2.134-9.97-1.168-.412.125-.852-.11-.977-.523-.125-.413.11-.852.523-.977 3.636-1.103 8.16-.57 11.242 1.328.367.226.482.707.256 1.074zm.106-2.836C14.692 8.95 9.375 8.775 6.297 9.71c-.495.15-1.023-.13-1.173-.625-.15-.496.13-1.024.625-1.174 3.532-1.072 9.404-.866 13.115 1.338.445.264.59.838.327 1.282-.264.444-.838.59-1.282.327z" />
          </svg>
        );

      case 'youtube-premium':
      case 'youtube-music':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z" />
          </svg>
        );

      case 'netflix':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M5.398 0v24c1.196-.134 2.392-.269 3.587-.403V9.757l6.817 14.137c1.196-.134 2.392-.269 3.587-.403V0h-3.587v14.243L8.985 0H5.398z" />
          </svg>
        );

      case 'chatgpt-plus':
      case 'chatgpt-pro':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M22.282 9.821a5.985 5.985 0 0 0-.516-4.91 6.046 6.046 0 0 0-6.51-2.9A6.065 6.065 0 0 0 4.981 4.18a5.985 5.985 0 0 0-3.998 2.9 6.046 6.046 0 0 0 .743 7.097 5.98 5.98 0 0 0 .51 4.911 6.051 6.051 0 0 0 6.515 2.9A5.985 5.985 0 0 0 13.26 24a6.056 6.056 0 0 0 5.772-4.206 5.99 5.99 0 0 0 3.997-2.9 6.056 6.056 0 0 0-.747-7.073zM13.26 22.43a4.476 4.476 0 0 1-2.876-1.04l.141-.081 4.779-2.758a.795.795 0 0 0 .392-.681v-6.737l2.02 1.168a.071.071 0 0 1 .038.052v5.583a4.504 4.504 0 0 1-4.494 4.494zM3.6 18.304a4.47 4.47 0 0 1-.535-3.014l.142.085 4.783 2.759a.771.771 0 0 0 .78 0l5.843-3.369v2.332a.08.08 0 0 1-.033.062L9.74 19.95a4.5 4.5 0 0 1-6.14-1.646zm-1.545-8.52a4.475 4.475 0 0 1 2.339-1.973v5.68a.79.79 0 0 0 .392.682l5.844 3.37-2.02 1.168a.08.08 0 0 1-.07 0l-4.839-2.791A4.494 4.494 0 0 1 2.055 9.784zm15.654 3.42l-5.844-3.37 2.02-1.168a.08.08 0 0 1 .07 0l4.839 2.791a4.494 4.494 0 0 1-.676 8.105v-5.678a.79.79 0 0 0-.409-.68zm2.04-3.111l-.142-.085-4.779-2.759a.775.775 0 0 0-.78 0L8.204 12.09V9.758a.08.08 0 0 1 .033-.062l4.84-2.796a4.5 4.5 0 0 1 6.677 4.655zm-11.49-1.678l-2.02-1.168a.076.076 0 0 1-.038-.052V3.712a4.504 4.504 0 0 1 7.37-3.454l-.141.08-4.779 2.759a.794.794 0 0 0-.392.681v6.737zm1.105 2.759l2.7-1.558 2.7 1.558v3.117l-2.7 1.558-2.7-1.558v-3.117z" />
          </svg>
        );

      case 'claude-pro':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 2l2.6 6.8L21.4 12l-6.8 2.6L12 21.4l-2.6-6.8L2.6 12l6.8-2.6L12 2zm0 4.8l-1.3 3.4L7.3 11.5l3.4 1.3 1.3 3.4 1.3-3.4 3.4-1.3-3.4-1.3L12 6.8z" />
          </svg>
        );

      case 'gemini-advanced':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M11.5 2C11.5 7.24671 7.24671 11.5 2 11.5C7.24671 11.5 11.5 15.7533 11.5 21C11.5 15.7533 15.7533 11.5 21 11.5C15.7533 11.5 11.5 7.24671 11.5 2Z" />
          </svg>
        );

      case 'midjourney':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 2L3 19h18L12 2zm0 5l5 10H7l5-10z" />
          </svg>
        );

      case 'perplexity-pro':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 2L4 7v10l8 5 8-5V7l-8-5zm6 14.1l-6 3.75-6-3.75V8.9l6-3.75 6 3.75v7.2zM12 9l-4 2.5v3L12 17l4-2.5v-3L12 9z" />
          </svg>
        );

      case 'cursor-pro':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M3 3l7 18 3-7 7-3L3 3zm6.5 10.5l-1.5-4 4 1.5-2.5 2.5z" />
          </svg>
        );

      case 'grok-x-premium':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z" />
          </svg>
        );

      case 'apple-music':
      case 'icloud-plus':
      case 'apple-tv':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M15.97 6.37c.64-.78 1.08-1.86.96-2.95-1 .04-2.14.67-2.8 1.44-.58.66-1.09 1.76-.95 2.82 1.11.09 2.17-.57 2.79-1.31z" />
          </svg>
        );

      case 'soundcloud':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M1.17 14.5c0-.6.4-.8.4-.8s-.4-.2-.4-.8v-1.8c0-.6.4-.8.4-.8s-.4-.2-.4-.8V8.3c0-.6.4-.8.4-.8s-.4-.2-.4-.8V5.5c0-.6.4-.8.4-.8s-.4-.2-.4-.8V3.2c0-.5.4-.7.4-.7s.4.2.4.7v16.1c0 .5-.4.7-.4.7s-.4-.2-.4-.7v-4.8zm3.2 2.8c-.5 0-.8-.4-.8-.8V6.5c0-.5.3-.8.8-.8s.8.3.8.8v10c0 .5-.3.8-.8.8zm3.3 1.1c-.5 0-.8-.4-.8-.8V5.3c0-.5.3-.8.8-.8s.8.3.8.8v12.3c0 .5-.3.8-.8.8zm3.2 0c-.5 0-.8-.4-.8-.8V5.3c0-.5.3-.8.8-.8s.8.3.8.8v12.3c0 .5-.3.8-.8.8zm3.3 0c-.5 0-.8-.4-.8-.8V7.5c0-.5.3-.8.8-.8s.8.3.8.8v10.1c0 .5-.3.8-.8.8zm5.8 0c-2.2 0-4-1.8-4-4 0-.4.1-.7.2-1.1-.1-.3-.2-.6-.2-.9 0-2.2 1.8-4 4-4 1.8 0 3.3 1.2 3.8 2.8.4-.2.8-.3 1.2-.3 1.7 0 3 1.3 3 3s-1.3 3-3 3h-5z" />
          </svg>
        );

      case 'telegram-premium':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm4.64 6.8c-.15 1.58-.8 5.42-1.13 7.19-.14.75-.42 1-.68 1.03-.58.05-1.02-.38-1.58-.75-.88-.58-1.38-.94-2.23-1.5-.99-.65-.35-1.01.22-1.59.15-.15 2.71-2.48 2.76-2.69.01-.03.01-.14-.07-.19-.08-.05-.19-.02-.27 0-.12.03-1.99 1.27-5.63 3.72-.53.36-1.02.54-1.45.53-.48-.01-1.4-.27-2.09-.49-.84-.27-1.51-.42-1.45-.89.03-.25.38-.51 1.05-.78 4.12-1.79 6.87-2.97 8.26-3.54 3.93-1.63 4.74-1.92 5.28-1.93.12 0 .39.03.56.17.15.12.19.28.21.4.02.13.02.26.01.4z" />
          </svg>
        );

      case 'discord-nitro':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028c.462-.63.874-1.295 1.226-1.994.021-.041.001-.09-.041-.106a13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.928 1.793 8.18 1.793 12.061 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.893.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.028zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.946 2.418-2.157 2.418z" />
          </svg>
        );

      case 'playstation-plus':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M8.7 16.5c0 .9-.5 1.4-1.5 1.4-.8 0-1.5-.4-1.5-1.1v-6.3L2 12c-.4.2-.8.2-1.1 0-.4-.2-.6-.6-.6-1 0-.3.1-.7.4-.9l5.3-3.6c.7-.5 1.6-.7 2.7-.7 1.8 0 3.2.7 4 1.8.8 1.1 1.2 2.5 1.2 4.1v5.1c0 .8-.5 1.4-1.5 1.4-.9 0-1.5-.5-1.5-1.4v-4.9c0-1.2-.2-2.1-.7-2.7-.5-.6-1.3-.9-2.2-.9-.8 0-1.5.2-2 .7-.5.4-.7 1.1-.7 1.9v5.6zm13.3-3.3c0 .8-.6 1.3-1.6 1.3-.8 0-1.4-.3-1.8-.8-.4-.5-.6-1.3-.6-2.2V7.1c0-.8.6-1.3 1.6-1.3.8 0 1.4.3 1.8.8.4.5.6 1.3.6 2.2v4.4z" />
          </svg>
        );

      case 'xbox-game-pass':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm0 2c1.7 0 3.3.5 4.6 1.4-1.2 1.1-2.9 2.5-4.6 4.3-1.7-1.8-3.4-3.2-4.6-4.3C8.7 4.5 10.3 4 12 4zM5.4 6.7c1.3 1.1 3 2.5 4.6 4.2-2.7 3.3-5.3 5.4-6.3 5.9A8 8 0 0 1 5.4 6.7zm13.2 0a8 8 0 0 1 1.7 10.1c-1-.5-3.6-2.6-6.3-5.9 1.6-1.7 3.3-3.1 4.6-4.2zM12 20a8 8 0 0 1-5.6-2.3c1.4-1 4.3-3.3 5.6-5.8 1.3 2.5 4.2 4.8 5.6 5.8A8 8 0 0 1 12 20z" />
          </svg>
        );

      case 'steam-ea-play':
      case 'steam':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M11.979 0C5.678 0 .511 4.86.022 11.037l6.432 2.658c.545-.371 1.203-.59 1.912-.59.063 0 .125.004.188.006l2.861-4.142V8.91c0-2.495 2.028-4.524 4.524-4.524 2.494 0 4.524 2.031 4.524 4.527s-2.03 4.525-4.524 4.525h-.105l-4.076 2.911c0 .052.004.105.004.159 0 1.875-1.515 3.396-3.39 3.396-1.635 0-3.016-1.173-3.331-2.727L.436 15.27C1.862 20.307 6.486 24 11.979 24c6.627 0 12-5.373 12-12s-5.373-12-12-12zM7.551 17.587l-1.849-.764c.319.76.994 1.334 1.821 1.542.492.124 1.009.102 1.481-.051.472-.152.883-.453 1.168-.857.284-.403.415-.89.37-1.378-.044-.488-.258-.941-.607-1.287-.349-.345-.806-.55-1.295-.584-.047-.003-.095-.005-.143-.005-.724 0-1.393.303-1.863.818l1.917.792c.381.157.564.59.407.971-.157.38-.59.564-.971.407l-.439-.185z" />
          </svg>
        );

      case 'nintendo-switch-online':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M7.7 2C4 2 1 5 1 8.7v6.6C1 19 4 22 7.7 22H9V2H7.7zm-.7 8.5a1.8 1.8 0 1 1 0-3.6 1.8 1.8 0 0 1 0 3.6zm9.3-8.5H15v20h1.3c3.7 0 6.7-3 6.7-6.7V8.7C23 5 20 2 16.3 2zM17 17a1.8 1.8 0 1 1 0-3.6 1.8 1.8 0 0 1 0 3.6z" />
          </svg>
        );

      case 'adobe-creative-cloud':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M13.96 2H24v20H13.96zm-3.92 0H0v20h10.04zM12 7.9L16.2 20h-3.1l-1.1-3.2H8l4-8.9z" />
          </svg>
        );

      case 'canva-pro':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1.6 14.5c-2.4 0-4.2-1.7-4.2-4.5 0-2.9 2-4.7 4.5-4.7 1.6 0 2.8.7 3.4 1.8l-1.6 1c-.4-.7-1.1-1.1-1.9-1.1-1.5 0-2.5 1.2-2.5 3 0 1.8 1.1 2.8 2.5 2.8.9 0 1.6-.5 2-1.2l1.6 1c-.8 1.2-2.1 1.9-3.7 1.9z" />
          </svg>
        );

      case 'figma-pro':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M8 2h4v5H8a2.5 2.5 0 0 1 0-5zm4 0h4a2.5 2.5 0 0 1 0 5h-4V2zm0 5v5H8a2.5 2.5 0 0 1 0-5h4zm0 5h4a2.5 2.5 0 0 1 0 5h-4v-5zm0 5v2.5a2.5 2.5 0 0 1-5 0 2.5 2.5 0 0 1 2.5-2.5H12z" />
          </svg>
        );

      case 'notion-plus':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M4.459 4.208c.746.606 1.026.56 2.428.466l13.215-.793c.28 0 .047-.28-.093-.373L17.72 1.73c-.56-.42-1.306-.7-2.333-.607L2.406 2.15c-.467.047-.56.28-.374.466zm.793 4.853v12.414c0 .793.373 1.12 1.213 1.073l13.822-.84c.84-.046 1.073-.606 1.073-1.353V8.079c0-.653-.28-.98-1.027-.933l-14.055.84c-.793.047-1.026.42-1.026 1.075zm13.122 1.306c.093.42 0 .84-.42.887l-.746.14v8.587c-.373.233-.793.373-1.213.373-.653 0-1.026-.28-1.633-.98l-5.086-7.98v7.42l1.4.327c.046.373-.28.746-.746.746l-3.92-.047c-.046-.373.187-.653.607-.746l.886-.187V11.16l-1.213-.14c-.093-.373.14-.84.606-.887l4.06.047 5.226 7.98V11.02l-1.166-.233c-.047-.42.233-.793.653-.84z" />
          </svg>
        );

      case 'microsoft-365':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M11 2H2v9h9V2zm11 0h-9v9h9V2zM11 13H2v9h9v-9zm11 0h-9v9h9v-9z" />
          </svg>
        );

      case 'zoom-pro':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M4.5 5h10a2.5 2.5 0 0 1 2.5 2.5v9a2.5 2.5 0 0 1-2.5 2.5h-10A2.5 2.5 0 0 1 2 16.5v-9A2.5 2.5 0 0 1 4.5 5zm13.5 4.5l4-3v11l-4-3V9.5z" />
          </svg>
        );

      case 'duolingo-super':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 2C6.5 2 2 6.5 2 12c0 2.2.7 4.2 2 5.8V22l4.4-1.7c1.1.5 2.3.7 3.6.7 5.5 0 10-4.5 10-10S17.5 2 12 2zm-3.5 8c1.1 0 2 .9 2 2s-.9 2-2 2-2-.9-2-2 .9-2 2-2zm7 0c1.1 0 2 .9 2 2s-.9 2-2 2-2-.9-2-2 .9-2 2-2z" />
          </svg>
        );

      case 'nordvpn':
      case 'surfshark-vpn':
      case 'proton-unlimited':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm0 10.99h7c-.53 4.12-3.28 7.79-7 8.94V12H5V6.3l7-3.11v8.8z" />
          </svg>
        );

      case 'jetbrains-all-products':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M0 0h24v24H0V0zm3.6 18h6v2.4h-6V18zm0-12h2.4v9.6H3.6V6zm8.4 0h3.6a3.6 3.6 0 1 1 0 7.2H12V6zm2.4 2.4v2.4h1.2a1.2 1.2 0 1 0 0-2.4H14.4z" />
          </svg>
        );

      case '1password':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 14.93V18h-2v-1.07a3.001 3.001 0 0 1 0-5.86V9h2v2.07a3.001 3.001 0 0 1 0 5.86zM12 15a1 1 0 1 0 0-2 1 1 0 0 0 0 2z" />
          </svg>
        );

      case 'tradingview':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M3 17h3v4H3v-4zm5-7h3v11H8V10zm5-5h3v16h-3V5zm5 4h3v12h-3V9zM2 3l7 7 4-4 9 9" stroke="currentColor" strokeWidth="2" fill="none" />
          </svg>
        );

      case 'disney-plus':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M10.8 13.8c-.8 0-1.4-.4-1.8-1.1-.3-.6-.5-1.4-.5-2.4 0-1.2.3-2.1.8-2.7.5-.6 1.2-.9 2-.9.7 0 1.3.2 1.7.7.4.5.6 1.1.6 1.9 0 .8-.2 1.6-.7 2.4-.6 1.4-1.3 2.1-2.1 2.1zm8.7-2.6c0 1.8-.5 3.3-1.6 4.4-1.1 1.2-2.6 1.8-4.5 1.8-1.5 0-2.8-.4-3.8-1.1-.9.8-1.9 1.2-3 1.2-1.2 0-2.1-.4-2.8-1.2-.7-.8-1-1.8-1-3 0-1.5.5-2.8 1.4-3.8.9-1 2.2-1.5 3.8-1.5.8 0 1.6.1 2.3.4.4-1 .6-2 .6-3 0-1.1-.3-1.8-.9-2.3-.6-.4-1.4-.6-2.5-.6-1 0-2 .2-3.1.7l-.6-2.1C5.2.4 6.7.1 8.2.1c1.9 0 3.3.4 4.3 1.2 1 .8 1.5 2 1.5 3.7 0 1.1-.2 2.3-.6 3.5 1.3-.2 2.6-.4 4-.4 1.1 0 2 .2 2.7.7.7.6 1.1 1.4 1.1 2.4z" />
          </svg>
        );

      case 'max-hbo':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M2 5h4l2.5 6L11 5h4v14h-3.5v-7L9 18H6.5l-2.5-6v7H2V5zm15.5 0h4.5l2 14h-3.5l-.5-3.5h-2.5L17 19h-3.5l4-14zm2.5 3l-.8 5.5h1.6L20 8z" />
          </svg>
        );

      case 'tinder-gold':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 2C10.5 4.5 8 8 8 11.5c0 3 2 5.5 5 5.5 1 0 2-.3 2.8-.8-.4 1.8-1.9 3.8-3.8 3.8C8 20 5 17 5 13c0-3.5 2-6.5 4.5-8.5C6.5 6.5 3 10 3 14c0 5 4 9 9 9s9-4 9-9c0-5-4.5-9.5-9-12z" />
          </svg>
        );

      case 'roblox-premium':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M5.3 1.8L1.8 18.7 18.7 22.2 22.2 5.3 5.3 1.8zm8.2 11.4l-3.4-.7.7-3.4 3.4.7-.7 3.4z" />
          </svg>
        );

      case 'deepl-pro':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M4 4h7v2H6v12h5v2H4V4zm9 0h7v16h-7v-2h5V6h-5V4zm-1.5 5.5l3.5 3.5-3.5 3.5-1.4-1.4 2.1-2.1H8v-2h4.7l-2.1-2.1 1.4-1.4z" />
          </svg>
        );

      case 'elevenlabs':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M6 3h3v18H6V3zm9 0h3v18h-3V3z" />
          </svg>
        );

      case 'splice':
        return (
          <svg width={iconSize} height={iconSize} viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm-4 6h2v8H8V8zm3-3h2v14h-2V5zm3 5h2v4h-2v-4z" />
          </svg>
        );

      default:
        return (
          <span className="font-black tracking-wider uppercase font-mono">
            {name.substring(0, 2)}
          </span>
        );
    }
  };

  return (
    <div
      className={`rounded-xl flex items-center justify-center font-bold text-white shadow-md transition-all shrink-0 border border-white/10 ${sizeClasses} ${className}`}
      style={{
        backgroundColor: color,
        boxShadow: `0 4px 14px ${color}33`,
      }}
      title={name}
    >
      {renderBrandIcon()}
    </div>
  );
};
