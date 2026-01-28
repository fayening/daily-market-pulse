# daily-market-pulse 

A personal, non-commercial, **read-only** analytics tool that summarizes public subreddit discussions into a daily “market pulse” digest (top tickers, engagement-weighted heat, and high-level bull/bear themes).

This project is designed to be **low-risk and policy-aligned**: conservative request volume, strict throttling, caching/deduplication, minimal data retention, and no content manipulation.

---

## What the app does (Read-only behavior)

**Inputs (public content only):**
- Reads a limited set of **recent posts** from an allowlisted subreddit (default: `r/wallstreetbets`) within the **last 24 hours**.
- Optionally reads a limited subset of **top-level comments** per post to improve ticker extraction and theme summarization.

**Processing:**
1. **Ticker extraction**  
   Detects candidate tickers (e.g., `$NVDA`, `NVDA`) using strict patterns plus a blacklist to reduce false positives (e.g., `CEO`, `USA`).
2. **Heat scoring (aggregated only)**  
   Computes per-ticker aggregated metrics (mentions, approximate unique authors, engagement-weighted score).
3. **Daily digest rendering**  
   Produces a compact daily summary and includes **links back to the original Reddit threads** (Reddit remains the primary destination for reading/participation).
4. **Discord delivery**  
   Posts the digest to a **private Discord channel** using a webhook (embeds supported).

**What it does NOT do:**
- Does **not** post, comment, vote, message, follow users, moderate, or perform any content manipulation.
- Does **not** attempt to identify users or infer sensitive attributes.

---

## Data Budget & Scope (conservative defaults)

To avoid rate-limit issues and minimize platform impact, the tool uses strict caps:

- **Frequency:** once per day
- **Subreddits:** allowlist only (default: `r/wallstreetbets`)
- **Time window:** last 24 hours only (no historical backfills by default)
- **Per-run caps (default):**
  - up to **150 posts**
  - up to **30 top-level comments per post** (when available)
- **Execution:** sequential requests only (no parallel bursts)
- **Throttling:** randomized delay between requests + backoff on rate-limit signals
- **Hard cap target:** comfortably below typical free-tier limits (intended to remain far under platform thresholds)

---

## Output & Redistribution

- Output is posted to a **private Discord** channel for personal use.
- The tool does **not** republish full posts/comments. It outputs:
  - aggregated metrics (counts/scores)
  - short, original summaries
  - thread links back to Reddit

---

## Caching, Deduplication, and Backoff

- **Deduplication:** stores post IDs (and optionally comment IDs) to avoid re-fetching the same content across runs.
- **Ephemeral caching:** short-lived caching may be used to reduce repeated API calls during a run.
- **Backoff:** on rate-limit signals or errors, the tool slows down and/or stops the run rather than retrying aggressively.

---

## Minimal Data Retention

The project is designed to retain **only what is necessary** for daily comparisons (e.g., vs1d/vs3d/vs5d):

- Stored (default):
  - daily aggregated ticker stats (date, ticker, counts/scores)
  - post IDs for deduplication and linking
- Not stored:
  - user profiles
  - attempts to re-identify users
  - sensitive inferences
  - full post/comment bodies (beyond ephemeral processing/caching)

Default retention is **7 days** for aggregated stats (configurable).

---

## Reddit API Access (Approval Required)

Reddit’s platform policies may require **explicit approval** before creating an application and accessing the Reddit Data API.

1. Review the Responsible Builder Policy.
2. Request API access via Reddit’s help/approval process as needed.
3. After approval, create an OAuth app (script-type) and obtain:
   - `REDDIT_CLIENT_ID`
   - `REDDIT_CLIENT_SECRET`
   - `REDDIT_USER_AGENT` (must be specific and descriptive)

---

## Configuration

Create a local `.env` (do **not** commit it) based on `.env.example`:

- Reddit:
  - `REDDIT_CLIENT_ID`
  - `REDDIT_CLIENT_SECRET`
  - `REDDIT_USERNAME` (if applicable)
  - `REDDIT_PASSWORD` (if applicable)
  - `REDDIT_USER_AGENT`
- Discord:
  - `DISCORD_WEBHOOK_URL`

---

## Install & Run (example)

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\activate
pip install -r requirements.txt

# Run once per day:
python -m pulse run --subreddit wallstreetbets --hours 24 --limit-posts 150 --limit-comments 30 --push discord
