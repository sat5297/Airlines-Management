import tkinter as tk
import os
from datetime import datetime

class RatanAirlines():
	def __init__(self,parent=None):
		app = tk.Tk()
		app.geometry('900x900')
		app.title("File Strucure Project")
		heading = tk.Label(app, text = 'Ratan Internationals', font=('aerial 36 bold'))
		heading.place(x=20,y=0)
		buttonSearch = tk.Button(app,text="Search Window",
				command=self.searchwindow)
		buttonBook = tk.Button(app,text="Book Window",
				command=self.bookwindow)
		buttondestroy = tk.Button(app,text="Close Window",
				command=app.destroy)
		buttonSearch.pack(padx=40,pady=80)
		buttonBook.pack(padx=50,pady=100)
		buttondestroy.pack(padx=60,pady=120)
		app.mainloop()
	
	def searchwindow(self):
		SearchClass()
	
	def bookwindow(self):
		BookingClass()

class BookingClass():
	global e1_val,e2_val,e3_val,e4_val,e5_val,e6_val
	global fname,lname,src,dest,gender,date,msg,name,hash_name
	def __init__(self,parent=None):
		global e1_val,e2_val,e3_val,e4_val,e5_val,e6_val
		screen = tk.Toplevel()
		screen.title('Booking Window')
		screen.geometry('700x1000')
		tk.Label(screen, text='First Name').grid(row=5) 
		tk.Label(screen, text='Last Name').grid(row=6) 
		tk.Label(screen, text='Source').grid(row=7) 
		tk.Label(screen, text='Destination').grid(row=8)
		tk.Label(screen, text='Date').grid(row=9) 
		tk.Label(screen, text='Gender').grid(row=10)
		e1_val = tk.StringVar()
		e2_val = tk.StringVar() 
		e3_val = tk.StringVar()
		e4_val = tk.StringVar()
		e5_val = tk.StringVar() 
		e6_val = tk.StringVar()
		e1 = tk.Entry(screen,textvariable=e1_val) 
		e2 = tk.Entry(screen,textvariable=e2_val) 
		e3 = tk.Entry(screen,textvariable=e3_val) 
		e4 = tk.Entry(screen,textvariable=e4_val)
		e5 = tk.Entry(screen,textvariable=e5_val) 
		e6 = tk.Entry(screen,textvariable=e6_val)
		e1.grid(row=5, column=1) 
		e2.grid(row=6, column=1) 
		e3.grid(row=7, column=1) 
		e4.grid(row=8, column=1)
		e5.grid(row=9, column=1) 
		e6.grid(row=10, column=1)
		button = tk.Button(screen, text = 'Book Tickets', bd = '5', command = self.execute_code)
		button2 = tk.Button(screen, text = 'Close Window', bd = '5', command = screen.destroy)
		button.grid(row = 75, column = 2) 
		button2.grid(row = 75, column = 5)
		screen.mainloop()

	def main_prog(self):
		global fname,lname,src,dest,gender,date,msg,name,hash_name
		## call hash function tp get rid of flat name
		hash_name = self.hash1()
		fname = fname.title()
		lname = lname.title()
		src = src.title()
		dest = dest.title()
		f1 = True
		#f1 = validate_date(date)
		f2 = self.flight_search()
		if f1 == False:
			msg = "Invalid Date. Try another date."
			self.newDisplay()
			screen.destroy()
		if f2 == False:
			msg = "No Flight available between these 2 cities."
			self.newDisplay()
			screen.destroy()
		else:
			self.check_seat()

	def validate_date(self):
		print(date)
		print(type(date))
		given_date = datetime.strptime(date,"%d/%m/%Y")
		today = datetime.now().date()
		given = given_date.date()
		print(given)
		print(today)
		print(given <= today)
		return (given >= today)

	def passenger_encrypt(self):
		fh = open('passenger_encrypt.txt','a')
		fh.write(hash_name + "|" + name + "#\n")
		fh.close()

	def passenger_details(self):
		fh = open('passenger_details.txt','a')
		fh.write(name + "|" + hash_name + "|" + gender + "#\n")
		fh.close()

	def flight_search(self):
		global fname,lname,src,dest,gender,date,msg,name
		fh = open('flights_order.txt','r')
		f = 0
		for line in fh.readlines():
			#print(line)
			list1 = line.split()
			if list1[0] == src and list1[1] == dest:
				f = 1
		fh.close()
		return(f%2==1)

	def hash1(self):
		global name
		hashval = 7
		for i in range(len(name)):
			hashval = hashval*31 + ord(name[i])
		return str(hashval)

	def check_seat(self):
		global fname,lname,src,dest,gender,date,msg,name
		max_limit = 4
		f = 0
		file1 = src+dest+date+".txt"
		#print(file1)
		dir_path = os.path.dirname(os.path.realpath(__file__)) 
		for root,dirs,files in os.walk(dir_path):
			for file12 in files:
		#		print(file12)
				if file12 == file1:
		#			print("file present")
					f = 1
		ctr = 0
		if f == 0:
			fh = open(file1,'a+')
			fh.write(name+"|"+src+"|"+dest+"#\n")
			fh.close()
			msg = name + "Booking Confirmed. Please make the payment at the baggage counter."
			self.newDisplay()
			self.passenger_history()
			self.passenger_details()
			self.passenger_encrypt()
		else:
		#	print("Counting")
			fh = open(file1,'r')
			for line in fh.readlines():
		#		print(line)
				ctr += 1
			fh.close()
		#	print("Counter " , ctr)
			if ctr < max_limit:
				fh = open(file1,'a')
				fh.write(name+"|"+src+"|"+dest+"#\n")
				fh.close()
				msg = name + "Booking Confirmed. Please make the payment at the baggage counter."
				self.newDisplay()
				self.passenger_history()
				self.passenger_details()
				self.passenger_encrypt()
			else:
				msg = "No Seat"
				self.newDisplay()

	def indexing(self):
		global fname,lname,src,dest,gender,date,msg,name
		fh = open('indexing.txt','a')
		fh.write(hash_name + "|" + index + "#\n")
		fh.close()

	def passenger_history(self):
		global fname,lname,src,dest,gender,date,msg,name,hash_name
		fh = open('passenger_history.txt','a')
		fh.write(hash_name + "|" + src + "|" + dest + "#\n")
		fh.close()

	def newDisplay(self):
		global msg
		screen1 = tk.Toplevel()
		screen1.geometry('700x700')
		screen1.title("Message Box")
		heading = tk.Label(screen1, text = msg, font=('aerial 10 bold'))
		heading.place(x=20,y=0)
		screen1.after(7000,screen1.destroy)
		screen1.mainloop()

	def execute_code(self):
		global e1_val,e2_val,e3_val,e4_val,e5_val,e6_val
		global fname,lname,src,dest,gender,date,msg,name
		#print("Hey theye")
		fname = str(e1_val.get())
		lname = str(e2_val.get())
		src = str(e3_val.get())
		dest = str(e4_val.get())
		date = str(e5_val.get())
		gender = str(e6_val.get())
		name = fname + lname
		if fname == "" or lname == "" or src == "" or dest == "" or date == "" or gender == "":
			msg = "Data Missing"
			self.newDisplay()
			mainloop()
		else:
			self.main_prog()	

