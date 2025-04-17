from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from datetime import datetime

#CONFIG
Scroll = float(0.05)                                                            # Text Scroll speed
X = [100, 100, 100]                                                             # WHITE
O = [0, 0, 0]                                                                   # BLACK
R = [100, 0, 0]                                                                 # RED
B = [0, 0, 100]                                                                 # BlUE
G = [0, 100, 0]                                                                 # GREEN
x = 3                                                                           # JOY-STICK X-Axis
y = 3                                                                           # JOY-STICK Y-Axis

class Action:
    def __init__(self, sense: SenseHat):
        self.sense = sense

    # def clamp(value, min_value=0, max_value=7):
    #     return min(max_value, max(min_value, value))

    def get_system_time(self):
        return datetime.now().strftime('%H:%M')

    def pushed_up(self, event):
        # global y
        if event.action != ACTION_RELEASED:
            # y = self.clamp(y - 1)
            temperature = self.sense.get_temperature() - 13
            # temperature = self.sense.get_temperature_from_humidity()
            # temperature = self.sense.get_temperature_from_pressure()

            self.sense.show_message(f"{temperature:.1f}", text_colour=X, scroll_speed=Scroll)


    def pushed_down(self, event):
        # global y
        if event.action != ACTION_RELEASED:
            # y = self.clamp(y + 1)
            pressure = int(self.sense.get_pressure())
            self.sense.show_message(f"{pressure}", text_colour=B, scroll_speed=Scroll)


    def pushed_left(self, event):
        # global x
        if event.action != ACTION_RELEASED:
            # x = self.clamp(x - 1)
            self.sense.show_message(self.get_system_time(), text_colour=R, scroll_speed=Scroll)

    def pushed_right(self, event):
        # global x
        if event.action != ACTION_RELEASED:
            humidity = self.sense.get_humidity()
            self.sense.show_message(f"{humidity:.1f}", text_colour=B, scroll_speed=Scroll)
            # x = self.clamp(x + 1)
            pass
