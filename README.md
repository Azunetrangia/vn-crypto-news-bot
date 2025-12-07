<div align="center">

# 🤖 VN Crypto News Bot

### *Professional Discord Bot for Crypto & Economic News Aggregation*

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Discord.py](https://img.shields.io/badge/discord.py-2.3.2+-blue.svg)](https://github.com/Rapptz/discord.py)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-success.svg)](https://github.com/Azunetrangia/vn-crypto-news-bot)
[![Audit](https://img.shields.io/badge/Audit-9.0%2F10-brightgreen.svg)](docs/COMPREHENSIVE_AUDIT_FINAL.md)

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-dashboard">Dashboard</a> •
  <a href="#-documentation">Documentation</a> •
  <a href="#-troubleshooting">Troubleshooting</a>
</p>

---

### 🌟 Multi-Source Aggregation | 🌐 Auto Translation | 📊 Web Dashboard | 🕐 UTC+7 Timezone

</div>

## 📋 Overview

VN Crypto News Bot is a production-ready Discord bot that automatically aggregates crypto & economic news from multiple sources with Vietnamese localization support. Built with enterprise-grade architecture and comprehensive monitoring capabilities.

**Key Highlights:**
- 📰 **Multi-Source News**: Glassnode, Santiment, The Block, 5phutcrypto, Custom RSS
- 📅 **Economic Calendar**: Investing.com with UTC+7 timezone conversion
- 🌐 **Smart Translation**: Auto-detect language and translate to Vietnamese
- 🎨 **Multi-Guild**: Independent configuration for multiple Discord servers
- 📊 **Web Dashboard**: Flask-based monitoring and management UI
- 🔒 **Production-Ready**: SQLite database, translation cache, rate limiting, health checks


## ✨ Features

### 🎯 Core Capabilities

<table>
<tr>
<td width="50%">

#### 📰 News Aggregation
- **Glassnode Insights**: On-chain analytics & research
- **Santiment API**: Blockchain data & insights
- **The Block**: Institutional-grade crypto news
- **5phutcrypto.io**: Vietnamese crypto news
- **Custom RSS**: Add any RSS/Atom feed
- **Smart Translation**: Auto-detect & translate
- **Anti-Duplicate**: Article tracking per guild

</td>
<td width="50%">

#### 📅 Economic Calendar
- **Source**: Investing.com scraper
- **Timezone**: UTC+7 (Vietnam time)
- **Impact Filter**: High & Medium only
- **Pre-Alerts**: Configurable timing (1-1440 min)
- **Daily Summary**: Automatic at 07:00 AM
- **Real-time Updates**: 3-minute polling
- **Result Tracking**: Post actual values

</td>
</tr>
<tr>
<td width="50%">

#### 🎨 Multi-Guild Support
- Independent configuration per server
- Separate article tracking
- Per-guild channel settings
- Isolated RSS feeds
- No data conflicts

</td>
<td width="50%">

#### 📊 Web Dashboard
- **Real-time Monitoring**: Stats, guilds, feeds
- **Article Management**: View posted articles
- **Cache Analytics**: Translation cache stats
- **Health Checks**: System status endpoint
- **Security**: HTTP Basic Auth (.env)

</td>
</tr>
</table>

### 🛠️ Technical Features

- ✅ **SQLite Database**: Persistent storage with automatic migration
- ✅ **Translation Cache**: MD5-based caching (50%+ hit rate)
- ✅ **Rate Limiting**: 4 services with configurable limits
- ✅ **Health Monitoring**: Cog health checker with auto-reload
- ✅ **Cross-Platform**: Windows, Linux, macOS support
- ✅ **Production-Grade**: Logging, error handling, data backups


## 🚀 Quick Start

### Prerequisites

- **Python**: 3.9 or higher
- **Discord Bot**: Token from [Discord Developer Portal](https://discord.com/developers/applications)
- **Optional APIs**: Santiment, CoinGecko (for enhanced features)

### Installation

#### 1️⃣ Clone Repository

```bash
git clone https://github.com/Azunetrangia/vn-crypto-news-bot.git
cd vn-crypto-news-bot
```

#### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

#### 3️⃣ Configure Environment

Create `.env` file from template:

```bash
cp .env.example .env
```

Edit `.env` with your credentials:

```env
# Required: Discord Bot Token
DISCORD_TOKEN=your_discord_bot_token_here

# Optional: API Keys
SANTIMENT_API_KEY=your_santiment_api_key_here
COINGECKO_API_KEY=your_coingecko_api_key_here

# Economic Calendar Pre-Alert Window (minutes)
# Default: 30 | Min: 1 | Max: 1440 (24 hours)
ECONOMIC_PREALERT_MINUTES=30

# Dashboard Credentials (for web UI)
DASHBOARD_USERNAME=admin
DASHBOARD_PASSWORD=your_secure_password_here
```

#### 4️⃣ Create Discord Bot

<details>
<summary>Click to expand Discord Bot Setup</summary>

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **"New Application"** and name it
3. Navigate to **"Bot"** tab → Click **"Add Bot"**
4. Copy **Bot Token** and paste into `.env`
5. Enable **Privileged Gateway Intents**:
   - ✅ PRESENCE INTENT
   - ✅ SERVER MEMBERS INTENT
   - ✅ MESSAGE CONTENT INTENT
6. Go to **"OAuth2"** → **"URL Generator"**:
   - Scopes: `bot`, `applications.commands`
   - Bot Permissions: `Administrator` (or specific permissions)
7. Copy generated URL and invite bot to your server

</details>

#### 5️⃣ Launch Bot

```bash
# Linux/macOS
python main_bot.py

# Windows
python main_bot.py

# Or use provided scripts
bash start.sh       # Linux/macOS
start.bat           # Windows
```

#### 6️⃣ Access Dashboard (Optional)

Start the web dashboard:

```bash
cd dashboard
python app.py
```

Then visit: `http://localhost:5000`

**For public access**, use [Ngrok](https://ngrok.com/):

```bash
ngrok http 5000
```

See [WINDOWS_SETUP.md](WINDOWS_SETUP.md) for detailed Windows instructions.


## 📖 Usage Guide

### 🎮 Primary Command: `/start`

The bot uses a **single slash command** with interactive menus:

```
Type: /start
```

<div align="center">

```
┌─────────────────────────────────────┐
│  🤖 VN Crypto News Bot              │
│  ───────────────────────────────    │
│  Select a function:                 │
│                                     │
│  📰 [News Management]               │
│  📅 [Economic Calendar]             │
└─────────────────────────────────────┘
```

</div>

### 📰 News Management (Admin Only)

Click **[News Management]** to access:

<table>
<tr>
<td width="50%">

#### 📊 Glassnode Channel
- On-chain analytics & research
- Auto-translation to Vietnamese
- Select Discord channel

#### 🔗 Santiment Channel
- Blockchain data insights
- On-chain metrics
- Auto-translation to Vietnamese

#### ⚡ 5phutcrypto Channel
- Vietnamese crypto news 🇻🇳
- No translation needed
- Local market analysis

</td>
<td width="50%">

#### 📰 The Block Channel
- Institutional-grade news
- Market analysis
- Auto-translation to Vietnamese

#### 📡 Add RSS Feed
- Custom news sources
- Auto language detection
- VNExpress, BBC, CNN, etc.

#### 🗑️ Remove RSS Feed
- Select from active feeds
- Clean removal process

</td>
</tr>
</table>

### 📅 Economic Calendar (Admin Only)

Click **[Economic Calendar]** to configure:

- **📊 Setup Channel**: Select Discord channel for calendar posts
- **🕐 Timezone**: Automatic UTC+7 conversion
- **🔴 Impact Filter**: High & Medium events only
- **⏰ Pre-Alerts**: Configurable (1-1440 minutes)
- **📅 Daily Summary**: Automatic at 07:00 AM UTC+7

#### Admin Test Commands

```bash
!testcalendar  # View today's full calendar
!schedulenow   # Trigger scheduler manually
```

### 🤖 Automatic Background Tasks

Bot runs automatic checks every **3 minutes**:

| Source | Feature | Translation |
|--------|---------|-------------|
| 📊 Glassnode | On-chain analytics | ✅ Yes |
| 🔗 Santiment | Blockchain insights | ✅ Yes |
| ⚡ 5phutcrypto | Vietnamese news | ❌ No |
| 📰 The Block | Institutional news | ✅ Yes |
| 📅 Economic Calendar | Events (UTC+7) | ❌ No |
| 📡 Custom RSS | User feeds | ✅ Auto-detect |


## 📊 Dashboard

### Web-Based Monitoring & Management

The bot includes a **Flask-based web dashboard** for real-time monitoring:

#### Features

- **📊 Statistics**: Total guilds, feeds, articles posted
- **🏢 Guild Management**: View all connected Discord servers
- **📡 Feed Monitoring**: Active RSS feeds and their status
- **📰 Article History**: Recently posted articles
- **💾 Cache Analytics**: Translation cache hit rate and size
- **❤️ Health Check**: System status endpoint (`/health`)

#### Launch Dashboard

```bash
cd dashboard
python app.py
```

Dashboard runs on `http://localhost:5000`

#### Configuration

Credentials are loaded from `.env`:

```env
DASHBOARD_USERNAME=admin
DASHBOARD_PASSWORD=your_secure_password
```

#### Public Access with Ngrok

To access dashboard remotely:

```bash
# Install Ngrok
# Visit: https://ngrok.com/download

# Configure authtoken
ngrok config add-authtoken YOUR_AUTHTOKEN

# Start tunnel
ngrok http 5000
```

Ngrok will provide a public HTTPS URL like:
```
https://abc123.ngrok-free.app
```

See [WINDOWS_SETUP.md](WINDOWS_SETUP.md) for Windows-specific instructions.


## 📁 Project Structure

```
vn-crypto-news-bot/
├── 📄 main_bot.py                   # Bot entry point
├── 📄 database.py                   # SQLite database wrapper
├── 📄 translation_cache.py          # Translation caching system
├── 📄 requirements.txt              # Python dependencies
├── 📄 .env.example                  # Environment template
├── 📄 .gitignore                    # Git exclusions
│
├── 📁 cogs/                         # Bot extensions
│   ├── news_cog.py                  # News aggregation logic
│   ├── health_checker.py            # Cog health monitoring
│   └── news/                        # News modules
│       ├── sources/                 # Source fetchers
│       ├── formatters/              # Message formatters
│       └── models/                  # Data models
│
├── 📁 dashboard/                    # Web UI
│   ├── app.py                       # Flask application
│   ├── templates/                   # HTML templates
│   └── static/                      # CSS/JS assets
│
├── 📁 utils/                        # Utilities
│   ├── rate_limiter.py              # API rate limiting
│   └── helpers.py                   # Helper functions
│
├── 📁 data/                         # Runtime data
│   ├── news_config.json             # Per-guild configuration
│   ├── last_post_ids.json           # Article tracking
│   ├── alerts.json                  # Alert settings
│   └── backups/                     # Auto backups
│
├── 📁 docs/                         # Documentation
│   ├── COMPREHENSIVE_AUDIT_FINAL.md # Project audit (9.0/10)
│   ├── WINDOWS_SETUP.md             # Windows guide
│   ├── API_REFERENCE.md             # Technical docs
│   ├── TROUBLESHOOTING.md           # Common issues
│   └── ...
│
├── 📁 scripts/                      # Utility scripts
│   ├── check_channels.py            # Channel verification
│   ├── verify_multi_guild_posts.py  # Multi-guild testing
│   └── apply_fixes.sh               # Auto-fix script
│
├── 📁 tests/                        # Test suite
│   ├── test_calendar.py             # Calendar tests
│   └── ...
│
└── 📁 logs/                         # Log files (auto-created)
```

## 🛠️ Tech Stack

### Core Technologies

<table>
<tr>
<td width="50%">

#### Backend
- **Python**: 3.9+
- **discord.py**: 2.3.2+ (Discord API wrapper)
- **aiohttp**: Async HTTP client
- **SQLite**: Embedded database
- **python-dotenv**: Environment management

</td>
<td width="50%">

#### Web Dashboard
- **Flask**: 3.0.0+ (Web framework)
- **Werkzeug**: WSGI utilities
- **Jinja2**: Template engine
- **HTTP Basic Auth**: Authentication

</td>
</tr>
<tr>
<td width="50%">

#### Data Processing
- **feedparser**: RSS/Atom parsing
- **BeautifulSoup4**: HTML scraping
- **deep-translator**: Google Translate API
- **pytz**: Timezone handling (UTC+7)
- **html**: HTML entities decoding

</td>
<td width="50%">

#### Development Tools
- **Git**: Version control
- **Ngrok**: Public tunnel (optional)
- **pytest**: Testing framework
- **VS Code**: Recommended IDE

</td>
</tr>
</table>

### Architecture

- **Modular Design**: Cogs-based architecture
- **Async/Await**: Non-blocking I/O operations
- **Database**: SQLite with WAL mode
- **Caching**: MD5-based translation cache
- **Rate Limiting**: Per-service token buckets
- **Health Monitoring**: Automatic cog reload


## ⚙️ System Architecture

### Background Tasks

The bot runs automated tasks in parallel:

#### 📰 News Aggregator (Every 3 minutes)
```
┌─────────────────────────────────────┐
│  1. Fetch from all sources          │
│     • Glassnode RSS                 │
│     • Santiment GraphQL             │
│     • 5phutcrypto RSS               │
│     • The Block RSS                 │
│     • Custom RSS feeds              │
│                                     │
│  2. Process each article            │
│     • Check if already posted       │
│     • Detect language               │
│     • Translate if needed           │
│     • Format Discord embed          │
│                                     │
│  3. Post to guilds                  │
│     • Per-guild configuration       │
│     • Independent tracking          │
│     • Error handling per source     │
└─────────────────────────────────────┘
```

#### 📅 Economic Calendar (Every 3 minutes + Daily)
```
┌─────────────────────────────────────┐
│  Polling Loop (every 3 min):        │
│  • Fetch events from Investing.com  │
│  • Filter: High & Medium impact     │
│  • Convert: UTC-5 → UTC+7           │
│  • Pre-alert: Configurable window   │
│  • Post results: When actual ≠ N/A  │
│                                     │
│  Daily Summary (07:00 UTC+7):       │
│  • Today's events overview          │
│  • Categorized by impact            │
│  • Country & time info              │
└─────────────────────────────────────┘
```

### Multi-Guild Architecture

<div align="center">

```
         ┌─────────────────┐
         │   Bot Instance  │
         └────────┬────────┘
                  │
         ┌────────┴────────┐
         │                 │
    ┌────▼────┐       ┌────▼────┐
    │ Guild A │       │ Guild B │
    └────┬────┘       └────┬────┘
         │                 │
    ┌────┴────┐       ┌────┴────┐
    │ Config  │       │ Config  │
    │ Feeds   │       │ Feeds   │
    │ Tracking│       │ Tracking│
    └─────────┘       └─────────┘
```

</div>

**Features:**
- Independent configuration per guild
- Separate article tracking
- No data conflicts
- Isolated channel settings


## 🔒 Security & Best Practices

### Environment Variables

✅ **DO:**
- Store credentials in `.env` file
- Use `.env.example` as template
- Add `.env` to `.gitignore`
- Load with `python-dotenv`

❌ **DON'T:**
- Hardcode API keys in code
- Commit `.env` to Git
- Share credentials publicly

### Bot Permissions

Required Discord permissions:
- ✅ Send Messages
- ✅ Embed Links
- ✅ Read Message History
- ✅ Use Slash Commands
- ✅ Administrator (for setup)

### Data Protection

- **SQLite Database**: Excluded from Git (`.gitignore`)
- **Logs**: Auto-rotated and gitignored
- **Backups**: Automatic daily backups in `data/backups/`
- **Dashboard**: HTTP Basic Auth required

### Rate Limiting

Configured limits per service:
- **Google Translate**: 100 requests/minute
- **Glassnode**: 12 requests/hour
- **Santiment**: 4 requests/hour
- **RSS Feeds**: 30 requests/minute


## 🐛 Troubleshooting

### Common Issues

<details>
<summary><b>❌ Bot not posting articles</b></summary>

**Possible causes:**
1. Missing API keys in `.env`
2. Channels not configured
3. Bot lacks permissions
4. Rate limit exceeded

**Solutions:**
```bash
# 1. Check configuration
cat data/news_config.json

# 2. Verify bot permissions
# Go to Discord → Server Settings → Roles → Bot Role

# 3. Check logs
tail -f logs/bot.log

# 4. Test calendar manually
# In Discord: !testcalendar
```

</details>

<details>
<summary><b>❌ Economic Calendar not showing events</b></summary>

**Possible causes:**
1. No High/Medium impact events today
2. All events in the past
3. Investing.com URL changed

**Solutions:**
```bash
# Test calendar fetch
python scripts/check_economic_history.py

# Verify timezone conversion
# Events should show UTC+7 time
```

</details>

<details>
<summary><b>❌ Vietnamese text displaying incorrectly</b></summary>

**Fixed in v1.2.0:**
- HTML entities automatically decoded
- UTF-8 encoding enforced

**If still broken:**
```python
# Check RSS feed encoding
import feedparser
feed = feedparser.parse("YOUR_RSS_URL")
print(feed.encoding)  # Should be 'utf-8'
```

</details>

<details>
<summary><b>❌ Translation not working</b></summary>

**No API key required** - uses `deep-translator`

**Troubleshooting:**
```bash
# Test translation
python -c "from deep_translator import GoogleTranslator; print(GoogleTranslator(source='en', target='vi').translate('Hello'))"

# Should output: "Xin chào"
```

</details>

<details>
<summary><b>❌ Dashboard not accessible</b></summary>

**Check:**
1. Dashboard process running: `ps aux | grep dashboard`
2. Port 5000 available: `netstat -tulpn | grep 5000`
3. Credentials in `.env`:
   ```env
   DASHBOARD_USERNAME=admin
   DASHBOARD_PASSWORD=your_password
   ```

**Restart dashboard:**
```bash
cd dashboard
python app.py
```

</details>

<details>
<summary><b>❌ Multi-guild conflicts</b></summary>

**Symptoms:**
- Articles posted to wrong guild
- Configuration overwriting

**Solution:**
```bash
# Verify guild configs
python scripts/verify_multi_guild_posts.py

# Check data structure
cat data/news_config.json | jq '.guilds'
```

</details>

### Getting Help

1. **📖 Documentation**: Check [docs/](docs/) folder
2. **🔍 Logs**: Review `logs/bot.log`
3. **🧪 Test Scripts**: Run scripts in `tests/` folder
4. **📊 Dashboard**: Check `/health` endpoint
5. **💬 Issues**: Open GitHub issue with logs

For detailed troubleshooting, see [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)


## 📚 Documentation

Comprehensive documentation available in the `docs/` folder:

| Document | Description |
|----------|-------------|
| [📊 COMPREHENSIVE_AUDIT_FINAL.md](docs/COMPREHENSIVE_AUDIT_FINAL.md) | **9.0/10 audit score** - Full project analysis |
| [🪟 WINDOWS_SETUP.md](docs/WINDOWS_SETUP.md) | Windows installation guide |
| [📖 API_REFERENCE.md](docs/API_REFERENCE.md) | Technical API documentation |
| [🐛 TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) | Common issues & solutions |
| [🏗️ PROJECT_OVERVIEW.md](docs/PROJECT_OVERVIEW.md) | Architecture & structure |
| [📋 CHANGELOG.md](docs/CHANGELOG.md) | Version history |
| [🚀 QUICKSTART.md](docs/QUICKSTART.md) | Quick setup guide |

## 📝 Changelog

### Version 2.0.0 (December 2025) - **Production Ready**

#### 🎉 Major Features
- ✅ **Web Dashboard**: Flask-based monitoring UI
  - Real-time statistics and guild management
  - Article history and cache analytics
  - Health check endpoint
  - HTTP Basic Auth security

- ✅ **Database Migration**: SQLite integration
  - Persistent article storage
  - Guild configuration management
  - Translation cache optimization
  - Automatic WAL mode

- ✅ **Rate Limiting System**: Per-service token buckets
  - Google Translate: 100/min
  - Glassnode: 12/hour
  - Santiment: 4/hour
  - RSS Feeds: 30/min

- ✅ **Health Monitoring**: Automatic cog reload
  - Watchdog system for cog failures
  - Auto-recovery mechanisms
  - Error logging and alerts

#### 📦 New Components
- `database.py` - SQLite wrapper with migrations
- `translation_cache.py` - MD5-based caching
- `utils/rate_limiter.py` - Token bucket rate limiter
- `cogs/health_checker.py` - Cog health monitoring
- `dashboard/` - Complete Flask web application

#### 🔧 Improvements
- Cross-platform support (Windows, Linux, macOS)
- Comprehensive audit (9.0/10 rating)
- Production-grade security
- Automated backups
- Enhanced error handling

### Version 1.3.0 (November 2025)

#### 🎯 Economic Calendar Improvements
- ✅ Polling-based architecture (3-minute loop)
- ✅ Configurable pre-alert window (1-1440 minutes)
- ✅ Daily summary at 07:00 UTC+7
- ✅ Admin test commands: `!testcalendar`, `!schedulenow`

### Version 1.2.0 (November 2025)

#### 🎉 New Features
- ✅ **The Block Integration**: Institutional-grade crypto news
- ✅ **HTML Entities Fix**: Vietnamese text rendering
- ✅ **Santiment GraphQL**: Updated API queries

#### 🐛 Bug Fixes
- Fixed VNEconomy malformed HTML entities
- Updated Santiment query structure
- Multi-guild tracking improvements

### Version 1.1.0 (October 2025)
- ✅ Multi-guild support
- ✅ Economic Calendar (UTC+7)
- ✅ 5phutcrypto.io integration
- ✅ Auto translation with language detection

### Version 1.0.0 (Initial Release)
- ✅ Basic news aggregation
- ✅ RSS feeds support
- ✅ Discord slash commands

## 🎯 Roadmap

### Phase 3: Production Scaling (Q1 2026)
- [ ] Docker containerization
- [ ] CI/CD pipeline (GitHub Actions)
- [ ] Automated testing (50%+ coverage)
- [ ] Load balancing for multiple guilds

### Phase 4: Monitoring & Analytics (Q2 2026)
- [ ] Prometheus metrics
- [ ] Grafana dashboards
- [ ] Alert system (Discord webhooks)
- [ ] Performance profiling

### Phase 5: Advanced Features (Q3 2026)
- [ ] AI-powered summaries
- [ ] Sentiment analysis
- [ ] Portfolio tracking
- [ ] Trading signals
- [ ] User preferences system

## 📊 Project Statistics

<div align="center">

| Metric | Value |
|--------|-------|
| **Lines of Code** | 320,000+ |
| **Python Files** | 864 |
| **Project Size** | 48 MB |
| **Audit Score** | 9.0/10 |
| **Production Ready** | 80% |
| **Test Coverage** | TBD |

</div>

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit** your changes
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push** to the branch
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open** a Pull Request

### Contribution Guidelines

- Follow PEP 8 style guide
- Add docstrings to functions
- Update documentation
- Include tests for new features
- Ensure all tests pass

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

Free to use, modify, and distribute with attribution.

## 📧 Contact & Support

### Getting Help

- **📖 Documentation**: Check [docs/](docs/) folder first
- **🐛 Bug Reports**: [Open an issue](https://github.com/Azunetrangia/vn-crypto-news-bot/issues)
- **💡 Feature Requests**: [Submit suggestions](https://github.com/Azunetrangia/vn-crypto-news-bot/issues)
- **💬 Discussions**: [GitHub Discussions](https://github.com/Azunetrangia/vn-crypto-news-bot/discussions)

### Project Links

- **🌐 Repository**: [github.com/Azunetrangia/vn-crypto-news-bot](https://github.com/Azunetrangia/vn-crypto-news-bot)
- **📊 Dashboard Demo**: See [WINDOWS_SETUP.md](docs/WINDOWS_SETUP.md) for setup
- **📚 Full Docs**: [docs/INDEX.md](docs/INDEX.md)

---

<div align="center">

### 🌟 Made with ❤️ for the Vietnamese Crypto Community

**⭐ Star this repo if you find it useful!**

[![GitHub stars](https://img.shields.io/github/stars/Azunetrangia/vn-crypto-news-bot?style=social)](https://github.com/Azunetrangia/vn-crypto-news-bot/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Azunetrangia/vn-crypto-news-bot?style=social)](https://github.com/Azunetrangia/vn-crypto-news-bot/network/members)

</div>
