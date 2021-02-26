import random
userChoice = ""
gameOver = False
#setting the loop
while not gameOver or userChoice != 4:
  userChoice = int(input("Select 1 for Rock, 2 for Paper, 3 for Scissors or 4 to Quit: "))
  if userChoice == 4:
    print("Thanks for playing")
    gameOver = True
    break
    
  else:
    computerChoice = random.randint(1, 3)
    print(f"Your choice is: {userChoice}")
    print(f"The computer's choice is: {computerChoice}")
    if userChoice == computerChoice:
      print("Tie game")
    elif userChoice == 1:
      if computerChoice == 2:
        print("You lose")
      else:
        print("You win")
    elif userChoice == 2:
      if computerChoice == 3:
        print("You lose")
      else:
        print("You win")
    elif userChoice == 3:
      if computerChoice == 1:
        print("You lose")
      else:
        print("You win")