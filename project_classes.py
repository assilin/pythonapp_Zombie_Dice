import random
import time
from colorama import init, Fore
init(autoreset=True)


class OneTurn:
    """One turn class."""

    # phrases
    phrase_to_play = [
        "What're you going to do?",
        "Are we still playing?",
        "You're not scared, are you?",
        "Try your best",
        "Fortune favours the bold",
        "You've got nothing to lose",
    ]
    phrase_finish = ["Well done!!!", "Bravo!!!", "My congrtulations!"]
    phrase_to_play_comp = ["I'm still hungry!", "Moooooore..", "Wanna more!"]
    phrase_finish_comp = ["Enough..", "I'm full!", "Ok.. next time.."]

    # player action
    next_turn = True

    def __init__(self, score=0, max_score=0):
        """Call functions in order."""
        self.speed = 0.1  # default speed = 0.1

        self.score = score
        self.max_score = max_score

        # all types of dices in the jar
        self.dices_in_jar = [
            "red", "red", "red",
            "yellow", "yellow", "yellow", "yellow",
            "green", "green", "green", "green", "green", "green"
        ]

        self.number_shots = 0  # score in one turn
        self.number_brains = 0  # score in one turn
        self.dices_in_hand = []  # types of dices in hand
        self.dices_to_take = 3  # max number of dices in hand
        self.number_in_jar = 13  # number of dices at the begining

    def thinking(self):
        """Wait a little bit."""
        print(" ", end="")
        for i in range(3):
            print(".", end="")
            time.sleep(self.speed * 3)
        print(" ", end="")


    def in_hand(self):
        """Choose dices in hand randomly or add missing ones."""
        # the required number of dices in hand, can be 0-1-2-3 after each roll
        if self.dices_to_take > self.number_in_jar:
            self.dices_to_take = self.number_in_jar
        i = {
            self.dices_to_take == 1: 1,
            self.dices_to_take == 2: 2,
            self.dices_to_take >= 3: 3,
        }[True]
        self.number_in_jar -= i

        # random choice of missing ones
        for _ in range(i):
            # 'if' to avoid IndexError
            if len(self.dices_in_jar) == 1:
                dice_x = self.dices_in_jar[0]
            else:
                dice_x = random.choice(self.dices_in_jar)
            self.dices_in_hand.append(dice_x)
            self.dices_in_jar.remove(dice_x)

    def roll_dices(self):
        """
        Make a roll with dices in hand.

        Print and analyze 'faces' fallen on dice.
        """
        # rolling dices
        dice_type_red = ["shot", "shot", "shot", "run", "run", "brain"]
        dice_type_yellow = ["shot", "shot", "run", "run", "brain", "brain"]
        dice_type_green = ["shot", "run", "run", "brain", "brain", "brain"]

        last_roll = []
        for i in range(len(self.dices_in_hand)):
            dice = locals()["dice_type_" + self.dices_in_hand[i]]
            face = random.choice(dice)
            roll_dice = {
                "dice_number": i + 1,
                "dice_type": self.dices_in_hand[i],
                "face": face,
            }
            last_roll.append(roll_dice)

        # wait a little
        self.thinking()

        for _dice in last_roll:
            match _dice["dice_type"]:
                case "green":
                    print(Fore.GREEN + _dice["face"], end=" ")
                case "yellow":
                    print(Fore.YELLOW + _dice["face"], end=" ")
                case _:
                    print(Fore.RED + _dice["face"], end=" ")

        self.dices_in_hand = []
        for _dice in last_roll:
            match _dice["face"]:
                case "run":
                    self.dices_in_hand.append(_dice["dice_type"])
                case "shot":
                    self.number_shots += 1
                case _:
                    self.number_brains += 1
        self.dices_to_take = 3 - len(self.dices_in_hand)
        print(f"brains: {self.number_brains}, shots: {self.number_shots}", end="")

        # wait a little
        self.thinking()

    def next_roll_player(self):
        """Request action from the user."""
        global next_turn
        next_turn = ""

        if self.number_shots >= 3:
            print(Fore.CYAN + "You got shot, next player")
            time.sleep(self.speed * 10)
        else:
            if self.number_in_jar == 0 and len(self.dices_in_hand) == 0:
                print(Fore.CYAN + random.choice(self.phrase_finish))
                time.sleep(self.speed * 5)
            else:
                print(Fore.CYAN + random.choice(self.phrase_to_play), end=" ")
                turn = input(
                    "(press ENTER to roll, or input smth to stop) "
                    )
                if turn != "":
                    self.score += self.number_brains
                    self.number_in_jar = 0
                    self.dices_in_hand = []
                    time.sleep(self.speed * 5)

    def next_roll_comp(self):
        """Model actions of the bot."""
        if self.number_shots >= 3:
            print(Fore.CYAN + "Player got shot, next player")
        else:
            actual_score = self.number_brains + self.score

            # computer action algorithm
            _stop = False
            if self.number_shots == 1:
                if (self.dices_in_hand.count("red") == 3
                        and self.number_brains > 0):
                    _stop = True
                if ((sorted(self.dices_in_hand) == ["red", "red", "yellow"]
                        or self.dices_in_jar.count("yellow") > self.dices_in_jar.count("green"))
                        and self.number_brains > 1):
                    _stop = True
                if ((sorted(self.dices_in_hand) == ["green", "red", "red"]
                        or self.dices_in_jar.count("green") > self.dices_in_jar.count("yellow"))
                        and self.number_brains > 2):
                    _stop = True
            if self.number_shots == 2:
                if (self.dices_in_hand.count("green") == 3
                        and self.number_brains > 1):
                    _stop = True
                if (self.dices_in_hand.count("green") != 3
                        and self.number_brains > 0):
                    _stop = True

            if self.number_in_jar == 0 and len(self.dices_in_hand) == 0:
                print(Fore.CYAN + random.choice(self.phrase_finish))
            else:
                # if someone got 13,
                # playing without results of computer action algorithm
                if self.max_score >= 13 and actual_score <= self.max_score:
                    _stop = False
                match _stop:
                    case True:
                        print(
                            Fore.CYAN + random.choice(self.phrase_finish_comp)
                            )
                        self.score += self.number_brains
                        self.number_in_jar = 0
                        self.dices_in_hand = []
                    case _:
                        print(
                            Fore.CYAN + random.choice(self.phrase_to_play_comp)
                            )

    def get(self):
        """Return score."""
        return self.score


class OneTurnPlayer(OneTurn):
    """One turn player."""

    def __init__(self, score=0):
        """Make roll for player."""
        super().__init__()
        self.score = score
        while (
            self.number_in_jar > 0 or len(self.dices_in_hand) > 0
        ) and self.number_shots < 3:
            if self.dices_to_take != 0 and self.number_in_jar != 0:
                self.in_hand()
            self.roll_dices()
            self.next_roll_player()


class OneTurnComp(OneTurn):
    """One turn comp."""

    def __init__(self, score=0, max_score=0):
        """Make roll for comp."""
        super().__init__()
        self.score = score
        self.max_score = max_score
        while (
            self.number_in_jar > 0 or len(self.dices_in_hand) > 0
        ) and self.number_shots < 3:
            if self.dices_to_take != 0 and self.number_in_jar != 0:
                self.in_hand()
            self.roll_dices()
            self.next_roll_comp()
