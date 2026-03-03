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
# | sale_id | product_id | quantity_sold | date |

myconn.execute("""CREATE TABLE sales (
               sales_id AUTO_INCREMENT UNIQUE ID ,
               product_id INT ,
               quantity_sold INT ,
               Date TIMESTAMP)""")
def  add_product():
    num1=int(input("Enter your product-id :"))
    name=str(input("Enter your product name :"))
    price=int(input("Enter your price in in ruppees: "))
    quantity =int(input("Enter your quantity "))
    category =input("Enter your catgory :")
    sql="INSERT INTO product(product_id, product_name, price, quantity , category ) VALUES(%s,%s,%s,%s,%s)"
    value=(num1,name,price,quantity,category)
    myconn.execute(sql,value)
    mydb.commit()
    print("successfully saved ")

while True:
    print("\n" + "="*40)
    print("     INVENTORY MANAGEMENT SYSTEM")
    print("="*40)
    print("  1. Add New Product")
    print("  2. View All Products")
    print("  3. Update Stock (IN/OUT)")
    print("  4. Exit")
    print("-"*40)

    choice = input("Enter your choice (1-4): ").strip()

    if choice == '1':
        add_product()


    elif choice == '4':
        print("\nThank you! Exiting program...")
        break

    else:
        print("Invalid choice! Please enter 1, 2, 3 or 4.")
        # optional: time.sleep(1.5)  # if you imported time