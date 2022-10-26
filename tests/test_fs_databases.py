# test_databases.py

import unittest
from DbInterfaceSingleton import Database
from providers.file_system_provider import FileStoreProvider
from providers.sqlite_provider import SQLiteProvider
from phoneBook import PhoneBook

class PhoneBookFSTests(unittest.TestCase):
    """Tests for File and SQL usage by the phonebook"""
    def getDatabaseService(self,db_name):
        """choose database service"""
        if db_name == "filesystem":
            self.provider = FileStoreProvider()
            self.location = './databases/PhoneBookFileSystemDb/contacts.txt'
        elif db_name == "sqlitedatabase":
            self.provider = SQLiteProvider()
            self.location = 'sqlite:///databases/shop.db'

    def db_service(self,db_name):
        self.getDatabaseService(db_name)
        phoneBook = PhoneBook(location= self.location, db_provider=self.provider)
        phoneBook.setupSystem()
        return phoneBook

    def test_create_contact(self):
        db_service = self.db_service('filesystem')
        contact = {'contacts': [
    {'Name':'Mark T', 'Phone':'0751079239'},
]}
        returned = db_service.createContact(contact)
        expected = (True, 'Contact created successfully')
        assert returned, expected

    def test_fail_create(self):
        db_service=self.db_service('filesystem')
        self.location = 5
        contact = {'contacts': [
    {'Name':'Mark T', 'Phone':0},
]}
        db_service.createContact(contact)
        output = db_service.createContact(contact)
        reason = "failed to create contact"
        expected = (False, reason)
        assert output, expected


    def test_list_contacts(self):
        db_service=self.db_service('filesystem')
        output = db_service.listContacts()
        expected = (True, 'Contact read successfully', "")
        assert output, expected

    def test_fail_list_contacts(self):
        db_service=self.db_service('filesystem')
        output = db_service.listContacts()
        expected = (False, 'failed to read contact', "")
        assert output, expected


    def test_edit_contact(self):
        db_service=self.db_service('filesystem')
        contact = {'Name':'Mark T', 'Phone':'0786531980'}
        output = db_service.editContact(contact)
        expected = (True, 'Contact updated successfully')
        assert output, expected

    def test_fail_edit_contact(self):
        db_service=self.db_service('filesystem')
        contact = {'Name':'Mark T', 'Phone':'0786531980'}
        output = db_service.editContact(contact)
        reason = "failed to update contact"
        expected = (False, reason)
        assert output, expected


    def test_delete_contact(self):
        db_service = self.db_service('filesystem')
        contact = {'Name':'Mark T', 'Phone':'0786531980'}
        output = db_service.deleteContact(contact)
        expected = (True, 'Contact deleted successfully')
        assert output, expected
        assert db_service.closePhonebook() == "Phonebook Closed"

    def test_sql_create_contact(self):
        db_service = self.db_service('sqlitedatabase')
        contact = {'contacts': [
    {'Name':'Mark T', 'Phone':'0751079239'},
]}
        returned = db_service.createContact(contact)
        expected = (True, 'Contact created successfully')
        assert returned, expected

    def test_sql_fail_create(self):
        db_service=self.db_service('sqlitedatabase')
        contact = {'contacts': [
    {'Name':'Mark T', 'Phone':0},
]}

        db_service.createContact(contact)
        output = db_service.createContact(contact)
        reason = "failed to create contact"
        expected = (False, reason)
        assert output, expected


    def test_sql_list_contacts(self):
        db_service=self.db_service('sqlitedatabase')
        output = db_service.listContacts()
        expected = (True, 'Contact read successfully', "")
        assert output, expected

    def test_sql_fail_list_contacts(self):
        db_service=self.db_service('sqlitedatabase')
        self.location = ''
        output = db_service.listContacts()
        expected = (False, 'failed to read contact', "")
        assert output, expected


    def test_sql_edit_contact(self):
        db_service=self.db_service('sqlitedatabase')
        contact = {'Name':'Mark T', 'Phone':'0786531980'}
        output = db_service.editContact(contact)
        expected = (True, 'Contact updated successfully')
        assert output, expected

    def test_sql_fail_edit_contact(self):
        db_service=self.db_service('sqlitedatabase')
        self.location = ''
        contact = {'Name':'Mark T', 'Phone':'0786531980'}
        output = db_service.editContact(contact)
        reason = "failed to update contact"
        expected = (False, reason)
        assert output, expected


    def test_sql_delete_contact(self):
        db_service = self.db_service('sqlitedatabase')
        contact = {'Name':'Mark T', 'Phone':'0786531980'}
        output = db_service.deleteContact(5)
        expected = (True, 'Contact deleted successfully')
        assert output, expected
        db_service.closePhonebook()

    def test_instance(self):
        instance = Database.get_instance(provider=FileStoreProvider())
        assert type(instance) == Database

if __name__=='__main__':     
    unittest.main()
