#Code to learn classes
import datetime

class Employee:

    num_of_emp = 0
    raise_amount = 1.04


    def __init__(self, first, last, pay, join):
        self.first = first
        self.last = last
        self.pay = pay
        self.join = join
        self.email = first + "." + last + "@infomineo.com"

        Employee.num_of_emp +=1
    
    def employee_info(self):
        return f"{self.first} {self.last} works at infomineo since {self.join}, his email adress is {self.email}. He's paid {self.pay}, expected to grow at {Employee.raise_amount - 1}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount) :
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls, emp_str) :
        first, last, pay, join = emp_str.split('-')
        return cls(first, last, pay, join)
    
    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday == 6 :
            return False
        else :
            return True
        

#creating a subclass to learn about  inheritance

class Developper(Employee):
    raise_amount = 1.1

    def __init__(self, first, last, pay, join, prog_lang):
        super().__init__(first, last, pay, join)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, join, employees=None):
        super().__init__(first, last, pay, join)
        if employees is None :
            self.employees = []
        else :
            self.employees = employees

    def add_employee(self, emp) :
        if emp not in self.employees :
            self.employees.append(emp)
    
    def remove_employee(self, emp) :
        if emp in self.employees :
            self.employees.remove(emp)
    
    def print_emps(self) :
        for emp in self.employees :
            print("-->",emp.employee_info())

#testing inputs

dev1 = Developper("Ali", "Alkharassani", 12014, "8/09/2023", "Python")
dev2 = Developper("Saad", "Tariq", 11900, "14/03/2023", "Java")

mgr1 = Manager('sue', 'smith', 90000, '8/12/2019', [dev1])
mgr1.add_employee(dev2)

print(mgr1.email)
print(mgr1.print_emps())


