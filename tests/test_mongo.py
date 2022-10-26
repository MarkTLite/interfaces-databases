import unittest, sys, os

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,path)
from providers.mongo_provider import MongoDBProvider
from phoneBook import PhoneBook


class PhoneBookMongoDBTests(unittest.TestCase):
    """Tests for MongoDB usage by the phonebook"""

    def getDatabaseService(self,db_name):
        """choose database service"""
        if db_name == "mongoDB":
            self.provider = MongoDBProvider()
            self.location = ''

    def db_service(self,db_name):
        self.getDatabaseService(db_name)
        phoneBook = PhoneBook(location= self.location, db_provider=self.provider)
        phoneBook.setupSystem()        
        return phoneBook

    def test_setup_system(self):
        self.getDatabaseService('mongoDB')
        phoneBook = PhoneBook(location= self.location, db_provider=self.provider)
        returned = phoneBook.setupSystem() 
        expected = (True, 'Connection Successful')
        self.assertEqual(returned, expected, "Check MongoDB connect test")

    def test_close_phonebook(self):
        self.getDatabaseService('mongoDB')
        phoneBook = PhoneBook(location= self.location, db_provider=self.provider)
        returned = phoneBook.closePhonebook()
        expected = 'Phonebook Closed'
        self.assertEqual(returned, expected, "Check MongoDB disconnect test")

    def test_create_phonebook(self):
        self.getDatabaseService('mongoDB')
        phoneBook = PhoneBook(location= self.location, db_provider=self.provider)
        data = {
            "contact list":[
        ('Mark',"+256751079239"),
        ('Asahi Glass Co Ltd.',"+256751079239"),
        ('Daikin Industries Ltd.',"+256751079239"),
        ('Dynacast International Inc.',"+256751079239"),
        ('Foster Electric Co. Ltd.',"+256751079239"),
        ('Murata Manufacturing Co. Ltd.',"+256751079239")
    ]}
        returned = phoneBook.createContact(data)        
        expected = (True, 'Contact created successfully')
        self.assertEqual(returned, expected, "Check MongoDB create test")

    # def test_fail_create(self):
    #     self.getDatabaseService('mongoDB')
    #     phoneBook = PhoneBook(location= self.location, db_provider=self.provider)
    #     data = {
    #         "contact lis":[
    #             (10,10)
    # ]}
    #     returned = phoneBook.createContact(data)        
    #     expected = (False, "Failed to create contact Error")
    #     self.assertEqual(returned, expected, "Check MongoDB fail create test")


    def test_list_contacts(self):
        self.getDatabaseService('mongoDB')
        phoneBook = PhoneBook(location= self.location, db_provider=self.provider)
        returned = phoneBook.listContacts()
        self.assertIn(True, returned, "Check MongoDB list all test")

    # def test_fail_list_contacts(self):
    #     db_service=self.db_service('mongoDB')
    #     output = db_service.listContacts()
    #     expected = (False, 'failed to read contact', "")
    #     assert output, expected


    def test_edit_contact(self):
        self.getDatabaseService('mongoDB')
        phoneBook = PhoneBook(location= self.location, db_provider=self.provider)
        data = {
            "contact":("+0000000000","Asahi Glass Co Ltd.")
        }
        returned = phoneBook.editContact(data)
        expected = (True, "Contact updated successfully")
        self.assertEqual(returned, expected, "Check MongoDB editContact test")

#     def test_fail_edit_contact(self):
#         db_service=self.db_service('mongoDB')
#         contact = {'Name':'Mark T', 'Phone':'0786531980'}
#         output = db_service.editContact(contact)
#         reason = "failed to update contact"
#         expected = (False, reason)
#         assert output, expected


    def test_delete_contact(self):
        self.getDatabaseService('mongoDB')
        phoneBook = PhoneBook(location= self.location, db_provider=self.provider)
        data = {
            "contact":("Asahi Glass Co Ltd.",)
        }
        returned = phoneBook.deleteContact(data)
        expected = (True, "Contact deleted successfully")
        self.assertEqual(returned, expected, "Check MongoDB deleteContact test")

    def test_shutdown(self):
        self.getDatabaseService('mongoDB')
        phoneBook = PhoneBook(location= self.location, db_provider=self.provider)        
        returned = phoneBook.closePhonebook()
        expected = "Phonebook Closed"
        self.assertEqual(returned, expected, "Check Shut Phonebook test")

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
    unittest.main()
