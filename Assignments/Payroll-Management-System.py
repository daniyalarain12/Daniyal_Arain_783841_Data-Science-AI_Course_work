# =========================================
#        PAYROLL MANAGEMENT SYSTEM
# =========================================

# Parent Class
class Employee:

    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    # Method to be overridden in child classes
    def calculate_salary(self):
        pass

    def get_info(self):
        return f"ID: {self.id}, Name: {self.name}"

# =========================================
# Child Class 1
# =========================================

class FullTimeEmployee(Employee):

    def __init__(self, id: str, name: str,
                 base_salary: float, bonus: float):

        super().__init__(id, name)
        self.base_salary = base_salary
        self.bonus = bonus

    # Overriding Method
    def calculate_salary(self):
        return self.base_salary + self.bonus

    # Overriding Method
    def get_info(self):
        return (
            f"\nFull Time Employee"
            f"\nID            : {self.id}"
            f"\nName          : {self.name}"
            f"\nBase Salary   : {self.base_salary}"
            f"\nBonus         : {self.bonus}"
            f"\nTotal Salary  : {self.calculate_salary()}"
        )

# =========================================
# Child Class 2
# =========================================

class PartTimeEmployee(Employee):

    def __init__(self, id: str, name: str,
                 hourly_rate: float, hours_worked: int):

        super().__init__(id, name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    # Overriding Method
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

    # Overriding Method
    def get_info(self):
        return (
            f"\nPart Time Employee"
            f"\nID            : {self.id}"
            f"\nName          : {self.name}"
            f"\nHourly Rate   : {self.hourly_rate}"
            f"\nHours Worked  : {self.hours_worked}"
            f"\nTotal Salary  : {self.calculate_salary()}"
        )

# =========================================
# Child Class 3
# =========================================

class Contractor(Employee):

    def __init__(self, id: str, name: str,
                 daily_rate: float, days_worked: int):

        super().__init__(id, name)
        self.daily_rate = daily_rate
        self.days_worked = days_worked

    # Overriding Method
    def calculate_salary(self):
        return self.daily_rate * self.days_worked

    # Overriding Method
    def get_info(self):
        return (
            f"\nContractor"
            f"\nID            : {self.id}"
            f"\nName          : {self.name}"
            f"\nDaily Rate    : {self.daily_rate}"
            f"\nDays Worked   : {self.days_worked}"
            f"\nTotal Salary  : {self.calculate_salary()}"
        )

# =========================================
# Creating Objects
# =========================================

employee1 = FullTimeEmployee("E101", "Daniyal", 80000, 10000)
employee2 = PartTimeEmployee("E102", "Ali", 500, 40)
employee3 = Contractor("E103", "Nabeel", 3000, 20)

employees = [employee1, employee2, employee3]

for employee in employees:
    print("===================================")
    print(employee.get_info())
    print("===================================")
