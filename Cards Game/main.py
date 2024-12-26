import random

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    
class LinkedList:
  def __init__(self):
    self.head = None
    
  def append(self, value):
    new_node = Node(value)
    if not self.head:
      self.head = new_node
    
    else:
      current = self.head
      while current.next:
        current = current.next
      current.next = new_node
      
  def pop(self):
    if not self.head:
      return None
    value = self.head.value
    self.head = self.head.next
    return value
  
  def to_list(self):
    current = self.head
    result = []
    while current:
      result.append(current.value)
      current = current.next
    return result
  
  def shuffle(self):
    cards = self.to_list()
    random.shuffle(cards)
    self.head = None
    for card in cards:
      self.append(card)
      
def create_deck():
  suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
  ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
  
  deck = LinkedList()
  for suit in suits:
    for rank in ranks:
      deck.append(f"{rank} of {suit}")
  return deck

def play_game():
  print("Wlcome to the card shuffle Game!")
  deck = create_deck()
  print("Deck created!. Shuufling the deck...")
  deck.shuffle()
  
  while True:
    print("\nOptions: [1] Draw a card [2] Shuffle deck [3] Exit")
    choice = input("Choose an option: ")
    
    if choice == '1':
      card = deck.pop()
      if card:
        print(f"You drew: {card}")
      else:
        print("The deck is empty!")
        
    elif choice == '2':
      deck.shuffle()
      print("Shuffling the deck...")
      
    elif choice == '3':
      print("Thanks for playing!")
      break
    else:
      print("Invalid choice. Please try again.")
      
if __name__ == "__main__":
  play_game()
  
