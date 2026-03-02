#!/usr/bin/env python3
"""
🎙️ Voice Mood Detector
Detects voice type based on decibel levels:
  😊 Happy  - Calm, moderate voice (normal dB)
  😒 Bad    - Loud / raised voice (high dB spike)
  🤢 Harsh  - Very loud / harsh noise (very high dB)
"""

import pyaudio
import numpy as np
import time
import sys

# ── Config ──────────────────────────────────────────────────────────────────
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# Decibel thresholds
SILENCE_THRESHOLD = 30   # Below this = silence
HAPPY_MAX  = 55          # 30 – 55 dB  → 😊 Happy / calm
BAD_MAX    = 75          # 56 – 75 dB  → 😒 Bad / raised
                         # >75 dB      → 🤢 Harsh noise

HISTORY_SIZE = 8         # Smoothing window

# ── Helpers ─────────────────────────────────────────────────────────────────
def rms_to_db(rms: float) -> float:
    if rms < 1:
        rms = 1
    return 20 * np.log10(rms)

def classify(db: float):
    if db < SILENCE_THRESHOLD:
        return "Silence", "🔇"
    elif db <= HAPPY_MAX:
        return "Happy", "😊"
    elif db <= BAD_MAX:
        return "Bad", "😒"
    else:
        return "Harsh", "🤢"

def db_bar(db: float, width: int = 40) -> str:
    filled = max(0, min(int((db / 100) * width), width))
    bar = "█" * filled + "░" * (width - filled)
    if db < SILENCE_THRESHOLD:
        color = "\033[90m"
    elif db <= HAPPY_MAX:
        color = "\033[92m"
    elif db <= BAD_MAX:
        color = "\033[93m"
    else:
        color = "\033[91m"
    return f"{color}[{bar}]\033[0m"

# ── Main ─────────────────────────────────────────────────────────────────────
def main():
    print("\033[96m")
    print("╔══════════════════════════════════════╗")
    print("║      🎙️  Voice Mood Detector          ║")
    print("╠══════════════════════════════════════╣")
    print(f"║  😊 Happy  :  0 – {HAPPY_MAX} dB              ║")
    print(f"║  😒 Bad    : {HAPPY_MAX+1} – {BAD_MAX} dB              ║")
    print(f"║  🤢 Harsh  : > {BAD_MAX} dB                   ║")
    print("╚══════════════════════════════════════╝")
    print("\033[0mPress  Ctrl+C  to quit.\n")

    p = pyaudio.PyAudio()
    try:
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                        input=True, frames_per_buffer=CHUNK)
    except OSError as e:
        print(f"❌  Could not open microphone: {e}")
        p.terminate()
        sys.exit(1)

    print("🎤  Listening…\n\n\n")

    history = []
    label_counts = {"Happy 😊": 0, "Bad 😒": 0, "Harsh 🤢": 0}

    try:
        while True:
            data = stream.read(CHUNK, exception_on_overflow=False)
            samples = np.frombuffer(data, dtype=np.int16).astype(np.float32)
            rms = np.sqrt(np.mean(samples ** 2))
            db = rms_to_db(rms)

            history.append(db)
            if len(history) > HISTORY_SIZE:
                history.pop(0)
            smooth_db = float(np.mean(history))

            label, emoji = classify(smooth_db)
            bar = db_bar(smooth_db)

            if label != "Silence":
                key = f"{label} {emoji}"
                label_counts[key] = label_counts.get(key, 0) + 1

            # Overwrite last 3 lines
            sys.stdout.write("\033[3A")
            print(f"  dB Level : {smooth_db:5.1f} dB   {bar}     ")
            print(f"  Mood     : {emoji}  {label:<10}               ")
            print(f"  Counts   → 😊 {label_counts.get('Happy 😊',0):4d}  "
                  f"😒 {label_counts.get('Bad 😒',0):4d}  "
                  f"🤢 {label_counts.get('Harsh 🤢',0):4d}  ")

            time.sleep(0.05)

    except KeyboardInterrupt:
        print("\n\n\033[96m── Session Summary ──────────────────────")
        total = sum(label_counts.values()) or 1
        for k, v in label_counts.items():
            pct = v / total * 100
            bar = "█" * int(pct / 2)
            print(f"  {k:12s}: {v:5d} frames  ({pct:5.1f}%)  {bar}")
        dominant = max(label_counts, key=label_counts.get)
        print(f"\n  Overall mood: {dominant}")
        print("─────────────────────────────────────────\033[0m\n")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

if __name__ == "__main__":
    main()
