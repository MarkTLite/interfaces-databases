from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine

from DbInterfaceSingleton import DatabaseInterface


class SQLiteProvider(DatabaseInterface):
    """An sqlite provider that implements the [DatabaseInterface] methods to persist data 
        on an sqlite actual database."""
    def __init__(self):
        self.meta = MetaData()

    def connect(self):
        pass
    
    def disconnect(self):
        pass
        
    def create(self, location: str, data: dict):
        """creates an sqlite db in the given file location and a table.
         Returns a Tuple with a boolean and a string."""
        try:
            self.engine = create_engine(location)

            self.products = Table(
                'products', self.meta,
                Column('Id',Integer,primary_key=True),
                Column('Name',String),
                Column('Quantity',Integer)
            )
            self.meta.create_all(self.engine)

            #Insert init data
            ins = self.products.insert()
            self.conn = self.engine.connect()
            self.conn.execute(ins, data['products'])   

        except(Exception):
            return (False, f'Error: {Exception}')

        finally:
            return (True, 'Record created')

    def read(self, location: str):
        """ reads a file,returns a tuple - (boolean, string, and the dictionary containing the read data)"""
        data, data_dict = [], {}
        try:
            s = self.products.select()
            result = self.conn.execute(s)

            for row in result:
                data.append(row)

            data_dict["products"] = data   

        except(Exception):
            return (False, f'Error: {Exception}')
            
        finally:
            return (True, 'Read Success', data_dict)

    def update(self, location: str, data: dict):
        """updates a table in location, returns a boolean, string tuple."""
        try:
            # Update a table with a given value 
            stmt= self.products.update().where(self.products.c.Name==data['Name']).values(Quantity=data['Quantity'])
            s = self.products.select()
            self.conn.execute(stmt)
            self.conn.execute(s).fetchall()

        except(Exception):
            return (False, f'Error: {Exception}')

        finally:
            return (True, 'Record updated')

    def delete(self, location: str, data: dict):
        """Perform the delete operation in a given file, returns a boolean, string tuple"""
        try:
            stmt = self.products.delete() #.where(self.products.c.Name==data['Name'])
            self.conn.execute(stmt)

        except(Exception):
            return (False, f'Error: {Exception}')

        finally:
            return (True, 'Table deleted')    


 