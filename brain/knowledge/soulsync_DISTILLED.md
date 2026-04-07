---
id: soulsync
type: knowledge
owner: OA_Triage
---
# soulsync
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: main.py
```py

#!/usr/bin/env python3

import sys
import asyncio
import time
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QStackedWidget
from PyQt6.QtCore import QThread, pyqtSignal, QTimer, QThreadPool
from PyQt6.QtGui import QFont, QPalette, QColor

from config.settings import config_manager
from utils.logging_config import setup_logging, get_logger
from core.spotify_client import SpotifyClient
from core.plex_client import PlexClient
from core.jellyfin_client import JellyfinClient
from core.navidrome_client import NavidromeClient
from core.soulseek_client import SoulseekClient

from ui.sidebar import ModernSidebar
from ui.pages.dashboard import DashboardPage
from ui.pages.sync import SyncPage
from ui.pages.downloads import DownloadsPage
from ui.pages.artists import ArtistsPage
from ui.pages.settings import SettingsPage
from ui.components.toast_manager import ToastManager

logger = get_logger("main")

class ServiceStatusThread(QThread):
    status_updated = pyqtSignal(str, bool)
    
    def __init__(self, spotify_client, plex_client, jellyfin_client, navidrome_client, soulseek_client):
        super().__init__()
        self.spotify_client = spotify_client
        self.plex_client = plex_client
        self.jellyfin_client = jellyfin_client
        self.navidrome_client = navidrome_client
        self.soulseek_client = soulseek_client
        self.running = True
        
        # Import here to avoid circular imports
        from config.settings import config_manager
        self.config_manager = config_manager
    
    def run(self):
        while self.running:
            try:
                # Check Spotify authentication - but don't trigger OAuth
                spotify_status = self.spotify_client.sp is not None
                self.status_updated.emit("spotify", spotify_status)
                
                # Check active media server connection
                active_server = self.config_manager.get_active_media_server()
                if active_server == "plex":
                    server_status = self.plex_client.is_connected()
                    self.status_updated.emit("plex", server_status)
                elif active_server == "jellyfin":
                    # Use the JellyfinClient for status checking
                    jellyfin_status = self.jellyfin_client.is_connected()
                    self.status_updated.emit("jellyfin", jellyfin_status)
                elif active_server == "navidrome":
                    # Use the NavidromeClient for status checking
                    navidrome_status = self.navidrome_client.is_connected()
                    self.status_updated.emit("navidrome", navidrome_status)
                
                # Check Soulseek connection (simplified check to avoid event loop issues)
                soulseek_status = self.soulseek_client.is_configured()
                self.status_updated.emit("soulseek", soulseek_status)
                
                self.msleep(10000)  # Check every 10 seconds (less aggressive)
                
            except Exception as e:
                logger.error(f"Error checking service status: {e}")
                self.msleep(10000)
    
    def stop(self):
        self.running = False
        self.quit()
        self.wait(2000)  # Wait max 2 seconds

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Track application start time for uptime calculation
        self.app_start_time = time.time()
        
        self.spotify_client = SpotifyClient()
        self.plex_client = PlexClient()
        self.jellyfin_client = JellyfinClient()
        self.navidrome_client = NavidromeClient()
        self.soulseek_client = SoulseekClient()
        
        self.status_thread = None
        self.init_ui()
        self.setup_status_monitoring()
        
        # Setup periodic search maintenance (rolling 50-search window)
        self.setup_search_maintenance()
    
    def setup_search_maintenance(self):
        """Setup periodic search history maintenance to keep only the 50 most recent searches"""
        try:
            # Create timer for periodic search maintenance
            self.search_maintenance_timer = QTimer()
            self.search_maintenance_timer.timeout.connect(self._run_search_maintenance)
            
            # Run maintenance every 2 minutes (120 seconds)
            # This keeps search history clean without being too frequent
            self.search_maintenance_timer.start(120000)
            
            logger.info("Search maintenance timer started (every 2 minutes, keeps 200 most recent searches)")
            
        except Exception as e:
            logger.error(f"Error setting up search maintenance: {e}")
    
    def _run_search_maintenance(self):
        """Run search maintenance in background thread to avoid blocking UI"""
        try:
            # Only run if Soulseek client seems to be available
            if hasattr(self.soulseek_client, 'base_url') and self.soulseek_client.base_url:
                # Run maintenance in background thread
                import threading
                
                def maintenance_thread():
                    try:
                        import asyncio
                        loop = asyncio.new_event_loop()
                        asyncio.set_event_loop(loop)
                        
                        # Run the maintenance (keep 200 most recent searches)
                        success = loop.run_until_complete(self.soulseek_client.maintain_search_history(200))
                        
                        if not success:
                            logger.warning("Search maintenance completed with some failures")
                            
                    except Exception as e:
                        logger.error(f"Error in search maintenance thread: {e}")
                    finally:
                        loop.close()
                
                thread = threading.Thread(target=maintenance_thread, daemon=True)
                thread.start()
            else:
                logger.debug("Soulseek client not configured, skipping search maintenance")
                
        except Exception as e:
            logger.error(f"Error running search maintenance: {e}")
    
    def init_ui(self):
        self.setWindowTitle("SoulSync - Music Sync & Manager")
        self.setGeometry(100, 100, 1400, 900)
        
        # Set dark theme palette
        self.setStyleSheet("""
            QMainWindow {
                background: #121212;
            }
        """)
        
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Create sidebar
        self.sidebar = ModernSidebar()
        self.sidebar.page_changed.connect(self.change_page)
        main_layout.addWidget(self.sidebar)
        
        # Create stacked widget for pages
        self.stacked_widget = QStackedWidget()
        
        # Create toast manager
        self.toast_manager = ToastManager(self)
        
        # Create and add pages
        self.dashboard_page = DashboardPage()
        self.downloads_page = DownloadsPage(self.soulseek_client)
        self.sync_page = SyncPage(
            spotify_client=self.spotify_client,
            plex_client=self.plex_client,
            soulseek_client=self.soulseek_client,
            downloads_page=self.downloads_page,
            jellyfin_client=self.jellyfin_client,
            navidrome_client=self.navidrome_client
        )
        self.artists_page = ArtistsPage(downloads_page=self.downloads_page)
        self.settings_page = SettingsPage()
        
        # Set toast manager for pages that need direct access
        self.downloads_page.set_toast_manager(self.toast_manager)
        self.sync_page.set_toast_manager(self.toast_manager)
        self.artists_page.set_toast_manager(self.toast_manager)
        self.settings_page.set_toast_manager(self.toast_manager)
        
        # Configure dashboard with service clients and page references
        self.dashboard_page.set_service_clients(self.spotify_client, self.plex_client, self.jellyfin_client, self.navidrome_client, self.soulseek_client)
        self.dashboard_page.set_page_references(self.downloads_page, self.sync_page)
        self.dashboard_page.set_app_start_time(self.app_start_time)
        self.dashboard_page.set_toast_manager(self.toast_manager)
        
        # Connect download completion signal for session tracking
        self.downloads_page.download_session_completed.connect(
            self.dashboard_page.data_provider.increment_completed_downloads
        )
        
        # Connect sync activities to dashboard
        self.sync_page.sync_activity.connect(
            self.dashboard_page.add_activity_item
        )
        
        # Connect download activities to dashboard
        self.downloads_page.download_activity.connect(
            self.dashboard_page.add_activity_item
        )
        
        # --- ADD THESE TWO LINES TO FIX THE UI UPDATE ---
        self.sync_page.database_updated_externally.connect(self.dashboard_page.database_updated_externally)
        self.artists_page.database_updated_externally.connect(self.dashboard_page.database_updated_externally)
        # ------------------------------------------------
        
        self.stacked_widget.addWidget(self.dashboard_page)
        self.stacked_widget.addWidget(self.sync_page)
        self.stacked_widget.addWidget(self.downloads_page)
        self.stacked_widget.addWidget(self.artists_page)
        self.stacked_widget.addWidget(self.settings_page)
        
        main_layout.addWidget(self.stacked_widget)
        
        # Set dashboard as default page
        self.change_page("dashboard")
        
        # Connect media player signals between sidebar and downloads page
        self.setup_media_player_connections()
        
        # Connect settings change signals for live updates
        self.setup_settings_connections()
    
    def setup_status_monitoring(self):
        # Start status monitoring thread
        self.status_thread = ServiceStatusThread(
            self.spotify_client,
            self.plex_client,
            self.jellyfin_client,
            self.navidrome_client,
            self.soulseek_client
        )
        self.status_thread.status_updated.connect(self.update_service_status)
        self.status_thread.start()
    
    def setup_media_player_connections(self):
        """Connect signals between downloads page and sidebar media player"""
        # Connect downloads page signals to sidebar media player
        self.downloads_page.track_started.connect(self.sidebar.media_player.set_track_info)
        self.downloads_page.track_paused.connect(lambda: self.sidebar.media_player.set_playing_state(False))
        self.downloads_page.track_resumed.connect(lambda: self.sidebar.media_player.set_playing_state(True))
        self.downloads_page.track_stopped.connect(self.sidebar.media_player.clear_track)
        self.downloads_page.track_finished.connect(self.sidebar.media_player.clear_track)
        
        # Connect loading animation signals
        self.downloads_page.track_loading_started.connect(lambda result: self.sidebar.media_player.show_loading())
        self.downloads_page.track_loading_finished.connect(lambda result: self.sidebar.media_player.hide_loading())
        self.downloads_page.track_loading_progress.connect(lambda progress, result: self.sidebar.media_player.set_loading_progress(progress))
        
        # Connect sidebar media player signals to downloads page
        self.sidebar.media_player.play_pause_requested.connect(self.downloads_page.handle_sidebar_play_pause)
        self.sidebar.media_player.stop_requested.connect(self.downloads_page.handle_sidebar_stop)
        self.sidebar.media_player.volume_changed.connect(self.downloads_page.handle_sidebar_volume)
        
        logger.info("Media player connections established between sidebar and downloads page")
    
    def setup_settings_connections(self):
        """Connect settings change signals for live updates across pages"""
        self.settings_page.settings_changed.connect(self.on_settings_changed)
        logger.info("Settings change connections established")
    
    def on_settings_changed(self, key: str, value: str):
        """Handle settings changes and broadcast to relevant pages"""
        # Reinitialize service clients when their settings change
        if key.startswith('spotify.'):
            try:
                self.spotify_client._setup_client()
            except Exception as e:
                logger.error("Failed to reinitialize Spotify client")
        
        elif key.startswith('plex.'):
            try:
                # Reset Plex connection to force reconnection with new settings
                self.plex_client.server = None
                self.plex_client.music_library = None
                self.plex_client._connection_attempted = False
            except Exception as e:
                logger.error("Failed to reset Plex client")
        
        elif key.startswith('soulseek.'):
            try:
                self.soulseek_client._setup_client()
            except Exception as e:
                logger.error("Failed to reinitialize Soulseek client")
        
        # Broadcast to all pages that need to know about path changes
        if hasattr(self.downloads_page, 'on_paths_updated'):
            self.downloads_page.on_paths_updated(key, value)
        if hasattr(self.artists_page, 'on_paths_updated'):
            self.artists_page.on_paths_updated(key, value)
    
    def change_page(self, page_id: str):
        page_map = {
            "dashboard": 0,
            "sync": 1,
            "downloads": 2,
            "artists": 3,
            "settings": 4
        }
        
        if page_id in page_map:
            self.stacked_widget.setCurrentIndex(page_map[page_id])
            logger.info(f"Changed to page: {page_id}")
    
    def update_service_status(self, service: str, connected: bool):
        self.sidebar.update_service_status(service, connected)
        
        # Update dashboard with service status
        if hasattr(self.dashboard_page, 'data_provider'):
            self.dashboard_page.data_provider.update_service_status(service, connected)
        
        # Force a refresh of the Spotify client if needed
        if service == "spotify" and not connected:
            try:
                self.spotify_client._setup_client()
            except Exception as e:
                logger.error(f"Error refreshing Spotify client: {e}")
    
    def closeEvent(self, event):
        logger.info("Clo
... [TRUNCATED]
```

