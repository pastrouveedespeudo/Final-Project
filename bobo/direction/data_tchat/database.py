import psycopg2

from .CONFIG import HOST
from .CONFIG import USER
from .CONFIG import PASSWORD
from .CONFIG import DATABASE



def database(data):
    

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""INSERT INTO tchat_map
                (message)
                values(%s)
                """, (data,))
    
    conn.commit()











    
