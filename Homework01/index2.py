import random

def number_to_name(num):
    if num == 0:
        result = "rock"
    elif num == 1:
        result = "Spock"
    elif num == 2:
        result = "paper"
    elif num == 3:
        result = "lizard"
    elif num == 4:
        result = "scissors"
    return result


def name_to_number(name):
    if name == "rock":
        result = 0
    elif name == "Spock":
        result = 1
    elif name == "paper":
        result = 2
    elif name == "lizard":
        result = 3
    elif name == "scissors":
        result = 4
    return result


def rpsls(name):
    player_number = name_to_number(name)
    comp_number = random.randrange(0, 5)

    print ("Player chooses", name)
    print ("Computer chooses", number_to_name(comp_number))

    if (comp_number + 1) % 5 == player_number:
        print ("Player wins!")
    elif (comp_number + 2) % 5 == player_number:
        print ("Player wins!")
    elif comp_number == player_number:
        print ("Player and computer tie!")
    else:
        print ("Computer wins!")
    print ("")


rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
