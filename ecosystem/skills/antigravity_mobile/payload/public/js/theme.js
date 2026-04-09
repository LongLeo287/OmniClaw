/* ============================================
 * Theme — Switching, icons, sidebar state
 * ============================================ */

function setTheme(theme) {
    // Remove all theme classes
    document.body.classList.remove('light-theme', 'pastel-theme', 'rainbow-theme', 'slate-theme');

    // Add the selected theme class (dark is default with no class)
    if (theme === 'light') {
        document.body.classList.add('light-theme');
    } else if (theme === 'pastel') {
        document.body.classList.add('pastel-theme');
    } else if (theme === 'rainbow') {
        document.body.classList.add('rainbow-theme');
    } else if (theme === 'slate') {
        document.body.classList.add('slate-theme');
    }

    localStorage.setItem('theme', theme);

    // Update theme selectors
    const sidebarSelect = document.getElementById('sidebarThemeSelect');
    const settingsSelect = document.getElementById('themeSelect');
    if (sidebarSelect) sidebarSelect.value = theme;
    if (settingsSelect) settingsSelect.value = theme;

    // Update theme icon
    updateThemeIcon(theme);
}

function updateThemeIcon(theme) {
    const iconBtn = document.getElementById('themeIconBtn');
    if (!iconBtn) return;

    const icons = {
        'dark': '🌙',
        'light': '☀️',
        'pastel': '🌸',
        'rainbow': '🌈',
        'slate': '◼'
    };
    iconBtn.textContent = icons[theme] || '🌙';

    // Sync topbar theme button too
    const topbarThemeBtn = document.getElementById('topbarThemeBtn');
    if (topbarThemeBtn) topbarThemeBtn.textContent = icons[theme] || '🌙';
}

function cycleTheme() {
    const themes = ['dark', 'light', 'pastel', 'rainbow', 'slate'];
    const currentTheme = localStorage.getItem('theme') || 'dark';
    const currentIndex = themes.indexOf(currentTheme);
    const nextIndex = (currentIndex + 1) % themes.length;
    setTheme(themes[nextIndex]);
}

async function loadTheme() {
    const localTheme = localStorage.getItem('theme');
    if (localTheme) {
        setTheme(localTheme);
    } else {
        // No local preference — try to use admin-configured default
        try {
            const res = await authFetch('/api/admin/mobile-ui');
            const data = await res.json();
            setTheme(data.theme || 'dark');
        } catch {
            setTheme('dark');
        }
    }
}

// Sidebar toggle
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const isExpanded = sidebar.classList.toggle('expanded');
    document.body.classList.toggle('sidebar-expanded', isExpanded);
    localStorage.setItem('sidebarExpanded', isExpanded);
}

function loadSidebarState() {
    const expanded = localStorage.getItem('sidebarExpanded') === 'true';
    if (expanded) {
        document.getElementById('sidebar').classList.add('expanded');
        document.body.classList.add('sidebar-expanded');
    }
}

// ====================================================================
// Model/Mode Selector
// ====================================================================
let availableModels = [];
let currentModel = 'Unknown';
let currentMode = 'Planning';
