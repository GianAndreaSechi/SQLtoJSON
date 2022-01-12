from typing import List
import pyodbc

#you need to install odbc driver on your pc for
# mssql server (just installed into windows)
# mariadb (maria db connector per windows)
# mysql (old version)
# each other database you wanna user
drivers = {"sql": "{SQL Server}", "mysql": "{MySQL ODBC 3.51 Driver}", "maria":"{maria}"}

def openConnection(driver, server, database, username=None ,password=None) -> pyodbc:     
    db_driver = drivers[driver]
    # Trusted Connection to Named Instance
    if username is None:
        connection_string = f'DRIVER={db_driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
    elif password is None:
        connection_string = f'DRIVER={db_driver};SERVER={server};DATABASE={database};uid={username};Trusted_Connection=yes;'
    else:
        connection_string = f'DRIVER={db_driver};SERVER={server};DATABASE={database};uid={username};PASSWORD={password};Trusted_Connection=yes;'

    print(connection_string)    
    connection = pyodbc.connect(connection_string)
    return connection
def getSchema(connection, cursor=None, query=None) -> List:
    if query is not None:
        #executing the query
        cursor=connection.cursor()
        cursor.execute(query)

    #get columns name
    columns = [column[0] for column in cursor.description]
    
    #close the cursor in case of different query
    if query is not None:
        cursor.close()

    return columns

def exportToJSON(connection, query):
    #executing the query
    try:
        cursor=connection.cursor()
        cursor.execute(query)

        #getting columns name
        columns = getSchema(connection, cursor)

        #get all data
        data = cursor.fetchall()

        #creating a JSON data list that will contain the query data
        JSON_Data = []
        #for each row in database i will create the json row
        for row in data:
            #dictionary that will copy the database schema
            JSON_row = {}
            #puttin the database data into the json file
            for i in range(len(columns)):
                JSON_row[columns[i]] = row[i]
            JSON_Data.append(JSON_row)        

        cursor.close()

        return JSON_Data
    except:
        print("Error occured during query execution!")
        return dict()
    

    

if __name__ == "__main__":
    # open connection to the database
    # driver name:      odbc driver used to connect, you can expand using the "drivers" dictionary on top
    # server name:      address of the server istance
    # database_name:    the name of the database you want to access
    # user_id:          username account that access the database
    # password:         password of the account to access the database
    connection = openConnection("driver_name","server_name/ip","database_name","user_id","password")

    #defining the query, you can insert whatever you want
    #example SELECT * FROM table_name
    query = input("Insert the query you want to execute: ")

    #get the data from database and export to dictionary JSON like
    JSON_Data = exportToJSON(connection, query)

    #closing opened connection
    connection.close()

    print(JSON_Data)