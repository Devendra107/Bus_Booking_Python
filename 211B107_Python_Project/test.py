import sqlite3
con=sqlite3.Connection('Bus_Booking')
cur=con.cursor()
value=1234567890
cur.execute('delete from admin')
con.commit()
result=cur.fetchall()
print(result)
