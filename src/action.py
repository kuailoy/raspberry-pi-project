from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from datetime import datetime
from features.animations import SenseHATAnimations
from time import sleep
from debounce import debounce
from datetime import datetime
import os
import random
import globals

#CONFIG
Scroll = float(0.1)                                                            # Text Scroll speed
X = [100, 100, 100]                                                             # WHITE
O = [0, 0, 0]                                                                   # BLACK
R = [100, 0, 0]                                                                 # RED
B = [0, 0, 100]                                                                 # BlUE
G = [0, 100, 0]                                                                 # GREEN
x = 3                                                                           # JOY-STICK X-Axis
y = 3                                                                           # JOY-STICK Y-Axis

styles = [
    {
        "text_colour": [0, 255, 180],    # 霓虹青绿色
        "bg_colour": [10, 0, 20]         # 夜色紫黑
    },
    {
        "text_colour": [255, 20, 147],   # 赛博粉红
        "bg_colour": [5, 0, 10]
    },
    {
        "text_colour": [0, 191, 255],    # 电光蓝
        "bg_colour": [0, 0, 0]
    },
    {
        "text_colour": [255, 0, 255],    # 荧光紫
        "bg_colour": [10, 0, 20]
    },
    {
        "text_colour": [173, 255, 47],   # 荧光黄绿
        "bg_colour": [20, 10, 0]
    }
]


def get_path(image_path: str):
    return os.path.join(os.path.dirname(__file__), "images", image_path)

class Action:
    def __init__(self, sense: SenseHat, animation: SenseHATAnimations):
        self.sense = sense
        self.animation = animation

    def get_system_time(self):
        return datetime.now().strftime('%H:%M')

    def pushed_up(self):
        self.sense.clear()
        temperature = self.sense.get_temperature() - 13
        print(f'globals.text_mode: {globals.text_mode}')

        if globals.text_mode:
            self.sense.set_rotation(90)
            self.sense.show_message(f"T:{temperature:.1f}", text_colour=styles[0]["text_colour"], back_colour=styles[0]["bg_colour"], scroll_speed=Scroll)
        else:
            if temperature >= 10:
                image_path1 = get_path("temperature_hot_1.png")
                image_path2 = get_path("temperature_hot_2.png")
            else:
                image_path1 = get_path("temperature_cold_1.png")
                image_path2 = get_path("temperature_cold_2.png")

            self.animation.shifting(image_path1, image_path2)

    def pushed_down(self):
        self.sense.clear()
        pressure = int(self.sense.get_pressure())
        print(f'globals.text_mode: {globals.text_mode}')

        if globals.text_mode:
            self.sense.set_rotation(270)
            self.sense.show_message(f"P:{pressure}", text_colour=styles[1]["text_colour"], back_colour=styles[1]["bg_colour"], scroll_speed=Scroll)

    def pushed_left(self):
        self.sense.clear()
        # Get current time
        current_time = datetime.now()
        hour = current_time.hour
        print(f'globals.text_mode: {globals.text_mode}')

        if globals.text_mode:
            self.sense.set_rotation(180)
            self.sense.show_message(self.get_system_time(),  text_colour=styles[2]["text_colour"], back_colour=styles[2]["bg_colour"], scroll_speed=Scroll)
        else:
            if hour >= 6 and hour <= 17:
                image_path1 = get_path("time_day_1.png")
                image_path2 = get_path("time_day_2.png")
            else:
                image_path1 = get_path("time_night_1.png")
                image_path2 = get_path("time_night_2.png")

            self.animation.shifting(image_path1, image_path2)

    def pushed_right(self):
        self.sense.clear()
        humidity = self.sense.get_humidity()
        print(f'globals.text_mode: {globals.text_mode}')

        if globals.text_mode:
            self.sense.set_rotation(0)
            self.sense.show_message(f"H:{humidity:.1f}%",  text_colour=styles[4]["text_colour"], back_colour=styles[4]["bg_colour"], scroll_speed=Scroll)
        else:
            if humidity >= 30:
                image_path1 = get_path("humidity_high_1.png")
                image_path2 = get_path("humidity_high_2.png")
            else:
                image_path1 = get_path("humidity_low_1.png")
                image_path2 = get_path("humidity_low_2.png")

            self.animation.shifting(image_path1, image_path2)

    # deprecated
    def refresh(self):
        self.sense.clear()
        self.animation.question_mark()
