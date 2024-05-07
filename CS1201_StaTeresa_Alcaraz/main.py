import os
from utils.user_manager import Usermanager

def main():
    print("Welcome to Dice Roll Game")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice or leave blank to cancel: ")
    if choice == '1':
        Usermanager.register()
    elif choice == '2':
        Usermanager.log_in()
    elif choice  == '3':
        print("Exitimg game!!!!")
    else:
        print("Invalid Output")

main()
        
    

