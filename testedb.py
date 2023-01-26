import mysql.connector


try:
    cnx = mysql.connector.connect(
        user='botpython', 
        password='Py287948#@',
        host='assesi-mysql-cluser.cypeiqhtjcfr.sa-east-1.rds.amazonaws.com',
        database='assesi-mapa'
        )
    
except Exception as e:
    print(e)

mycursor = cnx.cursor()

mycursor.execute("")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

cnx.close()