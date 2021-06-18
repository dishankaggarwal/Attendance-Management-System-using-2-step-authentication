import sqlite3

#Create a database
conn = sqlite3.connect('attendance.db')

#Creating a cursor
c=conn.cursor()

c.execute("""UPDATE students SET qr_code='NO' WHERE enrollment_no='40415003117'""")

#Commiting the changes
conn.commit()


#Closing the connection 
conn.close()