class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id} {self.name} {self.age} {self.salary}"

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def print_data(self):
        for employee in self.employees:
            print(employee)

    def sort_data(self, key):
        self.employees.sort(key=lambda x: getattr(x, key))

# Sample data
employee1 = Employee("161E90", "Ramu", 35, 59000)
employee2 = Employee("171E22", "Tejas", 30, 82100)
employee3 = Employee("171G55", "Abhi", 25, 100000)
employee4 = Employee("152K46", "Jaya", 32, 85000)

# Creating EmployeeDatabase and adding employees
database = EmployeeDatabase()
database.add_employee(employee1)
database.add_employee(employee2)
database.add_employee(employee3)
database.add_employee(employee4)

# User input for sorting parameter
sort_parameter = input("Choose sorting parameter (1. Age, 2. Name, 3. Salary): ")

# Mapping user input to corresponding attribute
sort_mapping = {
    "1": "age",
    "2": "name",
    "3": "salary"
}

if sort_parameter in sort_mapping:
    database.sort_data(sort_mapping[sort_parameter])
    print("\nSorted Data:")
    database.print_data()
else:
    print("Invalid sorting parameter.")
