### Create a class object/blueprint.
### Create instance of the class.
### Define class attributes vs instance attributes in constructor method "__init__()".


## class
class SoftwareEngineer:
    
    ## class attribute
    alias = "Expert in OOP"

    ## constructor method
    def __init__(self, name, age, level, salary):
        ## instance attributes
        self.name = name
        self.age = age
        self.lavel = level
        self.salary = salary

## instance of the class
se1 = SoftwareEngineer("Mark", 23, "Junior", 5000)
se2 = SoftwareEngineer("Jenny", 27, "Senior", 8000)

## class attribute
print(SoftwareEngineer.alias)

## instace attributes
print(se1.name, se1.age, se1.salary)
print(se2.name, se2.age, se2.salary)