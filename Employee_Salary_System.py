class EmployeeSystem:
    def __init__(self):
        self.__employees = []

    def addEmployee(self, name, position, salary):
        employee = {
            "name":name,
            "position":position,
            "salary":salary
        }

        self.__employees.append(employee)
        print(name, "has been added to Employee system")


#this method displays all employee records 

    def displayEmployeesRecords(self):
        if len(self.__employees) == 0:
            print("No Employee found by this name.")

        else:
            print("\nEmployees' Records:")
            print("==================")

            for employee in self.__employees:
                print("Name:",employee["name"])
                print("Position:",employee["position"])
                print("Salary:",employee["salary"])
                print("====================")



#this method is for searching employes by their name

    def searchEmployee(self, name):
        for employee in self.__employees:
            if employee["name"].lower() == name.lower():
                print("\nEmployee Found in the system!!")
                print("Name:",employee["name"])
                print("Position:",employee["position"])
                print("Salary:",employee["salary"])
                return
            
        print("Employee not found in the system")




# Increase employee salary

    def increase_salary(self, name, amount):
        for employee in self.__employees:
            if employee["name"].lower() == name.lower():
                employee["salary"] += amount
                print("Salary updated successfully.")
                print("New Salary:", employee["salary"])
                return

        print("Employee not found.")


    def countEmployee(self):
        return len(self.__employees)
    

employe = EmployeeSystem() #creating object of the class

#employe name, salary, position and quantity of employee input section
number_of_employee = int(input("How many Employees you want to add:"))
for i in range(number_of_employee):
    print("\nEnter Employee", i + 1)
    name = input("Enter employee name:")
    position = input("Enter employee position:")
    salary = float(input("Enter employee salary :"))

    employe.addEmployee(name,position,salary)

employe.displayEmployeesRecords()

#salary increament input

name = input("Enter employee name to increase salary: ")
amount = float(input("Enter salary increase amount: "))

employe.increase_salary(name, amount)

#search employe input
searchEmployeeName = input("\nSearch Employee:")
employe.searchEmployee(searchEmployeeName)

print("\nTotal Employees:",employe.countEmployee())
