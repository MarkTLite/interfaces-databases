#File Docstring

def code_class_factory():
    """Returns a class during code"""

    class Example:
        def __init__(self,object):
            self.att = object

        def some_function(self):
            return self.att

    return Example
    
Apple = code_class_factory()
appleObj = Apple('red')
print(appleObj.some_function())
