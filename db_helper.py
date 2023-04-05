import sqlite3

class DatabaseActions:
    def __init__(self, db_name) -> None:
        # Connect to DB and create a cursor [Production]
        db_connection_string = '/home/arsalananwar/Arsalan-Portfolio/' + db_name
        self.sqliteConnection = sqlite3.connect(db_connection_string)

        # Connect to DB and create a cursor [Local]
        # self.sqliteConnection = sqlite3.connect(db_name)
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

        # Close DB Connection irrespective of success or failure
        finally:
            if self.sqliteConnection:
                self.sqliteConnection.close()
                print('[SUCCESS] SQLite Connection Closed')