class Employee:
    ID = None
    salary = None
    department = None


Steve = Employee()

Steve.ID = 3789
Steve.salary = 2500
Steve.department = "Human Resources"
Steve.title = "Manager"

print("ID =", Steve.ID)
print("Salary", Steve.salary)
print("Department:", Steve.department)
print("Title:", Steve.title)

Employee.ID = '000'
print(Employee.ID)
