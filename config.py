"""
ShopifyChk — Configuration
===========================
All tunables in one place. Override via env vars for production.
"""

import os

# ── Telegram Bot ────────────────────────────────────────────────────────────────
BOT_TOKEN = os.environ.get("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

# ── Channel / Group Membership Gate ────────────────────────────────────────────
# Users MUST join BOTH before using any command.
# Set these as @username (public), or use invite links for private groups.

REQUIRED_CHANNEL = os.environ.get("REQUIRED_CHANNEL", "@nativecodes")
REQUIRED_GROUP   = os.environ.get("REQUIRED_GROUP", "@shadylocar_Gc")

# Public invite links for when a user hasn't joined yet
CHANNEL_INVITE = os.environ.get(
    "CHANNEL_INVITE", "https://t.me/nativecodes"
)
GROUP_INVITE = os.environ.get(
    "GROUP_INVITE", "https://t.me/shadylocar_Gc"
)

# ── Admin Control ───────────────────────────────────────────────────────────────
# Comma-separated Telegram user IDs
ADMINS = [
    int(x.strip())
    for x in os.environ.get("ADMINS", "").split(",")
    if x.strip()
]

# ── Checker Engine ──────────────────────────────────────────────────────────────
MAX_CONCURRENCY   = int(os.environ.get("MAX_CONCURRENCY", "50"))
GRAPHQL_TIMEOUT   = int(os.environ.get("GRAPHQL_TIMEOUT", "28"))
PRODUCT_TIMEOUT   = int(os.environ.get("PRODUCT_TIMEOUT", "12"))
PROXY_RETRIES     = int(os.environ.get("PROXY_RETRIES", "2"))

# ── Rate Limits ─────────────────────────────────────────────────────────────────
RATE_LIMIT_CHECKS  = int(os.environ.get("RATE_LIMIT_CHECKS", "10"))   # per window
RATE_LIMIT_WINDOW  = int(os.environ.get("RATE_LIMIT_WINDOW", "60"))   # seconds

# ── Branding ────────────────────────────────────────────────────────────────────
TITLE             = "Native CC Checker"
CREDITS           = "@Poriot_ke"
SIGNATURE         = "@nativecodes"

# ── Paths ───────────────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HITS_FILE = os.path.join(BASE_DIR, "hits.txt")

BANNER = r"""
  ____  _                 _  __      _____ _     _    
 / ___|| |__   ___  _ __ (_)/ _|_   / ____| |__ | | __
 \___ \| '_ \ / _ \| '_ \| | |_| | | |    | '_ \| |/ /
  ___) | | | | (_) | |_) | |  _| |_| |____| | | |   < 
 |____/|_| |_|\___/| .__/|_|_|  \__, |\_____|_| |_|_|\_\
                   |_|          |___/                    
        ── Native CC checker  ──
        ── Credits: @Poriot_ke        ──
"""

# ── Bot Metadata (for /start) ───────────────────────────────────────────────────
ABOUT_TEXT = f"""
🔥 **{TITLE}** —    Checker

 Autoshopify Checker Ultra fast

**Commands:**
`/sh CC|MM|YYYY|CVV` — Check a single card
`/gate <url>` — Scan a site for gateway info
`/mst` — Mass check (reply to or attach a .txt file)
`/start` — Show this message

**Credits:** {CREDITS}
**Signature:** {SIGNATURE}
"""
