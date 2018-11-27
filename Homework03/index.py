import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

gap = 100
mlsec = 0
all_stops = 0
win_stops = 0
stop = True

def view_timer(a):
    ten_mlseconds = int(a) % 10
    seconds = int(a / 10) % 10
    ten_seconds = int(a / 100) % 6
    minutes = int(a / 600) % 600
    string = str(minutes) + ":" + str(ten_seconds) + str(seconds) + "." + str(ten_mlseconds)
    return string

def start():
    global mlsec, stop
    stop = False
    timer.start()

def stop():
    global all_stops, win_stops, stop
    if stop == False:
        if mlsec % 10 == 0:
            win_stops += 1
            all_stops += 1
        elif mlsec != 0:
            all_stops += 1
    stop = True
    timer.stop()

def reset():
    global mlsec, win_stops, all_stops, stop
    mlsec = 0
    stop = True
    all_stops = 0
    win_stops = 0
    timer.stop()

def teak():
    global mlsec
    mlsec += 1

def draw(canvas):
    text = view_timer(mlsec)
    canvas.draw_text(text, (100, 150), 50, "white")
    canvas.draw_text(str(win_stops) + "/" + str(all_stops), (250, 35), 30, "yellow")

f = simplegui.create_frame("Stop: game", 300, 300)
f.set_canvas_background("blue")

f.add_button("start", start, 100)
f.add_button("stop", stop, 100)
f.add_button("reset", reset, 100)

f.set_draw_handler(draw)

timer = simplegui.create_timer(gap, teak)

f.start()

reset()