"""We define direction with degrees"""


def function_calcul_vent(direction):
    """This is our tool direction we input a degrees from
    Openweather API and go out his associated name"""

    out = ''

    if 112.5 < direction <= 135:
        out = 'estsudest'

    elif direction == 135:
        out = 'sudest'

    elif 135 < direction <= 157.5:
        out = 'sudsudest'

    elif 157.5 < direction <= 180:
        out = 'sudsudest'

    elif direction == 180:
        out = 'sud'

    elif 180 < direction <= 202.5:
        out = 'sudsudouest'

    elif 202.5 < direction <= 225:
        out = 'sudsudouest'

    elif direction == 225:
        out = 'sudouest'

    elif 225 < direction <= 247.5:
        out = 'sudouest'

    elif  247.5 < direction <= 270:
        out = 'ouestsudouest'

    elif 270 < direction < 360:
        out = 'ouest'


    return out

def calcul_vent(direction):
    """We define direction of wind
    we try for example if direction is 0 or 360 degrees so it's
    the north, elif direction if superior to 0 and inferior
    to 22.5 degrees so it's the north east."""

    out = ''

    if direction in (0, 360):
        out = 'nord'

    elif 0 < direction <= 22.5:
        out = 'nordnordest'

    elif 22.5 <= direction <= 45:
        out = 'nordnordest'

    elif direction == 45:
        out = 'nordest'

    elif 45 < direction <= 67.5:
        out = 'estnordest'

    elif 67.5 < direction <= 90:
        out = 'estnordest'

    elif 90 < direction <= 112.5:
        out = 'est'

    elif 270 < direction <= 292.5:
        out = 'ouestnordouest'

    elif 292.5 < direction <= 315:
        out = 'nordouest'

    elif direction == 315:
        out = 'nordouest'

    elif 315 < direction <= 337.5:
        out = 'nordnordouest'

    else:
        out = function_calcul_vent(direction)

    return out
