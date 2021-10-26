basic.show_icon(IconNames.COW)
basic.pause(1000)
basic.clear_screen()
def on_button_pressed_a():
    basic.show_icon(IconNames.HAPPY)
input.on_button_pressed(Button.A, on_button_pressed_a)
def on_button_pressed_b():
    basic.show_icon(IconNames.SAD)
input.on_button_pressed(Button.B, on_button_pressed_b)

#def scutura():
    #    zar = randint(1, 6)
    #    basic.show_number(zar)
    #input.on_gesture(Gesture.SHAKE, scutura)

# Automatul de decizie
def on_gesture_shake():
    alegere = randint(0, 3)
    if alegere == 0:
        basic.show_string("Da")
    elif alegere == 1:
        basic.show_string("Nu")
    elif alegere == 2:
        basic.show_string("Poate")
    else:
        basic.show_string("Nu stiu")

input.on_gesture(Gesture.SHAKE, on_gesture_shake)

# Prinde punctul
x=0
y=0
def on_button_pressed_ab():
    punct_x = randint(0,4)
    punct_y = randint(0,4)
    led.plot(punct_x, punct_y)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def inclina_dreapta():
    global x
    global y
    led.unplot(x, y)
    x = x+1
    led.plot(x, y)
input.on_gesture(Gesture.TILT_RIGHT, inclina_dreapta)
def inclina_stanga():
    global x
    global y
    led.unplot(x, y)
    x = x-1
    led.plot(x, y)
input.on_gesture(Gesture.TILT_LEFT, inclina_stanga)
def inclina_sus():
    global x
    global y
    led.unplot(x, y)
    y = y-1
    led.plot(x, y)
input.on_gesture(Gesture.LOGO_DOWN, inclina_sus)
def inclina_jos():
    global x
    global y
    led.unplot(x, y)
    y = y+1
    led.plot(x, y)
input.on_gesture(Gesture.LOGO_UP, inclina_jos)