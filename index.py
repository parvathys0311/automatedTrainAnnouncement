from tkinter import *
import pyttsx3

# text to speech python library
# create object
engine = pyttsx3.init()
engine.setProperty('rate', 180)     # setting up voice speed rate

def speak(text):
    engine.say(text)
    engine.runAndWait()

# greeting message
def greetme():
    engine.say("Welcome to V I A. Rail Canada")
    engine.runAndWait()

# function to generate the announcementText
def generate_announcement():
    trainNum = txtTrainNo.get()
    trainName = txtTrainName.get()
    fromStation = txtFromStation.get()
    toStation = txtToStation.get()
    platformNo = txtPlatformNo.get()
    greetme()
    announcement = f'Passengers your kind Attention Please. Train number, {trainNum}, {trainName} train . from {fromStation} . to  {toStation} .  will arrive shortly at platform number {platformNo} . Thank you!!"'
    speak(announcement)

root = Tk()
root.title("Automated Train Announcement")
root.geometry('400x400+100+200')

# train info form fields
lblTrainNo = Label(root, text='Train Number')
txtTrainNo = Entry(root)
lblTrainName = Label(root, text='Train Name')
txtTrainName = Entry(root)
lblFromStation = Label(root, text='From Station')
txtFromStation = Entry(root)
lblToStation = Label(root, text='To Station')
txtToStation = Entry(root)
lblPlatformNo = Label(root, text='Platform No')
txtPlatformNo = Entry(root)


btnEnter = Button(root, text='Submit', command=generate_announcement)

# ui display
lblTrainNo.grid(row=0,column=0)
txtTrainNo.grid(row=0, column=1)
lblTrainName.grid(row=1, column=0)
txtTrainName.grid(row=1,column=1)
lblFromStation.grid(row=2, column=0)
txtFromStation.grid(row=2, column=1)
lblToStation.grid(row=3, column=0)
txtToStation.grid(row=3, column=1)
lblPlatformNo.grid(row=4, column=0)
txtPlatformNo.grid(row=4, column=1)
btnEnter.grid(row=5,column=1)

root.mainloop()