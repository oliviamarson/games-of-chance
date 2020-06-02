Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> import random

money = 100

#Write your game of chance functions here
def coin_flip(guess, bet):
  print("Welcome to the game Heads or Tails!")
  
  #Make sure bet is above 0
  if bet <= 0:
    print("Your bet must be more than 0. Please try again.")
    print("-------------------")
    return 0

  #Make sure guess is Heads or Tails only
  if guess != "Heads" and guess != "Tails":
    print("Your guess is not valid. Please enter either 'Heads' or 'Tails'.")
    print("-------------------")
    return 0  

  #Flip the coin. 1 = Heads and 2 = Tails.
  num = random.randint(1,2)
  if num == 1:
    print("Coin Flip is: Heads")
  elif num == 2:
    print("Coin Flip is: Tails")  
  
  #If the guess is right you double your bet, if not you lose.
  if (num == 1 and guess == "Heads") or (num == 2 and guess == "Tails"):
    winnings = bet * 2
    print("You won! Your winnings are: £" + str(winnings))
    print("-------------------")
    return winnings
  else:
    winnings = - bet
    print("You lost your bet. You lose: £" + str(winnings))
    print("-------------------")
    return winnings



def cho_han(guess, bet):
  print("Welcome to the game Cho Han!")
  
  #Make sure bet is above 0
  if bet <= 0:
    print("Your bet must be more than 0. Please try again.")
    print("-------------------")
    return 0
  
  #Make sure guess is Even or Odd only
  if guess != "Even" and guess != "Odd":
    print("Your guess is not valid. Please enter either 'Even' or 'Odd'.")
    print("-------------------")
    return 0

  #Roll the two dice and total the number.  
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  result = dice1 + dice2
  print("Sum of Dice is: " + str(result))
  
  #Guess Odd or Even and if the guess is right you double your bet, if not your lose.
  if (result % 2 == 0 and guess == "Even") or (result % 2 != 0 and guess == "Odd"):
    winnings = bet * 2
    print("You won! Your winnings are: £" + str(winnings))
    print("-------------------")
    return winnings
  else:
    winnings = - bet
    print("You lost your bet. You lose: £" + str(winnings))
    print("-------------------")
    return winnings
    


def deck_of_cards(bet):
  print("Welcome to the game High Card or Lower!")
  
  #Make sure bet is above 0
  if bet <= 0:
    print("Your bet must be more than 0. Please try again.")
    print("-------------------")
    return 0

  #Draw two cards for each player.
  draw1 = random.randint(1, 10)
  draw2 = random.randint(1, 10)
  print("Your card is: " + str(draw1))
  print("Your opponent's card is: " + str(draw2))
  
  #If your card or opponents card won they double their bet, and the other player loses. If both players tie they get their money back.
  if draw1 > draw2:
    winnings = bet * 2
    print("You won! Your winnings are: £" + str(winnings))
    print("-------------------")
    return winnings
  elif draw2 > draw1:
    winnings = - bet
    print("Your opponent won. You lose: £" + str(winnings))
    print("-------------------")
    return winnings
  else:
    print("You both tied! You get your money back: £" + str(bet))
    print("-------------------") 
    return bet    




def roulette(guess, bet):
  print("Welcome to the game Roulette!")
  
  #Make sure bet is above 0
  if bet <= 0:
    print("Your bet must be more than 0. Please try again.")
    print("-------------------")
    return 0
  
  #Spin the wheel to find the number you land on 
  result = random.randint(0, 36)
  print("You landed on: " + str(result))
  
  #If the result is even and not equal to 0 and the guess was 'Even', bet is doubled. 
  #If the result is odd and not equal to 0 and the guess was 'Odd', bet is doubled.
  #If the guess equals the result exactly and result does not equal 0, bet is 20 times the bet.
  #If no guess is right you lose your bet.
  if (result % 2 == 0) and (result != 0) and (guess == "Even"):
    winnings = bet * 2
    print("You won! Your winnings are: £" + str(winnings))
    return winnings 
  elif (result % 2 != 0) and (result != 0) and guess == "Odd":
    winnings = bet * 2
    print("You won! Your winnings are: £" + str(winnings))
    return winnings
  elif guess == result and (result != 0):
    winnings = bet * 20
    print("You won! Your winnings are: £" + str(winnings))
    return winnings  
  else:
    winnings = - bet
    print("You lost your bet. You lose: £" + str(winnings))
    return winnings

       
#Call your game of chance functions here
money += coin_flip("Heads", 100)
money += cho_han("Odd", 50)
money += deck_of_cards(7.38)
money += roulette(13, 5)
print("-------------------")
print("Your total amount of winnings are: £" + str(money))

