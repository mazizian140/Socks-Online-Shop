# now create the table
import mysql.connector
#use your own user and passwd
mydb = mysql.connector.connect(
  host="localhost",
  user="sam",
  passwd="****",
  auth_plugin="mysql_native_password",
  database="BEST_SOCKS"
)
mycursor = mydb.cursor()
mycursor.execute("DROP TABLE IF EXISTS SOCKS")

# You need to create the entire string for what you want.
value = " CREATE TABLE socks (" \
+ "ID_number INT KEY AUTO_INCREMENT," \
+ "CustomerFirstName VARCHAR(25)," \
+ "CustomerLastName VARCHAR(25)," \
+ "TypeOfWool INT," \
+ "SockSize INT, " \
+ "SockQuantity INT)"

mycursor.execute(value)
mydb.close()
