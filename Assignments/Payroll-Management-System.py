# ===== PAYROLL MANAGEMENT SYSTEM =====

class Employee:
    def __init__(self, id:str, name:str):
        self.id = id
        self.name = name
        
    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    
    def calculate_salary(self):
        pass
    def get_info(self):
        return f"ID : {self.id}\nNAME : {self.name}"

class FullTimeEmployee(Employee):
    def __init__(self, id:str, name:str, base_salary:float, bonus:float):
        super().__init__(id, name)
        self.base_salary = base_salary
        self.bonus = bonus
    
    def calculate_salary(self):
        return self.base_salary + self.bonus
    
    def get_info(self):
        return (
            "*"*20 + "\n"
            f"{super().get_info()}\n"
            f"BASE SALARY : {self.base_salary}\n"
            f"BONUS : {self.bonus}\n"
            f"TOTAL SALARY : {self.calculate_salary()}"
            )

class PartTimeEmployee(Employee):
    def __init__(self, id:str, name:str, hourly_rate:float, hours_worked:float):
        super().__init__(id, name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked
    
    def get_info(self):
        return (
            "*"*20 + "\n"
            f"{super().get_info()}\n"
            f"HOURLY RATE : {self.hourly_rate}\n"
            f"HOURS WORKED : {self.hours_worked}\n"
            f"TOTAL SALARY : {self.calculate_salary()}"
            )

class Contractor(Employee):
    def __init__(self, id:str, name:str, daily_rate:float, days_worked:float):
        super().__init__(id, name)
        self.daily_rate = daily_rate
        self.days_worked = days_worked

    def calculate_salary(self):
        return self.daily_rate * self.days_worked
    
    def get_info(self):
        return (
            "*"*20 + "\n"
            f"{super().get_info()}\n"
            f"DAILY RATE : {self.daily_rate}\n"
            f"DAYS WORKED : {self.days_worked}\n"
            f"TOTAL SALARY : {self.calculate_salary()}"
            )

emp1 = FullTimeEmployee("24SW039","DANIYAL ARAIN",500000,10000)
emp2 = PartTimeEmployee("24SW038","NABEEL SHAHID",500,8)
emp3 = Contractor("24SW069","TARIQUE JAMEEL",5000,28)

print(emp1.get_info())
print(emp2.get_info())
print(emp3.get_info())
