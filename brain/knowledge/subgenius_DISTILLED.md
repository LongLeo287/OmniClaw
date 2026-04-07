---
id: subgenius
type: knowledge
owner: OA_Triage
---
# subgenius
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "subgenius_v2",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview",
    "lint": "tsc --noEmit"
  },
  "dependencies": {
    "@ffmpeg/ffmpeg": "^0.12.15",
    "@ffmpeg/util": "^0.12.2",
    "@google/genai": "^1.39.0",
    "@xenova/transformers": "2.17.2",
    "lucide-react": "^0.563.0",
    "mp4-muxer": "^5.2.2",
    "react": "^19.2.4",
    "react-dom": "^19.2.4",
    "webm-muxer": "^5.1.4"
  },
  "devDependencies": {
    "@types/node": "^22.14.0",
    "@vitejs/plugin-react": "^5.0.0",
    "typescript": "~5.8.2",
    "vite": "^6.2.0"
  }
}

```

### File: README.md
```md
<div align="center">
<img width="1200" height="475" alt="GHBanner" src="https://github.com/user-attachments/assets/0aa67016-6eaf-458a-adb2-6e31a0763ed6" />
</div>

# Run and deploy your AI Studio app

This contains everything you need to run your app locally.

View your app in AI Studio: https://ai.studio/apps/ee0a3291-716a-4f7c-9cd0-ee27d20e1c56

## Run Locally

**Prerequisites:**  Node.js


1. Install dependencies:
   `npm install`
2. Set the `GEMINI_API_KEY` in [.env.local](.env.local) to your Gemini API key
3. Run the app:
   `npm run dev`

```

### File: constants.ts
```ts

import { Language, SplitMode, ModelType, SubtitleStyle } from './types';

export const SUPPORTED_LANGUAGES = [
  { value: 'English', label: 'English', flag: '🇺🇸', code: 'en' },
  { value: 'Vietnamese', label: 'Tiếng Việt', flag: '🇻🇳', code: 'vi' },
  { value: 'Japanese', label: '日本語', flag: '🇯🇵', code: 'ja' },
  { value: 'Korean', label: '한국어', flag: '🇰🇷', code: 'ko' },
  { value: 'Chinese (Simplified)', label: '简体中文', flag: '🇨🇳', code: 'zh-CN' },
  { value: 'Chinese (Traditional)', label: '繁體中文', flag: '🇹🇼', code: 'zh-TW' },
  { value: 'Spanish', label: 'Español', flag: '🇪🇸', code: 'es' },
  { value: 'French', label: 'Français', flag: '🇫🇷', code: 'fr' },
  { value: 'German', label: 'Deutsch', flag: '🇩🇪', code: 'de' },
  { value: 'Italian', label: 'Italiano', flag: '🇮🇹', code: 'it' },
  { value: 'Portuguese', label: 'Português', flag: '🇵🇹', code: 'pt' },
  { value: 'Russian', label: 'Русский', flag: '🇷🇺', code: 'ru' },
  { value: 'Hindi', label: 'हिन्दी', flag: '🇮🇳', code: 'hi' },
  { value: 'Thai', label: 'ไทย', flag: '🇹🇭', code: 'th' },
  { value: 'Indonesian', label: 'Bahasa Indonesia', flag: '🇮🇩', code: 'id' },
  { value: 'Arabic', label: 'العربية', flag: '🇸🇦', code: 'ar' },
  { value: 'Turkish', label: 'Türkçe', flag: '🇹🇷', code: 'tr' },
  { value: 'Dutch', label: 'Nederlands', flag: '🇳🇱', code: 'nl' },
  { value: 'Polish', label: 'Polski', flag: '🇵🇱', code: 'pl' },
  { value: 'Swedish', label: 'Svenska', flag: '🇸🇪', code: 'sv' },
  { value: 'Filipino', label: 'Filipino', flag: '🇵🇭', code: 'tl' },
  { value: 'Malay', label: 'Bahasa Melayu', flag: '🇲🇾', code: 'ms' },
  { value: 'Ukrainian', label: 'Українська', flag: '🇺🇦', code: 'uk' },
  { value: 'Greek', label: 'Ελληνικά', flag: '🇬🇷', code: 'el' },
  { value: 'Czech', label: 'Čeština', flag: '🇨🇿', code: 'cs' },
  { value: 'Danish', label: 'Dansk', flag: '🇩🇰', code: 'da' },
  { value: 'Finnish', label: 'Suomi', flag: '🇫🇮', code: 'fi' },
  { value: 'Hungarian', label: 'Magyar', flag: '🇭🇺', code: 'hu' },
  { value: 'Norwegian', label: 'Norsk', flag: '🇳🇴', code: 'no' },
  { value: 'Romanian', label: 'Română', flag: '🇷🇴', code: 'ro' },
  { value: 'Slovak', label: 'Slovenčina', flag: '🇸🇰', code: 'sk' },
  { value: 'Bengali', label: 'বাংলা', flag: '🇧🇩', code: 'bn' },
  { value: 'Urdu', label: 'اردو', flag: '🇵🇰', code: 'ur' },
  { value: 'Persian', label: 'فارسی', flag: '🇮🇷', code: 'fa' },
  { value: 'Hebrew', label: 'עברית', flag: '🇮🇱', code: 'he' }
];

export const FONT_FAMILIES = [
  { value: 'Inter, sans-serif', label: 'Inter' },
  { value: '"SF Pro Display", sans-serif', label: 'SF Pro' },
  { value: 'Arial, sans-serif', label: 'Arial' },
  { value: '"Times New Roman", serif', label: 'Times New Roman' },
  { value: '"Courier New", monospace', label: 'Courier New' },
  { value: 'Georgia, serif', label: 'Georgia' },
  { value: 'Impact, sans-serif', label: 'Impact' },
  { value: 'Verdana, sans-serif', label: 'Verdana' },
  { value: 'Tahoma, sans-serif', label: 'Tahoma' },
  { value: 'Montserrat, sans-serif', label: 'Montserrat' },
  { value: 'Oswald, sans-serif', label: 'Oswald' },
  { value: 'Raleway, sans-serif', label: 'Raleway' },
  { value: '"Playfair Display", serif', label: 'Playfair Display' },
  { value: '"Roboto Mono", monospace', label: 'Roboto Mono' },
  { value: 'Ubuntu, sans-serif', label: 'Ubuntu' },
  { value: '"Open Sans", sans-serif', label: 'Open Sans' },
  { value: 'Kanit, sans-serif', label: 'Kanit' },
  { value: 'Be Vietnam Pro, sans-serif', label: 'Be Vietnam Pro' },
  { value: '"Lexend Deca", sans-serif', label: 'Lexend Deca' },
  { value: 'Lobster, cursive', label: 'Lobster' },
  { value: '"Pacifico", cursive', label: 'Pacifico' },
];

