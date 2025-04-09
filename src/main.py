from sense_hat import SenseHat
from src.action import Action
from features.animations import SenseHATAnimations
# from signal import pause

sense = SenseHat()
action = Action(sense)
temperature = sense.get_temperature() - 13
pressure = int(sense.get_pressure())
animation = SenseHATAnimations(sense = sense)

# Initialization SenseHAT pressure sensor
sense.stick.direction_up = action.pushed_up
sense.stick.direction_down = action.pushed_down
sense.stick.direction_left = action.pushed_left
sense.stick.direction_right = action.pushed_right

while True:
  pass  # This keeps the program running to receive joystick events