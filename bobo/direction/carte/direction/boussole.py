"""We define direction with degrees"""


def function_calcul_vent(direction):
    """We define direction of wind"""

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
    """We define direction of wind"""

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
