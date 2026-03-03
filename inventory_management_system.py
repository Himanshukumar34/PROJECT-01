import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    name="himanshu kumar ",
    database="inventory",
    password="12qwQW?@"
    
)
print("connected")

# perfectly connected 

myconn=mydb.cursor()

# create a table 
myconn.execute("""CREATE  TABLE product(
               product_id UNIQUE ID PRIMARY KEY ,
               product_name VARCHAR(255),
               price INT,
               quantity INT,
               category_id VARCHAR(255)
               ) """)

# create  2nd table 

myconn.execute("")

