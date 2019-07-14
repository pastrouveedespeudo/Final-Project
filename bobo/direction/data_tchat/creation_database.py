"""Create database for wind map tchat"""

import psycopg2

from CONFIG import HOST
from CONFIG import USER
from CONFIG import PASSWORD
from CONFIG import DATABASE

def create_database():
    """Create table tchatmap"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""CREATE TABLE tchat_map1(
                id serial PRIMARY KEY,
                message TEXT,
                date varchar(20))
                """)
    
    conn.commit()

if __name__ == "__main__":
    create_database()
