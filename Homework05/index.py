import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

click1 = 0
click2 = 0

# starting a new game
def new_game():
    global deck_cards, exposed, turns, state
    state = 0
    turns = 0
    deck_cards = [i % 8 for i in range(16)]
    exposed = [False for i in range(16)]

    random.shuffle(deck_cards)
    label.set_text("Turns = " + str(turns))
    pass

# event handlers
def mouseclick(pos):
    global state, exposed, click1, click2, turns, deck_cards
    choice = int(pos[0] / 50)
    if state == 0:
        state = 1
        click1 = choice
        exposed[click1] = True
    elif state == 1:
        if not exposed[choice]:
            state = 2
            click2 = choice
            exposed[click2] = True
            turns += 1
    elif state == 2:
        if not exposed[choice]:
            if deck_cards[click1] == deck_cards[click2]:
                pass
            else:
                exposed[click1] = False
                exposed[click2] = False
            click1 = choice
            exposed[click1] = True
            state = 1
    label.set_text("Turns = " + str(turns))
    pass

# drawing cards
def draw(canvas):
    for i in range(16):
        if exposed[i]:
            canvas.draw_text(str(deck_cards[i]), (50 * i + 10, 60), 40, "Blue")
        else:
            canvas.draw_polygon([(50 * i, 0), (50 * i, 100), (50 * i + 50, 0), (50 * i + 50, 100)], 3, "Yellow", "Green")
    pass


# create frame, add a button and label
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game, 150)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get starting
new_game()
frame.start()