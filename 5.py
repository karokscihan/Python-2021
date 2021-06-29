
import sqlite3
import os
os.system('clear')


conn = sqlite3.connect('customer.db')

c = conn.cursor()

'''c.execute("""Create Table customer( 
	first_name text,
	last_name text,
	email text)""")
'''
'''c.execute("INSERT INTO customer VALUES ('Cihan','Ogeturk','karoks@ubuntu')")'''

c.execute("SELECT * FROM customer")

print(c.fetchall()[0][0])

conn.commit()




conn.close()