class Employee():
    def __init__(self, pay):
        self.pay = pay
    
    def receive_salary(self, much):
        pass


#### Code to complete [START] ####

class EmployeeDidntWorked(Exception):
    def __str__(self):
        return "Employee didnt worked !"

class EmployeeWorkedNegatively(Exception):
    def __str__(self):
        return "Employee worked negatively"

class EmployeeWorkedTooMuch(Exception):
    def __str__(self):
        return "Employee worked too much"

class PayIsNegative(Exception):
    def __str__(self):
        return "Pay is negative"

class PayIsTooBig(Exception):
    def __str__(self):
        return "Pay is too big"


def pay_employee(employee, hours_worked):
    to_receive = hours_worked * employee.pay
    if hours_worked == 0 :
        raise EmployeeDidntWorked
    if hours_worked < 0 : 
        raise EmployeeWorkedNegatively
    if hours_worked > 744 :
        raise EmployeeWorkedTooMuch
    if employee.pay < 0 :
        raise PayIsNegative
    if employee.pay > 100 :
        raise PayIsTooBig
    employee.receive_salary(to_receive)



