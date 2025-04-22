from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from datetime import datetime
from features.animations import SenseHATAnimations
from time import sleep

#CONFIG
Scroll = float(0.05)                                                            # Text Scroll speed
X = [100, 100, 100]                                                             # WHITE
O = [0, 0, 0]                                                                   # BLACK
R = [100, 0, 0]                                                                 # RED
B = [0, 0, 100]                                                                 # BlUE
G = [0, 100, 0]                                                                 # GREEN
x = 3                                                                           # JOY-STICK X-Axis
y = 3                                                                           # JOY-STICK Y-Axis

styles = [
    {
        "text_colour":  [80, 130, 210],
        "bg_colour": [20, 35, 50]
    },
    {
        "text_colour":  [100, 180, 120],
        "bg_colour": [25, 45, 30]
    },
    {
        "text_colour":  [220, 150, 80],
        "bg_colour": [50, 30, 15]
    },
    {
        "text_colour":  [170, 110, 200],
        "bg_colour": [40, 20, 50]
    }
]

class Action:
    def __init__(self, sense: SenseHat, animation: SenseHATAnimations):
        self.sense = sense
        self.animation = animation

    def get_system_time(self):
        return datetime.now().strftime('%H:%M')

    def pushed_up(self):
        self.sense.clear()
        temperature = self.sense.get_temperature() - 13
        if temperature >= 10:
            self.animation.shifting("images/temperature_high_1.png","images/temperature_high_2.png")
        else:
            self.animation.shifting("images/temperature_low_1.png","images/temperature_low_2.png")
        self.sense.show_message(f"{temperature:.1f}", text_colour=styles[0]["text_colour"], back_colour=styles[0]["bg_colour"], scroll_speed=Scroll)

    def pushed_down(self):
        self.sense.clear()
        pressure = int(self.sense.get_pressure())
        self.sense.show_message(f"{pressure}", text_colour=styles[1]["text_colour"], back_colour=styles[1]["bg_colour"], scroll_speed=Scroll)

    def pushed_left(self):
        self.sense.clear()
        hour = int(self.get_system_time) // 100
        if hour >= 6 and hour <= 17:
            self.animation.shifting("images/time_day_1.png","images/time_day_2.png")
        else:
            self.animation.shifting("images/time_night_1.png","images/time_night_2.png")
        self.sense.show_message(self.get_system_time(),  text_colour=styles[2]["text_colour"], back_colour=styles[2]["bg_colour"], scroll_speed=Scroll)

    def pushed_right(self):
        self.sense.clear()
        humidity = self.sense.get_humidity()
        if humidity >= 50:
            self.animation.shifting("images/humidity_wet_1.png","images/humidity_wet_2.png")
        else:
            self.animation.shifting("images/humidity_dry_1.png","images/thumidity_dry_2.png")
        self.sense.show_message(f"{humidity:.1f}%",  text_colour=styles[3]["text_colour"], back_colour=styles[3]["bg_colour"], scroll_speed=Scroll)

    def refresh(self):
        self.sense.clear()
        self.animation.question_mark()
