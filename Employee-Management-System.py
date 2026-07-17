# ---------------------------------- Employee_Management_System --------------------------------------------- #

# ==========================================
# 1. BASE CLASSES (Person & Employee)
# ==========================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Employee(Person):
    # Method Overloading via Default Parameters (Allows multiple ways of creating an object)
    def __init__(self, name=None, age=None, employee_id=None, salary=None):
        super().__init__(name, age)
        # Encapsulation: Using double underscores (__) to make attributes private
        self.__employee_id = employee_id
        self.__salary = salary

    # Getter and Setter for Employee ID
    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    # Getter and Setter for Salary
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    # Method Overriding: Modifying parent's display behavior
    def display(self):
        super().display()
        print(f"Employee ID: {self.get_employee_id()}")
        print(f"Salary: ${float(self.get_salary()):.1f}")

    # Destructor: Cleans up resources when object or program finishes
    def __del__(self):
        pass 


# ==========================================
# 2. DERIVED CLASSES (Manager & Developer)
# ==========================================

class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        # Use super() to call the parent class constructor
        super().__init__(name, age, employee_id, salary)
        self.department = department

    # Method Overriding
    def display(self):
        super().display()
        print(f"Department: {self.department}")


class Developer(Employee):
    def __init__(self, name, age, employee_id, salary, programming_language):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    # Method Overriding
    def display(self):
        super().display()
        print(f"Programming Language: {self.programming_language}")


# ==========================================
# 3. INTERACTIVE CONSOLE INTERFACE (UI)
# ==========================================

def main():
    # Global tracking lists to act as our "database"
    people_list = []
    employees_list = []
    managers_list = []

    print("--- Python OOP Project: Employee Management System... ---")

    while True:
        print("\nChoose an operation:")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Show Details")
        print("5. Exit")

        choice = input("\n // - Enter your choice: ").strip()

        if choice == '1':
            name = input("\nEnter Name: ")
            age = int(input("Enter Age: "))
            
            p = Person(name, age)
            people_list.append(p)
            print(f"\n ~ Person created successfully with name: {p.name} and age: {p.age}.")

        elif choice == '2':
            name = input("\nEnter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            
            e = Employee(name, age, emp_id, salary)
            employees_list.append(e)
            print(f"\n ~ Employee created successfully with name: {e.name}, age: {e.age}, ID: {e.get_employee_id()}, and salary: ${float(e.get_salary()):.1f}.")

        elif choice == '3':
            name = input("\nEnter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            dept = input("Enter Department: ")
            
            m = Manager(name, age, emp_id, salary, dept)
            managers_list.append(m)
            print(f"\n ~ Manager created successfully with name: {m.name}, age: {m.age}, ID: {m.get_employee_id()}, salary: ${float(m.get_salary()):.1f}, and department: {m.department}.")

        elif choice == '4':
            print("\n ==== Choose details to show: ==== ")
            print("1. Person")
            print("2. Employee")
            print("3. Manager")
            
            show_choice = input("Enter your choice: ").strip()

            if show_choice == '1':
                if not people_list:
                    print("\n *~ No records found.")
                    print("\t *~ Please Enter Valide Choice..")
                for p in people_list:
                    print("\n ~ Person Details:")
                    p.display()

            elif show_choice == '2':
                if not employees_list:
                    print("\n *~ No records found.")
                    print("\t *~ Please Enter Valide Choice..")
                for e in employees_list:
                    # Demonstrating use of issubclass() constraint safely
                    if issubclass(Employee, Person):
                        print("\n ~ Employee Details:")
                        e.display()

            elif show_choice == '3':
                if not managers_list:
                    print("\n *~ No records found.")
                    print("\t *~ Please Enter Valide Choice..")
                for m in managers_list:
                    print("\n ~ Manager Details:")
                    m.display()
            else:
                print("\n *~ Invalid display choice.")
                print("\t *~ Please Enter Valide Choice..")

        elif choice == '5':
            # Explicitly clear out object references to invoke destructors safely
            people_list.clear()
            employees_list.clear()
            managers_list.clear()
            print("\nExiting the system. All resources have been freed.")
            print("\n ~ Thank you for visiting our system..")
            print("\n ~ Welcome back soon")
            break
            
        else:
            print("Invalid selection. Please enter a choice between 1 and 5.")
            
        print("\n--- Choose another operation ---")

if __name__ == '__main__':
    main()
