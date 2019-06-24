import mysql.connector
from analysis.database import *


class exportation:
    def donnée(self):
        a = visualisation_table.visualisation_donnée(self)


        for i in a:
            print(i)
            print('\n')
            print(i[0])
            print(i[1])

            


            
            print('\n')





if __name__ == '__main__':
    
    exportation = exportation()
    exportation.donnée()
