import random

def get_choices():
    print("Welcome to the Game")
    player_choice = input("Enter a choice (Rock, Paper, Scissors): ")
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, Computer chose {computer}")
    if player == computer:
        return "It's a Tie!"
    elif player == "Rock":
        if computer == "Scissors":   
            return "Rock smashes Scissors! You Win."
        else:
            return "Paper covers Rock! You Lose."
    elif player == "Paper":
        if computer == "Scissors":   
            return "Scissors cut Paper! You Lose."
        else:
            return "Paper covers Rock! You Win."
    elif player == "Scissors":
        if computer == "Paper":   
            return "Scissors cut Paper! You Win."
        else:
            return "Rock smashes Scissors! You Lose."

while True:
    choices = get_choices()
    result = check_win(choices["player"], choices["computer"])
    print(result)
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break
