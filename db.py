import sqlite3 

from typing import Union

def createConnection(databaseName: str) -> object: 
    connection = sqlite3.connect(databaseName)
    return connection

def tableSetup(connectionObject: object) -> bool: 
    try:
        cursor = connectionObject.cursor() 
        cursor.execute("""CREATE TABLE IF NOT EXISTS countingChannels (
                            guild BIGINT,
                            channel BIGINT,
                            count BIGINT
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
    try:
        connection = createConnection("database.db") 
        cursor = connection.cursor() 

        response = cursor.execute("SELECT channel FROM countingChannels WHERE guild = ?", (channel.guild.id,))

        if response.fetchone() is None: 
            cursor.execute("INSERT INTO countingChannels (guild, channel, count) VALUES (?, ?, ?)", (channel.guild.id, channel.id, 0))
            connection.commit()
        else:
            cursor.execute("DELETE FROM countingChannels WHERE guild = ?", (channel.guild.id,))
            cursor.execute("INSERT INTO countingChannels (guild, channel, count) VALUES (?, ?, ?)", (channel.guild.id, channel.id, 0))
            connection.commit()
            
        return True
    except Exception as e:
        print(e) 
        return False
    
def getChannel(message: object) -> Union[int, str]: 
    try:
        connection = createConnection("database.db")
        cursor = connection.cursor() 

        cursor.execute("SELECT channel, count FROM countingChannels WHERE guild = ?", (message.guild.id,))

        return cursor.fetchone()[0]
    except Exception as e: 
        print(e);return "error"

def getCount(message: object) -> Union[int, str]: 
    try:
        connection = createConnection("database.db")
        cursor = connection.cursor() 

        cursor.execute("SELECT channel, count FROM countingChannels WHERE guild = ?", (message.guild.id,))

        return cursor.fetchone()[1]
    except Exception as e: 
        print(e);return "error"

def updateCount(message: object, count: int) -> Union[int, str]: 
    connection = createConnection("database.db")
    cursor = connection.cursor() 

    cursor.execute("UPDATE countingChannels SET count = ? WHERE guild = ?", (count, message.guild.id))
    connection.commit()

    
def addToCount(message: object, botid) -> int:
    if message.author.id == botid:
        return
    else:
        currentCount = getCount(message)
        countnewValue = currentCount + 1
        countingChannel = getChannel(message)

        if currentCount == "error" or countingChannel == "error":
            return
        
        elif countingChannel == message.channel.id: 
            if message.content.isnumeric() is True: 
                if int(countnewValue) == int(message.content): 
                    updateCount(message, countnewValue)
                else:
                    return 5
            else: 
                return 0
            