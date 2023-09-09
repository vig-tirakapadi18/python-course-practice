import mysql.connector

con = mysql.connector.connect(
    host="localhost", user="root", password="rootvig26")

print(mysql)

sql = "DROP DATABASE django_project"
c = con.cursor()
c.execute(sql)
