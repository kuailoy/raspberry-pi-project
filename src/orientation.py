from time import sleep
from action import Action

# 方向阈值配置（单位：度）
TILT_THRESHOLD = 30    # 最小倾斜角度
DOMINANCE_RATIO = 1.5  # 主方向判定比例（主要倾斜/次要倾斜）


def execute_action(direction, action):
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



def get_cardinal_direction(sense):
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


def orientation_register(sense, action):
    stable_count = 0
    last_read_direction = None
    last_triggered_direction = None
    cooldown_counter = 0

    STABLE_THRESHOLD = 2        # How many stable readings needed
    COOLDOWN_CYCLES = 10        # Delay before allowing another trigger
    direction = get_cardinal_direction(sense)


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
            execute_action(direction, action)
            last_triggered_direction = direction
            cooldown_counter = COOLDOWN_CYCLES
            stable_count = 0

    sleep(0.05)