import sqlite3 

def createConnection(databaseName: str) -> object: 
    connection = sqlite3.connect(databaseName)
    return connection

def tableSetup(connectionObject: object) -> bool: 
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
    try:
        connection = createConnection(databaseName)
        if tableSetup(connection) == False: 
            return False 
        else:
            return True
    except:
        return False
    
def addChannel(channel: object) -> bool: 
    connection = createConnection("database.db") 
    cursor = connection.cursor() 

    response = cursor.execute("SELECT channel FROM countingChannels WHERE guild = ?", (channel.guild.id,))

    if response.fetchone() is None: 
        cursor.execute("INSERT INTO countingChannels (guild, channel) VALUES (?, ?)", (channel.guild.id, channel.id))
        connection.commit()
    else:
        cursor.execute("UPDATE countingChannels SET channel = ? WHERE guild = ?", (channel.id, channel.guild.id))
        connection.commit()
    

    
