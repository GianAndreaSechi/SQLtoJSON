# SQL to JSON 

simple python utility to generating a JSON Data from a SQL Query Data retrieved.

You have to insert:

```
# open connection to the database
# driver name:      odbc driver used to connect, you can expand using the "drivers" dictionary on top
# server name:      address of the server istance
# database_name:    the name of the database you want to access
# user_id:          username account that access the database
# password:         password of the account to access the database

connection = openConnection("driver_name","server_name/ip","database_name","user_id","password")
```

You have to insert your query (here is asked to user but you can pass as a parameter from another function).

Getting the JSON Data:
```
JSON_Data = exportToJSON(connection, query)
```

at the end closing the connection to the database
```
#closing opened connection
connection.close()
```

NB: you have to install pyodbc (pip install pyodb) and you have to install the correct odbc driver on your pc/server