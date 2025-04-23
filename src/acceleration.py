from sense_hat import SenseHat
from debounce import debounce

@debounce(0.5)
def acceleration_register(sense: SenseHat, eventHandler):

    x, y, z = sense.get_accelerometer_raw().values()

    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 3 or y > 3 or z > 3 :
        eventHandler()
    else:
        pass
        # sense.clear()
        # animations.question_mark()