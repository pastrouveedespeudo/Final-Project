"""Here for the site web we document variables"""

def habitant(lieu):
    """We define variables"""

    out = ''

    if lieu == 'lyon':
        out = 'supp300K'

    if lieu == 'paris':
        out = 'sup1M'

    if lieu == 'marseille':
        out = 'sup500K'

    return out
