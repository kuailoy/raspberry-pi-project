from sense_hat import SenseHat
from action import Action
from features.animations import SenseHATAnimations
from time import sleep, time

sense = SenseHat()
sense.set_imu_config(True, True, True)  # 启用所有IMU传感器
animations = SenseHATAnimations(sense=sense)
action = Action(sense, animation=animations)


# 方向阈值配置（单位：度）
TILT_THRESHOLD = 20    # 最小倾斜角度
DOMINANCE_RATIO = 1.5  # 主方向判定比例（主要倾斜/次要倾斜）

def get_cardinal_direction():
    # 获取主要基本方向（上/下/左/右）
    orientation = sense.get_orientation_degrees()
    pitch = orientation["pitch"]
    roll = orientation["roll"]

    # 规范化角度到-180~180范围
    pitch = pitch if pitch <= 180 else pitch - 360
    roll = roll if roll <= 180 else roll - 360

    abs_pitch = abs(pitch)
    abs_roll = abs(roll)

    # 检查是否达到最小倾斜阈值
    if abs_pitch < TILT_THRESHOLD and abs_roll < TILT_THRESHOLD:
        return None

    # 判断主要倾斜方向
    if abs_pitch > abs_roll * DOMINANCE_RATIO:
        return "up" if pitch > 0 else "down"
    elif abs_roll > abs_pitch * DOMINANCE_RATIO:
        return "right" if roll > 0 else "left"

    return None  # 处于对角线方向

try:
    while True:
        direction = get_cardinal_direction()

        match direction:
            case "up":
                print('up')
                action.pushed_up()
                # sleep(0.2)
            case "down":
                print('down')
                action.pushed_down()
                # sleep(0.2)
            case "left":
                print('left')
                action.pushed_left()
                # sleep(0.2)

            case "right":
                print('right')
                action.pushed_right()
                sleep(0.2)

        # if direction:
        #     print(direction)




        #     sense.show_letter(direction[0].upper())  # LED显示首字母
        # else:
        #     sense.clear()
        #     print("level")

        sleep(0.1)

except KeyboardInterrupt:
    sense.clear()
    print("Program stopped")