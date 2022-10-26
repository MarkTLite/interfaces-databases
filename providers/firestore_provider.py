from database_interface import DatabaseInterface
from firebase_admin import firestore


class FireStoreProvider(DatabaseInterface):
    """Implements the [DatabaseInterface] methods to persist data on a firestore database."""
    def __init__(self):   
        self.connect()

    def connect(self):
        try:        
            print('Connecting to firestore db')
            self.db = firestore.Client(project='interfaces-prac')
            print('Connected to firestore successfully')
            return (True, "Connection Successful")

        except(Exception) as err:
            print(f'Error: {err}')
            return (False, "Error")

    def create(self, location: str, data: dict):
        try:
            doc_id = data['contact list'][0][0]
            doc_ref = self.db.collection(location).document(f'{doc_id}')
            doc_ref.set({
                'contact_name': doc_id,
                'contact_number': data['contact list'][0][1]
                })            
            return (True, "Created")

        except(Exception) as err:
            print(f'Error: {err}')
            return (False, "Error")
   
    def read(self, location:str):
        try:
            docs = self.db.collection(location).stream()
            data = {'list':[]}   
            for doc in docs:
                data['list'].append(doc.to_dict())                      

            return (True, "Read Successful", data)          

        except(Exception) as err:
            print(f'Error: {err}')
            return (False, "Error", {})

    def update(self, location: str, data: dict):
        doc_id = data['contact'][1]
        doc_ref = self.db.collection(location).document(f'{doc_id}')
        doc_ref.update({
                'contact_name': doc_id,
                'contact_number': data['contact'][0]
                })
        return (True, "Updated Succesfully")

    def delete(self, location: str, data: dict):
        doc_id = data['contact'][0]
        doc_ref = self.db.collection(location).document(f'{doc_id}')
        doc_ref.delete()

        return (True, "Updated Succesfully")

    def disconnect(self):
        return (True, "Disconnected")
        