#!/usr/bin/env python3

import pandas as pd
import os
import sys

# ── Colors ──────────────────────────────────────────────────────────────────
GREEN  = "\033[92m"
CYAN   = "\033[96m"
YELLOW = "\033[93m"
RED    = "\033[91m"
BOLD   = "\033[1m"
DIM    = "\033[2m"
RESET  = "\033[0m"

BANNER = f"""
{CYAN}{BOLD}╔══════════════════════════════════════════════════════╗
║         🥩  PROTEIN LOOKUP BOT  🥗                   ║
║     Top 500 Foods · Protein per 100g Database        ║
╚══════════════════════════════════════════════════════╝{RESET}
{DIM}Type a food name to look it up. Commands: help | list | top | quit{RESET}
"""

HELP_TEXT = f"""
{BOLD}Available Commands:{RESET}
  {CYAN}<food name>{RESET}     → Search for protein content (partial match supported)
  {CYAN}top [N]{RESET}         → Show top N highest-protein foods (default: 10)
  {CYAN}list [category]{RESET} → List all foods in a category
  {CYAN}categories{RESET}      → Show all available categories
  {CYAN}help{RESET}            → Show this help message
  {CYAN}quit / exit{RESET}     → Exit the bot
"""

# ── Load Data ────────────────────────────────────────────────────────────────
def load_data():
    # Look for the Excel file next to the script or in current directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.path.join(script_dir, "Top500_Protein_Foods.xlsx"),
        "Top500_Protein_Foods.xlsx",
        os.path.join(script_dir, "top500_protein_foods.xlsx"),
    ]
    for path in candidates:
        if os.path.exists(path):
            df = pd.read_excel(path)
            df.columns = ["rank", "food", "category", "protein"]
            df["food_lower"] = df["food"].str.lower()
            df["category_lower"] = df["category"].str.lower()
            return df
    print(f"{RED}❌  Could not find 'Top500_Protein_Foods.xlsx'.")
    print(f"    Place it in the same folder as this script and try again.{RESET}")
    sys.exit(1)

# ── Protein bar visual ───────────────────────────────────────────────────────
def protein_bar(value, max_val=100):
    filled = int((value / max_val) * 30)
    bar = "█" * filled + "░" * (30 - filled)
    if value >= 50:
        color = GREEN
    elif value >= 20:
        color = CYAN
    elif value >= 10:
        color = YELLOW
    else:
        color = DIM
    return f"{color}{bar}{RESET}"

# ── Search ───────────────────────────────────────────────────────────────────
def search_food(df, query):
    q = query.lower().strip()
    # Exact match first
    exact = df[df["food_lower"] == q]
    if not exact.empty:
        return exact

    # Partial match (all words in query appear in food name)
    words = q.split()
    mask = df["food_lower"].apply(lambda f: all(w in f for w in words))
    partial = df[mask]
    if not partial.empty:
        return partial

    # Single-word fuzzy: any word from query
    mask2 = df["food_lower"].apply(lambda f: any(w in f for w in words))
    return df[mask2]

# ── Display results ──────────────────────────────────────────────────────────
def display_results(results):
    if results.empty:
        print(f"\n{RED}  No foods found matching your query.{RESET}")
        print(f"{DIM}  Try a simpler term like 'chicken', 'egg', 'beef'{RESET}\n")
        return

    print()
    print(f"  {'#':<5} {'Food Item':<40} {'Category':<22} {'Protein/100g':>12}  {'Bar'}")
    print(f"  {'─'*5} {'─'*40} {'─'*22} {'─'*12}  {'─'*30}")

    for _, row in results.iterrows():
        bar = protein_bar(row["protein"])
        protein_str = f"{BOLD}{YELLOW}{row['protein']:.1f}g{RESET}"
        print(f"  {int(row['rank']):<5} {row['food']:<40} {DIM}{row['category']:<22}{RESET} {protein_str:>12}  {bar}")
    print()

# ── Top N ────────────────────────────────────────────────────────────────────
def show_top(df, n=10):
    top = df.nlargest(n, "protein")
    print(f"\n{BOLD}{CYAN}  🏆 Top {n} Highest Protein Foods (per 100g){RESET}\n")
    display_results(top)

# ── Categories ───────────────────────────────────────────────────────────────
def show_categories(df):
    cats = df["category"].value_counts()
    print(f"\n{BOLD}{CYAN}  📂 Available Categories:{RESET}\n")
    for cat, count in cats.items():
        print(f"  {CYAN}•{RESET} {cat:<30} {DIM}({count} foods){RESET}")
    print()

def list_category(df, cat_query):
    q = cat_query.lower().strip()
    mask = df["category_lower"].str.contains(q)
    results = df[mask].sort_values("protein", ascending=False)
    if results.empty:
        print(f"\n{RED}  Category '{cat_query}' not found.{RESET}")
        print(f"{DIM}  Use 'categories' to see all available categories.{RESET}\n")
    else:
        print(f"\n{BOLD}{CYAN}  📋 Foods in category matching '{cat_query}':{RESET}\n")
        display_results(results)

# ── Main Loop ────────────────────────────────────────────────────────────────
def main():
    print(BANNER)
    df = load_data()
    print(f"{GREEN}  ✅ Loaded {len(df)} foods from database.{RESET}\n")

    while True:
        try:
            user_input = input(f"{BOLD}{GREEN}🔍 Search food > {RESET}").strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n{CYAN}  👋 Goodbye! Stay protein-rich!{RESET}\n")
            break

        if not user_input:
            continue

        cmd = user_input.lower()

        if cmd in ("quit", "exit", "q"):
            print(f"\n{CYAN}  👋 Goodbye! Stay protein-rich!{RESET}\n")
            break

        elif cmd in ("help", "h", "?"):
            print(HELP_TEXT)

        elif cmd == "categories":
            show_categories(df)

        elif cmd.startswith("top"):
            parts = cmd.split()
            n = 10
            if len(parts) > 1:
                try:
                    n = int(parts[1])
                    n = max(1, min(n, 500))
                except ValueError:
                    print(f"{RED}  Usage: top [number]  e.g. top 20{RESET}\n")
                    continue
            show_top(df, n)

        elif cmd.startswith("list"):
            cat = user_input[4:].strip()
            if not cat:
                show_categories(df)
            else:
                list_category(df, cat)

        else:
            results = search_food(df, user_input)
            display_results(results)

if __name__ == "__main__":
    main()
