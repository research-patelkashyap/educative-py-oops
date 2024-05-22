class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary

    def displaySalary(self):
        print("Salary:", self.__salary)

    def __displayID(self):
        print("ID:", self.ID)


Steve = Employee(3789, 2500)
Steve.displaySalary()
# print(Steve.__salary)  # this will generate an error
# Steve.__displayID()  # this will generate an error
