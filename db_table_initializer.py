import sqlite3

try:

	# Connect to DB and create a cursor
	sqliteConnection = sqlite3.connect('arsalan_site_db.db')
	cursor = sqliteConnection.cursor()
	print('[SUCCESS] DB Initialized')

	# Write a query and execute it with cursor
	query = 'CREATE TABLE MESSAGES (Email varchar(100), Name varchar (100), Subject text, Message text)'
	cursor.execute(query)

	print('[SUCCESS] Messages Table Created')

	# Close the cursor
	cursor.close()

# Handle errors
except sqlite3.Error as error:
	print('[ERROR] Error occurred - ', error)

# Close DB Connection irrespective of success or failure
finally:
	if sqliteConnection:
		sqliteConnection.close()
		print('[SUCCESS] SQLite Connection Closed')
