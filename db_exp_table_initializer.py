import sqlite3

try:

	db_name = 'arsalan_site_db.db'
	environment = 'dev'
	if environment == 'prod':
		# Create a cursor [Production]
		db_connection_string = '/home/arsalananwar/Arsalan-Portfolio/' + db_name
	elif environment == 'dev':
		# Create a cursor [Dev]
		db_connection_string = db_name
	
	sqliteConnection = sqlite3.connect(db_connection_string)
	cursor = sqliteConnection.cursor()
	print('[SUCCESS] DB Initialized')

	# Write a query and execute it with cursor
	query = 'DROP TABLE EXPERIENCE'
	cursor.execute(query)
	print('[SUCCESS] Query executed')
	
	query = """CREATE TABLE EXPERIENCE (ExperienceId int PRIMARY KEY, Designation varchar(80), Organization varchar(100), StartDate varchar(25), EndDate varchar(25) DEFAULT "Present", WorkType varchar(20), Description text DEFAULT "No description provided", Priority int, OrgImage varchar(50))"""
	cursor.execute(query)
	print('[SUCCESS] Query executed')

	query = """INSERT INTO EXPERIENCE VALUES (1, 'Data Scientist', 'Course5 Intelligence', 'Feb 2023', 'Present', 'Full-time', 'No description provided', 1, 'course5i.jpg');"""
	cursor.execute(query)

	query = """INSERT INTO EXPERIENCE (ExperienceId, Designation, Organization, StartDate, EndDate, WorkType, Priority, OrgImage) VALUES (2, 'Adjunct Faculty', 'Intellipaat', 'Jan 2023', 'Present', 'Part-time', 2, 'intellipaat.jpg');"""
	cursor.execute(query)

	query = """INSERT INTO EXPERIENCE (ExperienceId, Designation, Organization, StartDate, EndDate, WorkType, Priority, OrgImage) VALUES (3, 'Data Scientist', 'West Pharmaceutical Services', 'Aug 2022', 'Feb 2023', 'Full-time', 3, 'westpharma.jpg');"""
	cursor.execute(query)
	
	query = """INSERT INTO EXPERIENCE (ExperienceId, Designation, Organization, StartDate, EndDate, WorkType, Priority, OrgImage) VALUES (4, 'Associate Data Scientist', 'West Pharmaceutical Services', 'Jul 2020', 'Jul 2022', 'Full-time', 4, 'westpharma.jpg');"""
	cursor.execute(query)
	
	query = """INSERT INTO EXPERIENCE (ExperienceId, Designation, Organization, StartDate, EndDate, WorkType, Priority, OrgImage) VALUES (5, 'Graduate Software Trainee', 'West Pharmaceutical Services', 'Jan 2020', 'Jun 2020', 'Full-time', 5, 'westpharma.jpg');"""
	cursor.execute(query)
	
	print('[SUCCESS] Query executed')

	sqliteConnection.commit()
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
