import pandas as pd
import os
import sys

# ==============================
# COLORS FOR TERMINAL
# ==============================

class Color:
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN    = "\033[96m"
    WHITE   = "\033[97m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    RESET   = "\033[0m"

# ==============================
# LOAD EXCEL FILE
# ==============================

FILE_PATH = "Top500_Protein_Foods.xlsx"

def load_data():
    if not os.path.exists(FILE_PATH):
        print(f"\n{Color.RED}[ERROR] File '{FILE_PATH}' not found!")
        print(f"        Make sure 'Top500_Protein_Foods.xlsx' is in the same folder as this script.{Color.RESET}\n")
        sys.exit(1)

    try:
        df = pd.read_excel(FILE_PATH)
        df.columns = df.columns.str.strip()
        df["Food Item"] = df["Food Item"].astype(str).str.strip()
        df["Category"]  = df["Category"].astype(str).str.strip()
        df["Protein per 100g (g)"] = pd.to_numeric(df["Protein per 100g (g)"], errors="coerce")
        return df
    except Exception as e:
        print(f"\n{Color.RED}[ERROR] Could not read file: {e}{Color.RESET}\n")
        sys.exit(1)

# ==============================
# PROTEIN BAR VISUAL
# ==============================

def protein_bar(value):
    max_val = 100
    filled  = int((min(value, max_val) / max_val) * 25)
    bar     = "█" * filled + "░" * (25 - filled)

    if value >= 50:
        color = Color.GREEN
    elif value >= 25:
        color = Color.CYAN
    elif value >= 10:
        color = Color.YELLOW
    else:
        color = Color.DIM

    return f"{color}{bar}{Color.RESET} {Color.BOLD}{value:.1f}g{Color.RESET}"

# ==============================
# PROTEIN LEVEL LABEL
# ==============================

def protein_label(value):
    if value >= 50:
        return f"{Color.GREEN}★ Very High Protein{Color.RESET}"
    elif value >= 25:
        return f"{Color.CYAN}▲ High Protein{Color.RESET}"
    elif value >= 10:
        return f"{Color.YELLOW}● Medium Protein{Color.RESET}"
    else:
        return f"{Color.DIM}▼ Low Protein{Color.RESET}"

# ==============================
# SEARCH FOOD (SMART MATCHING)
# ==============================

def find_protein(df, food_name):
    query = food_name.strip().lower()
    food_col = df["Food Item"].str.lower()

    # 1. Exact match
    result = df[food_col == query]

    # 2. All words match
    if result.empty:
        words = query.split()
        mask  = food_col.apply(lambda f: all(w in f for w in words))
        result = df[mask]

    # 3. Any word match
    if result.empty:
        words  = query.split()
        mask   = food_col.apply(lambda f: any(w in f for w in words))
        result = df[mask]

    if result.empty:
        print(f"\n{Color.RED}  ✗ No results found for '{food_name}'.{Color.RESET}")
        print(f"{Color.DIM}  Try simpler keywords like 'chicken', 'egg', 'salmon', 'beef'{Color.RESET}\n")
        return

    print(f"\n{Color.BOLD}{Color.CYAN}  Found {len(result)} result(s) for '{food_name}':{Color.RESET}")
    print(f"  {'─'*65}")

    for _, row in result.iterrows():
        protein = row["Protein per 100g (g)"]
        label   = protein_label(protein)
        bar     = protein_bar(protein)

        print(f"\n  {Color.BOLD}{Color.WHITE}🍽  {row['Food Item']}{Color.RESET}")
        print(f"  {Color.DIM}Category :{Color.RESET}  {Color.MAGENTA}{row['Category']}{Color.RESET}")
        print(f"  {Color.DIM}Protein  :{Color.RESET}  {bar}")
        print(f"  {Color.DIM}Level    :{Color.RESET}  {label}")
        print(f"  {'─'*65}")

    print()

# ==============================
# TOP N HIGH PROTEIN FOODS
# ==============================

def show_top(df, n=10):
    n   = max(1, min(n, len(df)))
    top = df.nlargest(n, "Protein per 100g (g)")

    print(f"\n{Color.BOLD}{Color.YELLOW}  🏆 Top {n} Highest Protein Foods (per 100g){Color.RESET}")
    print(f"  {'─'*65}")
    print(f"  {Color.BOLD}{'#':<5}{'Food Item':<35}{'Category':<20}{'Protein':>10}{Color.RESET}")
    print(f"  {'─'*65}")

    for i, (_, row) in enumerate(top.iterrows(), 1):
        protein = row["Protein per 100g (g)"]
        medal   = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f" {i}."
        color   = Color.GREEN if protein >= 50 else Color.CYAN if protein >= 25 else Color.YELLOW
        print(f"  {medal:<5}{row['Food Item']:<35}{Color.DIM}{row['Category']:<20}{Color.RESET}{color}{protein:.1f}g{Color.RESET}")

    print()

# ==============================
# LIST CATEGORIES
# ==============================

def show_categories(df):
    cats = df["Category"].value_counts()
    print(f"\n{Color.BOLD}{Color.CYAN}  📂 All Categories ({len(cats)} total):{Color.RESET}\n")

    for i, (cat, count) in enumerate(cats.items(), 1):
        avg_protein = df[df["Category"] == cat]["Protein per 100g (g)"].mean()
        bar_len     = int((avg_protein / 100) * 20)
        mini_bar    = "█" * bar_len + "░" * (20 - bar_len)

        color = Color.GREEN if avg_protein >= 30 else Color.CYAN if avg_protein >= 15 else Color.YELLOW
        print(f"  {Color.DIM}{i:>2}.{Color.RESET} {cat:<28} {Color.DIM}{count} foods{Color.RESET}  {color}{mini_bar}{Color.RESET} avg {avg_protein:.1f}g")

    print()

# ==============================
# LIST FOODS IN A CATEGORY
# ==============================

def list_category(df, cat_query):
    query   = cat_query.strip().lower()
    matches = df[df["Category"].str.lower().str.contains(query, na=False)]

    if matches.empty:
        print(f"\n{Color.RED}  ✗ No category matching '{cat_query}' found.{Color.RESET}")
        print(f"{Color.DIM}  Type 'categories' to see all available categories.{Color.RESET}\n")
        return

    matches = matches.sort_values("Protein per 100g (g)", ascending=False)
    cats    = matches["Category"].unique()

    for cat in cats:
        cat_df = matches[matches["Category"] == cat]
        print(f"\n{Color.BOLD}{Color.CYAN}  📋 {cat} ({len(cat_df)} foods){Color.RESET}")
        print(f"  {'─'*65}")
        print(f"  {Color.BOLD}{'#':<5}{'Food Item':<42}{'Protein':>10}{Color.RESET}")
        print(f"  {'─'*65}")

        for i, (_, row) in enumerate(cat_df.iterrows(), 1):
            protein = row["Protein per 100g (g)"]
            color   = Color.GREEN if protein >= 50 else Color.CYAN if protein >= 25 else Color.YELLOW if protein >= 10 else Color.DIM
            print(f"  {i:<5}{row['Food Item']:<42}{color}{protein:.1f}g{Color.RESET}")

        print()

# ==============================
# COMPARE TWO FOODS
# ==============================

def compare_foods(df, query):
    lower_query = query.lower()
    idx = lower_query.find(" vs ")
    if idx == -1:
        print(f"\n{Color.RED}  Usage: compare chicken vs beef{Color.RESET}\n")
        return
    parts = [query[:idx].strip(), query[idx+4:].strip()]

    results = []
    for part in parts:
        food_col = df["Food Item"].str.lower()
        match    = df[food_col.str.contains(part.lower(), na=False)]
        if match.empty:
            print(f"\n{Color.RED}  ✗ '{part}' not found in database.{Color.RESET}\n")
            return
        results.append(match.iloc[0])

    r1, r2 = results
    p1, p2 = r1["Protein per 100g (g)"], r2["Protein per 100g (g)"]

    print(f"\n{Color.BOLD}{Color.CYAN}  ⚡ Protein Comparison (per 100g){Color.RESET}")
    print(f"  {'─'*55}")
    print(f"\n  {Color.BOLD}{r1['Food Item']}{Color.RESET}")
    print(f"  {protein_bar(p1)}")
    print(f"\n  {Color.BOLD}{r2['Food Item']}{Color.RESET}")
    print(f"  {protein_bar(p2)}")
    print()

    if p1 > p2:
        diff = p1 - p2
        print(f"  {Color.GREEN}✔ {r1['Food Item']} has MORE protein by {diff:.1f}g{Color.RESET}\n")
    elif p2 > p1:
        diff = p2 - p1
        print(f"  {Color.GREEN}✔ {r2['Food Item']} has MORE protein by {diff:.1f}g{Color.RESET}\n")
    else:
        print(f"  {Color.YELLOW}= Both have equal protein ({p1:.1f}g){Color.RESET}\n")

# ==============================
# SHOW HELP
# ==============================

def show_help():
    print(f"""
{Color.BOLD}{Color.CYAN}  ╔══════════════════════════════════════════════════╗
  ║               AVAILABLE COMMANDS                ║
  ╚══════════════════════════════════════════════════╝{Color.RESET}

  {Color.YELLOW}<food name>{Color.RESET}              Search protein content
                           Example: {Color.DIM}chicken{Color.RESET}, {Color.DIM}salmon{Color.RESET}, {Color.DIM}egg{Color.RESET}

  {Color.YELLOW}top [N]{Color.RESET}                  Show top N high-protein foods
                           Example: {Color.DIM}top 10{Color.RESET}, {Color.DIM}top 25{Color.RESET}

  {Color.YELLOW}compare X vs Y{Color.RESET}           Compare protein of two foods
                           Example: {Color.DIM}compare chicken vs beef{Color.RESET}

  {Color.YELLOW}list <category>{Color.RESET}          Show all foods in a category
                           Example: {Color.DIM}list fish{Color.RESET}, {Color.DIM}list dairy{Color.RESET}

  {Color.YELLOW}categories{Color.RESET}               Show all food categories with avg protein

  {Color.YELLOW}help{Color.RESET}                     Show this help message

  {Color.YELLOW}exit / quit{Color.RESET}              Exit the chatbot
""")

# ==============================
# MAIN CHATBOT LOOP
# ==============================

def main():
    # Banner
    print(f"""
{Color.CYAN}{Color.BOLD}╔══════════════════════════════════════════════════════╗
║                                                      ║
║         🥩  PROTEIN INFO CHATBOT  🥗                 ║
║                                                      ║
║       500 Foods · Protein per 100g Database          ║
║                                                      ║
╚══════════════════════════════════════════════════════╝{Color.RESET}
{Color.DIM}  Type a food name, a command, or 'help' to get started.{Color.RESET}
""")

    # Load data
    df = load_data()
    print(f"{Color.GREEN}  ✔ Database loaded: {len(df)} foods across {df['Category'].nunique()} categories.{Color.RESET}\n")

    # Chat loop
    while True:
        try:
            user_input = input(f"{Color.BOLD}{Color.GREEN}💬 You > {Color.RESET}").strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n{Color.CYAN}  👋 Goodbye! Stay healthy and protein-rich!{Color.RESET}\n")
            break

        if not user_input:
            continue

        cmd = user_input.lower()

        # --- EXIT ---
        if cmd in ("exit", "quit", "q", "bye"):
            print(f"\n{Color.CYAN}  👋 Goodbye! Stay healthy and protein-rich!{Color.RESET}\n")
            break

        # --- HELP ---
        elif cmd in ("help", "h", "?", "commands"):
            show_help()

        # --- CATEGORIES ---
        elif cmd == "categories":
            show_categories(df)

        # --- TOP N ---
        elif cmd.startswith("top"):
            parts = cmd.split()
            n = 10
            if len(parts) > 1:
                try:
                    n = int(parts[1])
                except ValueError:
                    print(f"\n{Color.RED}  Usage: top 10  (enter a number after 'top'){Color.RESET}\n")
                    continue
            show_top(df, n)

        # --- LIST CATEGORY ---
        elif cmd.startswith("list"):
            cat = user_input[4:].strip()
            if not cat:
                show_categories(df)
            else:
                list_category(df, cat)

        # --- COMPARE ---
        elif " vs " in user_input.lower():
            # Strip optional "compare" prefix
            clean = user_input
            if clean.lower().startswith("compare "):
                clean = clean[8:]
            compare_foods(df, clean)

        # --- SEARCH FOOD ---
        else:
            find_protein(df, user_input)


if __name__ == "__main__":
    main()
