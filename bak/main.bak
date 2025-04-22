from sense_hat import SenseHat,ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from action import Action
from features.animations import SenseHATAnimations
from time import sleep

def loading_animation(animations):
    animations.loading()

def reg_acc(sense):
    x, y, z = sense.get_accelerometer_raw().values()

    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 3 or y > 3 or z > 3 :
        animations.loading()
    else:
        pass
        # sense.clear()
        # animations.question_mark()

# sense = SenseHat()
# animations = SenseHATAnimations(sense=sense)
# action = Action(sense, animation=animations)

# sense.set_imu_config(False, False, True)  # gyroscope only
# loading_animation(animations)
# action.refresh()

# Initialization SenseHAT pressure sensor
# sense.stick.direction_up = action.pushed_up
# sense.stick.direction_down = action.pushed_down
# sense.stick.direction_left = action.pushed_left
# sense.stick.direction_right = action.pushed_right
# sense.stick.direction_any = action.refresh

while True:
    pass
    # This keeps the program running to receive joystick events
    # x, y, z = sense.get_accelerometer_raw().values()

    # x = abs(x)
    # y = abs(y)
    # z = abs(z)

    # if x > 3 or y > 3 or z > 3 :
    #     animations.loading()
    # else:
    #     # sense.clear()
    #     animations.question_mark()
    # reg_acc(sense)


    # for event in sense.stick.get_events():
    #     sense.show_message('hh')
    #     print("The joystick was {} {}".format(event.action, event.direction))
    # sleep(0.5)
    # if (pitch)
    # print(pitch,roll,yaw)
	# p = round(float(pitch), 1)
	# r = round(float(roll), 1)
	# y = round(float(yaw), 1)
	# print("p: {p}, r: {r}, y: {y}")
