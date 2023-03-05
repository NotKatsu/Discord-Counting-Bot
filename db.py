import sqlite3 

def createDatabase(databaseName: str) -> object: 
    connection = sqlite3.connect(databaseName)
    return connection

def tableSetup(connectionObject: object) -> bool: 
    print(connectionObject)

def databaseSetup(databaseName: str) -> bool: 
    try:
        connection = createDatabase(databaseName)
        if tableSetup(connection) == False: 
            return False 
        else:
            return True
    except:
        return False
    
