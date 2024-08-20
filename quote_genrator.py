from quote import quote

import random

def generate_quote():
  
  quotes_list = quote("motivation", limit=50)
  
  random_quote = random.choice(quotes_list)
  
  return f'"{random_quote["quote"]}" - {random_quote["author"]}'


if __name__ == "__main__":
  print("Here is a quote for you:")
  print(generate_quote())
  