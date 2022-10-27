from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine

from database_interface import DatabaseInterface


class SQLiteProvider(DatabaseInterface):
    """An sqlite provider that implements the [DatabaseInterface] methods to persist data 
        on an sqlite actual database."""
    def __init__(self, location):
        self.meta = MetaData()
        self.location = location
        self.connect()

    def connect(self):
        self.engine = create_engine(self.location)
        self.conn = self.engine.connect()
        return (True, 'Connection Successful')
    
    def disconnect(self):
        if self.conn:
            self.conn.close()

        return (True, "Disconnected")
        
    def create(self, location: str, data: dict):
        """creates an sqlite db in the given file location and a table.
         Returns a Tuple with a boolean and a string."""
        try:          
            self.phonebook = Table(
                'phonebook', self.meta,
                Column('Id',Integer,primary_key=True),
                Column('contact_name',String),
                Column('contact_number',String)
            )
            self.meta.create_all(self.engine)

            #Insert init data
            ins = self.phonebook.insert()
            data = {'contact_name': data['contact list'][0][0], 'contact_number':data['contact list'][0][1]}
            self.conn.execute(ins, data) 
          
            return (True, 'Created')

        except(Exception) as err:
            print(err)
            return (False, 'Error')
            
        finally:
            self.conn.close()
            print("SQLite DB closed")

    def read(self, location: str):
        """ reads a file,returns a tuple - (boolean, string, and the dictionary containing the read data)"""
        data, data_dict = [], {}
        try: 
            if location is None:
                raise Exception()           
            sql = "SELECT * FROM phonebook"
            result = self.conn.execute(sql)

            for row in result:
                data.append(row)

            data_dict["contact list"] = data
            return (True, 'Read Success', data_dict)   

        except(Exception) as err:
            print(err)
            return (False, 'Error', {})
            
        finally:
            self.conn.close()
            print("SQLite DB closed")

    def update(self, location: str, data: dict):
        """updates a table in location, returns a boolean, string tuple."""
        try:
            # Update a table with a given value 
            sql = """UPDATE phonebook
                    SET contact_number=?
                    WHERE contact_name = ?"""
            self.conn.execute(sql, data['contact'])
            # self.conn.execute(s).fetchall()
            return (True, "Updated")

        except(Exception) as err:
            print(err)
            return (False, 'Error')
            
        finally:
            self.conn.close()
            print("SQLite DB closed")

    def delete(self, location: str, data: dict):
        """Perform the delete operation in a given file, returns a boolean, string tuple"""
        try:
            sql = "DELETE FROM phonebook WHERE contact_name = ?"
            self.conn.execute(sql, data['contact'])
            return (True, "Deleted")

        except(Exception) as err:
            print(err)
            return (False, 'Error')
            
        finally:
            self.conn.close()
            print("SQLite DB closed")   


 