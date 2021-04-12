import csv, smtplib, random





def getData(file):
	with open(file, newline="") as csvfile:
		testData = csv.reader(csvfile)
		students = {}
		for row in testData:
			students[row[0]] = row[1:len(row)]
		return students

def generateBody(students):
	bookReport = random.randint(0,len(students)-1)
	studentsKeys = students.keys()
	emails = []
	for key in studentsKeys:
		emails.append(key)
	for email in emails:
		student = students[email]
		body = "Dear {}, Your score for the book assignment is broken down below by question number.\n\n1. {} : {}\n2. {} : {}\n3. {} : {}\n\n".format(
			student[1], student[2], student[3],  student[4], student[5], student[6], student[7])
		if emails[bookReport] == email:
			body += "You've been randomly chosen to present a summary of the book in the next class. Looking forward to it!\n\n"
		body += "Very Respectfully, \n Your Teacher\n"
		send_email(email,body)

def send_email(email, body):
	#Enter your email's server and required port and your email address into the appropriate variables
	mailServer = ""
	port = ""
	myEmail = ""

	#Enter your username and password if required by your server"
	myUsername = ''
	myPassword = ''


	server = smtplib.SMTP_SSL(mailServer, port)
	server.login(myUsername,myPassword)
	server.sendmail(myEmail,	
	email,
	body)
	server.quit()


file = 'exam.csv'
students = {}
students = getData(file)
generateBody(students)
