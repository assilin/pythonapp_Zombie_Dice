from project import congratulations, beginning, one_round

def main():
    test_beginning()
    test_one_round()
    test_congratulations()


def test_beginning():
    # Check type of valuable and lenght of the list
    name = "John"
    number = 9
    assert type(beginning(name, number)) == list
    assert len(beginning(name, number)) == number + 1

    # Check repeating of names
    name = "John"
    number = 9
    players_list = beginning(name, number)
    coincidence = False
    for i in range(number):
        for j in range(i + 1, number):
            if players_list[i] == players_list[j]:
                coincidence = True
                quit()
    assert coincidence is False


def test_one_round():
    """This test is for a function that uses 'time.sleep', it lasts for about 20-25 seconds."""
    name = "Some_name"
    max_score_before = 7
    player_list_before = [
        {"Name": "Chloe", "Score": 5},
        {"Name": "Samuel", "Score": 6},
        {"Name": "Michael", "Score": 7},
        {"Name": "Benjamin", "Score": 5}
        ]

    player_list_after = []
    for player in player_list_before:
        player_list_after.append(player.copy())

    player_list_after, max_score_after = one_round(player_list_after, name, max_score_before)

    assert max_score_after >= max_score_before

    for i in range(len(player_list_after)):
        assert player_list_after[i]["Name"] == player_list_before[i]["Name"]
        assert player_list_after[i]["Score"] >= player_list_before[i]["Score"]


def test_congratulations():
    player_list = [
        {"Name": "Chloe", "Score": 15},
        {"Name": "Samuel", "Score": 6},
        {"Name": "Michael", "Score": 7},
        {"Name": "Benjamin", "Score": 5}
        ]
    assert congratulations(player_list) == "Chloe"

    player_list = [
        {"Name": "Chloe", "Score": 15},
        {"Name": "Samuel", "Score": 6},
        {"Name": "Michael", "Score": 15},
        {"Name": "Benjamin", "Score": 5}
        ]
    assert congratulations(player_list) == "We have no winner!"

    player_list = [
        {"Name": "Chloe", "Score": 13},
        {"Name": "Samuel", "Score": 6},
        {"Name": "Michael", "Score": 17},
        {"Name": "Benjamin", "Score": 5}
        ]
    assert congratulations(player_list) == "Michael"


if __name__ == "__main__":
    main()
