

def some():
	import mysql.connector
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="albertbolt23",
  		database="sports2",
  		auth_plugin='mysql_native_password'
  		)

	mycursor = mydb.cursor()

	sql = "SELECT name FROM project_sportsman "

	mycursor.execute(sql)

	sportsman = mycursor.fetchall()

	sportsmanname=[]
	for i in sportsman:
		for j in i:
			sportsmanname.append(j)


	sql = "SELECT name FROM project_competition "
	mycursor.execute(sql)

	competitions = mycursor.fetchall()


	sql = "SELECT DISTINCT event_name FROM project_event"
	mycursor.execute(sql)

	event= mycursor.fetchall()
	eventname=[]

	competitionsname=[]
	for i in competitions:
		for j in i:
			competitionsname.append(j)

	for i in event:
		for j in i:
			eventname.append(j)

	



	a=[sportsmanname,competitionsname,eventname]

	return a

