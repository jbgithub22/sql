import sqlite3

connection = sqlite3.connect(“database_name.db”)
cursor = connection.cursor()
cursor.execute(“SELECT * FROM table_name”).fetchall()

# for MSDS SQL Northwinds Database
#
# select  orderid, customerid, shippeddate
# from    orders
# where   shipcountry = 'Canada' and
#         shippeddate between '1996-12-31' and '1997-01-31';
