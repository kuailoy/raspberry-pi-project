from sense_hat import SenseHat
from action import Action
from features.animations import SenseHATAnimations
from time import sleep, time
import globals
from acceleration import acceleration_register
from joystick import Joystick
from orientation import orientation_register

sense = SenseHat()
sense.set_imu_config(True, True, True)  # enable all IMU sensors
animations = SenseHATAnimations(sense=sense)
action = Action(sense, animation=animations)
joystick = Joystick(sense, animation=animations)

def shake():
    globals.text_mode = not globals.text_mode
    print(f'text_mode: {globals.text_mode}')
    animations.switching_mode()
    joystick.reset()

try:
    # regist joystick evnet
    joystick.register()

    # regist orientation if joystick dosen't work
    # orientation_register(sense, action)
    while True:
        # regist shaking event
        acceleration_register(sense, shake)


except KeyboardInterrupt:
    # sense.clear()
    # print('global except')
    joystick.reset()
    print("Program stopped by user.")