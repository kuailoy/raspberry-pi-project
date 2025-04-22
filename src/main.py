from sense_hat import SenseHat
from action import Action
from features.animations import SenseHATAnimations
from time import sleep, time
from debounce import debounce
import globals

sense = SenseHat()
sense.set_imu_config(True, True, True)  # 启用所有IMU传感器
animations = SenseHATAnimations(sense=sense)
action = Action(sense, animation=animations)

@debounce(0.5)
def reg_acc(sense):

    x, y, z = sense.get_accelerometer_raw().values()

    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 2 or y > 2 or z > 2 :
        globals.text_mode = not globals.text_mode
        print(f'text_mode: {globals.text_mode}')
        animations.switching_mode()
        sense.clear()
    else:
        pass
        # sense.clear()
        # animations.question_mark()


# 方向阈值配置（单位：度）
TILT_THRESHOLD = 30    # 最小倾斜角度
DOMINANCE_RATIO = 1.5  # 主方向判定比例（主要倾斜/次要倾斜）

def get_cardinal_direction():
    # orientation = get_smoothed_orientation()
    orientation = sense.get_orientation_degrees()

    pitch = orientation["pitch"]
    roll = orientation["roll"]

    # print(f"Pitch: {pitch:.2f}, Roll: {roll:.2f}")

    # 规范化角度到-180~180范围
    pitch = pitch if pitch <= 180 else pitch - 360
    roll = roll if roll <= 180 else roll - 360

    abs_pitch = abs(pitch)
    abs_roll = abs(roll)

    # 检查是否达到最小倾斜阈值
    if abs_pitch < TILT_THRESHOLD and abs_roll < TILT_THRESHOLD:
        return None

    # 判断主导方向 + 增加差值限制，防止 pitch/roll 相近时误判
    diff = abs(abs_pitch - abs_roll)

    if abs_pitch > abs_roll * DOMINANCE_RATIO and diff > 5:
        return "up" if pitch > 0 else "down"
    elif abs_roll > abs_pitch * DOMINANCE_RATIO and diff > 5:
        return "right" if roll > 0 else "left"

    return None  # direction not clear

def execute_action(direction):
    if direction:  # 只在方向不为None时执行
        match direction:
            case "up":
                print('up')
                action.pushed_up()
            case "down":
                print('down')
                action.pushed_down()
            case "left":
                print('left')
                action.pushed_left()
            case "right":
                print('right')
                action.pushed_right()

try:
    stable_count = 0
    last_read_direction = None
    last_triggered_direction = None
    cooldown_counter = 0

    STABLE_THRESHOLD = 2        # How many stable readings needed
    COOLDOWN_CYCLES = 10        # Delay before allowing another trigger

    while True:
        reg_acc(sense)

        direction = get_cardinal_direction()

        # Cooldown logic
        if cooldown_counter > 0:
            cooldown_counter -= 1

        # Stability check
        if direction == last_read_direction and direction is not None:
            stable_count += 1
        else:
            stable_count = 0
            last_read_direction = direction

        # Trigger action if stable & not in cooldown & direction changed
        if stable_count >= STABLE_THRESHOLD:
            if cooldown_counter == 0 and direction != last_triggered_direction:
                execute_action(direction)
                last_triggered_direction = direction
                cooldown_counter = COOLDOWN_CYCLES
                stable_count = 0

        sleep(0.05)

except KeyboardInterrupt:
    sense.clear()
    print("Program stopped by user.")