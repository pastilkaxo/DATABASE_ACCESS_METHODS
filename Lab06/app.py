import sqlite3

conn = sqlite3.connect("MyLabDb.db")
cursor = conn.cursor()


conn.execute("begin transaction;")
#conn.execute("INSERT INTO Sales (ProductID,CarID, SaleDate, Quantity) VALUES (3,4, '2024-03-21', 1150);")
#cursor.execute("SELECT * FROM Sales")
cursor.execute("SELECT * FROM Cars")
#cursor.execute("SELECT * FROM Products")
print("\n")


for row in cursor.fetchall():
    print(row)

conn.execute("rollback;")


conn.close()