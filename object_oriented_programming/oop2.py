### Create a class object/blueprint.
### Create instance of the class.
### Define class attributes vs instance attributes in constructor method "__init__()".

### instance methods - can access intance attributes.
### special "double underscore methods" __str__ and __eq__ methods.
### @staticmethod - use with class. can not be tied to instance of the class. Can not access instance attributes inside the static method.

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

    ## instance method - 1
    def coding(self):
        return f"{self.name} can write code." 

    ## instance method - 2
    def code_language(self, language):
        return f"{self.name} can write a code in {language}."

    ## special method - 1
    def __str__(self) -> str:
        info = f"name = {self.name}, age = {self.age}, level = {self.lavel}"
        return info

    def __eq__(self, value: object) -> bool:
        return self.age == value.age

    @staticmethod
    def get_salary(age):
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000

## instance of the class
se1 = SoftwareEngineer("Mark", 23, "Junior", 5000)
se2 = SoftwareEngineer("Jenny", 27, "Senior", 8000)


## @staticmethod - only access by class
print( SoftwareEngineer.get_salary(26) )

## instance methods
print( se1.code_language('Python') )
print( se2.code_language('Jave') )