"""
Rock paper scissor game using random module and other concepts 

"""

import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock,paper,scissors] #created a list for above images

user_choice = int(input("What do you choose? 0 for rock, 1 for paper, 2 for scissors \n"))

if user_choice > 3: # i pasted this here to solve the bug which occured when i input 5 index out of range somethin..
    print("You entered a invalid number, You lose")
else:
    print(game_images[user_choice]) # printing of the user choice 

computer_choice = random.randint(0,2) #generating a random number using random module

print(f"computer chooose {computer_choice}")

print(game_images[computer_choice]) #printing image of computer choice

#These are the possible combinations of rock paper and scissor with and logical operator
# if user_choice > 3:
#     print("You entered a invalid number, You lose") #this should be at top as invalid number should be checked first

if user_choice ==0 and computer_choice==2:  # follow a pattern  0 and 2 
    print("You win")
elif user_choice ==2 and computer_choice ==0: # 2 and 0
    print("You lose")
elif user_choice == 2 and computer_choice ==0:
    print("You lose")
elif user_choice ==0 and computer_choice==2:
    print("You win")
elif user_choice==2 and computer_choice==1:
    print("you win")
elif user_choice==1 and computer_choice==2:
    print("you lose")
elif user_choice==0 and computer_choice==1:
    print("you lose")
elif user_choice==1 and computer_choice==0:
    print("You win")
else:
    print("its a draw")

