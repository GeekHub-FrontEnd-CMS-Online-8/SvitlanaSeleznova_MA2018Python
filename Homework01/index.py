from random import randrange
game = {'rock': 0, 'spock': 1, 'paper': 2, 'lizard': 3, 'scissors': 4}


def name_to_number(name):
    if name in game.keys():
        return game[name]
    else:
        print("There is no such name\n")


def number_to_name(number):
    if number in game.values():
        return list(game.keys())[number]
    else:
        print("There is no such number\n")


def rpsls(player_choice):
    player_number = name_to_number(player_choice)
    comp_number = randrange(0, 5)
    result = (player_number - comp_number) % 5
    print('Player chooses ' + player_choice)
    print('Computer chooses ' + number_to_name(comp_number))

    win = result == 1 or result == 2
    lose = result == 3 or result == 4

    if win:
        print('Player wins!\n')
    elif lose:
        print('Computer wins!\n')
    else:
        print('Player and computer tie!\n')


rpsls("rock")
rpsls("spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")