import requests
from bs4 import BeautifulSoup
import csv

# --- CONFIGURATION ---
URL = "https://quotes.toscrape.com"  # Example website with open data
OUTPUT_FILE = "quotes.csv"

# --- SCRAPER FUNCTION ---
def scrape_quotes(url):
    quotes_data = []
    while url:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to fetch {url}")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")

        for q in quotes:
            text = q.find("span", class_="text").get_text()
            author = q.find("small", class_="author").get_text()
            tags = [tag.get_text() for tag in q.find_all("a", class_="tag")]
            quotes_data.append({"text": text, "author": author, "tags": ", ".join(tags)})

        next_button = soup.find("li", class_="next")
        if next_button:
            url = "https://quotes.toscrape.com" + next_button.find("a")["href"]
        else:
            url = None

    return quotes_data

# --- SAVE TO CSV ---
def save_to_csv(data, filename):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["text", "author", "tags"])
        writer.writeheader()
        writer.writerows(data)
    print(f"Data saved to {filename}")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    data = scrape_quotes(URL)
    save_to_csv(data, OUTPUT_FILE)
