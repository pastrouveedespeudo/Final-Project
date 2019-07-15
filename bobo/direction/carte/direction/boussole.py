"""This is our tool direction"""

def calcul_vent1(direction):
    """PEP8 function"""

    direction_input = ''

    if 180 < direction <= 202.5:
        direction_input = 'sudsudouest'

    if 202.5 < direction <= 225:
        direction_input = 'sudsudouest'

    if direction == 225:
        direction_input = 'sudouest'

    if 225 < direction <= 247.5:
        direction_input = 'sudouest'

    if 247.5 < direction <= 270:
        direction_input = 'ouestsudouest'

    if direction > 270:
        direction_input = 'ouest'

    if 270 < direction <= 292.5:
        direction_input = 'ouestnordouest'

    if 292.5 < direction <= 315:
        direction_input = 'nordouest'

    if direction == 315:
        direction_input = 'nordouest'

    if 315 < direction <= 337.5:
        direction_input = 'nordnordouest'

    return direction_input


def calcul_vent(direction):
    """We using trigonometric circle
       for determinate orientation of wind
       we transform degrees to str"""

    direction_input = ''

    if direction in (0, 360):
        direction_input = 'nord'

    if 0 < direction <= 22.5:
        direction_input = 'nordnordest'

    if 22.5 < direction <= 45:
        direction_input = 'nordnordest'

    if direction == 45:
        direction_input = 'nordest'

    if 45 < direction <= 67.5:
        direction_input = 'estnordest'

    if 67.5 < direction <= 90:
        direction_input = 'estnordest'

    if 90 < direction <= 112.5:
        direction_input = 'est'

    if 112.5 < direction <= 135:
        direction_input = 'estsudest'

    if direction == 135:
        direction_input = 'sudest'

    if 135 < direction <= 157.5:
        direction_input = 'sudsudest'

    if 157.5 < direction <= 180:
        direction_input = 'sudsudest'

    if direction == 180:
        direction_input = 'sud'

    direction_input = calcul_vent1(direction)

    return direction_input
