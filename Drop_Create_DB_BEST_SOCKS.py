#Create the database BEST_SOCKS
import mysql.connector
#use your own user and passwd
mydb = mysql.connector.connect(
  host="localhost",
  user="sam",
  passwd="sesame",
  auth_plugin="mysql_native_password",
)

mycursor = mydb.cursor()
mycursor.execute("DROP DATABASE IF EXISTS BEST_SOCKS")

mycursor.execute("CREATE DATABASE BEST_SOCKS")
mydb.close()
