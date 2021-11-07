import random
chosen_num = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors."))

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
hands = [rock, paper, scissors]

print(hands[chosen_num])

computer_choice = random.randint(0,2)

print("Computer chose:")
print(hands[computer_choice])

if chosen_num == computer_choice:
  print("It's a draw")
elif chosen_num == 0 and computer_choice == 1:
  print("You lose.")
elif chosen_num == 1 and computer_choice == 0:
  print("You win.")
elif chosen_num == 1 and computer_choice == 2:
  print("You lose.")
elif chosen_num == 2 and computer_choice == 1:
  print("You win.")
elif chosen_num == 0 and computer_choice == 2:
  print("You win.")
elif chosen_num == 2 and computer_choice == 0:
  print("You lose.")