export const DEFAULT_SUBTITLE_STYLE: SubtitleStyle = {
  fontSize: 24,
  fontFamily: 'Inter, sans-serif',
  textColor: '#ffffff',
  backgroundColor: '#000000',
  showBackground: true,
  backgroundOpacity: 0.6,
  borderRadius: 8,
  padding: 12,
  fontWeight: 'bold',
  fontStyle: 'normal',
  textDecoration: 'none',
  highlightWords: true,
  highlightColor: '#44d62c',
  highlightBold: true,
  highlightItalic: false,
  highlightUnderline: false,
  textAlign: 'center',
  verticalPosition: 85,
  horizontalPosition: 50,
  maxWidth: 90,
  showGlow: true,
  glowColor: '#44d62c',
  glowOpacity: 0.5,
  glowBlur: 15,
  showSecondarySubtitle: false,
};

export const LANGUAGE_CODE_MAP: Record<string, string> = SUPPORTED_LANGUAGES.reduce((acc, lang) => {
  acc[lang.value] = lang.code.toUpperCase();
  return acc;
}, {} as Record<string, string>);

export const MODEL_OPTIONS = [
  { value: ModelType.GEMINI, label: 'Gemini 3 Flash' },
];

export const DEFAULT_MAX_CHARS = 40;

const BASE_EN = {
  appTitle: 'SubGenius',
  tagline: 'AI Powered Subtitle Generator',
  description: 'Create professional subtitles in seconds using the power of Gemini 3.',
  config: 'CONFIG',
  modelSelect: 'Transcription Engine',
  apiKeyLabel: 'Gemini API Settings',
  selectKeyBtn: 'SELECT PERSONAL KEY',
  useDefaultKey: 'Use System Default Key',
  useDefaultKeyHelp: 'Standard speed. No billing required from your side.',
  usePersonalKey: 'Use Personal API Key',
  usePersonalKeyHelp: 'Recommended for long files to avoid truncation or quota limits.',
  saveClose: 'SAVE & CLOSE',
  targetLang: 'Target Languages',
  targetLangHelp: 'Note: Translations are generated using high-accuracy Cloud AI.',
  splitRules: 'Split Rules',
  splitModes: [
    { value: SplitMode.SENTENCE, label: 'Sentence', hint: 'Natural flow' },
    { value: SplitMode.SINGLE_WORD, label: 'Word', hint: '1 word per line' },
    { value: SplitMode.THREE_WORDS, label: 'Groups', hint: '3 words per line' },
    { value: SplitMode.SHORT_PHRASE, label: 'Phrase', hint: 'Max 6 words' },
  ],
  generateBtn: 'GENERATE',
  processing: 'PROCESSING...',
  cancel: 'CANCEL',
  uploadTitle: 'Upload Audio',
  uploadDesc: 'MP3, WAV, M4A, MP4',
  ready: 'PROJECT SETTINGS',
  readyDesc: 'Upload audio or record to begin sequence.',
  generatedTitle: 'GENERATED CUES',
  exportSRT: 'Export as SRT',
  exportASS: 'Export as ASS (Styled)',
  exportDOC: 'Word Document (.doc)',
  exportExcel: 'Excel (CSV)',
  exportJSON: 'Project File (JSON)',
  exportJSONDesc: 'Single file backup including audio',
  importSRT: 'Import SRT',
  importCSV: 'Import CSV',
  importSRTHelp: 'Upload an .srt file to replace text in the current tab.',
  importCSVHelp: 'Upload a .csv file to completely replace the current project data.',
  saveProject: 'SAVE',
  savePrompt: 'Enter a name for your project:',
  projects: 'HISTORY',
  noProjects: 'No saved projects found.',
  replace: 'Replace',
  replaceAll: 'ALL',
  search: 'Search',
  recording: 'Recording...',
  stopRec: 'STOP RECORDING',
  recTitle: 'Record Voice',
  recDesc: 'Click to start',
  analyzing: 'Analyzing audio...',
  decoding: 'Decoding audio data...',
  resampling: 'Resampling to 16kHz...',
  transcribing: 'Executing transcription...',
  translating: 'Refining translations...',
  initSpeechModel: 'Initializing Speech AI...',
  initTranslatorModel: 'Initializing Translator AI...',
  original: 'ORIG',
  refreshTranslation: 'Translate',
  refreshHelp: 'Re-translate based on current Original text',
  reference: 'REFERENCE (ORIGINAL)',
  translation: 'TRANSLATION',
  printBtn: 'PRINT TO PDF',
  newProject: 'NEW',
  history: 'HISTORY',
  deleteConfirm: 'Delete this project? This cannot be undone.',
  renameTitle: 'Rename Project',
  toastSaved: 'Project Saved Successfully!',
  toastNew: 'New Project Started',
  toastExport: 'Project Exported',
  noSegmentsSearch: 'No segments matching search',
  clearSearch: 'Clear Search',
  liveEditor: 'Live Editor',
  standbySeek: 'Standby / Seeking Audio',
  focusedEditing: 'Focused Editing',
  focusedSearch: 'Focused Search',
  textUpdateTip: 'Text updates instantly on the main grid',
  exportTitle: 'Select Export Format',
  downloadFiles: 'Download Files',
  apiStatus: 'AI Engine Status',
  authError: 'Auth or Quota error. Please check your API Key or switch to a personal one.',
  generalError: 'Error occurred during AI processing.',
  importBtn: 'IMPORT FILE',
  togglePlayer: 'Toggle Player',
  playerSize: 'Player Size',
  zoomIn: 'Zoom In',
  zoomOut: 'Zoom Out',
  keyRequired: 'Please select a personal API Key or use the system default.',
  searchPlaceholder: 'Search segments...',
  viewModeGrid: 'Grid View',
  viewModeText: 'Text Review',
  processingChunk: 'Processing chunk',
  noMedia: 'No media connected',
  selectMedia: 'Select Media File',
  selectMediaHelp: 'Please select a media file to start previewing and editing timeline',
  ok: 'OK',
  close: 'CLOSE',
  start: 'Start',
  end: 'End',
  rename: 'Rename',
  delete: 'Delete',
  speaker: 'Speaker',
  subtitleStyle: 'Subtitle Style',
  fontSize: 'Size',
  fontColor: 'Color',
  bgColor: 'Background',
  bgOpacity: 'Opacity',
  borderRadius: 'Rounded',
  padding: 'Padding',
  highlight: 'Highlight',
  highlightPerWord: 'Word Highlight',
  textAlign: 'Alignment',
  yPosition: 'Position (Y)',
  xPosition: 'Position (X)',
  maxWidth: 'Max Width',
  glow: 'Glow Effect',
  glowColor: 'Glow Color',
  glowOpacity: 'Glow Opacity',
  glowBlur: 'Glow Spread',
  exportVideo: 'Export Video',
  exportSubtitles: 'Export Subtitles',
  exportProject: 'Export Project',
  videoFormat: 'Video Format',
  renderingVideo: 'Rendering Video...',
  renderComplete: 'Video Rendered Successfully',
  guideTitle: 'User Guide',
  fontSearch: 'Search font...',
  uploadFont: 'Upload custom font',
  showSecondary: 'Show Original (Dual-Sub)',
  originalReference: 'Reference Original:',
  undo: 'Undo',
  splitTool: 'Split Tool',
  trimTool: 'Trim Tool',
  selectTool: 'Select Tool',
  timecodeJump: 'Jump to Timecode',
  themeSelect: 'Theme Selection',
  guide: {
    title: 'SubGenius AI - User Guide',
    tagline: 'Professional AI-Powered Subtitle Generation Suite',
    version: 'Official Documentation - Version 5.0',
    c1: { title: '01. Overview', desc: 'SubGenius AI utilizes Gemini 3 for ultra-fast audio transcription with millisecond word-alignment and high-quality translation.' },
    c2: { title: '02. Timeline Editor', subtitle: 'Advanced Editing Tools', desc: 'Use the Select Tool (V) for moving, Split Tool (C) for cutting segments, and Trim Tool (Shift) for simultaneous dual-edge trimming. Undo (Ctrl+Z) is available for quick corrections.' },
    c3: { title: '03. Pro Styling & Themes', uploadTitle: 'Style Palette', uploadDesc: 'Customize fonts, colors, and background. Use the Palette icon to change the overall app theme and gradients.', recTitle: 'Dual-Sub Mode', recDesc: 'Display original text alongside translations for bilingual viewers.' },
    c4: { title: '04. Search & Replace', subtitle: 'Mass Editing', desc: 'Use the Search panel to instantly find and replace terms across all segments and languages.' },
    c5: { title: '05. Exporting', subtitle: 'Pro Formats', desc: 'Export to SRT, ASS (Styled), or Video Overlay. Use Project JSON for a complete backup including the audio file.' },
    c6: { title: '06. Navigation', srtTitle: 'Timecode Jump', srtDesc: 'Click on the timecode in the timeline to jump to a specific position instantly.', csvTitle: 'Keyboard Shortcuts', csvDesc: 'C: Split, V: Select, Shift: Dual Trim, Ctrl+Z: Undo.' },
    c7: { title: '07. Privacy', desc: 'Data is processed securely. We never store your audio or subtitles on our own servers permanently.' }
  }
};

