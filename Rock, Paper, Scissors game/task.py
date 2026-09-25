rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
sign=[rock,paper,scissors]
choice=input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

if choice=="0":
    print(rock)
elif choice=="1":
    print(paper)
elif choice=="2":
    print(scissors)

print("Computer choice:")
random_choice=random.choice(sign)
if random_choice==rock:
    print(rock)
elif random_choice==paper:
    print(paper)
elif random_choice==scissors:
    print(scissors)

if choice=="0":
    if  random_choice==rock:
        print("Its a draw")
    elif random_choice==paper:
        print("you loose")
    else:
        print("You win")
if choice=="1":
    if  random_choice==rock:
        print("you win")
    elif random_choice==paper:
        print("Its a draw")
    else:
        print("You loose")
if choice=="2":
    if  random_choice==rock:
        print("you loose")
    elif random_choice==paper:
        print("you win")
    else:
        print("Its a draw")
