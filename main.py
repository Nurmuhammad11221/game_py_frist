import random

randomInteger = random.randint(1, 10)
print(randomInteger)

randomFloat = random.random() * 5

print(randomFloat)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.(___)
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
---.(___)
'''



#Kodni shu yerdan davom ettiring 👇



game_images = [rock, paper, scissors] 

user_choise = int(input("what do you choice? Type 0 for Rock, 1 for paper, 2 for scissors.\n"))

print(game_images[user_choise])

computer_choice = random.randint(0, 2)
print("Camputer choice")
print(game_images[computer_choice])

if user_choise >= 3 or user_choise < 0:
    print("Siz notogri raqam tanladingiz, yutqazadingiz!")

elif user_choise == 0 and computer_choice == 2:
    print("Siz yutdingiz!")

elif computer_choice == 0 and user_choise == 2:
    print("Siz Maglub boldingiz!")

elif computer_choice > user_choise:
    print("Siz Maglub boldingiz!")

elif user_choise > computer_choice:
    print("Siz yutdingiz!")

elif computer_choice == user_choise:
    print("Durang!")


































# love_score = random.randint(1 ,100)
# print(f"Your love score is {love_score}")