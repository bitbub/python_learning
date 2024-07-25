## Encapsulation - 
#   mechanism of hidding data emplimentation. 
#   Instance variable/methods is kept private by restricting access from public methods like getter and setter mothods
#   and only one accesser method from outside can access/change the instance variable/methods.
#   protected attributes - one underscore
#   private attributes - double underscore


## abstraction - extention of encapsulation. Hide the internal implementation.

class SoftwareEngineer():
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = None             ## protected attributes - one underscore - only use internaly
        self._num_problem_solved = 0    ## protected attributes   - one underscore - only use internaly

    def code(self):
        self._num_problem_solved += 1

    ## getter - public
    def get_salary(self):
        return self._salary
    
    ## setter - public
    def set_salary(self, base_value):
        self._salary = self._calculate_salary(base_value)

    ## protected method - also abtraction.
    def _calculate_salary(self, base_value):
        if self._num_problem_solved < 10:
            return base_value
        if self._num_problem_solved < 100:
            return base_value * 2
        return base_value * 3


se = SoftwareEngineer('Mark', 26)
print(se.name, se.age)

for i in range(70):
    se.code()

se.set_salary(6000)
print(se.get_salary())

