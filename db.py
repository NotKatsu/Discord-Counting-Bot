import sqlite3 

def createConnection(databaseName: str) -> object: 
    connection = sqlite3.connect(databaseName)
    return connection

def tableSetup(connectionObject: object) -> bool: 
    print("recieved table creation request")
    try:
        cursor = connectionObject.cursor() 
        cursor.execute("""CREATE TABLE IF NOT EXISTS countingChannels (
                            guild BIGINT,
                            channel BIGINT
        )""")
        return True
    except:
        return False

def databaseSetup(databaseName: str) -> bool: 
    print("recieved request")
    try:
        connection = createConnection(databaseName)
        print("created connection")
        if tableSetup(connection) == False: 
            print("table setup complete")
            return False 
        else:
            return True
    except:
        return False
    
def addChannel(channel: int) -> bool: 
    print(channel)
    

    
