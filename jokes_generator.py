import pyjokes

def generate_jokes():
  joke = pyjokes.get_joke()
  return joke

if __name__ == "__main__":
  print("Here's a joke for you:")
  print(generate_jokes())
  