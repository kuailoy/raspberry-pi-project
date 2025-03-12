from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause
import subprocess


#CONFIG
Scroll = float(0.05)                                                            # Text Scroll speed
O = [100, 100, 100]                                                             # WHITE
X = [0, 0, 0]                                                                   # BLACK
R = [100, 0, 0]                                                                 # RED
B = [0, 0, 100]                                                                 # BlUE
G = [0, 100, 0]                                                                 # GREEN
x = 3                                                                           # JOY-STICK X-Axis
y = 3                                                                           # JOY-STICK Y-Axis
sense = SenseHat()                                                              # Initialization SenseHAT
temp = sense.get_temperature() - 13                                             # Initialization SenseHAT temperature sensor 
pressure = int(sense.get_pressure())                                            # Initialization SenseHAT pressure sensor
result = subprocess.run(['python', 'ai.py'], capture_output=True, text=True)    # Initialization subprecess for AI part



def main():
    question_mark = [
    O, O, O, X, X, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    R, O, O, O, O, O, O, G,
    R, O, O, O, O, O, O, G,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, B, B, O, O, O
    ]

    sense.set_pixels(question_mark)
main()


def clamp(value, min_value=0, max_value=7):
    return min(max_value, max(min_value, value))


def pushed_up(event):
    global y
    if event.action != ACTION_RELEASED:
        y = clamp(y - 1)
        sense.show_message(f"{temp:.1f}", text_colour = X, scroll_speed = Scroll)
    main()

def pushed_down(event):
    global y
    if event.action != ACTION_RELEASED:
        y = clamp(y + 1)
        sense.show_message(f"{pressure}", text_colour = B, scroll_speed = Scroll)
    main()

def pushed_left(event):
    global x
    if event.action != ACTION_RELEASED:
        x = clamp(x - 1)


def pushed_right(event):
    global x
    if event.action != ACTION_RELEASED:
        x = clamp(x + 1)
        print("AI OUTPUT", result.stdout)




sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right

while True:
  pass  # This keeps the program running to receive joystick events