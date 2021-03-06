from tkinter import *
from subprocess import *
from PIL import Image, ImageTk
import sys
import csv
from datetime import datetime
import time
#--------------------------------------------------------------------------------------------------------------
#create the window and add size and title to it
print('Enter your login credentials')
#input('')
window = Tk()
window.geometry("800x500+300+100")
#set size permanently   #or you can use window.resizabld(false, false)
window.minsize(800, 500)
window.maxsize(800, 500)
window.title("Login Page")


def remove(string): 
    pattern = re.compile(r'\s+') 
    return re.sub(pattern, '', string)
#---------------------------------------------------------------------------------------------------------------
#first get the picture then save it in pic and set as background
image = Image.open("blueBG.jpg")
pic = ImageTk.PhotoImage(image)

label0 = Label(image = pic)
label0.pack(fill = BOTH, expand = 'yes')

#------------------------------------------------------------
# -------------------------------------------------
#functions for the buttons to perform
def login():
    users = {'MananMadan': '1000', 'Soumyajit':'230802', 'Rishima': 'rishima', 'MamtaMadan': 'mamta', 'Rajneesh': 'rajneesh','Shefali':'shefali'}
    username = userName.get()
    Pass = password.get()
    username=remove(username)
    if username in users :
        if (users[username] == Pass):
            label5 = Label(window, text = ("Welcome " + username),width = "65",fg="green", font = ("arial", 15, "bold"))
            
            label5.place(x = 5, y = 465)
            #time.sleep(2)
            file = open('Record.csv','a')
            entry = username + "," + str(datetime.now())
            file.write('\n'+entry)
            file.close()
            print('Login Successfull')
            #Popen('python check-individual.py')
            sys.exit()
            
        else:
            label4 = Label(window, text = ("Error: Incorrect Password for " + username),fg="red",width="65", font = ("arial", 15, "bold"))
            label4.place(x = 5, y = 465)

    else:
        label4 = Label(window, text = ("Error: "+username + " does not exist"),fg="red",width="65", font = ("arial", 15, "bold"))
        label4.place(x = 5, y = 465)

#----------------------------------------------------------------------------------------------------------------
#first lable
label1 = Label(window, text = " Login System ", fg = "black", font = ("new times roman", 20, "bold"))
label1.place(x = 300, y = 50)

label2 = Label(window, text = "User Name :", font = ("arial", 16, "bold"))
label2.place(x = 110, y = 150)

userName = StringVar()
textBox1 = Entry(window, textvar = userName, width = 30, font = ("arial", 16, "bold"))
textBox1.place(x = 290, y = 150)

label3 = Label(window, text = "Password :", font = ("arial", 16, "bold"))
label3.place(x = 116, y = 250)

password = StringVar()
textBox2 = Entry(window, textvar = password, width = 30, font = ("arial", 16, "bold"),show='*')
textBox2.place(x = 290, y = 250)

button1 = Button(window, text = "   Login   ", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = login)
button1.place(x = 335, y = 340)

label4 = Label(window, text = "EXAM SHEILD", font = ("arial", 16, "bold"))
label4.place(x = 5, y = 5)

#display window
window.mainloop()
