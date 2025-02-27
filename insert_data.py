from pr1 import mydb,mycursor
def insert_data():
    id=int(input("Enter the id: "))
    name = input("Enter name: ")
    address = input("Enter address: ")
    sql = "INSERT INTO student (id,name, address) VALUES (%s, %s, %s)"
    val = (id, name, address)
    print("SQL Query:", sql)
    print("Values:", val)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
insert_data()
mycursor.execute('select * from student')
myresult=mycursor.fetchall()
for row in myresult:
    print(row)
mydb.close()