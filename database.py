import sqlite3

#import objects
from objects import objects

conn = sqlite3.connect('database.db')

c = conn.cursor()

# TABLES REPRESENTING STORES

# c.execute("""CREATE TABLE Amazon (
#             name text,
#             price real
#              )""")
# c.execute("""CREATE TABLE Target (
#             name text,
#             price real
#              )""")
# c.execute("""CREATE TABLE Walmart (
#             name text,
#             price real
#              )""")


# c.execute("INSERT INTO objects VALUES('car','22000')")


# obj_1 = Objects('frisbee',7.89)
# obj_2 = Objects('cup',2.99)
obj3 = objects()
obj4=objects()
item=[]
obj4 = obj3.commonObjects(item)
# print("len obj4", len(obj4))
#

# for i in range(0,35):
#      c.execute("INSERT INTO Amazon VALUES(?,?)", (obj4[i].getName(), obj4[i].getPrice()))
#      print(obj4[i].getName(),obj4[i].getPrice())
#
#
# for i in range(0,35):
#      c.execute("INSERT INTO Target VALUES(?,?)", (obj4[i].getName(), obj4[i].getPrice()))
#      print(obj4[i].getName(),obj4[i].getPrice())

for i in range(0,35):
     c.execute("INSERT INTO Walmart VALUES(?,?)", (obj4[i].getName(), obj4[i].getPrice()))
#     print(obj4[i].getName(),obj4[i].getPrice())

#c.execute("DELETE FROM objects WHERE name = 'umbrella'")
c.execute("SELECT * FROM Walmart")
#print(c.fetchone())
print(c.fetchall())
#conn.commit()

conn.close()