import os
import mongoengine as db_engine

from database_interface import DatabaseInterface
from dotenv import load_dotenv

class Phonebook(db_engine.Document):
    """Create a phonebook document collection"""

    book_id = db_engine.IntField()
    name = db_engine.StringField()
    author = db_engine.StringField()

    def to_json(self):
        return {
            "book_id": self.book_id,
            "name": self.name,
            "author": self.author
        }

class MongoDBProvider(DatabaseInterface):
    """Implements the [DatabaseInterface] methods to persist data on a mongoDB database."""
    def __init__(self) -> None:
        self.book = None

    def connect(self):
        try:
            load_dotenv()
            print('Connecting Mongo')
            DB_URI = os.getenv('MONGO_URI')
            db_engine.connect(host=DB_URI)
            print('Mongo Db successfully connected')
            return (True, "Connection Successful")

        except(Exception) as err:
            print(f'Error: {err}')
            return (False, "Error")

    def create(self, location: str, data: dict):        
        book = Phonebook(
            book_id = id,
            name = name,
            author = author
        )
        book.save()
        return book

    def read(self,location: str, data: dict):
        book = Phonebook.objects(book_id=id).first()
        return book.to_json()

    def update(self,location: str, data: dict):
        book = Phonebook.objects(book_id=id).first()
        book.update(name="Harry Potter", author="J.K. Rowling")
        return book

    def delete(self,location: str, data: dict):
        book = Phonebook.objects(book_id=id).first()
        print(f'deleting book: {book.to_json()}')
        book.delete()

    def disconnect(self):
        return (True, "Disconnected")


