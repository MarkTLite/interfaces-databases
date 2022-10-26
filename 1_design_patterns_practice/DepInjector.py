# Dependency Injection Example 
instance = None

class DepInjector:
    """class docstring"""

    def __init__(self):
        """docstring"""
        self.provider = None
        global instance
        instance = self

    def performAction(self, arg):
        """perform action"""
        self.provider.performAction(arg)

    def setProvider(self, provider):
        """set provider"""
        self.provider = provider

    @staticmethod
    def getInstace(re_init=False):
        """get an instance of the Example class"""
        global instance
        if instance is None or re_init is True:
            return DepInjector()
        return instance