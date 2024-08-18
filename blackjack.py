import random

def deal_card():
  """Returns a random card from the deck."""
  cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
  card=random.choice(cards)
  return card

def calculate_score(cards):
  """Returns a calculated score of the cards"""
  if sum(cards)==21 and len(cards)==2:
    return 0
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def comparefunction(u_score,c_score):
  if u_score==c_score:
    return "Draw"
  elif c_score==0:
    return "Lose, opponent has Blackjack"
  elif u_score==0:
    return "Win with a Blackjack"
  elif u_score>21:
    return "You went over. You lose"
  elif c_score>21:
    return "Opponent went over. You win"
  elif u_score>c_score:
    return "You win"
  else:
    return "You lose"

def play_game():
  user_cards=[]
  computer_cards=[]
  is_gameover=False
  computer_score=-1
  user_score=-1
  
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not is_gameover:
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    if user_score==0 or computer_score==0 or user_score>21:
      is_gameover=True
    else:
      user_should_deal=input("Tyoe 'y' to get another card, type 'n' to pass:")
      if  user_should_deal=="y":
        user_cards.append(deal_card())
      else:
        is_gameover=True
  
  while computer_score!=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score=calculate_score(computer_cards)
  
  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Coumputer's final hand: {computer_cards}, final score: {computer_score}")
  print(comparefunction(user_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  print("\n"*20)#clear screen
  play_game()

  
    
      
  