### File: README.md
```md
<p align="center">
  <img src="./assets/trans.png" alt="SoulSync Logo">
</p>

# SoulSync - Intelligent Music Discovery & Automation Platform

**Spotify-quality music discovery for self-hosted libraries.** Automates downloads, curates playlists, monitors artists, and organizes your collection with zero manual effort.

> **IMPORTANT**: Configure file sharing in slskd to avoid Soulseek bans. Set up shared folders at `http://localhost:5030/shares`.

**Community**: [Discord](https://discord.gg/wGvKqVQwmy) | **Support**: [GitHub Issues](https://github.com/Nezreka/SoulSync/issues) | **Donate**: [Ko-fi](https://ko-fi.com/boulderbadgedad)

---

## What It Does

SoulSync bridges streaming services to your media server with automated discovery:

1. **Monitors artists** → Automatically detects new releases from your watchlist
2. **Generates playlists** → Release Radar, Discovery Weekly, Seasonal, Decade/Genre mixes, Cache-powered discovery
3. **Downloads missing tracks** → From Soulseek, Deezer, Tidal, Qobuz, HiFi, YouTube, or any combination via Hybrid mode
4. **Verifies downloads** → AcoustID fingerprinting for P2P sources (skipped for trusted API sources)
5. **Enriches metadata** → 9 enrichment workers (Spotify, MusicBrainz, iTunes, Deezer, AudioDB, Last.fm, Genius, Tidal, Qobuz)
6. **Tags consistently** → Picard-style MusicBrainz release preflight ensures all album tracks get the same release ID
7. **Organizes files** → Custom templates for clean folder structures
8. **Syncs media server** → Plex, Jellyfin, or Navidrome stay updated automatically
9. **Scrobbles plays** → Automatic scrobbling to Last.fm and ListenBrainz from your media server

---

## Key Features

<p align="center">
  <img src="./assets/pages.gif" alt="SoulSync Interface">
</p>

### Discovery Engine

**Release Radar** — New tracks from watchlist artists, personalized by listening history

**Discovery Weekly** — 50 tracks from similar artists with serendipity weighting

**Seasonal Playlists** — Halloween, Christmas, Valentine's, Summer, Spring, Autumn (hemisphere-aware)

**Personalized Playlists** (12+ types)
- Recently Added, Top Tracks, Forgotten Favorites
- Decade Playlists (1960s-2020s), Genre Playlists (15+ categories)
- Because You Listen To, Daily Mixes, Hidden Gems, Popular Picks, Discovery Shuffle, Familiar Favorites
- Custom Playlist Builder (1-5 seed artists → similar artists → random albums → shuffled tracks)

**Cache-Powered Discovery** (zero API calls)
- Undiscovered Albums — albums by your most-played artists that aren't in your library
- New In Your Genres — recently released albums matching your top genres
- From Your Labels — popular albums on labels already in your library
- Deep Cuts — low-popularity tracks from artists you listen to
- Genre Explorer — genre landscape pills with artist counts, tap for Genre Deep Dive modal

**ListenBrainz** — Import recommendation and community playlists

**Beatport** — Full electronic music integration with genre browser (39+ genres)

### Multi-Source Downloads

**6 Download Sources**: Soulseek, Deezer, Tidal, Qobuz, HiFi, YouTube — use any single source or Hybrid mode with drag-to-reorder priority

**Deezer Downloads** — ARL token authentication, FLAC lossless / MP3 320 / MP3 128 with automatic quality fallback and Blowfish decryption

**Tidal Downloads** — Device-flow OAuth, quality tiers from AAC 96kbps to FLAC 24-bit/96kHz Hi-Res

**Qobuz Downloads** — Email/password auth, quality up to Hi-Res Max (FLAC 24-bit/192kHz)

**HiFi Downloads** — Free lossless via public API instances, no account required

**Soulseek** — FLAC priority with quality profiles, peer quality scoring, source reuse for album consistency

**YouTube** — Audio extraction with cookie-based bot detection bypass

**Hybrid Mode** — Enable any combination of sources, drag to set priority order, automatic fallback chain

**Playlist Sources**: Spotify, Tidal, YouTube, Deezer, Beatport charts, ListenBrainz, Spotify Link (no API needed)

**Post-Download**
- Lossy copy creation: MP3, Opus, AAC with configurable bitrate (Opus capped at 256kbps)
- Hi-Res FLAC downsampling to 16-bit/44.1kHz CD quality
- Blasphemy Mode — delete original FLAC after conversion
- Synchronized lyrics (LRC) via LRClib
- Picard-style album consistency — pre-flight MusicBrainz release lookup ensures all tracks get the same release ID

### Listening Stats & Scrobbling

**Listening Stats Page** — Full dashboard with Chart.js visualizations
- Overview cards: total plays, listening time, unique artists/albums/tracks
- Timeline bar chart, genre breakdown donut with legend
- Top artists visual bubbles, top albums and tracks with play buttons and cover art
- Library health: format breakdown bar, enrichment coverage rings, database storage chart
- Time range filters: 7 days, 30 days, 12 months, all time

**Scrobbling** — Automatic Last.fm and ListenBrainz scrobbling from Plex, Jellyfin, or Navidrome

### Audio Verification

**AcoustID Fingerprinting** (optional) — Verifies downloaded files match expected tracks
- Automatically skipped for trusted API sources (Deezer, Tidal, Qobuz, HiFi)
- Only runs for P2P (Soulseek) and extracted audio (YouTube) where mislabeling is possible
- Fail-open design: verification errors never block downloads

### Metadata & Enrichment

**9 Background Enrichment Workers**: Spotify, MusicBrainz, iTunes, Deezer, AudioDB, Last.fm, Genius, Tidal, Qobuz
- Each worker independently processes artists, albums, and tracks
- Pause/resume controls on dashboard, auto-pause during database scans
- Error items don't auto-retry in infinite loops (fixed in v2.1)

**Dual-Source Metadata**
- Primary: Spotify — richer data, discovery features, playlist sync
- Fallback: iTunes/Apple Music or Deezer — configurable, no authentication required
- MusicBrainz enrichment with Picard-style album consistency

**Post-Processing Tag Embedding**
- Granular per-service tag toggles (18+ MusicBrainz tags, Spotify/iTunes/Deezer IDs, AudioDB mood/style, Tidal/Qobuz ISRCs, Last.fm tags, Genius URLs)
- Album art embedding, cover.jpg download
- Spotify rate limit protection across all API calls

### Advanced Matching Engine

- Version-aware matching: strictly rejects remixes when you want the original (and vice versa)
- Unicode and accent handling (KoЯn, Bjork, A$AP Rocky)
- Fuzzy matching with weighted confidence scoring (title, artist, duration)
- Album variation detection (Deluxe, Remastered, Taylor's Version, etc.)
- Streaming source results bypass filename-matching engine (API results trusted directly)
- Short title protection: prevents "Love" from matching "Loveless"

### Automation

**Automation Engine** — Visual drag-and-drop builder for custom workflows
- **Triggers**: Schedule, Daily/Weekly Time, Track Downloaded, Batch Complete, Playlist Changed, Discovery Complete, Signal Received, and 10+ more
- **Actions**: Process Wishlist, Scan Watchlist, Refresh Mirrored, Discover Playlist, Sync Playlist, Scan Library, Database Update, Quality Scan, Full Cleanup, and more
- **Then Actions**: Fire Signal (chain automations), Discord, Telegram, Pushbullet notifications
- **Pipelines**: 11 pre-built one-click pipeline deployments (Release Radar, Discovery Weekly, Nightly Operations, etc.)
- **Signal Chains**: playlist_id forwarded from events to action handlers for proper chain execution

**Watchlist** — Monitor unlimited artists with per-artist configuration
- Release type filters: Albums, EPs, Singles
- Content filters: Live, Remixes, Acoustic, Compilations
- Auto-discover similar artists, periodic scanning

**Wishlist** — Failed downloads automatically queued for retry with auto-processing

**Mirrored Playlists** — Mirror from Spotify, Tidal, YouTube, Deezer and keep synced
- Automatic refresh detects changes, discovery pipeline matches metadata
- Followed Spotify playlists with 403 errors fall back to public embed scraper

**Local Profiles** — Multiple configuration profiles with isolated settings, watchlists, and playlists

### Library Management

**Dashboard** — Service status, system stats, activity feed, enrichment worker controls
- Unified glass UI design across all tool cards, service cards, and stat cards

**Library Page** — Artist grid with staggered card animations, per-artist enrichment coverage rings
- Artist Radio button — play random track with auto-queue radio mode
- Play buttons on Last.fm top tracks sidebar

**Enhanced Library Manager** — Toggle between Standard and Enhanced views
- Inline metadata editing, per-service manual matching
- Write Tags to File (MP3/FLAC/OGG/M4A), tag preview with diff
- Server sync after tag writes (Plex, Jellyfin, Navidrome)
- Bulk operations, sortable columns, multi-disc support

**Library Maintenance** — 10+ automated repair jobs
- Track Number, Dead Files, Duplicates, Metadata Gaps, Album Completeness, Missing Cover Art, AcoustID Scanner, Orphan Files, Fake Lossless, Library Reorganize, Lossy Converter, MBID Mismatch, Album Tag Consistency
- Enrichment workers auto-pause during database scans
- One-click Fix All with findings dashboard

**Database Storage Visualization** — Donut chart showing per-table storage breakdown

**Import System** — Tag-first matching, auto-grouped album cards, staging folder workflow

**Template Organization** — `$albumartist/$album/$track - $title` and 10+ variables

### Built-in Media Player

- Stream tracks from your library with queue system
- Now Playing modal with album art ambient glow and Web Audio visualizer
- Smart Radio mode — auto-queue similar tracks by genre, mood, and style
- Repeat modes, shuffle, keyboard shortcuts, Media Session API

### Mobile Responsive

- Comprehensive mobile layouts for Stats, Automations, Hydrabase, Issues, Help pages
- Artist hero section, enhanced library track table with bottom sheet action popover
- Enrichment rings, filter bars, and discover cards all adapt to narrow screens

---

## Installation

### Docker (Recommended)

```bash
curl -O https://raw.githubusercontent.com/Nezreka/SoulSync/main/docker-compose.yml
docker-compose up -d
# Access at http://localhost:8008
```

### Unraid

SoulSync is available as an Unraid template. Install from Community Applications or manually add the template from:
```
https://raw.githubusercontent.com/Nezreka/SoulSync/main/templates/soulsync.xml
```

PUID/PGID are exposed in the template — set them to match your Unraid permissions (default: 99/100 for nobody/users).

### Python (No Docker)

```bash
git clone https://github.com/Nezreka/SoulSync
cd SoulSync
pip install -r requirements-webui.txt
python web_server.py
# Open http://localhost:8008
```

---

## Setup Guide

### Prerequisites

- **slskd** running and accessible ([Download](https://github.com/slskd/slskd/releases)) — required for Soulseek downloads
- **Spotify API** credentials ([Dashboard](https://developer.spotify.com/dashboard)) — optional but recommended for discovery
- **Media Server** (optional): Plex, Jellyfin, or Navidrome
- **Deezer ARL token** (optional): For Deezer downloads — get from browser cookies after logging into deezer.com
- **Tidal account** (optional): For Tidal downloads — authenticate via device flow in Settings
- **Qobuz account** (optional): For Qobuz downloads — email/password login in Settings

### Step 1: Set Up slskd

SoulSync talks to slskd through its API. See the [slskd setup guide](https://github.com/slskd/slskd) for API key configuration.

1. Add an API key in slskd's `settings.yml` under `web > authentication > api_keys`
2. Restart slskd
3. Paste the key into SoulSync's Settings → Downloads → Soulseek section

**Configure file sharing in slskd to avoid Soulseek bans.** Set up shared folders at `http://localhost:5030/shares`.

### Step 2: Set Up Spotify API (Optional)

Spotify gives you the best discovery features. Without it, SoulSync falls back to iTunes/Deezer for metadata.

1. Create an app at [developer.spotify.com/dashboard](https://developer.spotify.com/dashboard)
2. Add Redirect URI: `http://127.0.0.1:8888/callback`
3. Copy Client ID and Client Secret into SoulSync Settings

More detail in [Support/DOCKER-OAUTH-FIX.md](Support/DOCKER-OAUTH-FIX.md).

### Step 3: Configure SoulSync

Open SoulSync at `http://localhost:8008` and go to Settings.

**Download Source**: Choose your preferred source (Soulseek, Deezer, Tidal, Qobuz, HiFi, YouTube, or Hybrid)

**Paths**:
- **Download Path**: Container path to slskd's download folder (e.g., `/app/downloads`)
- **Transfer Path**: Where organized music goes (e.g., `/app/Transfer`)
- **Staging Path**: Optional import folder (e.g., `/app/Staging`)

**Media Server** (optional): Use your machine's actual IP (not `localhost` — that means inside the container)

### Step 4: Docker Path Mapping

| What | Container Path | Host Path |
|------|---------------|-----------|
| Config | `/app/config` | Your config folder |
| Logs | `/app/logs` | Your logs folder |
| Database | `/app/data` | Named volume (recommended) |
| Downloads | `/app/downloads` | Same folder slskd downloads to |
| Transfer | `/app/Transfer` | Where organized music goes |
| Staging | `/app/Staging` | Optional import folder |

**Important:** Use a named volume for the database (`soulsync_database:/app/data`). Direct host path mounts to `/app/data` can overwrite Python module files.

---

## Comparison

| Feature | SoulSync | Lidarr | Headphones | Beets |
|---------|----------|--------|------------|-------|
| Custom Discovery Playlists (15+) | ✓ | ✗ | ✗ | ✗ |
| Cache-Powered Discovery (zero API) | ✓ | ✗ | ✗ | ✗ |
| Listening Stats Dashboard | ✓ | ✗ | ✗ | ✗ |
| Last.fm/ListenBrainz Scrobbling | ✓ | ✗ | ✗ | ✗ |
| 6 Download Sources | ✓ | ✗ | ✗ | ✗ |
| Deezer Downloads (FLAC) | ✓ | ✗ | ✗ | ✗ |
| Tidal Downloads (Hi-Res) | ✓ | ✗ | ✗ | ✗ |
| Qobuz Downloads (Hi-Res Max) | ✓ | ✗ | ✗ | ✗ |
| Soulseek Downloads | ✓ | ✗ | ✗ | ✗ |
| Beatport Integration | ✓ | ✗ | ✗ | ✗ |
| Audio Fingerprint Verification | ✓ | ✗ | ✗ | ✓ |
| 9 Enrichment Workers | ✓ | ✗ | ✗ | Plugin |
| Picard-Style Album Tagging | ✓ | ✗ | ✗ | ✗ |
| Visual Automation Builder | ✓ | ✗ | ✗ | ✗ |
| Enhanced Library Manager | ✓ | ✗ | ✗ | ✗ |
| Library Maintenance Suite (10+ jobs) | ✓ | ✗ | ✗ | ✓ |
| Multi-Profile Support | ✓ | ✗ | ✗ | ✗ |
| Mobile Responsive | ✓ | ✓ | ✗ | ✗ |
| Built-in Media Player + Radio | ✓ | ✗ | ✗ | ✗ |

---

## Architecture

**Scale**: ~120,000 lines across Python backend and JavaScript frontend, 80+ API endpoints, handles 10,000+ album libraries

**Integrations**: Spotify, iTunes/Apple Music, Deezer, Tidal, Qobuz, YouTube, Soulseek (slskd), HiFi, Beatport, ListenBrainz, MusicBrainz, AcoustID, AudioDB, Last.fm, Genius, LRClib, music-map.com, Plex, Jellyfin, Navidrome

**Stack**: Python 3.11, Flask, SQLite (WAL mode), vanilla JavaScript SPA, Chart.js

**Core Components**:
- **Matching Engine** — version-aware fuzzy matching with streaming source bypass
- **Download Orchestrator** — routes between 6 sources with hybrid fallback and batch processing
- **Discovery System** — 
... [TRUNCATED]
```

### File: requirements.txt
```txt
PyQt6[multimedia]>=6.6.0
spotipy>=2.23.0
PlexAPI>=4.17.0
requests>=2.31.0
asyncio-mqtt>=0.16.0
python-dotenv>=1.0.0
cryptography>=41.0.0
mutagen>=1.47.0
Pillow>=10.0.0
aiohttp>=3.9.0
unidecode>=1.3.8
yt-dlp>=2024.12.13
Flask>=3.0.0
Flask-Limiter>=3.5.0
lrclibapi>=0.3.1
pyacoustid>=1.3.0
```

### File: entrypoint.sh
```sh
#!/bin/bash
# SoulSync Docker Entrypoint Script
# Handles PUID/PGID/UMASK configuration for proper file permissions

set -e

# Default values
PUID=${PUID:-1000}
PGID=${PGID:-1000}
UMASK=${UMASK:-022}

echo "🐳 SoulSync Container Starting..."
echo "📝 User Configuration:"
echo "   PUID: $PUID"
echo "   PGID: $PGID"
echo "   UMASK: $UMASK"

# Get current soulsync user/group IDs
CURRENT_UID=$(id -u soulsync)
CURRENT_GID=$(id -g soulsync)

# Only modify user/group if they differ from requested values
if [ "$CURRENT_UID" != "$PUID" ] || [ "$CURRENT_GID" != "$PGID" ]; then
    echo "🔧 Adjusting user permissions..."

    # Modify group ID if needed
    if [ "$CURRENT_GID" != "$PGID" ]; then
        echo "   Changing group ID from $CURRENT_GID to $PGID"
        groupmod -o -g "$PGID" soulsync
    fi

    # Modify user ID if needed
    if [ "$CURRENT_UID" != "$PUID" ]; then
        echo "   Changing user ID from $CURRENT_UID to $PUID"
        usermod -o -u "$PUID" soulsync
    fi

    # Fix ownership of app directories
    echo "🔒 Fixing permissions on app directories..."
    chown -R soulsync:soulsync /app/config /app/data /app/logs /app/downloads /app/Transfer /app/Staging 2>/dev/null || true
else
    echo "✅ User/Group IDs already correct"
fi

# Set umask for file creation permissions
echo "🎭 Setting UMASK to $UMASK"
umask "$UMASK"

# Initialize config files if they don't exist (first-time setup)
echo "🔍 Checking for configuration files..."

if [ ! -f "/app/config/config.json" ]; then
    echo "   📄 Creating default config.json..."
    cp /defaults/config.json /app/config/config.json
    chown soulsync:soulsync /app/config/config.json 2>/dev/null || true
else
    echo "   ✅ config.json already exists"
fi

# Always update settings.py — it's application code, not user configuration.
# Stale versions from older releases cause startup crashes (missing methods).
echo "   📄 Updating settings.py to current version..."
cp /defaults/settings.py /app/config/settings.py
chown soulsync:soulsync /app/config/settings.py 2>/dev/null || true

# Ensure all directories exist and have proper permissions
mkdir -p /app/config /app/data /app/logs /app/downloads /app/Transfer /app/Staging
chown -R soulsync:soulsync /app/config /app/data /app/logs /app/downloads /app/Transfer /app/Staging 2>/dev/null || true

echo "✅ Configuration initialized successfully"

# Auto-update yt-dlp — YouTube changes their API frequently and stale versions break downloads
echo "🔄 Updating yt-dlp..."
pip install -U yt-dlp --quiet --no-cache-dir 2>/dev/null && echo "   ✅ yt-dlp updated" || echo "   ⚠️ yt-dlp update failed (will use existing version)"

# Display final user info
echo "👤 Running as:"
echo "   User: $(id -u soulsync):$(id -g soulsync) ($(id -un soulsync):$(id -gn soulsync))"
echo "   UMASK: $(umask)"
echo ""
echo "🚀 Starting SoulSync Web Server..."

# Execute the main command as the soulsync user
# If already running as the correct user (e.g. Podman rootless with keep-id), skip gosu
if [ "$(id -u)" = "$PUID" ]; then
    exec "$@"
else
    exec gosu soulsync "$@"
fi

```

### File: license.txt
```txt
Copyright (c) [2025] [SoulSync]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### File: requirements-webui.txt
```txt
# SoulSync WebUI Requirements
# Docker-compatible requirements without PyQt6 dependencies

# Core web framework
Flask>=3.0.0
Flask-Limiter>=3.5.0

# Music service APIs
spotipy>=2.23.0
PlexAPI>=4.17.0

# HTTP and async support  
requests>=2.31.0
aiohttp>=3.9.0

# Configuration management
python-dotenv>=1.0.0

# Security and encryption
cryptography>=41.0.0

# Media metadata handling
mutagen>=1.47.0
Pillow>=10.0.0

# Text processing
unidecode>=1.3.8
beautifulsoup4>=4.12.0

# System monitoring
psutil>=6.0.0

# YouTube support
yt-dlp>=2024.12.13

# Lyrics support
lrclibapi>=0.3.1

# Optional: MQTT support (for future features)
asyncio-mqtt>=0.16.0

# Audio fingerprinting for download verification
pyacoustid>=1.3.0

# WebSocket client for Hydrabase connection
websocket-client>=1.7.0

# Tidal download support
tidalapi>=0.7.6

# WebSocket server for real-time UI updates
flask-socketio>=5.3.0
```

### File: test_acoustid.py
```py
#!/usr/bin/env python3
"""
AcoustID Integration Test Script

Run this script to test the AcoustID verification system before using it in production.
It will check:
1. fpcalc binary availability
2. API key validation
3. Fingerprint generation (if audio file provided)
4. Full verification flow (if audio file and expected track info provided)

Usage:
    python test_acoustid.py                          # Basic tests
    python test_acoustid.py path/to/audio.mp3        # Test with audio file
    python test_acoustid.py path/to/audio.mp3 "Song Title" "Artist Name"  # Full test
"""

import sys
import os
import io

# Fix Windows encoding issues
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pathlib import Path


def print_header(text):
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60)


def print_result(success, message):
    icon = "[PASS]" if success else "[FAIL]"
    print(f"  {icon} {message}")


def test_chromaprint():
    """Test if chromaprint/fpcalc is available for fingerprinting."""
    print_header("Testing fingerprint backend availability")

    from core.acoustid_client import CHROMAPRINT_AVAILABLE, ACOUSTID_AVAILABLE, FPCALC_PATH

    if not ACOUSTID_AVAILABLE:
        print_result(False, "pyacoustid library not installed!")
        print("\n  To install:")
        print("    pip install pyacoustid")
        return False

    if CHROMAPRINT_AVAILABLE and FPCALC_PATH:
        print_result(True, f"fpcalc ready: {FPCALC_PATH}")
        return True

    if CHROMAPRINT_AVAILABLE:
        print_result(True, "Fingerprint backend available")
        return True

    print_result(False, "No fingerprint backend available!")
    print("\n  fpcalc will be auto-downloaded on first use.")
    print("  Or manually install:")
    print("    - Windows: Auto-download supported")
    print("    - macOS: brew install chromaprint")
    print("    - Linux: apt install libchromaprint-tools")
    return False


def test_api_key():
    """Test if AcoustID API key is configured and valid."""
    print_header("Testing AcoustID API key")

    from core.acoustid_client import AcoustIDClient
    from config.settings import config_manager

    api_key = config_manager.get('acoustid.api_key', '')

    if not api_key:
        print_result(False, "No API key configured in settings")
        print("\n  To configure:")
        print("    1. Get a free API key from https://acoustid.org/new-application")
        print("    2. Add it in Settings > AcoustID section")
        return False

    print(f"  API key found: {api_key[:8]}...{api_key[-4:]}")

    client = AcoustIDClient()
    success, message = client.test_api_key()

    print_result(success, message)
    return success


def test_enabled():
    """Test if AcoustID verification is enabled."""
    print_header("Testing AcoustID enabled status")

    from config.settings import config_manager

    enabled = config_manager.get('acoustid.enabled', False)

    if enabled:
        print_result(True, "AcoustID verification is ENABLED")
    else:
        print_result(False, "AcoustID verification is DISABLED")
        print("\n  To enable:")
        print("    1. Go to Settings > AcoustID section")
        print("    2. Check 'Enable Download Verification'")

    return enabled


def test_availability():
    """Test overall availability."""
    print_header("Testing overall availability")

    from core.acoustid_client import AcoustIDClient

    client = AcoustIDClient()
    available, reason = client.is_available()

    print_result(available, reason)
    return available


def test_fingerprint_and_lookup(audio_file):
    """Test fingerprint generation and AcoustID lookup for an audio file."""
    print_header(f"Testing fingerprint and AcoustID lookup")
    print(f"  File: {audio_file}")

    if not os.path.isfile(audio_file):
        print_result(False, f"File not found: {audio_file}")
        return None

    from core.acoustid_client import AcoustIDClient

    client = AcoustIDClient()

    available, reason = client.is_available()
    if not available:
        print_result(False, f"AcoustID not available: {reason}")
        return None

    print("  Fingerprinting and looking up (this may take a moment)...")
    result = client.fingerprint_and_lookup(audio_file)

    if result:
        recordings = result.get('recordings', [])
        score = result.get('best_score', 0)
        print_result(True, f"Found {len(recordings)} recording(s) (score: {score:.2f})")

        for i, rec in enumerate(recordings[:5]):  # Show first 5
            title = rec.get('title', '?')
            artist = rec.get('artist', '?')
            mbid = rec.get('mbid', '?')
            rec_score = rec.get('score', 0)
            print(f"    {i+1}. \"{title}\" by {artist} (score: {rec_score:.2f})")
            print(f"       https://musicbrainz.org/recording/{mbid}")

        if len(recordings) > 5:
            print(f"    ... and {len(recordings) - 5} more")

        return result
    else:
        print_result(False, "Track not found in AcoustID database")
        print("  This may be a rare/new track not yet fingerprinted.")
        return None


def test_musicbrainz_lookup(track_name, artist_name):
    """Test MusicBrainz lookup for expected track."""
    print_header("Testing MusicBrainz lookup")
    print(f"  Track: '{track_name}'")
    print(f"  Artist: '{artist_name}'")

    try:
        from database.music_database import MusicDatabase
        from core.musicbrainz_service import MusicBrainzService

        db = MusicDatabase()
        mb_service = MusicBrainzService(db)

        print("  Searching MusicBrainz...")
        result = mb_service.match_recording(track_name, artist_name)

        if result:
            mbid = result.get('mbid')
            confidence = result.get('confidence', 0)
            cached = result.get('cached', False)

            print_result(True, f"Found match (confidence: {confidence}%)")
            print(f"    MBID: {mbid}")
            print(f"    https://musicbrainz.org/recording/{mbid}")
            print(f"    Cached: {cached}")
            return result
        else:
            print_result(False, "No match found in MusicBrainz")
            return None

    except Exception as e:
        print_result(False, f"Error: {e}")
        return None


def test_full_verification(audio_file, track_name, artist_name):
    """Test the full verification flow."""
    print_header("Testing full verification flow")
    print(f"  File: {audio_file}")
    print(f"  Expected: '{track_name}' by '{artist_name}'")

    from core.acoustid_verification import AcoustIDVerification, VerificationResult

    verifier = AcoustIDVerification()

    # Check availability first
    available, reason = verifier.quick_check_available()
    if not available:
        print_result(False, f"Verification not available: {reason}")
        return

    print("  Running verification (this may take a moment)...")
    result, message = verifier.verify_audio_file(
        audio_file,
        track_name,
        artist_name
    )

    if result == VerificationResult.PASS:
        print_result(True, f"VERIFICATION PASSED: {message}")
    elif result == VerificationResult.FAIL:
        print_result(False, f"VERIFICATION FAILED: {message}")
    elif result == VerificationResult.SKIP:
        print(f"  [SKIP] Verification skipped: {message}")
    else:
        print(f"  [????] Unknown result: {result.value} - {message}")


def main():
    print("\n" + "=" * 60)
    print("  ACOUSTID VERIFICATION SYSTEM TEST")
    print("=" * 60)

    # Parse arguments
    audio_file = sys.argv[1] if len(sys.argv) > 1 else None
    track_name = sys.argv[2] if len(sys.argv) > 2 else None
    artist_name = sys.argv[3] if len(sys.argv) > 3 else None

    # Run basic tests
    chromaprint_ok = test_chromaprint()
    api_key_ok = test_api_key()
    enabled_ok = test_enabled()
    available_ok = test_availability()

    # Summary of basic tests
    print_header("Basic Tests Summary")
    print(f"  Chromaprint: {'OK' if chromaprint_ok else 'MISSING'}")
    print(f"  API key:     {'OK' if api_key_ok else 'MISSING/INVALID'}")
    print(f"  Enabled:     {'YES' if enabled_ok else 'NO'}")
    print(f"  Available:   {'YES' if available_ok else 'NO'}")

    if not audio_file:
        print("\n" + "-" * 60)
        print("  To test fingerprinting, provide an audio file:")
        print("    python test_acoustid.py path/to/audio.mp3")
        print("\n  To test full verification flow:")
        print("    python test_acoustid.py path/to/audio.mp3 \"Song Title\" \"Artist\"")
        print("-" * 60)
        return

    # Test with audio file (combined fingerprint + lookup)
    lookup_result = test_fingerprint_and_lookup(audio_file)

    if track_name and artist_name:
        # Test MusicBrainz lookup
        mb_result = test_musicbrainz_lookup(track_name, artist_name)

        # Test full verification
        if available_ok:
            test_full_verification(audio_file, track_name, artist_name)
        else:
            print("\n  Skipping full verification test (not available)")

    # Point to log file
    print("\n" + "-" * 60)
    log_path = Path(__file__).parent / "logs" / "acoustid.log"
    print(f"  Detailed logs: {log_path}")
    print("-" * 60 + "\n")


if __name__ == "__main__":
    main()

```

### File: test_hifi_client.py
```py
"""
Comprehensive tests for HiFi API Client (core/hifi_client.py).

Tests the client against live public hifi-api instances to validate:
- Instance availability and API versioning
- Track search (by title, artist, album, combined queries)
- Stream URL retrieval and base64 manifest decoding
- Album lookup and track listing
- Artist lookup
- Quality tier selection and fallback chain
- Instance failover when one goes down
- TrackResult / DownloadStatus compatibility with Soulseek interfaces
- Actual file download (small test track)
- Rate limiting behavior
- Error handling (bad IDs, empty queries, malformed data)
- Download lifecycle: start → progress → complete/cancel/error

Usage:
    python test_hifi_client.py                  # Run all tests
    python test_hifi_client.py -k search        # Run only search tests
    python test_hifi_client.py -v               # Verbose output
"""

import os
import sys
import json
import time
import asyncio
import tempfile
import shutil
import threading
from pathlib import Path
from unittest.mock import patch, MagicMock
from dataclasses import dataclass

import pytest

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.hifi_client import (
    HiFiClient,
    HIFI_QUALITY_MAP,
    DEFAULT_INSTANCES,
)
from core.soulseek_client import TrackResult, AlbumResult, DownloadStatus


# ===================== Fixtures =====================

@pytest.fixture(scope="session")
def temp_download_dir():
    """Create a temporary download directory for the entire test session."""
    d = tempfile.mkdtemp(prefix="hifi_test_")
    yield d
    shutil.rmtree(d, ignore_errors=True)


@pytest.fixture
def client(temp_download_dir):
    """Create a fresh HiFiClient for each test."""
    c = HiFiClient(download_path=temp_download_dir)
    return c


@pytest.fixture(scope="session")
def shared_client(temp_download_dir):
    """Shared client for read-only tests (avoids excessive instance creation)."""
    return HiFiClient(download_path=temp_download_dir)


@pytest.fixture
def event_loop():
    """Create an event loop for async tests."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


def run_async(coro):
    """Helper to run an async function synchronously."""
    loop = asyncio.new_event_loop()
    try:
        return loop.run_until_complete(coro)
    finally:
        loop.close()


# ===================== 1. Instance & Availability Tests =====================

class TestInstanceManagement:
    """Tests for API instance management and availability."""

    def test_01_default_instances_populated(self, client):
        """Client should have default instances loaded."""
        assert len(client._instances) >= 1
        assert client._current_instance is not None

    def test_02_custom_instance_priority(self, temp_download_dir):
        """Custom base_url should be first in instance list."""
        custom = "https://my-custom-instance.example.com"
        c = HiFiClient(download_path=temp_download_dir, base_url=custom)
        assert c._instances[0] == custom
        assert c._current_instance == custom

    def test_03_custom_instance_trailing_slash(self, temp_download_dir):
        """Trailing slash should be stripped from custom instance URL."""
        custom = "https://my-custom-instance.example.com/"
        c = HiFiClient(download_path=temp_download_dir, base_url=custom)
        assert c._instances[0] == "https://my-custom-instance.example.com"

    def test_04_is_available(self, shared_client):
        """At least one public instance should be reachable."""
        assert shared_client.is_available(), "No HiFi API instance is reachable"

    def test_05_get_version(self, shared_client):
        """Should return a version string from the API."""
        version = shared_client.get_version()
        # version may be None if endpoint doesn't expose it, that's okay
        # but the call shouldn't crash
        if version:
            assert isinstance(version, str)

    def test_06_instance_rotation(self, temp_download_dir):
        """Rotating an instance should move it to the back."""
        c = HiFiClient(download_path=temp_download_dir)
        first = c._instances[0]
        second = c._instances[1] if len(c._instances) > 1 else None

        c._rotate_instance(first)

        assert c._instances[-1] == first
        if second:
            assert c._current_instance == second

    def test_07_rotate_nonexistent_instance(self, client):
        """Rotating a URL not in the list shouldn't crash."""
        original_first = client._current_instance
        client._rotate_instance("https://nonexistent.example.com")
        assert client._current_instance == original_first

    def test_08_all_instances_exhausted(self, temp_download_dir):
        """_api_get should return None when all instances fail."""
        c = HiFiClient(download_path=temp_download_dir)
        c._instances = ["https://definitely-not-real-1.invalid", "https://definitely-not-real-2.invalid"]
        c._current_instance = c._instances[0]
        c._min_interval = 0  # No rate limiting in test

        result = c._api_get("/", timeout=3)
        assert result is None


# ===================== 2. Rate Limiting Tests =====================

class TestRateLimiting:
    """Tests for rate limiting between API calls."""

    def test_09_rate_limit_enforces_interval(self, temp_download_dir):
        """Rate limiting should enforce minimum interval between calls."""
        c = HiFiClient(download_path=temp_download_dir)
        c._min_interval = 0.3

        start = time.time()
        c._rate_limit()
        c._rate_limit()
        elapsed = time.time() - start

        assert elapsed >= 0.25, f"Rate limiting should enforce ~0.3s gap, got {elapsed:.3f}s"

    def test_10_rate_limit_first_call_no_delay(self, temp_download_dir):
        """First API call shouldn't have artificial delay."""
        c = HiFiClient(download_path=temp_download_dir)
        c._min_interval = 1.0
        c._last_api_call = 0  # Reset

        start = time.time()
        c._rate_limit()
        elapsed = time.time() - start

        assert elapsed < 0.1, f"First call should be instant, took {elapsed:.3f}s"


# ===================== 3. Search Tests =====================

class TestSearch:
    """Tests for track search functionality."""

    def test_11_search_by_title(self, shared_client):
        """Search by title should return results."""
        results = shared_client.search_tracks(title="Bohemian Rhapsody")
        assert len(results) > 0, "Expected results for 'Bohemian Rhapsody'"
        assert results[0]['title'], "Track should have a title"

    def test_12_search_by_artist(self, shared_client):
        """Search by artist alone may return empty (API returns artist objects, not tracks).
        This test validates it doesn't crash."""
        results = shared_client.search_tracks(artist="Queen")
        # Artist-only search hits /search/?a=Queen which returns artist objects,
        # not tracks — so 0 results is expected behavior.
        assert isinstance(results, list)

    def test_13_search_by_title_and_artist(self, shared_client):
        """Combined title + artist search should return relevant results."""
        results = shared_client.search_tracks(title="Stairway to Heaven", artist="Led Zeppelin")
        assert len(results) > 0, "Expected results for 'Stairway to Heaven' by Led Zeppelin"

        # Check that at least one result mentions the artist
        found_artist = False
        for r in results:
            if 'led zeppelin' in r.get('artist', '').lower():
                found_artist = True
                break
        assert found_artist, "Expected at least one result from Led Zeppelin"

    def test_14_search_by_album(self, shared_client):
        """Search by album alone may return empty (API returns album objects, not tracks).
        This test validates it doesn't crash."""
        results = shared_client.search_tracks(album="Dark Side of the Moon")
        # Album-only search hits /search/?al=... which returns album objects,
        # not tracks — so 0 results is expected behavior.
        assert isinstance(results, list)

    def test_15_search_limit(self, shared_client):
        """Search should respect the limit parameter."""
        results = shared_client.search_tracks(title="Love", limit=5)
        assert len(results) <= 5, f"Expected ≤5 results, got {len(results)}"

    def test_16_search_no_terms(self, client):
        """Search with no terms should return empty list."""
        results = client.search_tracks()
        assert results == []

    def test_17_search_gibberish(self, shared_client):
        """Search for gibberish should return empty or handle gracefully."""
        results = shared_client.search_tracks(title="xzqwkjhgf9876zzz")
        assert isinstance(results, list)

    def test_18_search_generic(self, shared_client):
        """Generic search_raw() should call search_tracks with title."""
        results = shared_client.search_raw("Never Gonna Give You Up")
        assert len(results) > 0

    def test_19_search_result_fields(self, shared_client):
        """Search results should have all expected fields."""
        results = shared_client.search_tracks(title="Yesterday", artist="Beatles")
        assert len(results) > 0

        track = results[0]
        required_fields = ['id', 'title', 'artist', 'album', 'duration_ms']
        for field in required_fields:
            assert field in track, f"Missing field: {field}"

        assert track['id'] is not None, "Track ID should not be None"
        assert isinstance(track['title'], str)
        assert isinstance(track['artist'], str)

    def test_20_search_duration_is_milliseconds(self, shared_client):
        """Duration should be in milliseconds (typically > 30000 for a normal song)."""
        results = shared_client.search_tracks(title="Bohemian Rhapsody", artist="Queen")
        if results:
            track = results[0]
            duration = track.get('duration_ms', 0)
            # Bohemian Rhapsody is ~6 minutes = ~360000ms
            if duration > 0:
                assert duration > 10000, f"Duration {duration}ms seems too low — might be in seconds"

    def test_21_search_special_characters(self, shared_client):
        """Search should handle special characters."""
        results = shared_client.search_tracks(title="What's Going On", artist="Marvin Gaye")
        assert isinstance(results, list)

    def test_22_search_unicode(self, shared_client):
        """Search should handle unicode characters."""
        results = shared_client.search_tracks(title="Für Elise")
        assert isinstance(results, list)

    def test_23_search_very_long_query(self, shared_client):
        """Very long query should not crash."""
        results = shared_client.search_tracks(title="A" * 500)
        assert isinstance(results, list)


# ===================== 4. Track Info Tests =====================

class TestTrackInfo:
    """Tests for individual track info retrieval."""

    def _get_test_track_id(self, client):
        """Helper: search for a track and return its ID."""
        results = client.search_tracks(title="Bohemian Rhapsody", artist="Queen")
        if results:
            return results[0]['id']
        return None

    def test_24_get_track_info(self, shared_client):
        """Should return track info for a valid ID."""
        track_id = self._get_test_track_id(shared_client)
        if not track_id:
            pytest.skip("No search results to get a track ID")

        info = shared_client.get_track_info(track_id)
        assert info is not None, f"Expected track info for ID {track_id}"
        assert info.get('title'), "Track info should have a title"
        assert info.get('artist'), "Track info should have an artist"

    def test_25_get_track_info_invalid_id(self, shared_client):
        """Invalid track ID should return None, not crash."""
        info = shared_client.get_track_info(99999999999)
        # May return None or an error — just shouldn't raise
        assert info is None or isinstance(info, dict)

    def test_26_get_track_info_zero_id(self, shared_client):
        """Zero ID should handle gracefully."""
        info = shared_client.get_track_info(0)
        assert info is None or isinstance(info, dict)


# ===================== 5. Stream URL / Manifest Tests =====================

class TestStreamURL:
    """Tests for stream URL retrieval and manifest decoding."""

    def _get_test_track_id(self, client):
        results = client.search_tracks(title="Bohemian Rhapsody", artist="Queen")
        return results[0]['id'] if results else None

    def test_27_get_stream_url_lossless(self, shared_client):
        """Should return a stream URL for lossless quality."""
        track_id = self._get_test_track_id(shared_client)
        if not track_id:
            pytest.skip("No search results")

        stream = shared_client.get_stream_url(track_id, quality='lossless')
        if stream is None:
            pytest.skip("Stream URL not available (may be geo-restricted)")

        assert 'url' in stream, "Stream info should contain 'url'"
        assert stream['url'].startswith('http'), f"URL should be HTTP(S): {stream['url'][:100]}"
        assert stream['quality'] == 'lossless'

    def test_28_get_stream_url_hires(self, shared_client):
        """Should try to get hi-res stream URL."""
        track_id = self._get_test_track_id(shared_client)
        if not track_id:
            pytest.skip("No search results")

        stream = shared_client.get_stream_url(track_id, quality='hires')
        # Hi-res may not be available for all tracks — just shouldn't crash
        if stream:
            assert 'url' in stream

    def test_29_get_stream_url_high(self, shared_client):
        """Should get AAC stream URL."""
        track_id = self._get_test_track_id(shared_client)
        if not track_id:
            pytest.skip("No search results")

        stream = shared_client.get_stream_url(track_id, quality='high')
        if stream:
            assert 'url' in stream
            assert stream['quality'] == 'high'

    def test_30_get_stream_url_invalid_track(self, shared_client):
        """Invalid track ID should return None."""
        stream = shared_client.get_stream_url(99999999999, quality='lossless')
        assert stream is None

    def test_31_get_stream_url_invalid_quality(self, shared_client):
        """Invalid quality key should fall back to lossless."""
        track_id = self._get_test_track_id(shared_client)
        if not track_id:
            pytest.skip("No search results")

        # 'nonexistent' isn't in HIFI_QUALITY_MAP, should fall back
        stream = shared_client.get_stream_url(track_id, quality='nonexistent')
        # Should not crash — either returns data with lossless fallback or None

    def test_32_stream_url_has_encryption
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
