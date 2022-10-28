from database_interface import DatabaseInterface
import json

class FileStoreProvider(DatabaseInterface):
    """A file system provider that implements the DatabaseInterface methods to persist data 
        on the filesystem"""
        
    def connect(self):
        return (True, 'Connection Successful')
    
    def disconnect(self):
        return (True, "Disconnected")

    def create(self, location: str, data: dict):
        """creates a file and stores in that file location. Returns a Tuple with a boolean and a string."""
        try:
            file = open(location, mode='w', encoding='utf-8')
            if data:
               json.dump(data, file, indent=4)
               file.close() 
               print("file closed")
               return (True, "Created")
            else:
                raise Exception()  

        except(Exception):
            return (False, 'Error')

    def read(self, location: str):
            """ reads a file,returns a tuple - (boolean, string, and the dictionary containing the read data)"""
        # try:
            file = open(location, mode='r', encoding='utf-8' )
            data = json.load(file)
            file.close() 
            print("file closed") 
            return (True, 'Read Successful', data)

        # except(Exception):
        #     return (False, 'Error', {})             

    def update(self, location: str, data: dict):
        """updates a given file, returns a boolean, string tuple."""
        try:
            data = [data['contact'][1], data['contact'][0]]
            file = open(location, mode='r+', encoding='utf-8' )
            read = json.load(file)
            for table in read.values():
                count = 0
                for row in table:               
                    if data[0] == row[0]:
                        read['contact list'][count] = data
                        file.seek(0)
                    count += 1
            file.close()
            self.create(location, read)
            file.close() 
            print("file closed")                               

            return (True, 'Update Successful')

        except(Exception):
            return (False, 'Error')

    def delete(self, location: str, data: dict):
        """Perform the delete operation in a given file, returns a boolean, string tuple"""
        try:
            name = data['contact'][0]
            file = open(location, mode='r+', encoding='utf-8' )
            read = json.load(file)
            for table in read.values():
                count = 0
                for row in table:               
                    if name == row[0]:                        
                        read['contact list'].pop(count)
                        print(read)
            file.close()
            self.create(location, read)     
            file.close() 
                       

            return (True, 'Delete Successful')

        except(Exception):
            return (False, 'Error')
             