#!/usr/bin/env python3

import time
import sys
import os
import random

# ──────────────────────────────────────────────
#  ANSI Colors & Styles
# ──────────────────────────────────────────────
R      = "\033[0m"
BOLD   = "\033[1m"
DIM    = "\033[2m"
CYAN   = "\033[96m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
RED    = "\033[91m"
BLUE   = "\033[94m"
MAG    = "\033[95m"
WHITE  = "\033[97m"

# ──────────────────────────────────────────────
#  Utility / Animation Functions
# ──────────────────────────────────────────────

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def slow_print(text, delay=0.025, end="\n"):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()

def spinner(text="Calculating", seconds=1.6, color=CYAN):
    frames = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
    end_t = time.time() + seconds
    i = 0
    while time.time() < end_t:
        sys.stdout.write(f"\r  {color}{frames[i % len(frames)]}{R}  {text} ")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write(f"\r  {GREEN}✔{R}  {text} {DIM}done{R}          \n")
    sys.stdout.flush()

def progress_bar(label="Analyzing Match Situation", duration=2.0):
    total = 35
    print(f"\n  {CYAN}{BOLD}{label}:{R}")
    for i in range(total + 1):
        filled = "█" * i
        empty  = "░" * (total - i)
        pct    = int((i / total) * 100)
        color  = GREEN if pct == 100 else YELLOW if pct > 60 else CYAN
        sys.stdout.write(f"\r  [{color}{filled}{DIM}{empty}{R}] {BOLD}{pct:>3}%{R}")
        sys.stdout.flush()
        time.sleep(duration / total)
    print("\n")

def loading_bar(label, total=25, delay=0.04):
    sys.stdout.write(f"  {CYAN}{label}{R}  [")
    for _ in range(total):
        time.sleep(delay)
        sys.stdout.write(f"{GREEN}█{R}")
        sys.stdout.flush()
    sys.stdout.write(f"]  {GREEN}Ready!{R}\n\n")
    sys.stdout.flush()

def divider(char="═", length=56, color=CYAN):
    print(f"{color}  {char * length}{R}")

def score_meter(value, current_score, max_val, width=45):
    """Visual bar showing low/mid/high, always anchored at current_score."""
    filled = int((value / max_val) * width)
    filled = max(0, min(filled, width))
    return f"{GREEN}{'█' * filled}{DIM}{'░' * (width - filled)}{R}"

# ──────────────────────────────────────────────
#  Banner
# ──────────────────────────────────────────────

def banner():
    clear()
    lines = [
        f"  {CYAN}{BOLD}╔══════════════════════════════════════════════════════╗",
        f"  ║   🏏  CRICKET SCORE PREDICTOR  —  Terminal Edition  ║",
        f"  ║          Smart Analytics · Powered by Python         ║",
        f"  ╚══════════════════════════════════════════════════════╝{R}",
    ]
    print()
    for line in lines:
        slow_print(line, delay=0.012)
    print()

# ──────────────────────────────────────────────
#  Input Helpers
# ──────────────────────────────────────────────

def get_float(prompt, min_v=0, max_v=9999):
    while True:
        try:
            val = float(input(f"  {YELLOW}➤{R}  {BOLD}{prompt}{R} : {GREEN}"))
            print(R, end="")
            if min_v <= val <= max_v:
                return val
            print(f"  {RED}✘  Must be between {min_v} and {max_v}{R}")
        except ValueError:
            print(f"  {RED}✘  Numbers only, please!{R}")

def get_int(prompt, min_v=0, max_v=9999):
    while True:
        try:
            val = int(input(f"  {YELLOW}➤{R}  {BOLD}{prompt}{R} : {GREEN}"))
            print(R, end="")
            if min_v <= val <= max_v:
                return val
            print(f"  {RED}✘  Must be between {min_v} and {max_v}{R}")
        except ValueError:
            print(f"  {RED}✘  Whole numbers only!{R}")

# ──────────────────────────────────────────────
#  Core Prediction Logic  (user's algorithm)
# ──────────────────────────────────────────────

def predict_score(current_overs, current_score, wickets, total_overs):
    remaining_overs = total_overs - current_overs

    current_rr = current_score / current_overs if current_overs > 0 else 0

    wickets_left = 10 - wickets

    if wickets_left >= 7:
        aggression_factor = 1.15
    elif wickets_left >= 4:
        aggression_factor = 1.0
    else:
        aggression_factor = 0.80

    projected_remaining = current_rr * aggression_factor * remaining_overs
    projected_remaining = max(0, projected_remaining)   # can't lose runs

    mid  = current_score + round(projected_remaining)
    low  = current_score + round(projected_remaining * 0.88)
    high = current_score + round(projected_remaining * 1.12)

    return low, mid, high, round(current_rr, 2), round(aggression_factor, 2)

# ──────────────────────────────────────────────
#  Risk & Phase Labels
# ──────────────────────────────────────────────

def risk_label(wickets, pct_done):
    if wickets >= 7:
        return f"{RED}HIGH RISK  – Running out of batters{R}"
    elif wickets >= 5:
        return f"{YELLOW}MODERATE   – Losing wickets quickly{R}"
    elif pct_done > 0.85:
        return f"{YELLOW}MODERATE   – Death overs pressure{R}"
    return f"{GREEN}LOW RISK   – Batting looks stable{R}"