export const UI_TEXT: Record<string, typeof BASE_EN> = {
  en: BASE_EN,
  vn: {
    ...BASE_EN,
    appTitle: 'SubGenius',
    tagline: 'Tạo Phụ Đề Bằng AI',
    description: 'Tạo phụ đề chuyên nghiệp trong giây lát sử dụng sức mạnh của Gemini 3.',
    config: 'CẤU HÌNH',
    importBtn: 'NHẬP FILE',
    togglePlayer: 'Ẩn/Hiện Video',
    playerSize: 'Kích thước Video',
    zoomIn: 'Phóng to',
    zoomOut: 'Thu nhỏ',
    apiKeyLabel: 'Cấu hình Gemini API',
    selectKeyBtn: 'CHỌN API KEY CÁ NHÂN',
    useDefaultKey: 'Sử dụng Key mặc định',
    useDefaultKeyHelp: 'Nhanh và miễn phí. Không yêu cầu thanh toán từ bạn.',
    usePersonalKey: 'Sử dụng Key cá nhân',
    usePersonalKeyHelp: 'Khuyên dùng cho file dài để tránh giới hạn hạn mức.',
    saveClose: 'LƯU & ĐÓNG',
    targetLang: 'Ngôn ngữ đích',
    targetLangHelp: 'Lưu ý: Bản dịch được tạo bằng AI Cloud độ chính xác cao.',
    splitRules: 'Quy tắc ngắt dòng',
    splitModes: [
      { value: SplitMode.SENTENCE, label: 'Theo câu', hint: 'Dòng chảy tự nhiên' },
      { value: SplitMode.SINGLE_WORD, label: 'Từng từ', hint: '1 từ mỗi dòng' },
      { value: SplitMode.THREE_WORDS, label: 'Nhóm từ', hint: '3 từ mỗi dòng' },
      { value: SplitMode.SHORT_PHRASE, label: 'Cụm từ', hint: 'Tối đa 6 từ' },
    ],
    generateBtn: 'TẠO',
    processing: 'ĐANG XỬ LÝ...',
    cancel: 'HỦY',
    uploadTitle: 'Tải File Audio',
    uploadDesc: 'MP3, WAV, M4A, MP4',
    ready: 'THIẾT LẬP DỰ ÁN',
    readyDesc: 'Tải lên âm thanh hoặc ghi âm để bắt đầu.',
    exportSRT: 'Xuất file SRT',
    exportASS: 'Xuất file ASS (Định dạng Pro)',
    exportDOC: 'Văn bản Word (.doc)',
    exportExcel: 'Excel (CSV)',
    exportJSON: 'Tệp Dự Án (JSON)',
    exportJSONDesc: 'Sao lưu duy nhất một tệp gồm cả âm thanh',
    importSRT: 'Nhập SRT',
    importCSV: 'Nhập CSV',
    saveProject: 'LƯU',
    savePrompt: 'Nhập tên cho dự án:',
    projects: 'LỊCH SỬ',
    history: 'LỊCH SỬ',
    noProjects: 'Chưa có dự án nào.',
    replace: 'Thay thế',
    replaceAll: 'TẤT CẢ',
    search: 'Tìm kiếm',
    recording: 'Đang ghi âm...',
    stopRec: 'DỪNG GHI ÂM',
    recTitle: 'Ghi âm',
    recDesc: 'Nhấn để bắt đầu',
    analyzing: 'Phân tích âm thanh...',
    decoding: 'Giải mã dữ liệu...',
    resampling: 'Đang chuyển đổi 16kHz...',
    transcribing: 'Trích xuất văn bản...',
    translating: 'Dịch thuật...',
    initSpeechModel: 'Khởi tạo AI giọng nói...',
    initTranslatorModel: 'Khởi tạo AI dịch thuật...',
    original: 'GỐC',
    refreshTranslation: 'Dịch',
    refreshHelp: 'Dịch lại dựa trên nội dung gốc',
    reference: 'THAM CHIẾU (GỐC)',
    translation: 'BẢN DỊCH',
    printBtn: 'XUẤT PDF',
    newProject: 'MỚI',
    deleteConfirm: 'Xóa dự án này? Thao tác này không thể hoàn tác.',
    renameTitle: 'Đổi tên dự án',
    rename: 'Đổi tên',
    delete: 'Xóa',
    speaker: 'Người nói',
    liveEditor: 'Trình chỉnh sửa',
    processingChunk: 'Đang xử lý đoạn',
    subtitleStyle: 'Kiểu Phụ Đề',
    fontSize: 'Kích cỡ',
    fontColor: 'Màu chữ',
    bgColor: 'Màu nền',
    bgOpacity: 'Độ mờ nền',
    borderRadius: 'Bo góc',
    padding: 'Căn lề',
    highlight: 'Làm nổi bật',
    highlightPerWord: 'Theo từng từ',
    textAlign: 'Căn lề chữ',
    yPosition: 'Vị trí (Y)',
    xPosition: 'Vị trí (X)',
    maxWidth: 'Dài tối đa',
    glow: 'Hiệu ứng đổ bóng',
    glowColor: 'Màu bóng',
    glowOpacity: 'Độ mờ bóng',
    glowBlur: 'Độ lan tỏa',
    exportVideo: 'Xuất Video',
    exportSubtitles: 'Xuất Phụ đề',
    exportProject: 'Xuất Dự án',
    videoFormat: 'Định dạng Video',
    renderingVideo: 'Đang xử lý Video...',
    re
... [TRUNCATED]
```

### File: index.html
```html

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>SubGenius AI - Subtitle Generator</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
      tailwind.config = {
        theme: {
          extend: {
            colors: {
              razer: {
                DEFAULT: 'rgb(var(--razer-rgb, 68, 214, 44))',
                dim: 'var(--razer-dim, #2b8a1b)',
                glow: 'var(--razer-glow, #6aff4d)',
              },
              dark: {
                950: '#050505', // Deepest black
                900: '#0a0a0a',
                800: '#111111',
                700: '#1a1a1a',
              },
              glass: {
                light: 'rgba(255, 255, 255, 0.05)',
                medium: 'rgba(255, 255, 255, 0.1)',
                heavy: 'rgba(20, 20, 20, 0.6)',
                border: 'rgba(255, 255, 255, 0.08)',
              }
            },
            fontFamily: {
              sans: ['SF Pro Display', '-apple-system', 'BlinkMacSystemFont', 'Inter', 'Roboto', 'sans-serif'],
            },
            boxShadow: {
              'glass': '0 8px 32px 0 rgba(0, 0, 0, 0.37)',
              'glow': '0 0 20px rgba(68, 214, 44, 0.3)',
            }
          }
        }
      }
    </script>
    <style>
      body {
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
      }
      
      /* Apple-style slender scrollbar */
      ::-webkit-scrollbar {
        width: 6px;
        height: 6px;
      }
      ::-webkit-scrollbar-track {
        background: transparent; 
      }
      ::-webkit-scrollbar-thumb {
        background: rgba(255, 255, 255, 0.15); 
        border-radius: 10px;
      }
      ::-webkit-scrollbar-thumb:hover {
        background: rgba(255, 255, 255, 0.3); 
      }
      
      .no-scrollbar::-webkit-scrollbar {
        display: none;
      }
      .no-scrollbar {
        -ms-overflow-style: none;
        scrollbar-width: none;
      }

      .razer-glow {
        box-shadow: 0 0 25px rgba(68, 214, 44, 0.2);
      }
      
      /* Glassmorphism Utilities */
      .glass-panel {
        background: rgba(10, 10, 10, 0.7);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.08);
      }

      .glass-button {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      }
      
      .glass-button:hover {
        background: rgba(255, 255, 255, 0.08);
        transform: translateY(-1px);
      }
      
      .glass-button:active {
        transform: scale(0.96);
      }

      /* Custom Font Injection Container */
      #custom-fonts-container {}
    </style>
  <script type="importmap">
{
  "imports": {
    "react-dom/": "https://esm.sh/react-dom@^19.2.4/",
    "react/": "https://esm.sh/react@^19.2.4/",
    "react": "https://esm.sh/react@^19.2.4",
    "@google/genai": "https://esm.sh/@google/genai@^1.39.0",
    "lucide-react": "https://esm.sh/lucide-react@^0.563.0",
    "@xenova/transformers": "https://cdn.jsdelivr.net/npm/@xenova/transformers@2.17.2",
    "react-dom": "https://esm.sh/react-dom@^19.2.4"
  }
}
</script>
<link rel="stylesheet" href="/index.css">
</head>
  <body class="bg-black text-gray-200 antialiased font-sans selection:bg-razer selection:text-black overflow-x-hidden">
    <div id="root"></div>
    <div id="custom-fonts-container"></div>
  <script type="module" src="/index.tsx"></script>
</body>
</html>

```

### File: metadata.json
```json
{
  "name": "SubGenius_V2",
  "description": "Professional AI-powered subtitle generator using Gemini 3. Supports multiple languages, sentence-based or character-limit splitting, and export to SRT.",
  "requestFramePermissions": [
    "microphone"
  ]
}
```

### File: package-lock.json
```json
{
  "name": "subgenius_v2",
  "version": "0.0.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "subgenius_v2",
      "version": "0.0.0",
      "dependencies": {
        "@ffmpeg/ffmpeg": "^0.12.15",
        "@ffmpeg/util": "^0.12.2",
        "@google/genai": "^1.39.0",
        "@xenova/transformers": "2.17.2",
        "lucide-react": "^0.563.0",
        "mp4-muxer": "^5.2.2",
        "react": "^19.2.4",
        "react-dom": "^19.2.4",
        "webm-muxer": "^5.1.4"
      },
      "devDependencies": {
        "@types/node": "^22.14.0",
        "@vitejs/plugin-react": "^5.0.0",
        "typescript": "~5.8.2",
        "vite": "^6.2.0"
      }
    },
    "node_modules/@babel/code-frame": {
      "version": "7.29.0",
      "resolved": "https://registry.npmjs.org/@babel/code-frame/-/code-frame-7.29.0.tgz",
      "integrity": "sha512-9NhCeYjq9+3uxgdtp20LSiJXJvN0FeCtNGpJxuMFZ1Kv3cWUNb6DOhJwUvcVCzKGR66cw4njwM6hrJLqgOwbcw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-validator-identifier": "^7.28.5",
        "js-tokens": "^4.0.0",
        "picocolors": "^1.1.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/compat-data": {
      "version": "7.29.0",
      "resolved": "https://registry.npmjs.org/@babel/compat-data/-/compat-data-7.29.0.tgz",
      "integrity": "sha512-T1NCJqT/j9+cn8fvkt7jtwbLBfLC/1y1c7NtCeXFRgzGTsafi68MRv8yzkYSapBnFA6L3U2VSc02ciDzoAJhJg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/core": {
      "version": "7.29.0",
      "resolved": "https://registry.npmjs.org/@babel/core/-/core-7.29.0.tgz",
      "integrity": "sha512-CGOfOJqWjg2qW/Mb6zNsDm+u5vFQ8DxXfbM09z69p5Z6+mE1ikP2jUXw+j42Pf1XTYED2Rni5f95npYeuwMDQA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.29.0",
        "@babel/generator": "^7.29.0",
        "@babel/helper-compilation-targets": "^7.28.6",
        "@babel/helper-module-transforms": "^7.28.6",
        "@babel/helpers": "^7.28.6",
        "@babel/parser": "^7.29.0",
        "@babel/template": "^7.28.6",
        "@babel/traverse": "^7.29.0",
        "@babel/types": "^7.29.0",
        "@jridgewell/remapping": "^2.3.5",
        "convert-source-map": "^2.0.0",
        "debug": "^4.1.0",
        "gensync": "^1.0.0-beta.2",
        "json5": "^2.2.3",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/babel"
      }
    },
    "node_modules/@babel/generator": {
      "version": "7.29.1",
      "resolved": "https://registry.npmjs.org/@babel/generator/-/generator-7.29.1.tgz",
      "integrity": "sha512-qsaF+9Qcm2Qv8SRIMMscAvG4O3lJ0F1GuMo5HR/Bp02LopNgnZBC/EkbevHFeGs4ls/oPz9v+Bsmzbkbe+0dUw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/parser": "^7.29.0",
        "@babel/types": "^7.29.0",
        "@jridgewell/gen-mapping": "^0.3.12",
        "@jridgewell/trace-mapping": "^0.3.28",
        "jsesc": "^3.0.2"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-compilation-targets": {
      "version": "7.28.6",
      "resolved": "https://registry.npmjs.org/@babel/helper-compilation-targets/-/helper-compilation-targets-7.28.6.tgz",
      "integrity": "sha512-JYtls3hqi15fcx5GaSNL7SCTJ2MNmjrkHXg4FSpOA/grxK8KwyZ5bubHsCq8FXCkua6xhuaaBit+3b7+VZRfcA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/compat-data": "^7.28.6",
        "@babel/helper-validator-option": "^7.27.1",
        "browserslist": "^4.24.0",
        "lru-cache": "^5.1.1",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-globals": {
      "version": "7.28.0",
      "resolved": "https://registry.npmjs.org/@babel/helper-globals/-/helper-globals-7.28.0.tgz",
      "integrity": "sha512-+W6cISkXFa1jXsDEdYA8HeevQT/FULhxzR99pxphltZcVaugps53THCeiWA8SguxxpSp3gKPiuYfSWopkLQ4hw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-imports": {
      "version": "7.28.6",
      "resolved": "https://registry.npmjs.org/@babel/helper-module-imports/-/helper-module-imports-7.28.6.tgz",
      "integrity": "sha512-l5XkZK7r7wa9LucGw9LwZyyCUscb4x37JWTPz7swwFE/0FMQAGpiWUZn8u9DzkSBWEcK25jmvubfpw2dnAMdbw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/traverse": "^7.28.6",
        "@babel/types": "^7.28.6"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-transforms": {
      "version": "7.28.6",
      "resolved": "https://registry.npmjs.org/@babel/helper-module-transforms/-/helper-module-transforms-7.28.6.tgz",
      "integrity": "sha512-67oXFAYr2cDLDVGLXTEABjdBJZ6drElUSI7WKp70NrpyISso3plG9SAGEF6y7zbha/wOzUByWWTJvEDVNIUGcA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-module-imports": "^7.28.6",
        "@babel/helper-validator-identifier": "^7.28.5",
        "@babel/traverse": "^7.28.6"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0"
      }
    },
    "node_modules/@babel/helper-plugin-utils": {
      "version": "7.28.6",
      "resolved": "https://registry.npmjs.org/@babel/helper-plugin-utils/-/helper-plugin-utils-7.28.6.tgz",
      "integrity": "sha512-S9gzZ/bz83GRysI7gAD4wPT/AI3uCnY+9xn+Mx/KPs2JwHJIz1W8PZkg2cqyt3RNOBM8ejcXhV6y8Og7ly/Dug==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-string-parser": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-string-parser/-/helper-string-parser-7.27.1.tgz",
      "integrity": "sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-validator-identifier": {
      "version": "7.28.5",
      "resolved": "https://registry.npmjs.org/@babel/helper-validator-identifier/-/helper-validator-identifier-7.28.5.tgz",
      "integrity": "sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-validator-option": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/helper-validator-option/-/helper-validator-option-7.27.1.tgz",
      "integrity": "sha512-YvjJow9FxbhFFKDSuFnVCe2WxXk1zWc22fFePVNEaWJEu8IrZVlda6N0uHwzZrUM1il7NC9Mlp4MaJYbYd9JSg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helpers": {
      "version": "7.28.6",
      "resolved": "https://registry.npmjs.org/@babel/helpers/-/helpers-7.28.6.tgz",
      "integrity": "sha512-xOBvwq86HHdB7WUDTfKfT/Vuxh7gElQ+Sfti2Cy6yIWNW05P8iUslOVcZ4/sKbE+/jQaukQAdz/gf3724kYdqw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/template": "^7.28.6",
        "@babel/types": "^7.28.6"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/parser": {
      "version": "7.29.0",
      "resolved": "https://registry.npmjs.org/@babel/parser/-/parser-7.29.0.tgz",
      "integrity": "sha512-IyDgFV5GeDUVX4YdF/3CPULtVGSXXMLh1xVIgdCgxApktqnQV0r7/8Nqthg+8YLGaAtdyIlo2qIdZrbCv4+7ww==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/types": "^7.29.0"
      },
      "bin": {
        "parser": "bin/babel-parser.js"
      },
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@babel/plugin-transform-react-jsx-self": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-react-jsx-self/-/plugin-transform-react-jsx-self-7.27.1.tgz",
      "integrity": "sha512-6UzkCs+ejGdZ5mFFC/OCUrv028ab2fp1znZmCZjAOBKiBK2jXD1O+BPSfX8X2qjJ75fZBMSnQn3Rq2mrBJK2mw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-plugin-utils": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0-0"
      }
    },
    "node_modules/@babel/plugin-transform-react-jsx-source": {
      "version": "7.27.1",
      "resolved": "https://registry.npmjs.org/@babel/plugin-transform-react-jsx-source/-/plugin-transform-react-jsx-source-7.27.1.tgz",
      "integrity": "sha512-zbwoTsBruTeKB9hSq73ha66iFeJHuaFkUbwvqElnygoNbj/jHRsSeokowZFN3CZ64IvEqcmmkVe89OPXc7ldAw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-plugin-utils": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0-0"
      }
    },
    "node_modules/@babel/template": {
      "version": "7.28.6",
      "resolved": "https://registry.npmjs.org/@babel/template/-/template-7.28.6.tgz",
      "integrity": "sha512-YA6Ma2KsCdGb+WC6UpBVFJGXL58MDA6oyONbjyF/+5sBgxY/dwkhLogbMT2GXXyU84/IhRw/2D1Os1B/giz+BQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.28.6",
        "@babel/parser": "^7.28.6",
        "@babel/types": "^7.28.6"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/traverse": {
      "version": "7.29.0",
      "resolved": "https://registry.npmjs.org/@babel/traverse/-/traverse-7.29.0.tgz",
      "integrity": "sha512-4HPiQr0X7+waHfyXPZpWPfWL/J7dcN1mx9gL6WdQVMbPnF3+ZhSMs8tCxN7oHddJE9fhNE7+lxdnlyemKfJRuA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.29.0",
        "@babel/generator": "^7.29.0",
        "@babel/helper-globals": "^7.28.0",
        "@babel/parser": "^7.29.0",
        "@babel/template": "^7.28.6",
        "@babel/types": "^7.29.0",
        "debug": "^4.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/types": {
      "version": "7.29.0",
      "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.29.0.tgz",
      "integrity": "sha512-LwdZHpScM4Qz8Xw2iKSzS+cfglZzJGvofQICy7W7v4caru4EaAmyUuO6BGrbyQ2mYV11W0U8j5mBhd14dd3B0A==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-string-parser": "^7.27.1",
        "@babel/helper-validator-identifier": "^7.28.5"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@esbuild/aix-ppc64": {
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/aix-ppc64/-/aix-ppc64-0.25.12.tgz",
      "integrity": "sha512-Hhmwd6CInZ3dwpuGTF8fJG6yoWmsToE+vYgD4nytZVxcu1ulHpUQRAB1UJ8+N1Am3Mz4+xOByoQoSZf4D+CpkA==",
      "cpu": [
        "ppc64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "aix"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/android-arm": {
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/android-arm/-/android-arm-0.25.12.tgz",
      "integrity": "sha512-VJ+sKvNA/GE7Ccacc9Cha7bpS8nyzVv0jdVgwNDaR4gDMC/2TTRc33Ip8qrNYUcpkOHUT5OZ0bUcNNVZQ9RLlg==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/android-arm64": {
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/android-arm64/-/android-arm64-0.25.12.tgz",
      "integrity": "sha512-6AAmLG7zwD1Z159jCKPvAxZd4y/VTO0VkprYy+3N2FtJ8+BQWFXU+OxARIwA46c5tdD9SsKGZ/1ocqBS/gAKHg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/android-x64": {
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/android-x64/-/android-x64-0.25.12.tgz",
      "integrity": "sha512-5jbb+2hhDHx5phYR2By8GTWEzn6I9UqR11Kwf22iKbNpYrsmRB18aX/9ivc5cabcUiAT/wM+YIZ6SG9QO6a8kg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/darwin-arm64": {
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/darwin-arm64/-/darwin-arm64-0.25.12.tgz",
      "integrity": "sha512-N3zl+lxHCifgIlcMUP5016ESkeQjLj/959RxxNYIthIg+CQHInujFuXeWbWMgnTo4cp5XVHqFPmpyu9J65C1Yg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/darwin-x64": {
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/darwin-x64/-/darwin-x64-0.25.12.tgz",
      "integrity": "sha512-HQ9ka4Kx21qHXwtlTUVbKJOAnmG1ipXhdWTmNXiPzPfWKpXqASVcWdnf2bnL73wgjNrFXAa3yYvBSd9pzfEIpA==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/freebsd-arm64": {
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/freebsd-arm64/-/freebsd-arm64-0.25.12.tgz",
      "integrity": "sha512-gA0Bx759+7Jve03K1S0vkOu5Lg/85dou3EseOGUes8flVOGxbhDDh/iZaoek11Y8mtyKPGF3vP8XhnkDEAmzeg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "freebsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/freebsd-x64": {
      "version": "0.25.12",
      "resolved": "https://registry.npmjs.org/@esbuild/freebsd-x64/-/freebsd-x64-0.25.12.tgz",
      "integrity": "sha512-TGbO26Yw2xsHzxtbVFGEXBFH0FRAP7gtcPE7P5yP7wGy7cXK2oO7RyOhL5NLiqTlBh47XhmIUXuGciXEqYFfBQ==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "freebsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-arm": {
      "version": "0.25.12",
      "resolved": "https
... [TRUNCATED]
```

### File: tsconfig.json
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "experimentalDecorators": true,
    "useDefineForClassFields": false,
    "module": "ESNext",
    "lib": [
      "ES2022",
      "DOM",
      "DOM.Iterable"
    ],
    "skipLibCheck": true,
    "types": [
      "node"
    ],
    "moduleResolution": "bundler",
    "isolatedModules": true,
    "moduleDetection": "force",
    "allowJs": true,
    "jsx": "react-jsx",
    "paths": {
      "@/*": [
        "./*"
      ]
    },
    "allowImportingTsExtensions": true,
    "noEmit": true
  }
}
```

### File: types.ts
```ts

export type Language = string;

export enum SplitMode {
  SENTENCE = 'Complete Sentence',
  SINGLE_WORD = '1 Word Per Line',
  THREE_WORDS = '3 Words Per Line',
  SHORT_PHRASE = 'Short Phrase (Max 6 Words)'
}

export enum ModelType {
  GEMINI = 'Gemini',
  WHISPER_LOCAL = 'Whisper (Offline)'
}

export interface WordData {
  text: string;
  start_ms: number;
  end_ms: number;
  is_eos: boolean;
}

export interface SegmentData {
  speaker: string;
  start_ms: number;
  end_ms: number;
  text: string;
  words: WordData[];
  translations: { [key in Language]?: string };
}

export interface MasterTranscript {
  segments: SegmentData[];
}

export interface SubtitleStyle {
  fontSize: number;
  fontFamily: string;
  textColor: string;
  backgroundColor: string;
  showBackground: boolean;
  backgroundOpacity: number;
  borderRadius: number;
  padding: number;
  
  // Text Styling
  fontWeight: 'normal' | 'bold';
  fontStyle: 'normal' | 'italic';
  textDecoration: 'none' | 'underline';

  // Highlight Logic
  highlightWords: boolean;
  highlightColor: string;
  
  // Highlight Specific Styling
  highlightBold: boolean;
  highlightItalic: boolean;
  highlightUnderline: boolean;

  textAlign: 'left' | 'center' | 'right';
  verticalPosition: number; // 0 (top) to 100 (bottom)
  horizontalPosition: number; // 0 (left) to 100 (right)
  maxWidth: number; // New property: 0 to 100 (%)

  // Glow/Shadow Styling
  showGlow: boolean;
  glowColor: string;
  glowOpacity: number;
  glowBlur: number;

  // Secondary Subtitle (Bilingual)
  showSecondarySubtitle: boolean;
}

export interface SubtitleBlock {
  id: number;
  speaker?: string;
  start: string; 
  end: string;   
  originalText: string;
  translations: { [key in Language]?: string };
  words?: WordData[]; 
}

export interface SubtitleCue {
  id: number;
  start: string;
  end: string;
  text: string;
}

export interface GenerationConfig {
  targetLanguages: Language[];
  splitMode: SplitMode;
  modelType: ModelType;
  isOffline: boolean;
  style?: SubtitleStyle;
}

export interface SavedProject {
  id: string;
  name: string;
  date: string;
  config: GenerationConfig;
  subtitles: SubtitleBlock[];
  masterTranscript?: MasterTranscript;
  fileData?: string;
  fileType?: string;
  fileName?: string;
}

export type ProcessingStatus = 'idle' | 'recording' | 'processing' | 'translating' | 'completed' | 'error' | 'loading_model';

export interface MobileEditState {
  blockId: number;
  lang: string;
  value: string;
}

```

### File: vite.config.ts
```ts
import path from 'path';
import { defineConfig, loadEnv } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig(({ mode }) => {
    const env = loadEnv(mode, '.', '');
    return {
      server: {
        port: 3000,
        host: '0.0.0.0',
      },
      plugins: [react()],
      define: {
        'process.env.API_KEY': JSON.stringify(env.GEMINI_API_KEY),
        'process.env.GEMINI_API_KEY': JSON.stringify(env.GEMINI_API_KEY)
      },
      resolve: {
        alias: {
          '@': path.resolve(__dirname, '.'),
        }
      }
    };
});

```

### File: services\geminiService.ts
```ts

import { GoogleGenAI, Type, GenerateContentResponse } from "@google/genai";
import { Language, SplitMode, SubtitleBlock, ModelType, MasterTranscript, SegmentData, WordData } from "../types";
import { msToTimeCode } from "../utils/timeUtils";

const getSystemInstruction = (targetLangsStr: string) => {
  return `
    Role: Professional Audio-to-Subtitle Alignment Expert.
    Task: Transcribe audio with high-precision timestamps and translate to [${targetLangsStr}].

    CRITICAL RULES FOR TIMESTAMPS:
    1. PRECISION: Provide timestamps in milliseconds (ms). Accuracy at the millisecond level is mandatory.
    2. WORD BOUNDARIES: Ensure each word's 'start_ms' and 'end_ms' capture the exact audible start and end. 
    3. TAIL-END ACCURACY: The 'end_ms' of the last word in any segment (especially the final segment of the file) MUST include the natural decay/reverb of the voice. DO NOT cut off early.
    4. SEGMENT ALIGNMENT: The 'start_ms' of a segment MUST be identical to the 'start_ms' of its first word. The 'end_ms' of a segment MUST be identical to the 'end_ms' of its last word.
    5. CONTINUITY: Words within a segment should have sequential timestamps. 
    6. NO GAPS: Ensure subtitles stay on screen until the next speaker starts or until the audio naturally concludes.

    OUTPUT GUIDELINES:
    - Output JSON ONLY.
    - Translations must reflect the meaning of the specific segment.

    JSON SCHEMA:
    {
      "segments": [
        {
          "speaker": "Speaker A",
          "start_ms": 1050,
          "end_ms": 4820,
          "text": "The exact transcription here.",
          "translations": { "Vietnamese": "Bản dịch chính xác.", "Japanese": "..." },
          "words": [
            { "text": "The", "start_ms": 1050, "end_ms": 1200, "is_eos": false },
            { "text": "exact", "start_ms": 1210, "end_ms": 1600, "is_eos": false }
          ]
        }
      ]
    }
  `;
};

const withRetry = async <T>(fn: () => Promise<T>, retries = 2): Promise<T> => {
  for (let i = 0; i <= retries; i++) {
    try {
      return await fn();
    } catch (error: any) {
      const errorStr = error.toString() || '';
      const isRetryable = errorStr.includes('429') || errorStr.includes('500') || errorStr.includes('503');
      if (isRetryable && i < retries) {
        const delay = Math.pow(2, i) * 2000 + Math.random() * 1000;
        await new Promise(resolve => setTimeout(resolve, delay));
        continue;
      }
      throw error;
    }
  }
  throw new Error("Maximum retries reached");
};

const tryParseJSON = (jsonString: string): any => {
    // 1. Remove Markdown code blocks
    let cleaned = jsonString.replace(/```json\n?|```/g, '').trim();

    try {
        return JSON.parse(cleaned);
    } catch (e) {
        // 2. Try to repair truncated JSON
        // Common truncation cases:
        // - Ends inside a string: ... "text": "some val
        // - Ends inside an object: ... "end_ms": 123
        // - Ends inside an array: ... { ... }, { ...
        
        // Attempt 1: Close string if needed, then close stack
        const stack: string[] = [];
        let inString = false;
        let isEscaped = false;
        
        for (let i = 0; i < cleaned.length; i++) {
            const char = cleaned[i];
            if (isEscaped) {
                isEscaped = false;
                continue;
            }
            if (char === '\\') {
                isEscaped = true;
                continue;
            }
            if (char === '"') {
                inString = !inString;
                continue;
            }
            if (!inString) {
                if (char === '{') stack.push('}');
                else if (char === '[') stack.push(']');
                else if (char === '}' || char === ']') {
                    if (stack.length > 0 && stack[stack.length - 1] === char) {
                        stack.pop();
                    }
                }
            }
        }

        let repaired = cleaned;
        if (inString) repaired += '"';
        while (stack.length > 0) {
            repaired += stack.pop();
        }

        try {
            return JSON.parse(repaired);
        } catch (e2) {
            // Attempt 2: If sophisticated repair fails, try simple suffixing
            const closers = ['}', ']', ']}', '"}', '"]', '"]}'];
            for (const closer of closers) {
                try {
                    return JSON.parse(cleaned + closer);
                } catch (e3) { /* continue */ }
            }
            
            // Attempt 3: Aggressive truncation to last valid object
            if (cleaned.includes('"segments":')) {
                 const lastObjectEnd = cleaned.lastIndexOf('}');
                 if (lastObjectEnd > -1) {
                     const truncated = cleaned.substring(0, lastObjectEnd + 1);
                     // Check if we need to close the array and root object
                     try {
                         return JSON.parse(truncated + ']}');
                     } catch (e4) {
                         try {
                             return JSON.parse(truncated + ']');
                         } catch (e5) {
                             try {
                                 return JSON.parse(truncated + '}');
                             } catch (e6) {}
                         }
                     }
                 }
            }
            
            console.warn("JSON Parse Failed. Returning empty segment list.", e);
            // Return empty structure to prevent crash
            return { segments: [] };
        }
    }
};

const localizeSpeakerName = (speaker: string, ui: any): string => {
    if (!speaker || !ui?.speaker) return speaker;
    return speaker.replace(/Speaker/gi, ui.speaker);
};

export const generateSubtitles = async (
  audioBase64: string,
  mimeType: string,
  targetLanguages: Language[],
  modelType: ModelType = ModelType.GEMINI,
  ui?: any
): Promise<MasterTranscript> => {
  
  const ai = new GoogleGenAI({ apiKey: process.env.API_KEY });
  const targetLangsStr = targetLanguages.join(', ');
  const systemInstruction = getSystemInstruction(targetLangsStr);

  try {
    const response: GenerateContentResponse = await withRetry(() => ai.models.generateContent({
      model: 'gemini-3-flash-preview',
      contents: {
        parts: [
          { inlineData: { mimeType: mimeType, data: audioBase64 } },
          { text: `Transcribe with millisecond timestamps and translate to ${targetLangsStr}. Return JSON.` }
        ]
      },
      config: {
        systemInstruction: systemInstruction,
        responseMimeType: "application/json",
        responseSchema: {
          type: Type.OBJECT,
          properties: {
            segments: {
                type: Type.ARRAY,
                items: {
                    type: Type.OBJECT,
                    properties: {
                        speaker: { type: Type.STRING },
                        start_ms: { type: Type.INTEGER },
                        end_ms: { type: Type.INTEGER },
                        text: { type: Type.STRING },
                        translations: {
                            type: Type.OBJECT,
                            properties: targetLanguages.reduce((acc, lang) => ({...acc, [lang]: {type: Type.STRING}}), {})
                        },
                        words: {
                            type: Type.ARRAY,
                            items: {
                                type: Type.OBJECT,
                                properties: {
                                    text: { type: Type.STRING },
                                    start_ms: { type: Type.INTEGER },
                                    end_ms: { type: Type.INTEGER },
                                    is_eos: { type: Type.BOOLEAN }
                                },
                                required: ["text", "start_ms", "end_ms", "is_eos"]
                            }
                        }
                    },
                    required: ["speaker", "start_ms", "end_ms", "text", "words", "translations"]
                }
            }
          }
        }
      }
    }));

    const jsonText = response.text;
    if (!jsonText) throw new Error("No response from AI engine.");

    const transcript = tryParseJSON(jsonText) as MasterTranscript;
    
    if (ui) {
        transcript.segments = transcript.segments.map(seg => ({
            ...seg,
            speaker: localizeSpeakerName(seg.speaker, ui)
        }));
    }

    return transcript;

  } catch (error: any) {
    console.error("AI API Error:", error);
    let errorMsg = `Generation failed.`;
    const errorStr = error.toString();
    if (errorStr.includes("401") || errorStr.includes("403")) errorMsg = "AUTH_ERROR";
    else if (errorStr.includes("429")) errorMsg = "QUOTA_EXHAUSTED";
    else errorMsg += " " + (error.message || "Unknown error");
    throw new Error(errorMsg);
  }
};

/**
 * Processes multiple audio chunks and merges the results.
 */
export const generateSubtitlesFromChunks = async (
  chunks: { blob: Blob; startOffsetMs: number }[],
  targetLanguages: Language[],
  modelType: ModelType = ModelType.GEMINI,
  ui?: any,
  onProgress?: (msg: string) => void,
  onCheckCancelled?: () => boolean
): Promise<MasterTranscript> => {
  const allSegments: SegmentData[] = [];
  const overlapMs = 5000; // Assuming 5s overlap as defined in audioUtils

  // Process chunks in series or small batches to avoid rate limits
  for (let i = 0; i < chunks.length; i++) {
    if (onCheckCancelled && onCheckCancelled()) {
      throw new Error("CANCELLED");
    }
    const chunk = chunks[i];
    if (onProgress) onProgress(`${ui?.processingChunk || 'Processing chunk'} ${i + 1} / ${chunks.length}...`);
    
    const base64 = await new Promise<string>((resolve) => {
      const reader = new FileReader();
      reader.onloadend = () => resolve((reader.result as string).split(',')[1]);
      reader.readAsDataURL(chunk.blob);
    });

    const transcript = await generateSubtitles(base64, chunk.blob.type, targetLanguages, modelType, ui);
    
    // Adjust timestamps and filter based on overlap boundaries
    const nextChunkStart = chunks[i + 1]?.startOffsetMs;
    const currentChunkStart = chunk.startOffsetMs;
    
    const lowerBound = i === 0 ? -1 : currentChunkStart + (overlapMs / 2);
    const upperBound = nextChunkStart ? nextChunkStart + (overlapMs / 2) : Infinity;

    transcript.segments.forEach(seg => {
      const adjustedSeg = {
        ...seg,
        start_ms: seg.start_ms + currentChunkStart,
        end_ms: seg.end_ms + currentChunkStart,
        words: seg.words.map(w => ({
          ...w,
          start_ms: w.start_ms + currentChunkStart,
          end_ms: w.end_ms + currentChunkStart
        }))
      };

      // Only keep segments that "start" in this chunk's designated area
      if (adjustedSeg.start_ms >= lowerBound && adjustedSeg.start_ms < upperBound) {
        allSegments.push(adjustedSeg);
      }
    });
  }

  // Sort by start time just in case
  allSegments.sort((a, b) => a.start_ms - b.start_ms);

  return { segments: allSegments };
};

export const processTranscriptToBlocks = (
    transcript: MasterTranscript, 
    splitMode: SplitMode
): SubtitleBlock[] => {
    const blocks: SubtitleBlock[] = [];
    let currentId = 1;

    const createBlock = (words: WordData[], translations: { [key in Language]?: string }, speaker: string, isLastOfAll: boolean = false) => {
        if (words.length === 0) return;
        const startMs = words[0].start_ms;
        let endMs = words[words.length - 1].end_ms;
        if (isLastOfAll) endMs += 400;

        blocks.push({
            id: currentId++,
            speaker: speaker,
            start: msToTimeCode(startMs),
            end: msToTimeCode(endMs),
            originalText: words.map(w => w.text).join(' '),
            translations: translations || {},
            words: words // Pass word level data
        });
    };

    if (splitMode === SplitMode.SENTENCE) {
        transcript.segments.forEach((seg, idx) => {
             const isLastSeg = idx === transcript.segments.length - 1;
             let endMs = seg.end_ms;
             if (isLastSeg) endMs += 400;
             blocks.push({
                 id: currentId++,
                 speaker: seg.speaker,
                 start: msToTimeCode(seg.start_ms),
                 end: msToTimeCode(endMs),
                 originalText: seg.text,
                 translations: seg.translations || {},
                 words: seg.words
             });
        });
        return blocks;
    }

    transcript.segments.forEach((seg, segIdx) => {
        let currentChunk: WordData[] = [];
        const totalWordsInSegment = seg.words.length;
        const isLastSeg = segIdx === transcript.segments.length - 1;

        const flushChunk = (isLastChunkInSeg: boolean) => {
             if (currentChunk.length > 0) {
                 const chunkStartIndex = seg.words.indexOf(currentChunk[0]);
                 const chunkWordCount = currentChunk.length;
                 const splitTranslations: { [key in Language]?: string } = {};
                 Object.entries(seg.translations || {}).forEach(([lang, fullText]) => {
                     if (!fullText) return;
                     const transWords = fullText.split(' ');
                     const start = Math.floor((chunkStartIndex / totalWordsInSegment) * transWords.length);
                     const end = Math.floor(((chunkStartIndex + chunkWordCount) / totalWordsInSegment) * transWords.length);
                     splitTranslations[lang as Language] = transWords.slice(start, Math.max(end, start + 1)).join(' ');
                 });
                 const isLastOfAll = isLastSeg && isLastChunkInSeg;
                 createBlock(currentChunk, splitTranslations, seg.speaker, isLastOfAll);
                 currentChunk = [];
             }
        };

        seg.words.forEach((word, index) => {
            currentChunk.push(word);
            let shouldSplit = false;
            const isLastWordInSeg = index === seg.words.length - 1;
            if (splitMode === SplitMode.SINGLE_WORD) shouldSplit = true;
            else if (splitMode === SplitMode.THREE_WORDS && currentChunk.length >= 3) shouldSplit = true;
            else if (splitMode === SplitMode.SHORT_PHRASE) {
                if (word.is_eos || currentChunk.length >= 6) shouldSplit = true;
                const nextWord = seg.words[index + 1];
                if (nextWord && (nextWord.start_ms - word.end_ms > 400)) shouldSplit = true;
            }
            if (shouldSplit || isLastWordInSeg) flushChunk(isLastWordInSeg);
        });
    });
    return blocks;
};

export const reTranslateSubtitles = async (
  blocks: SubtitleBlock[],
  targetLanguage: Language,
  modelType: ModelType = ModelType.GEMINI
): Promise<SubtitleBlock[]> => {
  const ai = new GoogleGenAI(
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
