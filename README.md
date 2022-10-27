# PhoneBook CLI (Interfaces)

## Description
A PhoneBook CLI.  

## Concepts applied
- Interfaces
- Dependency Injection
- Singleton pattern

## Adding Providers
add commandline argument for the new provider in the tests file
Make sure the test_databases.py tests even when unchanged pass for your newly added providers' logic

## Tests
pip install coverage<br>
Run tests for each provider in this format:<br/>
<code>
coverage run tests\test_databases.py postgres
</code>
<br/>
where "postgres" is one of:
- postgres
- mongoDB
- firestore
- sqlite
- filesystem

### Getting coverage
use -a to append individual tests<br/>
<code>
coverage run tests\test_databases.py filesystem && coverage run -a tests\test_databases.py sqlite && coverage run -a tests\test_databases.py postgres && coverage run -a tests\test_databases.py mongoDB && coverage run -a tests\test_databases.py firestore
</code><br/>
then
<code>coverage report</code>


## Environment files
Add these files in the /providers folder before running.
### dbconfig.ini for postgres
    [postgresql]
    host=****
    database=****
    port=5432
    user=user
    password=****

### .env for mongo
    MONGO_URI=****

### The service account json for firestore
    {}












