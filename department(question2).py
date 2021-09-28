import sqlite3
con = sqlite3.connect('employees.db')
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS EMPLOYEE ")
query = """CREATE TABLE EMPLOYEE(
         Name VARCHAR NOT NULL,
         ID INT PRIMARY KEY NOT NULL, 
         Salary INT NOT NULL,
         Department_id INT NOT NULL )"""
cur.execute(query)
addColumn = "ALTER TABLE EMPLOYEE ADD COLUMN CITY VARCHAR"
cur.execute(addColumn)
con.execute("INSERT INTO EMPLOYEE (Name,ID,Salary,Department_id,CITY) "
                 "VALUES ('Keshav',1 ,15000 ,5,'kochi')")
con.execute("INSERT INTO EMPLOYEE (Name,ID,Salary,Department_id,CITY) "
                 "VALUES ( 'Kavya',2,20000,3,'kozhikode')")
con.execute("INSERT INTO EMPLOYEE (Name,ID,Salary,Department_id,CITY) "
                 "VALUES ('Maya',3,15000,4,'kannur')")
con.execute("INSERT INTO EMPLOYEE (Name,ID,Salary,Department_id,CITY) "
                 "VALUES ('Mia',4,25000,6,'kollam')")
con.execute("INSERT INTO EMPLOYEE (Name,ID,Salary,Department_id,CITY) "
                 "VALUES ('isha',5,35000,8,'trivandrum')")
con.commit()
cur.execute("SELECT Name,ID,Salary FROM EMPLOYEE")
print(cur.fetchall())
a = input("enter the first letter")
cur1=con.execute("SELECT * FROM EMPLOYEE where upper(Name) LIKE'"+ a +"%'")
print(cur1.fetchall())
b = input("enter the id")
cur2=con.execute("SELECT * FROM EMPLOYEE where ID = "+ b +"")
print(cur2.fetchall())
c = input("Enter the id of employee whose name you want to change : ")
d = input("Enter new employee name : ")
cur3 = con.execute("UPDATE EMPLOYEE SET Name = '"+ d +"'where ID = '"+ c +"'")
cur = con.execute("SELECT * from EMPLOYEE")
print(cur.fetchall())
con.close()

con1 = sqlite3.connect('employees.db')
cur4 = con1.cursor()
cur4.execute("DROP TABLE IF EXISTS DEPARTMENTS ")
query1 = """CREATE TABLE DEPARTMENTS(
         Department_id INT REFERENCES DEPARTMENTS(Department_id),
         Department_name VARCHAR NOT NULL)"""
cur4.execute(query1)
con1.execute("INSERT INTO DEPARTMENTS (Department_id,Department_name) "
                 "VALUES (5,'HR')")
con1.execute("INSERT INTO DEPARTMENTS (Department_id,Department_name) "
                 "VALUES (6,'sales')")
con1.execute("INSERT INTO DEPARTMENTS (Department_id,Department_name) "
                 "VALUES (3,'Marketing')")
con1.execute("INSERT INTO DEPARTMENTS (Department_id,Department_name) "
                 "VALUES (4,'admin')")
con1.execute("INSERT INTO DEPARTMENTS (Department_id,Department_name) "
                 "VALUES (8,'planning')")
con1.commit()
cur4.execute("SELECT *FROM DEPARTMENTS ")
print(cur4.fetchall())
e=input("Enter Department ID")
print(con1.execute("Select Name,ID,Salary,EMPLOYEE.Department_id,CITY,Department_name from EMPLOYEE,DEPARTMENTS where EMPLOYEE.Department_id== '"+ e +"' and DEPARTMENTS.Department_id== '"+ e +"'" ).fetchall())

