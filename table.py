import mysql.connector as mysql
db = mysql.connect(
    host = "database-2.cshux5aaxeaw.us-east-1.rds.amazonaws.com",
    user = "admin",
    passwd = "rishi123"
)
cursor = db.cursor()
cursor.execute("CREATE DATABASE reg")
cursor.execute("USE reg")
cursor.execute("CREATE TABLE information (name VARCHAR(150), age INT(3), email VARCHAR(150), phone VARCHAR(150))")
