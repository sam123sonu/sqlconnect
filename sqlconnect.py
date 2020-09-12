import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root',password='sam@123')
print(mydb.connection_id)
db_Info = mydb.get_server_info()
print("Connected to MySQL Server version ", db_Info)
csr = mydb.cursor()
csr.execute('''use sakila''')
sql="select first_name from actor;"
csr.execute(sql)
result=csr.fetchall()
for record in result:
  print (record)