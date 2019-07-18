import matplotlib.pyplot as plt
import numpy as np

def histogramme(x_data, y_data):


    y = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
    x = [2]
    


    plt.bar(x, y, label = 'jour/pm') 


    plt.xlabel('Jour')
    plt.ylabel('Pm')
    plt.title('Pm selon les jours')

    plt.legend()

    plt.show()

    
histogramme('', '')
