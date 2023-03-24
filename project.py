from project_classes import OneTurnComp, OneTurnPlayer
import random
import time
import csv
from datetime import datetime
from tabulate import tabulate
from colorama import init, Fore, Back
init(autoreset=True)

speed = 0.03  # default speed = 0.03


def main():
    """Make the descripcion."""
    # Introducing
    intro1()

    # Asking for name
    player_name = name_input()

    # Number of players
    number_of_players = settings()

    # Creating list of players
    players_in_game_det = beginning(player_name, number_of_players)

    # Rules
    intro2(player_name)

    # loop for playing
    max_score = 0
    while max_score < 13:
        show_table(players_in_game_det)
        input(Fore.CYAN + "--- press ENTER to continue ---\n")
        players_in_game_det, max_score = one_round(
            players_in_game_det, player_name, max_score
            )

    # final score
    show_table(players_in_game_det)

    # congratulations
    winner_name = congratulations(players_in_game_det)
    print(
        Fore.CYAN + "The winner is... ",
        Fore.MAGENTA + Back.WHITE + f"   {winner_name}   "
    )

    # highscore
    highscore_write(player_name, players_in_game_det)
    top_ten_show()


def intro1():
    """Typing introduction."""
    introduce = "\nThis game is based on Steve Jackson's board game Zombie Dice.\nYou can check the rules here: http://www.sjgames.com/dice/zombiedice/img/ZDRules_English.pdf"
    for i in introduce:
        print(Fore.CYAN + i, end="")
        time.sleep(speed)
    print()


def name_input():
    """Check name."""
    player_name = ""
    while player_name == "":
        # player_name = "Tallahassee" # testing name
        print(Fore.BLACK + Back.WHITE + " What is your zombie name? ")
        player_name = input()
    return player_name


def settings():
    """Choose number of players."""
    prases_error = [
        "I know, zombies can read! Number from 1 to 9",
        "Uh, nope... Number from 1 to 9, please",
        "You can do it, only one number!",
        "1-2-3-4-5-6-7-8-9 Choose what you like!"
        ]
    number_of_players = 0
    while number_of_players > 9 or number_of_players < 1:
        try:
            print(
                Fore.BLACK + Back.WHITE + " How many zombies are hungry besides you? (1-9) "
                )
            number_of_players = int(input())
            if number_of_players > 9 or number_of_players < 1:
                raise ValueError
        except ValueError:
            print(random.choice(prases_error))
    return number_of_players


def intro2(name):
    """Typing introduction."""
    introduce = str(name) + ", during the game you might have dices like these:"
    for i in introduce:
        print(Fore.CYAN + i, end="")
        time.sleep(speed)
    print()

    print(Fore.GREEN + "shot", end=" ")
    print(Fore.YELLOW + "run", end=" ")
    print(Fore.RED + "brain")

    introduce = "That means, that you have 3 dices of different colors (green, yellow and red in this case)\nwith the corresponding names of the rolled values."
    for i in introduce:
        print(Fore.CYAN + i, end="")
        time.sleep(speed)
    print()

    introduce = "During your turn:\n   press ENTER to roll dices\n   input something to stop"
    for i in introduce:
        print(Fore.CYAN + i, end="")
        time.sleep(speed)
    print("\n")


def beginning(name, number):
    """Choose number of players and make detailed list."""
    caracters = [
        "John", "Sebastian", "William", "Michael", "Ethan",
        "Samuel", "Theodor", "Logan", "Benjamin", "Henry",
        "Olivia", "Elizabeth", "Luna", "Sofia", "Mia",
        "Isabella", "Emma", "Chloe", "Camila", "Ella",
    ]
    players_in_game = []
    players_in_game_det = []

    if name in caracters:
        caracters.remove(name)

    for i in range(number):
        player_i = random.choice(caracters)
        players_in_game.append(player_i)
        caracters.remove(player_i)

    players_in_game.append(name)
    players_in_game = random.sample(players_in_game, number + 1)

    for i in range(number + 1):
        players_in_game_det.append(
            {
                "Name": players_in_game[i],
                "Score": 0
                }
        )
    return players_in_game_det


def one_round(players_list, name, max_score):
    """Play one round."""
    i = 1
    for player in players_list:
        print(Fore.BLACK + Back.WHITE + f"  Player {i}: {player['Name']}, Score: {player['Score']}  ")
        score_before = player["Score"]
        if player["Name"] == name:
            player_i = OneTurnPlayer(score_before)
        else:
            player_i = OneTurnComp(score_before, max_score)
        score_after = player_i.get()
        player["Score"] = score_after

        if max_score < score_after:
            max_score = score_after

        print(f" Player {i}: {player['Name']}, Total score: {player['Score']}\n")
        i += 1
        time.sleep(1)

    return players_list, max_score


def show_table(players_list):
    """Show table with actual score."""
    headers = {"Name": "Name", "Score": "Score"}
    print(tabulate(players_list[0:], headers, tablefmt="simple"))
    print()


def congratulations(player_list):
    """Find and congratulate the winner."""
    max_score = 0
    for player in player_list:
        if player["Score"] > max_score:
            winner_name = player["Name"]
            max_score = player["Score"]
        elif player["Score"] == max_score:
            winner_name = "We have no winner!"
    return winner_name


def highscore_write(name, players_list):
    """Show top ten highscore."""
    for player in players_list:
        if player["Name"] == name:
            score = player["Score"]

    play_date = datetime.now().strftime("%m/%d/%Y-%H.%M")

    with open("highscore.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Score", "Date"])
        writer.writerow({"Name": name, "Score": score, "Date": play_date})


def top_ten_show():
    """Show top ten."""
    print("\n", Fore.CYAN + "Top zombies of all time:")
    headers = {"Name": "Name", "Score": "Score", "Date": "Date"}
    top_list = []
    with open("highscore.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            top_list.append(row)
    top_list = sorted(
        top_list, key=lambda score: int(score["Score"]), reverse=True
        )

    print(tabulate(top_list[0:10], headers, tablefmt="simple"), "\n")


if __name__ == "__main__":
    main()
