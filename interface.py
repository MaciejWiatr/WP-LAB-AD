from abc import ABC, abstractmethod

class Interface(ABC):
    
    @abstractmethod
    def first_method(self):
        raise "Not implemented"
    
class FirstClass(Interface):
    def first_method(self):
        return "fm_1"
    
class SecondClass(Interface):
    def first_method(self):
        return "fm_2"
    
def process_interface(obj: Interface):
    obj.first_method()
    "interface contract correctly"

first = FirstClass()
first.first_method()
second = SecondClass()
second.first_method()

process_interface(first)
process_interface(second)

