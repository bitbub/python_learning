## Inheritace - as name implies one class(child class) can access/inherits the attributes, methods of another class(parent class).
## polymorphism - allows you to eccess attribute/method of base and child class

## Parent class/ Base class
class Employee():
    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working.")

## Child class - of Employee class - - will inherit all the atrributes and method of Employee class
class SoftwareEngineer(Employee):
    def __init__(self, name, age, salary, level) -> None:
        super().__init__(name, age, salary)
        self.level = level

    ## override - Base class method.
    def work(self):
        print(f"{self.name} is writting code ...")
    
    ## only child class method
    def code(self):
        print(f"{self.name} can write code.")



## Child class - of Employee class - will inherit all the atrributes and method of Employee class
class Desiner(Employee):

    ## override - Base class method.
    def work(self):
        print(f"{self.name} is designing ...")
    
    ## only child class method
    def design(self):
        print(f"{self.name} can draw.")


se = SoftwareEngineer("Jack", "26", 8000, "Junior")
# se.work()
# se.code()

de = Desiner("Jenny", "28", 7000)
# de.work()
# de.design()

## polymorphism

employees = [Employee('Jack', '26', 8000),
             SoftwareEngineer("Jack", "26", 8000, "Junior"),
             Desiner("Jenny", "28", 7000)
             ]

for employee in employees:
    print(f"access work method depending on the class - {employee.__class__.__name__}.")
    employee.work()