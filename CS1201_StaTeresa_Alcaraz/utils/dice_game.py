import os
import main
import random
from utils.score import Score
from utils.user_manager import Usermanager
from utils.user import user
from datetime import datetime

class DiceGame:
    def load_scores(self):
        pass
    def save_scores(self):
        pass
    def play_game(self):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        
        print(f"{Usermanager.username} roled: {dice1}")
        print(f"CPU roled: {dice2}")
        if dice1 > dice2:
            print(f"{Usermanager.username} won")
        elif dice1 < dice2:
            print("CPU won")
        elif dice1 == dice2:
            print("It's a tie!!!!!")
        
    def show_top_scores(self):
        pass
    def logout(slef):
        main.main()
    def menu(self):
        print(f"\nWelcome,{Usermanager.username}")
        print("1. Start Game")
        print("2. Show Top Scores")
        print("3. Log-out")
        choice = input("Enter your pr leave blank to cancel: ")
        if choice == '1':
            DiceGame.play_game(self)
        if choice == '2':
            DiceGame.show_top_scores(self)
        if choice  == '3':
            DiceGame.logout(self)
            

