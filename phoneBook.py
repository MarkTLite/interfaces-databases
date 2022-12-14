"""This Phonebook CLI uses dependency injection to change to a particular database type. System logic must remain applicable 
regardless of the any newly added supported database type in the future"""

from database_interface import DatabaseInterface

class PhoneBook:
    """Class for the Phonebook CLI. 
    - location: is the location of the database"""
    def __init__(self, location: str, db_provider: DatabaseInterface) -> None:
        self.db_provider = db_provider
        self.location = location

    def setupSystem(self) -> None:
        print("Starting up System")
        return self.db_provider.connect()

    def createContact(self, data: dict) -> tuple[bool, str]:
        print("Creating contact")     
        created, reason = self.db_provider.create(self.location, data)
        if not created:
            print(reason)
            reason = "Failed to create contact " + reason
            return (False, reason)

        reason = "Contact created successfully"
        print(reason)
        return (True, reason)

    def listContacts(self) -> tuple[bool, str, dict]:
        print("Viewing all contact information")
        read, reason, output = self.db_provider.read(self.location)
        if not read:
            print(reason)
            reason = "failed to read contact"
            return (False, reason, output)

        reason = "Contact read successfully"
        print(output)
        return (True, reason, output)

    def editContact(self, data: dict) -> tuple[bool, str]:
        print("Updating contact")
        updated, reason = self.db_provider.update(self.location, data)
        print(reason)
        if not updated:
            reason = "failed to update contact " + reason
            print(reason)
            return (False, reason)

        reason = "Contact updated successfully"
        print(reason)
        return (True, reason)

    def deleteContact(self, data:dict) -> tuple[bool, str]:
        print("Deleting contact information")
        deleted, reason = self.db_provider.delete(self.location,data)
        if not deleted:
            reason = "failed to delete contact "+ reason
            print(reason)
            return False, reason

        reason = "Contact deleted successfully"
        print(reason)
        return True, reason

    def closePhonebook(self):
        print("Closing Phonebook")
        self.db_provider.disconnect()
        print("PhoneBook closed")
        return "Phonebook Closed"


# # Instantiate a provider dependency
# provider = FileStoreProvider()
# #provider = SQLiteProvider()

# #Setup Phonebook
# phonebook = PhoneBook(location='./databases/PhoneBookFileSystemDb/contacts.txt', db_provider=provider)
# phonebook.setupSystem()

# # Perform CRUD on some new products data depending on the method of the provider
# #Create
# contact = {'contacts': [
#     {'Name':'Mark T', 'Phone':'0751079239'},
# ]}
# phonebook.createContact(contact)

# #List(uses Read)
# phonebook.createContact(contact)
# phonebook.createContact(contact)
# phonebook.createContact(contact)
# phonebook.listContacts()

# #update by name
# contact = {'Name':'Mark T', 'Phone':'0786531980'}
# phonebook.editContact(contact)

# #delete by name
# phonebook.deleteContact(contact)

# phonebook.closePhonebook()


