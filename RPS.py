# A text based RPS game
# Author: Fred III Whiteman
# Date: July 19, 2020



from random import choice

# the welcom section simply welcomes the player and confirms that they wish to play the game.

def welcome():
    print("Welcome to my Rock Paper Scissors game!")
    while True:
        play = input("Would you like to play? [Y/N] ")
        if play.capitalize() == "N":
            print("Lame!")
            break
        elif play.capitalize() == "Y":
            game()
            break
        else:
            print(f"'{play}' is not a valid answer")

# the game section is the actual game, it provides three options for the player then randomly chooses for the computer and compairs to decide the winner

def game():
    state = ["Rock", "Paper", "Scissors"]
    while True:
        p_state = input("Choose between Rock, Paper, or Scissors. ")
        p_state = p_state.capitalize()
        if p_state not in state:
            print(f"{p_state} is not a vailid input")
            continue
        else:
            c_state = choice(state)
            if p_state == c_state:
                print(f"The computer also chose {p_state}!")
                game()
                break
            elif p_state == "Rock" and c_state == "Paper":
                print(f"The computer chose {c_state}! You loose!")
                play_again()
                break
            elif p_state == "Rock" and c_state == "Scissors":
                print(f"The computer chose {c_state}! You Win!")
                play_again()
                break
            elif p_state == "Paper" and c_state =="Scissors":
                print(f"The computer chose {c_state}! You loose!")
                play_again()
                break
            elif p_state == "Paper" and c_state == "Rock":
                print(f"The computer chose {c_state}! You Win!")
                play_again()
                break
            elif p_state == "Scissors" and c_state == "Rock":
                print(f"The computer chose {c_state}! You loose!")
                play_again()
                break
            elif p_state == "Scissors" and c_state == "Paper":
                print(f"The computer chose {c_state}! You Win!")
                play_again()
                break

# this section is the same as "welcome" but initailises after a round is ended. It also clears the screen of the last round.

def play_again():
    while True:
        p_a = input("Would you like to play again? [Y/N] ")
        if p_a.capitalize() == "N":
            print("Lame!")
            break
        elif p_a.capitalize() == "Y":
            import os
            os.system('cls' if os.name == 'nt' else 'clear')
            game()
            break
        else:
            print(f"'{p_a}' is not a valid answer")

def main():
    welcome()

main()