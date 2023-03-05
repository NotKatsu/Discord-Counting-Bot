import sqlite3 

def createConnection(databaseName: str) -> object: 
    connection = sqlite3.connect(databaseName)
    return connection

def tableSetup(connectionObject: object) -> bool: 
    cursor = connectionObject.cursor() 
    cursor.execute("""CREATE TABLE IF NOT EXISTS countingChannels (
                        guild BIGINT,
                        channel BIGINT
    )""")

def databaseSetup(databaseName: str) -> bool: 
    try:
        connection = createConnection(databaseName)
        if tableSetup(connection) == False: 
            return False 
        else:
            return True
    except:
        return False
    
def addChannel(channel: int) -> bool: 
    print(channel)
    

    
