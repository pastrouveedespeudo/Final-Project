"""We return fetilizer period"""


import datetime

def period_fertilizer():
    """Fertilizer period is between May and June"""
    month_fertilizer = [5, 6]

    date = datetime.datetime.now()

    month = date.month

    for i in month_fertilizer:
        if month == i:
            return 'oui'

    return 'non'
