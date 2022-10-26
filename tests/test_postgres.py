import unittest, sys, os

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,path)
from phoneBook import PhoneBook
from providers.file_system_provider import FileStoreProvider
from providers.sqlite_provider import SQLiteProvider
from providers.postgres_provider import PostgresDBProvider
from providers.mongo_provider import MongoDBProvider

class PhoneBookAllTests(unittest.TestCase):
    """Unit tests. Since dependency change should not fail the system, this class' tests are applicable to all supported
    db types: FileSystem, SQLAlchemy, PostgresSQL, MongoDB, Firestore. 
    No need for test modules for each.
    Run tests when one is chosen by the phonebook"""

    db_name = None
    def getDatabaseService(self, db_name):
        """choose database service"""
        if db_name == "filesystem":
            self.provider = FileStoreProvider()
            self.location = path + '\databases\PhoneBookFileSystemDb\contacts.txt'
        elif db_name == "sqlite":
            self.provider = SQLiteProvider()
            self.location = 'sqlite:///databases/shop.db'
        elif db_name == "postgres":
            self.provider = PostgresDBProvider()
            self.location = ''
        elif db_name == "mongoDB":
            self.provider = MongoDBProvider()
            self.location = ''
        
    def test_setup_system(self):
        self.getDatabaseService(self.db_name)
        phoneBook = PhoneBook(location= self.location, db_provider=self.provider)
        returned = phoneBook.setupSystem() 
        expected = (True, 'Connection Successful')
        self.assertEqual(returned, expected, f"Check {self.db_name} connect test")

    def test_create_contact(self):
        self.getDatabaseService(self.db_name)
        phoneBook = PhoneBook(location= self.location, db_provider=self.provider)
        data = {
            "contact list":[
        ('Mark',"+256751079239"),
    ]}
        returned = phoneBook.createContact(data)        
        expected = (True, 'Contact created successfully')
        self.assertEqual(returned, expected, f"Check {self.db_name} create test")

    # def test_list_contacts(self):
    #     self.getDatabaseService(self.db_name)
    #     phoneBook = PhoneBook(location= self.location, db_provider=self.provider)
    #     returned = phoneBook.listContacts()
    #     self.assertIn(True, returned, f"Check {self.db_name} list all test")

    # def test_edit_contact(self):
    #     self.getDatabaseService(self.db_name)
    #     phoneBook = PhoneBook(location= self.location, db_provider=self.provider)
    #     data = {
    #         "contact":("+0000000000","Mark")
    #     }
    #     returned = phoneBook.editContact(data)
    #     expected = (True, "Contact updated successfully")
    #     self.assertEqual(returned, expected, f"Check {self.db_name} editContact test")
    
    # def test_delete_contact(self):
    #     self.getDatabaseService(self.db_name)
    #     phoneBook = PhoneBook(location= self.location, db_provider=self.provider)
    #     data = {
    #         "contact":("Mark",)
    #     }
    #     returned = phoneBook.deleteContact(data)
    #     expected = (True, "Contact deleted successfully")
    #     self.assertEqual(returned, expected, "Check MongoDB deleteContact test")

    def test_close_phonebook(self):
        self.getDatabaseService(self.db_name)
        phoneBook = PhoneBook(location= self.location, db_provider=self.provider)
        returned = phoneBook.closePhonebook()
        expected = 'Phonebook Closed'
        self.assertEqual(returned, expected, f"Check {self.db_name} disconnect test")

    # def test_fail_create(self):
    #     self.getDatabaseService(self.db_name)
    #     phoneBook = PhoneBook(location= self.location, db_provider=self.provider)
    #     data = {
    #         "contact lis":[
    #             (10,10)
    # ]}
    #     returned = phoneBook.createContact(data)        
    #     expected = (False, "Failed to create contact Error")
    #     self.assertEqual(returned, expected, f"Check {self.db_name} fail create test")

    # def test_fail_list_contacts(self):
    #     db_service=self.db_service('postgres')
    #     output = db_service.listContacts()
    #     expected = (False, 'failed to read contact', "")
    #     assert output, expected

#     def test_fail_edit_contact(self):
#         db_service=self.db_service('postgres')
#         contact = {'Name':'Mark T', 'Phone':'0786531980'}
#         output = db_service.editContact(contact)
#         reason = "failed to update contact"
#         expected = (False, reason)
#         assert output, expected

#     def test_sql_create_contact(self):
#         db_service = self.db_service('sqlitedatabase')
#         contact = {'contacts': [
#     {'Name':'Mark T', 'Phone':'0751079239'},
# ]}
#         returned = db_service.createContact(contact)
#         expected = (True, 'Contact created successfully')
#         assert returned, expected

#     def test_sql_fail_create(self):
#         db_service=self.db_service('sqlitedatabase')
#         contact = {'contacts': [
#     {'Name':'Mark T', 'Phone':0},
# ]}

#         db_service.createContact(contact)
#         output = db_service.createContact(contact)
#         reason = "failed to create contact"
#         expected = (False, reason)
#         assert output, expected


#     def test_sql_list_contacts(self):
#         db_service=self.db_service('sqlitedatabase')
#         output = db_service.listContacts()
#         expected = (True, 'Contact read successfully', "")
#         assert output, expected

#     def test_sql_fail_list_contacts(self):
#         db_service=self.db_service('sqlitedatabase')
#         self.location = ''
#         output = db_service.listContacts()
#         expected = (False, 'failed to read contact', "")
#         assert output, expected


#     def test_sql_edit_contact(self):
#         db_service=self.db_service('sqlitedatabase')
#         contact = {'Name':'Mark T', 'Phone':'0786531980'}
#         output = db_service.editContact(contact)
#         expected = (True, 'Contact updated successfully')
#         assert output, expected

#     def test_sql_fail_edit_contact(self):
#         db_service=self.db_service('sqlitedatabase')
#         self.location = ''
#         contact = {'Name':'Mark T', 'Phone':'0786531980'}
#         output = db_service.editContact(contact)
#         reason = "failed to update contact"
#         expected = (False, reason)
#         assert output, expected


#     def test_sql_delete_contact(self):
#         db_service = self.db_service('sqlitedatabase')
#         contact = {'Name':'Mark T', 'Phone':'0786531980'}
#         output = db_service.deleteContact(5)
#         expected = (True, 'Contact deleted successfully')
#         assert output, expected
#         db_service.closePhonebook()

#     def test_instance(self):
#         instance = Database.get_instance(provider=FileStoreProvider())
#         assert type(instance) == Database

if __name__=='__main__':
    if len(sys.argv) > 1:
        PhoneBookAllTests.db_name = sys.argv.pop()

    if (PhoneBookAllTests.db_name == 'postgres'
     or PhoneBookAllTests.db_name == 'mongoDB' 
     or PhoneBookAllTests.db_name == 'filesystem'):
        unittest.main()

    else:
        print('Provide an expected dependency argument. Choose 1 of the supported dbs:\n1. "postgres"\n2. "mongoDB"\n3. "firestore"\n4. "sqlite"\n5. "filesystem"')
