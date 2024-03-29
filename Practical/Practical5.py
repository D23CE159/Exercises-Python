# A) Creating a class Employee to display employee details
class Employee:
    def __init__(self, name, emp_id, designation):
        self.name = name
        self.emp_id = emp_id
        self.designation = designation

    def display_details(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Designation:", self.designation)

emp1 = Employee("John Doe", 1001, "Manager")
emp1.display_details()


# B) Extending the Employee class to count the number of employees and display a raised salary amount
class Employee:
    total_employees = 0

    def __init__(self, name, emp_id, designation, salary):
        self.name = name
        self.emp_id = emp_id
        self.designation = designation
        self.salary = salary
        Employee.total_employees += 1

    def display_details(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Designation:", self.designation)

    def raise_salary(self):
        self.salary *= 1.04
        print("Raised Salary Amount:", self.salary)

emp1 = Employee("John Doe", 1001, "Manager", 50000)
emp2 = Employee("Jane Smith", 1002, "Developer", 60000)

emp1.raise_salary()
print("Total Employees:", Employee.total_employees)


# C) Implementing different types of inheritance with constructors

# Single Inheritance
class Parent:
    def __init__(self):
        print("Parent constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()  # Calling the constructor of the parent class
        print("Child constructor")

child = Child()

# Multilevel Inheritance
class GrandParent:
    def __init__(self):
        print("Grandparent constructor")

class Parent(GrandParent):
    def __init__(self):
        super().__init__()  # Calling the constructor of the grandparent class
        print("Parent constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()  # Calling the constructor of the parent class
        print("Child constructor")

child = Child()

# Multiple Inheritance
class Parent1:
    def __init__(self):
        print("Parent1 constructor")

class Parent2:
    def __init__(self):
        print("Parent2 constructor")

class Child(Parent1, Parent2):
    def __init__(self):
        Parent1.__init__(self)  # Calling the constructor of Parent1
        Parent2.__init__(self)  # Calling the constructor of Parent2
        print("Child constructor")

child = Child()


# D) Implementing polymorphism to find who will be first among two students
class Student:
    def __init__(self, name):
        self.name = name

    def compare(self, other):
        if self.name < other.name:
            print(f"{self.name} will be first.")
        elif self.name > other.name:
            print(f"{other.name} will be first.")
        else:
            print("Both students have the same name.")

student1 = Student("Alice")
student2 = Student("Bob")
student1.compare(student2)

