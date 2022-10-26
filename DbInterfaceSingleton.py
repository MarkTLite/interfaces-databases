"""A Database class that applies Singleton, Dependency injection and Interfaces"""
from database_interface import DatabaseInterface

instance = None

class Database(DatabaseInterface):
    def __init__(self, provider: "Database"):
        """Inject provider, init singleton"""
        self.provider = provider
        global instance
        instance = self

    @staticmethod
    def get_instance(provider: "Database", re_init=False):
        """get an instance of the Database class"""
        global instance
        if instance is None or re_init is True:
            return Database(provider)
        return instance

    def connect(self):
        return self.provider.connect()

    def disconnect(self):
        return self.provider.disconnect()        

    def create(self, location: str, data: dict):
        """takes a data location and a data dictionary with the data to be stored in that location. 
        Returns a Tuple with a boolean and a string."""
        return self.provider.create(location, data)

    def read(self, location: str):
        """ takes a location string and returns a tuple - (boolean, string, and the dictionary containing the read data)"""
        return self.provider.read(location)

    def update(self, location: str, data: dict):
        """takes a string and a dictionary and return a boolean, string tuple."""
        return self.provider.update(location, data)

    def delete(self, location: str):
        """Perform the delete operation take only a string and return a boolean, string tuple"""
        self.provider.delete(location)
