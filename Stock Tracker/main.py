"""
Stock Price Notifier
Requirements:
    pip install yfinance plyer

Usage:
    1. Create a file named config.json in the same folder as this script.
    2. Example config.json:
    {
      "poll_interval_seconds": 60,
      "notify_desktop": true,
      "email_alerts": false,
      "email": {
        "smtp_server": "smtp.gmail.com",
        "smtp_port": 587,
        "username": "you@gmail.com",
        "password": "app_password",
        "from_addr": "you@gmail.com",
        "to_addr": "target@gmail.com",
        "use_tls": true
      },
      "watchlist": [
        {"symbol": "AAPL", "target": 190.0, "direction": "above"},
        {"symbol": "TSLA", "target": 120.0, "direction": "below"}
      ]
    }

    3. Run: python stock_notifier.py
"""
import json
import time
import threading
import smtplib
from email.message import EmailMessage

try:
    from plyer import notification
    _HAS_PLYER = True
except Exception:
    _HAS_PLYER = False

import yfinance as yf

CONFIG_FILE = "config.json"

def load_config():
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def send_desktop(title, message):
    if _HAS_PLYER:
        try:
            notification.notify(title=title, message=message, timeout=8)
            return
        except Exception:
            pass
    print(f"[DESKTOP] {title} - {message}")

def send_email(cfg_email, subject, body):
    try:
        msg = EmailMessage()
        msg.set_content(body)
        msg["Subject"] = subject
        msg["From"] = cfg_email["from_addr"]
        msg["To"] = cfg_email["to_addr"]

        s = smtplib.SMTP(cfg_email["smtp_server"], cfg_email["smtp_port"], timeout=20)
        if cfg_email.get("use_tls", True):
            s.starttls()
        s.login(cfg_email["username"], cfg_email["password"])
        s.send_message(msg)
        s.quit()
        print("[EMAIL] Sent:", subject)
    except Exception as e:
        print("[EMAIL] Failed to send:", e)

def fetch_price(symbol):
    try:
        t = yf.Ticker(symbol)
        # Use fast history approach for reliable last price
        hist = t.history(period="1d", interval="1m")
        if not hist.empty:
            return float(hist["Close"].iloc[-1])
        # fallback to info
        info = t.fast_info if hasattr(t, "fast_info") else getattr(t, "info", {})
        if "last_price" in info:
            return float(info["last_price"])
        if "regularMarketPrice" in info:
            return float(info["regularMarketPrice"])
    except Exception as e:
        print(f"[FETCH] Error fetching {symbol}: {e}")
    return None

def check_and_alert(item, cfg, state):
    symbol = item["symbol"].upper()
    target = float(item["target"])
    direction = item.get("direction", "above").lower()
    price = fetch_price(symbol)
    if price is None:
        return
    key = f"{symbol}:{target}:{direction}"
    prev_triggered = state.get(key, False)
    triggered = False

    if direction == "above" and price >= target:
        triggered = True
    elif direction == "below" and price <= target:
        triggered = True

    if triggered and not prev_triggered:
        title = f"Stock Alert: {symbol}"
        msg = f"{symbol} current: {price:.2f} crossed {direction} {target:.2f}"
        print(f"[ALERT] {msg}")
        if cfg.get("notify_desktop", True):
            send_desktop(title, msg)
        if cfg.get("email_alerts", False):
            send_email(cfg["email"], title, msg)
        state[key] = True
    elif not triggered and prev_triggered:
        # reset when condition no longer holds so future crosses alert again
        state[key] = False
    # else no change

def worker(cfg, stop_event):
    watchlist = cfg.get("watchlist", [])
    interval = max(5, int(cfg.get("poll_interval_seconds", 60)))
    state = {}
    while not stop_event.is_set():
        for item in watchlist:
            try:
                check_and_alert(item, cfg, state)
            except Exception as e:
                print("[WORKER] error:", e)
        # sleep with stop support
        for _ in range(int(interval)):
            if stop_event.is_set():
                break
            time.sleep(1)

def main():
    cfg = load_config()
    stop_event = threading.Event()
    t = threading.Thread(target=worker, args=(cfg, stop_event), daemon=True)
    t.start()
    print("Stock notifier running. Press Ctrl+C to stop.")
    try:
        while t.is_alive():
            t.join(timeout=1)
    except KeyboardInterrupt:
        print("Stopping...")
        stop_event.set()
        t.join()
    print("Stopped.")

if __name__ == "__main__":
    main()
