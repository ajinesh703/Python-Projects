import pyshorteners

def shorten_url(url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(url)

url = input("Enter URL: ")
print("Shortened URL:", shorten_url(url))
