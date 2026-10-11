"""Credentials for scripts/medium_export.py.

Copy this file to scripts/medium_credentials.py and fill in the values. That file is
listed in .gitignore, so the cookies don't end up in the repository.

Medium has no password login any more and no API for reading posts, so the exporter
uses the session cookies of your browser:

1. Log in to medium.com in your browser.
2. Open the developer tools (F12) → Application (Chrome) / Storage (Firefox) → Cookies
   → https://medium.com.
3. Copy the values of the cookies below.
4. Copy your browser's user agent (DevTools → Console: navigator.userAgent).
   Cloudflare ties cf_clearance to it, so it has to be the same browser.

Alternatively set the environment variables MEDIUM_SID, MEDIUM_UID,
MEDIUM_CF_CLEARANCE and MEDIUM_USER_AGENT.

Without credentials, use Medium's data export instead (no cookies needed):
Medium → Settings → Security and apps → Download your information, then
`uv run python scripts/medium_export.py list --from-export medium-export.zip`.
"""

MEDIUM_USERNAME = "martinthoma"

COOKIES = {
    "sid": "",  # session id
    "uid": "",  # user id
    "cf_clearance": "",  # Cloudflare; without it Medium answers 403
}

USER_AGENT = ""  # e.g. "Mozilla/5.0 (X11; Linux x86_64) ..."
