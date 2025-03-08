import sqlite3
import pandas as pd

square = lambda x:x*x

with sqlite3.connect('northwin.db') as con:
    con.create_function('square',1,square)
    cursor = con.cursor()
    cursor.execute('''
                   SELECT *,square(price) FROM Products
                   ''')
    result=cursor.fetchall()
    df= pd.DataFrame(result)
    print(df)
#primer vistastado a integracion de fumciones 
