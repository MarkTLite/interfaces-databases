import unittest, sys, os

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,path)

from firebase_admin import credentials, initialize_app
from phoneBook import PhoneBook
from providers.file_system_provider import FileStoreProvider
from providers.sqlite_provider import SQLiteProvider
from providers.postgres_provider import PostgresDBProvider
from providers.mongo_provider import MongoDBProvider
from providers.firestore_provider import FireStoreProvider

class PhoneBookAllTests(unittest.TestCase):
    """Unit tests. Since dependency change should not fail the system, this class' tests are applicable to all supported
    db types: FileSystem, SQLAlchemy, PostgresSQL, MongoDB, Firestore. 
    No need for test modules for each.
    Run tests when one dependency choice is given by cli argument to the phonebook"""

    db_name = None
    def getDatabaseService(self, db_name):
        """choose database service"""
        if db_name == "filesystem":
            self.provider = FileStoreProvider()
            self.location = path + '\databases\PhoneBookFileSystemDb\contacts.json'
        elif db_name == "sqlite":
            self.location = 'sqlite:///databases/shop.db'
            self.provider = SQLiteProvider(self.location)            
        elif db_name == "postgres":
            self.provider = PostgresDBProvider()
            self.location = ''
        elif db_name == "mongoDB":
            self.provider = MongoDBProvider()
            self.location = ''
        elif db_name == "firestore":
            self.provider = FireStoreProvider()
            self.location = 'phonebook' # the phonebook collection on firestore
        
    def test_0_setup_system(self):
        self.getDatabaseService(self.db_name)
        phoneBook = PhoneBook(location= self.location, db_provider=self.provider)
        returned = phoneBook.setupSystem() 
        expected = (True, 'Connection Successful')
        self.assertEqual(returned, expected, f"Check {self.db_name} connect test")

    def test_1_create_contact(self):
        self.getDatabaseService(self.db_name)
        phoneBook = PhoneBook(location= self.location, db_provider=self.provider)
        data = {
            "contact list":[
        ('Mark@gmail.com',"+256751079239"), 
        ('John@gmail.com',"+254751079239"),          
    ]}
        returned = phoneBook.createContact(data)        
        expected = (True, 'Contact created successfully')
        self.assertEqual(returned, expected, f"Check {self.db_name} create test")

    def test_2_list_contacts(self):
        self.getDatabaseService(self.db_name)
        phoneBook = PhoneBook(location= self.location, db_provider=self.provider)
        returned = phoneBook.listContacts()
        self.assertIn(True, returned, f"Check {self.db_name} list all test")

    def test_3_edit_contact(self):
        self.getDatabaseService(self.db_name)
        phoneBook = PhoneBook(location= self.location, db_provider=self.provider)
        data = {
            "contact":("+0000000000","Mark@gmail.com")
        }
        returned = phoneBook.editContact(data)
        expected = (True, "Contact updated successfully")
        self.assertEqual(returned, expected, f"Check {self.db_name} editContact test")
    
    def test_4_delete_contact(self):
        self.getDatabaseService(self.db_name)
        phoneBook = PhoneBook(location= self.location, db_provider=self.provider)
        data = {
            "contact":("Mark@gmail.com",)
        }
        returned = phoneBook.deleteContact(data)
        expected = (True, "Contact deleted successfully")
        self.assertEqual(returned, expected, f"Check {self.db_name} deleteContact test")

    def test_5_fail_create_contact(self):
        self.getDatabaseService(self.db_name)
        phoneBook = PhoneBook(location= self.location, db_provider=self.provider)
        data = None
        returned = phoneBook.createContact(data)        
        expected = (False, "Failed to create contact Error")
        self.assertEqual(returned, expected, f"Check {self.db_name} create fail test")

    def test_6_fail_list_contacts(self):
        self.getDatabaseService(self.db_name)
        phoneBook = PhoneBook(location= None, db_provider=self.provider)
        returned = phoneBook.listContacts()
        self.assertIn(False, returned, f"Check {self.db_name} list all fail test")

    def test_7_fail_edit_contact(self):
        self.getDatabaseService(self.db_name)
        phoneBook = PhoneBook(location= self.location, db_provider=self.provider)
        data = None
        returned = phoneBook.editContact(data)
        expected = (False, "failed to update contact Error")
        self.assertEqual(returned, expected, f"Check {self.db_name} editContact fail test")
    
    def test_8_fail_delete_contact(self):
        self.getDatabaseService(self.db_name)
        phoneBook = PhoneBook(location= self.location, db_provider=self.provider)
        data = None
        returned = phoneBook.deleteContact(data)
        expected = (False, "failed to delete contact Error")
        self.assertEqual(returned, expected, f"Check {self.db_name} deleteContact fail test")

    def test_9_close_phonebook(self):
        self.getDatabaseService(self.db_name)
        phoneBook = PhoneBook(location= self.location, db_provider=self.provider)
        returned = phoneBook.closePhonebook()
        expected = 'Phonebook Closed'
        self.assertEqual(returned, expected, f"Check {self.db_name} disconnect test")

if __name__=='__main__':
    if len(sys.argv) > 1:
        PhoneBookAllTests.db_name = sys.argv.pop()

    if (PhoneBookAllTests.db_name == 'postgres'     
     or PhoneBookAllTests.db_name == 'sqlite'
     or PhoneBookAllTests.db_name == 'mongoDB'
     or PhoneBookAllTests.db_name == 'filesystem'):
        unittest.main()
    
    if (PhoneBookAllTests.db_name == 'firestore'):
        path2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        cred = credentials.Certificate(path2 + "\providers\interfaces-prac-firebase.json")   
        fireapp = initialize_app(credential=cred) 
        unittest.main()
        fireapp._cleanup()

    else:
        print('Provide an expected dependency argument. Choose 1 of the supported dbs:\n1. postgres\n2. mongoDB\n3. firestore\n4. sqlite\n5. filesystem')
