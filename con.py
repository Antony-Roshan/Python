import sqlite3

conn=sqlite3.connect('roshan. db')
'''print("Opened database successfully")

conn.execute("create table company (ID int primary key,Name text not null,Age int not null,Address cahr(50),salary real)")
#print ("Table creted Successfully")'''

conn.execute("insert into company(ID,Name,Age,Address,salary) values (1,'paul',32,'california',20000.00)");

conn.execute("insert into company(ID,Name,Age,Address,salary) values (2,'Alen',25,'Texas',15000.00)");

conn.execute("insert into company(ID,Name,Age,Address,salary) values (3,'Teddy',23,'Norway',20000.00)");
conn.execute("insert into company(ID,Name,Age,Address,salary) values (4,'Jiya',24,'Thrissur',10000.00)");
conn.execute("insert into company(ID,Name,Age,Address,salary) values (5,'Roshan',21,'Kerala',500000.00)");
print ("Record inserted successfully");

conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")

conn.execute("DELETE from COMPANY where ID = 2")


cursor=conn.execute("select * from company")
for row in cursor:
	print("ID=", row[0],"Name=", row[1],"\tAge=", row[2],"\tAddress=", row[3],"\tSalary=", row[4])
	
	
conn.commit()

conn.close()


