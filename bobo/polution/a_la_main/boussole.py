"""We define direction with degrees"""

def calcul_vent(direction):

    if direction == 0 or direction == 360:
        return 'nord'

    if direction > 0 and direction <= 22.5:
        return 'nordnordest'
    
    if direction > 22.5 and direction <= 45:
        return 'nordnordest'
    
    if direction == 45:
        return 'nordest'

    if direction > 45 and direction <= 67.5:
        return 'estnordest'
    
    if direction > 67.5 and direction <= 90:
        return 'estnordest'
    
    if direction > 90 and direction <= 112.5:
        return 'est'
    
    if direction > 112.5 and direction <= 135:
        return 'estsudest'
    
    if direction == 135:
        return 'sudest'

    if direction > 135 and direction <= 157.5:
        return 'sudsudest'

    if direction > 157.5 and direction <= 180:
        return 'sudsudest'

    if direction == 180:
         return 'sud'
         
    if direction > 180 and direction <= 202.5:
        return 'sudsudouest'

    if direction > 202.5 and direction <= 225:
        return 'sudsudouest'
    
    if direction == 225:
        return 'sudouest'

    if direction > 225 and direction <= 247.5:
        return 'sudouest'
    
    if direction > 247.5 and direction <= 270:
        return 'ouestsudouest'
    
    if direction > 270:
        return 'ouest'
    
    if direction > 270 and direction <= 292.5:
        return 'ouestnordouest'
    
    if direction > 292.5 and direction <= 315:
        return 'nordouest'
    
    if direction == 315:
        return 'nordouest'
    
    if direction > 315 and direction <= 337.5:
        return 'nordnordouest'
