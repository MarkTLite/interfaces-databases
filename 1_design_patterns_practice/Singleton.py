# file docstring
instance = None

class SingletonExample:
    """class docstring"""

    def __init__(self):
        """docstring"""
        global instance
        instance = self
        print('instance')

    @staticmethod
    def getInstace(re_init=False):
        """get an instance of the Example class"""
        global instance
        if instance is None or re_init is True:
            return SingletonExample()
        return instance

if __name__ == "__main__":
    # The client code.

    #Different instances
    #s1 = SingletonExample()
    #s2 = SingletonExample()

    #Same Instance
    s1 = SingletonExample.getInstace()
    s2 = SingletonExample.getInstace()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")        