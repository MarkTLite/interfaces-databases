from database_interface import DatabaseInterface
from firebase_admin import firestore

class FireStoreProvider(DatabaseInterface):
    """Implements the [DatabaseInterface] methods to persist data on a firestore database."""
    def __init__(self):
        self.db = None

    def connect(self):
        try:        
            self.db = firestore.Client(project='interfaces-prac')
            print('Connected to firestore successfully')
        except(Exception) as err:
            print(f'Error: {err}')

    def create(self, data: dict, collection_name:str, doc_id):
        try:
            doc_ref = self.db.collection(collection_name).document(f'{doc_id}')
            doc_ref.set(data)
        except(Exception) as err:
            print(f'Error: {err}')
   
    def read(self, collection_name:str, doc_id):
        try:
            doc_ref = self.db.collection(collection_name).document(f'{doc_id}')
            doc = doc_ref.get()
            if doc.exists:
                print(f'Document data: {doc.to_dict()}')
            else:
                print(u'No such document!')
            pass
        except(Exception) as err:
            print(f'Error: {err}')

    def update(self, data: dict, collection_name: str, doc_id):
        doc_ref = self.db.collection(collection_name).document(f'{doc_id}')
        doc_ref.update(data)

    def delete(self, collection_name: str, doc_id):
        doc_ref = self.db.collection(collection_name).document(f'{doc_id}')
        doc_ref.delete()

    def disconnect(self):
        self.db.close()