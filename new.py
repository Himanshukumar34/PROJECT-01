# write a program in which you have to take input from the user 
# here is the input you will get from the user 

# employee_name 
# employee_id
# employee_salary
# employee_department


# output 

# employee_name 
# employee_id
# employee_salary + 20% bonus
# employee_department


employee_name=str(input("write your employee_name"))
employee_id=str(input("write your employee_id"))
employee_salary=int(input("write your employee_salary"))
employee_department=str(input("write your employee_department"))



employee_salary2 = employee_salary * 1.2

print("name=",employee_name, "\n", "employee_id=",employee_id, "\n", "employee_salary=",employee_salary2, "\n","employee_department=",employee_department)