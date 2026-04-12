import abc # Abstract Base Classes (ABC)

class AbstractClass(abc.ABC):
    @abc.abstractmethod
    def required_method(self):
        pass
    
class ValidClass(AbstractClass):
    def required_method(self):
        pass

ValidClass()
# Can't instantiate abstract class ValidClass without an implementation
# for abstract method 'required_method' (if required_method is not defined)

# AbstractClass() # Can't instantiate abstract class AbstractClass without an implementation for abstract method 'required_method'