/* ============================================
 * Icons — SVG icon helper (replaces emojis)
 * ============================================ */

function svgIcon(name, size) {
    var s = size || 16;
    var icons = {
        brain: '<svg width="' + s + '" height="' + s + '" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="10" rx="2"/><circle cx="12" cy="5" r="2"/><path d="M12 7v4"/><line x1="8" y1="16" x2="8" y2="16"/><line x1="16" y1="16" x2="16" y2="16"/></svg>',
        clipboard: '<svg width="' + s + '" height="' + s + '" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1"/></svg>',
        clock: '<svg width="' + s + '" height="' + s + '" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
        play: '<svg width="' + s + '" height="' + s + '" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg>',
        check: '<svg width="' + s + '" height="' + s + '" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
        close: '<svg width="' + s + '" height="' + s + '" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>',
        dotGreen: '<svg width="' + s + '" height="' + s + '" viewBox="0 0 16 16"><circle cx="8" cy="8" r="5" fill="#22c55e"/></svg>',
        dotYellow: '<svg width="' + s + '" height="' + s + '" viewBox="0 0 16 16"><circle cx="8" cy="8" r="5" fill="#eab308"/></svg>',
        dotBlue: '<svg width="' + s + '" height="' + s + '" viewBox="0 0 16 16"><circle cx="8" cy="8" r="5" fill="#3b82f6"/></svg>',
        dotRed: '<svg width="' + s + '" height="' + s + '" viewBox="0 0 16 16"><circle cx="8" cy="8" r="5" fill="#ef4444"/></svg>',
        dotGray: '<svg width="' + s + '" height="' + s + '" viewBox="0 0 16 16"><circle cx="8" cy="8" r="5" fill="#6b7280"/></svg>'
    };
    return '<span style="display:inline-flex;align-items:center;vertical-align:middle;flex-shrink:0;min-width:' + s + 'px;min-height:' + s + 'px;">' + (icons[name] || '') + '</span>';
}
