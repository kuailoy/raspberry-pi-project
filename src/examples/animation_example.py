from sense_hat import SenseHat
from time import sleep
from features import SenseHATAnimations


s = SenseHat()
s.low_light = True
animations = SenseHATAnimations(sense=s)
animations.scroll_text("Hello!", [255, 0, 0])
animations.blink_all([255, 255, 0], times=1)
animations.blink_all([0, 255, 0], times=1)
animations.blink_all([0, 0, 255], times=1)
animations.move_dot(0, 0, 7, 7, [0, 0, 255])

animation_list = [animations.trinket_logo, animations.plus, animations.raspi_logo, animations.equals, animations.heart]
count = 0

while True:
    s.set_pixels(animation_list[count % len(animation_list)]())
    sleep(1.5)
    count += 1