import cx_Oracle

connection = cx_Oracle.connect(
    user="SCOTT",
    password="tiger",
    dsn="localhost/xe"
)
cursor = connection.cursor()
