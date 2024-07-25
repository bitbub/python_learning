

class SoftwareEngineer():
    
    def __init__(self):
        self._salary = None             ## protected attributes - one underscore - only use internaly
    
    ## property decorator - getter
    @property
    def salary(self):
        return self._salary

    ## property decorator - stter
    @salary.setter
    def salary(self, base_value):
        self._salary = base_value

se = SoftwareEngineer()

## only way to get from outside.
se.salary = 6000 # @salary.setter
print(se.salary) # @property getter