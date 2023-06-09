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
	#query = 'CREATE TABLE MESSAGES (Email varchar(100), Name varchar (100), Subject text, Message text)'
	query = 'DROP TABLE PROJECTS'
	cursor.execute(query)
	print('[SUCCESS] Query executed')
	
	query = 'CREATE TABLE PROJECTS (ProjectId int PRIMARY KEY, ProjectName text, ProjectBrief text, ProjectDescription text, Category text, ProjectLink text, FeaturedProject bit, ProjectCover text, ProjectSkills text)'
	cursor.execute(query)
	print('[SUCCESS] Query executed')

	query = """INSERT INTO PROJECTS VALUES (1, 'Aqua Analytica: Water Demand Forecast Analytics', 'A Water Consumption Analytics System for Bengaluru using advanced ML techniques such as ARIMA, SARIMA & Holt-Winters for forecasting', 'Project description not provided', 'Time Series Forecasting, Data Analytics', 'https://aquaanalytica.pythonanywhere.com', 1, 'aqua.png', 'Time Series Forecasting, Classical Machine Learning, SQL, Flask');"""
	cursor.execute(query)

	query = """INSERT INTO PROJECTS VALUES (2, 'Autonomous Robot Navigation using RL', 'Trained a Turtlebot3 Waffle Pi to autonomously navigate through the manufacturing plant without collision using DQN algorithm and human intervention data for faster learning', 'Project description not provided', 'Reinforcement Learning, ROS', 'https://github.com/arsalananwar11/Autonomous-Robot-Navigation-Using-DRL', 1, 'ros.jpg', 'Reinforcement Learning, ROS, Gazebo, OpenAI Gym, Turtlebot3 Waffle Pi');"""
	cursor.execute(query)

	query = """INSERT INTO PROJECTS VALUES (3, 'Stopper Defect Detection in Production Line', 'Designed a scalable architecture to identify and classify defects on the elastomer stoppers using XceptionNet model with an accuracy of ~92%', 'Project description not provided', 'Computer Vision, Deep Learning', 'https://github.com/arsalananwar11', 1, 'defectdetection.jpg', 'Deep Learning, OpenCV, Tensorflow, Pytorch, Image Classification, Image Segmentation, Flask, Azure ML, XAI');"""
	cursor.execute(query)

	query = """INSERT INTO PROJECTS VALUES (4, 'Customer Risk Assessment, Analysis and Management', 'Developed a system that identifies high value customers based on CLV who at risk of churning and flags them so that they can be incentivised for retention', 'Project description not provided', 'Churn Analysis, CLV Modeling', 'https://github.com/arsalananwar11', 1, 'cra.jpg', 'Churn Prediction, CLV Modeling, Clustering, Risk Analysis, Factor Analysis');"""
	cursor.execute(query)

	query = """INSERT INTO PROJECTS VALUES (5, 'Mum & Kin Food Services: An E-commerce platform', 'An E-commerce platform that allows people to order delicious and nutritious home-made food by connecting foodies with cooking enthusiasts', 'Project description not provided', 'DBMS, Web Application', 'https://github.com/arsalananwar11', 0, 'mumkinfoods.jpg', 'SQL, DBMS, HTML, CSS, JavaScript, jQuery, PHP');"""
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