class SearchClass():
	global e1_val,e2_val
	global fname,lname,msg,name,hash_name
	def __init__(self,parent=None):
		global e1_val,e2_val
		screen = tk.Toplevel()
		screen.title('Search Window')
		screen.geometry('700x700')
		tk.Label(screen, text='First Name').grid(row=5) 
		tk.Label(screen, text='Last Name').grid(row=6) 
		e1_val = tk.StringVar()
		e2_val = tk.StringVar() 
		e1 = tk.Entry(screen,textvariable=e1_val) 
		e2 = tk.Entry(screen,textvariable=e2_val) 
		e1.grid(row=5, column=1) 
		e2.grid(row=6, column=1)
		button = tk.Button(screen, text = 'Search User', bd = '5', command = self.execute_code)
		button2 = tk.Button(screen, text = 'Destroy Window', bd = '5', command = screen.destroy)
		button.grid(row = 15, column = 5) 
		button2.grid(row = 25, column = 5)
		screen.mainloop()
	
		#this function will check for a passenger in the flight.
	def search_passenger(self):
		global fname,lname,msg,name,hash_name
		hash_name = self.hash1()
		fh = open('passenger_history.txt','r')
		f = 0
		for line in fh.readlines():
			list1 = line.split('|')
			if list1[0] == hash_name:
				msg = "The user is with us."
				f = 1
		if f == 0:
			msg = "The user never travelled with us."
		self.newDisplay()
	
	def newDisplay(self):
		global msg
		screen1 = tk.Toplevel()
		screen1.geometry('700x700')
		screen1.title("Message Box")
		heading = tk.Label(screen1, text = msg, font=('aerial 10 bold'))
		heading.place(x=20,y=0)
		screen1.after(7000,screen1.destroy)
		screen1.mainloop()
	
	def hash1(self):
		global name
		hashval = 7
		for i in range(len(name)):
			hashval = hashval*31 + ord(name[i])
		return str(hashval)
	
	def execute_code(self):
		global e1_val,e2_val,e3_val,e4_val,e5_val,e6_val
		global fname,lname,msg,name
		#print("Hey theye")
		fname = str(e1_val.get())
		lname = str(e2_val.get())
		name = fname+lname
		if fname == "" or lname == "":
			msg = "Data Missing"
			self.newDisplay()
			mainloop()
		else:
			self.search_passenger()

def start():
	RatanAirlines()	

start()
