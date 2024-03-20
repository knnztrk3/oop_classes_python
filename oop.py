# Python Object-Oriented Programming

class Employee():

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Emplooye('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):

    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    raise_amt = 1.20

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


# print(emp1)
# print(emp2)

# print(Employee.num_of_emps)

emp_1 = Employee('BobEmp', 'Don', 6000)
emp_2 = Employee('SueEmp', 'Employee', 5000)

# dev_1 = Developer('BobDev', 'Don', 6000, "Python")
# dev_2 = Developer('JhonDev', 'Developer', 5000, "C#")

# mng_1 = Manager('BobMan', 'Don', 6000, [dev_1])
# mng_2 = Manager('SmithMan', 'Manager', 5000)

# print(Employee.num_of_emps)

# print(len(emp_1))

# print(len('test'))
# print('test'.__len__())

# print(emp_1 + emp_2)

# print(1 + 2)
# print('a' + 'b')

# print(repr(emp_1))
# print(str(emp_1))

# print(emp_1.__repr__())
# print(emp_1.__str__())

# print(1 + 2)
# print('a' + 'b')

# print(int.__add__(1, 2))
# print(str.__add__('a', 'b'))

# print(isinstance(mng_1, Manager))
# print(isinstance(mng_1, Employee))
# print(isinstance(dev_1, Manager))

# print(issubclass(Developer, Employee))
# print(issubclass(Manager, Employee))
# print(issubclass(Manager, Developer))

# print(mng_1.email)

# mng_1.add_emp(dev_2)

# mng_1.remove_emp(dev_1)

# mng_1.print_emps()

# print(dev_1.email)
# print(dev_1.prog_lang)

# print("Employee**")
# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)

# print("Developer**")
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# print("Manager**")
# print(mng_1.pay)
# mng_1.apply_raise()
# print(mng_1.pay)


# print(help(Developer))

# print(emp1.email)
# print(emp2.email)

# import datetime
# my_date = datetime.date(2024, 3, 20)

# print(Employee.is_workday(my_date))

# emp_str_1 = 'Jhon-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'

# new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.email)
# print(new_emp_1.pay)

# Employee.set_raise_amt(1.05)
# emp1.set_raise_amt(1.05)
# Employee.raise_amt = 1.05

# print(Employee.raise_amt)
# print(emp1.raise_amt)
# print(emp2.raise_amt)

# print(emp1.__dict__)
# print(Employee.__dict__)

# all instance bc class
# Employee.raise_amount = 1.05

# effect emp1 instance
# emp1.raise_amount = 1.05

# print(emp1.__dict__)

# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)

# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)

# emp1.first = 'Bob'
# emp1.last = 'Don'
# emp1.email = 'test.user@hotmail.com'
# emp1.pay = 60000

# emp2.first = 'Bob2'
# emp2.last = 'Don2'
# emp2.email = 'test.user2@hotmail.com'
# emp2.pay = 50000

# print(emp1.email)
# print(emp2.email)

# print('{} {}'.format(emp1.first, emp1.last))
# print('{} {}'.format(emp2.first, emp2.last))

# print(Employee.fullname(emp1))
# print(Employee.fullname(emp2))

# print(emp1.fullname())
# print(emp2.fullname())
