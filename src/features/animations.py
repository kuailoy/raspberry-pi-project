from time import sleep, time
from sense_hat import SenseHat
import globals

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

    def heart(self, color=pink):
        P = color
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

    #temperature
    def menu_temperature(self):
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

    #pressure
    def menu_pressure(self):
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

    #humidity
    def menu_humidity(self):
        logo = [
        O, O, O, O, G, O, O, O,
        O, O, O, O, G, O, O, O,
        O, O, O, G, O, G, O, O,
        G, O, O, G, O, G, O, O,
        G, O, G, O, O, O, G, O,
        O, O, G, O, O, O, G, O,
        O, O, G, O, O, O, G, O,
        O, O, O, G, G, G, O, O
        ]
        return logo

    #time
    def menu_time(self):
        logo = [
        O, O, O, O, O, O, O, O,
        O, O, Y, Y, Y, O, O, O,
        O, Y, O, Y, O, Y, O, O,
        Y, O, O, Y, O, O, Y, Y,
        Y, O, O, Y, Y, O, Y, Y,
        Y, O, O, O, O, O, Y, O,
        O, Y, O, O, O, Y, O, O,
        O, O ,Y, Y, Y, O, O, O
        ]
        return logo

    def question_mark(self):
        O = [0, 0, 0]                                                                   # BLACK
        X = [100, 100, 100]                                                             # WHITE
        O = [0, 0, 0]                                                                   # BLACK
        R = [100, 0, 0]                                                                 # RED
        B = [0, 0, 100]                                                                 # BlUE
        G = [0, 100, 0]                                                                 # GREEN
        logo = [
            O, O, O, X, X, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            R, O, O, O, O, O, O, G,
            R, O, O, O, O, O, O, G,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, B, B, O, O, O
        ]
        self.sense.set_pixels(logo)

        # return logo

    def rainbow(self):
        pixels = [
            [255, 0, 0], [255, 0, 0], [255, 87, 0], [255, 196, 0], [205, 255, 0], [95, 255, 0], [0, 255, 13], [0, 255, 122],
            [255, 0, 0], [255, 96, 0], [255, 205, 0], [196, 255, 0], [87, 255, 0], [0, 255, 22], [0, 255, 131], [0, 255, 240],
            [255, 105, 0], [255, 214, 0], [187, 255, 0], [78, 255, 0], [0, 255, 30], [0, 255, 140], [0, 255, 248], [0, 152, 255],
            [255, 223, 0], [178, 255, 0], [70, 255, 0], [0, 255, 40], [0, 255, 148], [0, 253, 255], [0, 144, 255], [0, 34, 255],
            [170, 255, 0], [61, 255, 0], [0, 255, 48], [0, 255, 157], [0, 243, 255], [0, 134, 255], [0, 26, 255], [83, 0, 255],
            [52, 255, 0], [0, 255, 57], [0, 255, 166], [0, 235, 255], [0, 126, 255], [0, 17, 255], [92, 0, 255], [201, 0, 255],
            [0, 255, 66], [0, 255, 174], [0, 226, 255], [0, 117, 255], [0, 8, 255], [100, 0, 255], [210, 0, 255], [255, 0, 192],
            [0, 255, 183], [0, 217, 255], [0, 109, 255], [0, 0, 255], [110, 0, 255], [218, 0, 255], [255, 0, 183], [255, 0, 74]
        ]

        msleep = lambda x: sleep(x / 1000.0)


        def next_colour(pix):
            r = pix[0]
            g = pix[1]
            b = pix[2]

            if (r == 255 and g < 255 and b == 0):
                g += 1

            if (g == 255 and r > 0 and b == 0):
                r -= 1

            if (g == 255 and b < 255 and r == 0):
                b += 1

            if (b == 255 and g > 0 and r == 0):
                g -= 1

            if (b == 255 and r < 255 and g == 0):
                r += 1

            if (r == 255 and b > 0 and g == 0):
                b -= 1

            pix[0] = r
            pix[1] = g
            pix[2] = b

        quit = False
        while True:
            for pix in pixels:
                next_colour(pix)

            self.sense.set_pixels(pixels)
            if quit:
                # Check for joystick press
                break
            # Check for joystick press
            for event in self.sense.stick.get_events():
                if event.action == 'pressed':
                    quit=True
                    self.sense.clear()

                    # raise KeyboardInterrupt
            msleep(5)



    def sunshine(self):
        # Colors
        R = (255, 80, 0)        # Red-orange (sun)
        O = (255, 140, 0)       # Orange (glow)
        D = (200, 100, 0)       # Dark orange (outer glow)
        B = (135, 206, 235)     # Sky blue

        # Frame 1: calm center sun
        frame1 = [
            B, B, B, B, B, B, B, B,
            B, B, B, O, O, B, B, B,
            B, B, O, R, R, O, B, B,
            B, O, R, R, R, R, O, B,
            B, O, R, R, R, R, O, B,
            B, B, O, R, R, O, B, B,
            B, B, B, O, O, B, B, B,
            B, B, B, B, B, B, B, B
        ]

        # Frame 2: outer glow spreads gently
        frame2 = [
            B, B, B, D, D, B, B, B,
            B, B, O, O, O, O, B, B,
            B, O, O, R, R, O, O, B,
            D, O, R, R, R, R, O, D,
            D, O, R, R, R, R, O, D,
            B, O, O, R, R, O, O, B,
            B, B, O, O, O, O, B, B,
            B, B, B, D, D, B, B, B
        ]

        # Frame 3: strongest pulse
        frame3 = [
            B, B, D, B, B, D, B, B,
            D, O, O, O, O, O, O, D,
            B, O, O, R, R, O, O, B,
            O, O, R, R, R, R, O, O,
            O, O, R, R, R, R, O, O,
            B, O, O, R, R, O, O, B,
            D, O, O, O, O, O, O, D,
            B, B, D, B, B, D, B, B
        ]

        # Frame 4: glow retracts slightly
        frame4 = [
            B, B, B, D, D, B, B, B,
            B, B, O, O, O, O, B, B,
            B, O, O, R, R, O, O, B,
            D, O, R, R, R, R, O, D,
            D, O, R, R, R, R, O, D,
            B, O, O, R, R, O, O, B,
            B, B, O, O, O, O, B, B,
            B, B, B, D, D, B, B, B
        ]

        frames = [frame1, frame2, frame3, frame4]


        for i in range(3):
            for frame in frames:
                self.sense.set_pixels(frame)
                sleep(0.3)

    def sunshine1(self):
        # 10种渐变色（两字母命名）
        BL = (  0,   0,   0)  # 背景黑
        DR = ( 40,   0,   0)  # 暗红
        CR = (120,   0,   0)  # 焦红
        RO = (200,  40,   0)  # 红橙
        OR = (255,  80,   0)  # 橙
        LO = (255, 120,   0)  # 亮橙
        YO = (255, 160,  20)  # 黄橙
        YE = (255, 200,  50)  # 黄
        LY = (255, 220,  80)  # 亮黄
        BY = (255, 255, 100)  # 炽黄

        # 太阳动画10帧（首尾连贯循环）
        frames = [
            # 帧0: 最小核心
            [BL,BL,BL,BL,BL,BL,BL,BL, BL,BL,BL,BL,BL,BL,BL,BL, BL,BL,BL,CR,CR,BL,BL,BL, BL,BL,CR,YO,YO,CR,BL,BL,
            BL,BL,CR,YO,YO,CR,BL,BL, BL,BL,BL,CR,CR,BL,BL,BL, BL,BL,BL,BL,BL,BL,BL,BL, BL,BL,BL,BL,BL,BL,BL,BL],

            # 帧1: 微扩
            [BL,BL,BL,CR,CR,BL,BL,BL, BL,CR,CR,RO,RO,CR,CR,BL, CR,RO,RO,YO,YO,RO,RO,CR, CR,RO,YO,LY,LY,YO,RO,CR,
            CR,RO,YO,LY,LY,YO,RO,CR, CR,RO,RO,YO,YO,RO,RO,CR, BL,CR,CR,RO,RO,CR,CR,BL, BL,BL,BL,CR,CR,BL,BL,BL],

            # 帧2: 橙光扩散
            [CR,CR,RO,OR,OR,RO,CR,CR, CR,OR,OR,LO,LO,OR,OR,CR, RO,LO,LO,YE,YE,LO,LO,RO, RO,LO,YE,BY,BY,YE,LO,RO,
            RO,LO,YE,BY,BY,YE,LO,RO, RO,LO,LO,YE,YE,LO,LO,RO, CR,OR,OR,LO,LO,OR,OR,CR, CR,CR,RO,OR,OR,RO,CR,CR],

            # 帧3: 黄光加强
            [OR,OR,LO,YO,YO,LO,OR,OR, LO,YO,YO,LY,LY,YO,YO,LO, YO,LY,LY,BY,BY,LY,LY,YO, YO,LY,BY,BY,BY,BY,LY,YO,
            YO,LY,BY,BY,BY,BY,LY,YO, YO,LY,LY,BY,BY,LY,LY,YO, LO,YO,YO,LY,LY,YO,YO,LO, OR,OR,LO,YO,YO,LO,OR,OR],

            # 帧4: 最大光晕
            [LO,LO,YO,LY,LY,YO,LO,LO, YO,LY,LY,BY,BY,LY,LY,YO, LY,BY,BY,BY,BY,BY,BY,LY, LY,BY,BY,BY,BY,BY,BY,LY,
            LY,BY,BY,BY,BY,BY,BY,LY, LY,BY,BY,BY,BY,BY,BY,LY, YO,LY,LY,BY,BY,LY,LY,YO, LO,LO,YO,LY,LY,YO,LO,LO],

            # 帧5-9: 逆向收缩（与帧4-0对称）
            # 帧5（同帧3逆向）
            [OR,OR,LO,YO,YO,LO,OR,OR, LO,YO,YO,LY,LY,YO,YO,LO, YO,LY,LY,BY,BY,LY,LY,YO, YO,LY,BY,BY,BY,BY,LY,YO,
            YO,LY,BY,BY,BY,BY,LY,YO, YO,LY,LY,BY,BY,LY,LY,YO, LO,YO,YO,LY,LY,YO,YO,LO, OR,OR,LO,YO,YO,LO,OR,OR],

            # 帧6（同帧2逆向）
            [CR,CR,RO,OR,OR,RO,CR,CR, CR,OR,OR,LO,LO,OR,OR,CR, RO,LO,LO,YE,YE,LO,LO,RO, RO,LO,YE,BY,BY,YE,LO,RO,
            RO,LO,YE,BY,BY,YE,LO,RO, RO,LO,LO,YE,YE,LO,LO,RO, CR,OR,OR,LO,LO,OR,OR,CR, CR,CR,RO,OR,OR,RO,CR,CR],

            # 帧7（同帧1逆向）
            [BL,BL,BL,CR,CR,BL,BL,BL, BL,CR,CR,RO,RO,CR,CR,BL, CR,RO,RO,YO,YO,RO,RO,CR, CR,RO,YO,LY,LY,YO,RO,CR,
            CR,RO,YO,LY,LY,YO,RO,CR, CR,RO,RO,YO,YO,RO,RO,CR, BL,CR,CR,RO,RO,CR,CR,BL, BL,BL,BL,CR,CR,BL,BL,BL],

            # 帧8（过渡到初始）
            [BL,BL,BL,BL,BL,BL,BL,BL, BL,BL,BL,DR,DR,BL,BL,BL, BL,DR,DR,YO,YO,DR,DR,BL, BL,DR,YO,LY,LY,YO,DR,BL,
            BL,DR,YO,LY,LY,YO,DR,BL, BL,DR,DR,YO,YO,DR,DR,BL, BL,BL,BL,DR,DR,BL,BL,BL, BL,BL,BL,BL,BL,BL,BL,BL],
        ]

        for i in range(3):
            for frame in frames:
                self.sense.set_pixels(frame)
                sleep(0.3)


    def switching_mode(self):
        for i in range(3):
            self.sense.set_pixels(self.raspi_logo())
            sleep(0.3)
            self.sense.clear()
            sleep(0.3)
            # self.sense.set_pixels(self.heart())
            # sleep(0.3)
            # self.sense.clear()
            # sleep(0.3)

    def shifting(self, image_1, image_2):
        for i in range(5):
            self.sense.load_image(image_1)
            sleep(0.25)
            self.sense.load_image(image_2)
            sleep(0.25)
        # self.sense.load_image(image_1)
        # sleep(0.25)
        # self.sense.load_image(image_2)
        # sleep(0.25)
