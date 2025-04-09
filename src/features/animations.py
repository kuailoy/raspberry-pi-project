from time import sleep
from sense_hat import SenseHat

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)
G = green
Y = yellow
B = blue
R = red
W = white
O = nothing
P = pink

class SenseHATAnimations:
    def __init__(self, sense):
        # pass the sense hat instance here
        self.sense = sense

    def clear(self):
        self.sense.clear()

    def scroll_text(self, text, color, speed=0.05):
        self.sense.show_message(text, text_colour=color, scroll_speed=speed)

    def blink_all(self, color, times=5, delay=0.5):
        for _ in range(times):
            self.sense.clear(color)
            sleep(delay)
            self.sense.clear()
            sleep(delay)

    def move_dot(self, start_x, start_y, end_x, end_y, color, delay=0.1):
        x, y = start_x, start_y
        while x != end_x or y != end_y:
            self.sense.clear()
            self.sense.set_pixel(x, y, *color)
            if x < end_x:
                x += 1
            elif x > end_x:
                x -= 1
            if y < end_y:
                y += 1
            elif y > end_y:
                y -= 1
            sleep(delay)
        self.sense.clear()

    def trinket_logo(self):
        G = green
        Y = yellow
        B = blue
        O = nothing
        logo = [
        O, O, O, O, O, O, O, O,
        O, Y, Y, Y, B, G, O, O,
        Y, Y, Y, Y, Y, B, G, O,
        Y, Y, Y, Y, Y, B, G, O,
        Y, Y, Y, Y, Y, B, G, O,
        Y, Y, Y, Y, Y, B, G, O,
        O, Y, Y, Y, B, G, O, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def raspi_logo(self):
        G = green
        R = red
        O = nothing
        logo = [
        O, G, G, O, O, G, G, O,
        O, O, G, G, G, G, O, O,
        O, O, R, R, R, R, O, O,
        O, R, R, R, R, R, R, O,
        R, R, R, R, R, R, R, R,
        R, R, R, R, R, R, R, R,
        O, R, R, R, R, R, R, O,
        O, O, R, R, R, R, O, O,
        ]
        return logo

    def plus(self):
        W = white
        O = nothing
        logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, W, W, O, O, O,
        O, O, O, W, W, O, O, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, O, O, W, W, O, O, O,
        O, O, O, W, W, O, O, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def equals(self):
        W = white
        O = nothing
        logo = [
        O, O, O, O, O, O, O, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo

    def heart(self):
        P = pink
        O = nothing
        logo = [
        O, O, O, O, O, O, O, O,
        O, P, P, O, P, P, O, O,
        P, P, P, P, P, P, P, O,
        P, P, P, P, P, P, P, O,
        O, P, P, P, P, P, O, O,
        O, O, P, P, P, O, O, O,
        O, O, O, P, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]
        return logo
    
    def menu_temperature():
        logo = [
        O, O, O, R, R, O, O, O,
        O, O, O, O, O, O, R, O,
        O, R, R, R, O, R, O, R,
        R, O, O, O, R, O, R, O,
        R, O, O, O, O, O, O, O,
        R, O, O, O, O, O, O, O,
        R, O, O, O, R, O, O, O,
        O, R, R, R, O, O, O, O
        ]
        return logo
    
    def menu_pressure():
        logo = [
        O, B, B, B, B, B, O, O,
        O, B, O, O, O, O, B, O,
        O, B, O, O, O, O, B, O,
        O, B, O, O, O, O, B, O,
        O, B, B, B, B, B, O, O, 
        O, B, O, O, O, O, O, O,
        O, B, O, O, O, O, O, O,
        O, B, O, B, B, O, O, O
        ]
        return logo
    
    def menu_