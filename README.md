# Daily Market Pulse

A read-only Reddit market sentiment analyzer with responsible data practices.

## Core Principles

### 🔒 Read-Only Access
- **No posting, voting, or modification** of Reddit content
- Uses read-only Reddit API credentials
- Minimizes API surface area to reduce risk

### 🚦 Rate Limiting & Throttling
- Strict rate limiting: 30 requests/minute (configurable)
- Request queuing with backoff
- Respects Reddit API guidelines

### 💾 Caching Strategy
- HTTP response caching (5-minute default)
- Reduces redundant API calls
- Configurable cache expiration

### 🗑️ Minimal Data Retention
- **Default: 7 days** data retention
- Auto-cleanup of old records
- No long-term storage of personal data
- GDPR/privacy-conscious design

### ⏸️ Rate Limit Backoff
- Exponential backoff on 429 errors
- Maximum retry limit (5 retries default)
- Base delay: 60 seconds
- Graceful degradation on API failures

## Setup

1. Copy environment template:
   ```bash
   cp .env.example .env
   ```

2. Configure Reddit API (read-only):
   - Visit https://www.reddit.com/prefs/apps
   - Create "script" app (not "web app")
   - Add credentials to `.env`

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

```bash
python -m src.pulse.cli
```

## Project Structure

```
src/pulse/
├── config.py           # Configuration loader
├── reddit_client.py    # Reddit API client with rate limiting
├── ticker_extract.py   # Stock ticker extraction
├── storage.py          # Data persistence with auto-cleanup
├── report.py           # Sentiment report generation
├── discord_webhook.py  # Optional Discord notifications
└── cli.py              # Command-line interface
```

## Compliance

- **Read-only**: No modification of Reddit content
- **Rate-limited**: Respects API quotas
- **Cached**: Minimizes redundant requests
- **Privacy-first**: Minimal data retention
- **Resilient**: Automatic backoff on rate limits

## License

MIT
