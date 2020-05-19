import os
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
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close the connection regardless of whether the above was successful or not
    cursor.close()