def phase_label(pct_done):
    if pct_done < 0.33:
        return f"{BLUE}Powerplay / Early Innings{R}"
    elif pct_done < 0.67:
        return f"{YELLOW}Middle Overs{R}"
    return f"{RED}Death Overs{R}"

def aggression_label(af):
    if af >= 1.15:
        return f"{GREEN}Aggressive  (wickets in hand){R}"
    elif af >= 1.0:
        return f"{YELLOW}Steady  (balanced resources){R}"
    return f"{RED}Cautious  (low wickets){R}"

# ──────────────────────────────────────────────
#  Results Display
# ──────────────────────────────────────────────

def show_results(current_overs, current_score, wickets, total_overs,
                 low, mid, high, crr, af):

    overs_rem  = total_overs - current_overs
    pct_done   = current_overs / total_overs
    meter_max  = total_overs * 13  # rough upper bound for bar scale

    divider("═", 56, CYAN)
    slow_print(f"\n  {BOLD}{CYAN}📊  MATCH SUMMARY{R}\n", delay=0.02)

    rows = [
        ("Current Score",      f"{current_score}/{wickets}"),
        ("Current Run Rate",   f"{crr}  runs/over"),
        ("Overs Played",       f"{current_overs}"),
        ("Overs Remaining",    f"{overs_rem:.1f}"),
        ("Match Phase",        phase_label(pct_done)),
        ("Batting Approach",   aggression_label(af)),
        ("Risk Assessment",    risk_label(wickets, pct_done)),
    ]

    for label, val in rows:
        print(f"  {DIM}│{R}  {WHITE}{label:<22}{R}  {val}")

    # Progress bars
    print()
    print(f"  {DIM}Over Progress:{R}")
    op_fill = int((current_overs / total_overs) * 45)
    op_fill = max(0, min(op_fill, 45))
    print(f"  [{CYAN}{'█'*op_fill}{DIM}{'░'*(45-op_fill)}{R}]  {YELLOW}{current_overs}/{total_overs} ov{R}")

    print(f"  {DIM}Wickets Used:{R}")
    wk_color = RED if wickets >= 7 else YELLOW if wickets >= 5 else GREEN
    wk_fill = int((wickets / 10) * 45)
    print(f"  [{wk_color}{'█'*wk_fill}{DIM}{'░'*(45-wk_fill)}{R}]  {wk_color}{wickets}/10{R}")

    divider("─", 56, DIM)

    # Animated calculation steps
    print()
    spinner("Processing match data        ", 1.2, CYAN)
    spinner("Applying aggression factor   ", 0.9, YELLOW)
    spinner("Calculating score projection ", 1.0, MAG)
    progress_bar("Finalizing Prediction", duration=1.8)

    # Result box
    divider("═", 56, MAG)
    slow_print(f"  {BOLD}{MAG}🎯  PREDICTED FINAL SCORE{R}\n", delay=0.02)
    divider("─", 56, DIM)

    slow_print(f"  {GREEN}{BOLD}  Optimistic   :  {high:<6}{R}   {DIM}(best case  — things go well){R}",   delay=0.01)
    slow_print(f"  {YELLOW}{BOLD}  Most Likely  :  {mid:<6}{R}   {DIM}(expected   — current form){R}",    delay=0.01)
    slow_print(f"  {RED}{BOLD}  Conservative :  {low:<6}{R}   {DIM}(worst case — pressure/wickets){R}", delay=0.01)

    divider("─", 56, DIM)

    # Score meter
    print(f"\n  {DIM}Score Meter  (current={current_score}, scale to ~{meter_max}):{R}")
    print(f"  {DIM}Conservative:{R}  {score_meter(low,  current_score, meter_max)}  {RED}{low}{R}")
    print(f"  {DIM}Most Likely :{R}  {score_meter(mid,  current_score, meter_max)}  {YELLOW}{mid}{R}")
    print(f"  {DIM}Optimistic  :{R}  {score_meter(high, current_score, meter_max)}  {GREEN}{high}{R}")

    print()
    divider("═", 56, CYAN)
    slow_print(f"\n  {GREEN}{BOLD}✔  Prediction Complete!{R}\n", delay=0.02)

# ──────────────────────────────────────────────
#  Main
# ──────────────────────────────────────────────

def main():
    banner()
    loading_bar("Initialising Cricket Analytics Engine", total=28, delay=0.035)

    while True:
        divider("─", 56, CYAN)
        slow_print(f"\n  {BOLD}{WHITE}Enter match details below:{R}\n", delay=0.02)

        total_overs   = get_float("Total Overs in match         (e.g. 20 / 50)", 1, 50)
        current_overs = get_float(f"Current Overs completed      (e.g. 12.3, max {total_overs})", 0.1, total_overs - 0.1)
        current_score = get_int(  "Current Score  (runs)",  0, 999)
        wickets       = get_int(  "Wickets Fallen               (0 – 10)",        0, 9)

        low, mid, high, crr, af = predict_score(
            current_overs, current_score, wickets, total_overs
        )

        show_results(current_overs, current_score, wickets, total_overs,
                     low, mid, high, crr, af)

        print(f"  {CYAN}Predict another innings?{R}")
        again = input(f"  {YELLOW}➤{R}  {BOLD}(y / n){R} : {GREEN}").strip().lower()
        print(R)
        if again != "y":
            slow_print(f"\n  {CYAN}{BOLD}Thanks for using Cricket Score Predictor! 🏏{R}\n", delay=0.03)
            break

if __name__ == "__main__":
    main()
