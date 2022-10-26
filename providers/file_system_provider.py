from DbInterfaceSingleton import DatabaseInterface


class FileStoreProvider(DatabaseInterface):
    """A file system provider that implements the DatabaseInterface methods to persist data 
        on the filesystem and not an actual database."""
    def __init__(self):
        pass

    def connect(self):
        pass
    
    def disconnect(self):
        pass

    def create(self, location: str, data: dict):
        """creates a file and stores in that file location. Returns a Tuple with a boolean and a string."""
        try:
            file = open(location, mode='w', encoding='utf-8' )
            for content in data:                
                file.write(content +',')
                file.write(data[content] +'\n')    

        except(Exception):
            return (False, f'Error: {Exception}')

        finally:
            file.close() 
            print("file closed")    
            return (True, 'Record created')

    def read(self, location: str):
        """ reads a file,returns a tuple - (boolean, string, and the dictionary containing the read data)"""
        data_dict = {}
        try:
            file = open(location, mode='r', encoding='utf-8' )
            datalist = []
            for eachline in file:
                datalist.append(eachline.strip())
    
            #Create dict from datalist here 
            data = dict.fromkeys(datalist, "In stock")

        except(Exception):
            return (False, f'Error: {Exception}')
            
        finally:
            file.close() 
            print("file closed")    
            return (True, 'Read Success', data)

    def update(self, location: str, data: dict):
        """updates a given file, returns a boolean, string tuple."""
        return self.create(location, data)

    def delete(self, location: str, data: dict):
        """Perform the delete operation in a given file, returns a boolean, string tuple"""
        return self.create(location, '')       