import os
import datetime
import pymysql

# GET Username
# Username = 'root'

username = 'root'

# Connect to the database

connection = pymysql.connect(host='localhost',
                             user=username,
                             password='ikonpass',
                             db='Chinook')


try:
    # Run a query
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute("UPDATE Friends SET age = 22 WHERE name = 'BOB'")
        connection.commit()
finally:
    # Close the connection regardless of whether the above was successful or not
    cursor.close()
