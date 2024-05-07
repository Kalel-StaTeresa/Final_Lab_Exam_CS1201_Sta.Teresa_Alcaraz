from utils.dice_game import DiceGame
from utils.user import user

def main():
    print("Welcome to Dice Roll Game")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice or leave blank to cancel: ")
    if choice == '1':
        user.register()
    if choice == '2':
        user.log_in()
    if choice
    

