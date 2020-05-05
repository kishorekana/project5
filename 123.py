

import mysql.connector
import csv
##conn=MySQLdb.connect(host='localhost',user='root',passwd='amul7155',db='db1') 
mycursor=conn.cursor()
mydb=mysql.connector.connect(user='root',host='localhost',password='amul7155',db='db1')
csv_data=csv.reader(open('‪F:\python\emp1.csv'))
print(type(csv_data))
cursor=mydb.cursor()
for line in csv_data:
    if(emp_id!=2):
        
        (emp_id,emp_name,emp_email)=line #---stored procedure attributes should be given-------
        print(type(line))
        print(emp_id,emp_name,emp_email)
        sql="insert into employees1(emp_id,emp_name,emp_email) values ('%s','%s','%s')"%\
             (emp_id,emp_name,emp_email) #----first attributes are table attributes and second attributes are stored procedure attributes---
    cursor.execute(sql)
cursor.execute("select * from employees")
print(cursor.fetchall())
mydb.commit()
