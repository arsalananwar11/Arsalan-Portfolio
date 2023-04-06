import sqlite3

class DatabaseActions:
    def __init__(self, db_name) -> None:
        # Create a cursor [Production]
        db_connection_string = '/home/arsalananwar/Arsalan-Portfolio/' + db_name

        # Create a cursor [Local]
        # db_connection_string = db_name

        # Connect to DB
        self.sqliteConnection = sqlite3.connect(db_connection_string)
        print('[SUCCESS] DB Initialized')
    
    def add_message(self, requestor_message ):
        try:
            self.connection_obj = self.sqliteConnection.cursor()
            query = f"""INSERT INTO MESSAGES (EMAIL, NAME, SUBJECT, MESSAGE) VALUES (?,?,?,?)"""
            self.connection_obj.execute(query, requestor_message)
            
            self.sqliteConnection.commit()
            print(f"[SUCCESS] Message with the following details added:\nEmail: { requestor_message[0] }\nName: { requestor_message[1] }\nSubject: { requestor_message[2] }\nMessage: { requestor_message[3] }")
            self.connection_obj.close()

        # Handle errors
        except sqlite3.Error as error:
            print('[ERROR] Error occurred while adding the message- ', error)
            print(f"[ERROR] Message details:\nEmail: { requestor_message[0] }\nName: { requestor_message[1] }\nSubject: { requestor_message[2] }\nMessage: { requestor_message[3] }")

    def fetch_all_projects(self):
        try:
            self.connection_obj = self.sqliteConnection.cursor()
            query = """SELECT * FROM PROJECTS"""
            self.connection_obj.execute(query)
            
            all_projects = self.connection_obj.fetchall()
            all_projects_list = []
            for project in all_projects:
                all_projects_list.append(project)

            self.sqliteConnection.commit()
            print(f"[SUCCESS] All projects successfully fetched")
            self.connection_obj.close()

            return all_projects_list

        # Handle errors
        except sqlite3.Error as error:
            print('[ERROR] Error occurred while fetching all the projects - ', error)

    def fetch_featured_projects(self):
        try:
            self.connection_obj = self.sqliteConnection.cursor()
            query = """SELECT * FROM PROJECTS WHERE FEATUREDPROJECT = 1 LIMIT 4"""
            self.connection_obj.execute(query)
            
            featured_projects = self.connection_obj.fetchall()
            featured_projects_list = []
            for project in featured_projects:
                featured_projects_list.append(project)

            self.sqliteConnection.commit()
            print(f"[SUCCESS] Featured projects successfully fetched")
            self.connection_obj.close()
            return featured_projects_list

        # Handle errors
        except sqlite3.Error as error:
            print('[ERROR] Error occurred while fetching the featured projects - ', error)

    def close_db_connection(self):
        # Close DB Connection irrespective of success or failure
        if self.sqliteConnection:
            self.sqliteConnection.close()
            print('[SUCCESS] SQLite Connection Closed')