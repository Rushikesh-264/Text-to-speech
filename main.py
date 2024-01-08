# PROJECT TO CONVERT TEXT TO SPEECH

from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root = Tk()
root.title("TEXT TO SPEECH")
root.geometry("950x450+200+200")
root.resizable(False, False)
root.configure(bg="#305065")

engine = pyttsx3.init()


def speaknow():                                             # function to speak (convert the input text to speech)
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():                                  # function to set the voice of different genders  (male and female)
        if gender == "Male":
            engine.setProperty("voice", voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty("voice", voices[1].id)
            engine.say(text)
            engine.runAndWait()
    if text:                                                    # to modify the pace of the speech
        if speed == "Fast":
            engine.setProperty("rate", 250)
            setvoice()
        elif speed == "Normal":
            engine.setProperty("rate", 150)
            setvoice()
        else:
            engine.setProperty("rate", 60)
            setvoice()


def download():                                                  # function to donwload the speech
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if gender == "Male":                                        # if the gender is male
            engine.setProperty("voice", voices[0].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, "text.mp3")
            engine.runAndWait()
        else:                                                       # if the gender is female
            engine.setProperty("voice", voices[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, "text.mpe")
            engine.runAndWait()

    if text:
        if speed == "Fast":
            engine.setProperty("rate", 250)
            setvoice()
        elif speed == "Normal":
            engine.setProperty("rate", 150)
            setvoice()
        else:
            engine.setProperty("rate", 60)
            setvoice()


image_icon = PhotoImage(file="mic.png")
root.iconphoto(False, image_icon)

# Top Frame
top_frame = Frame(root, bg="white", width=4000, height=111)                     # building the top frame
top_frame.place(x=0, y=0)

logo = PhotoImage(file="mic.png")                                         # adding the image of the mic to the top_frame
Label(top_frame, image=logo, bg="White").place(x=12, y=8)

Label(top_frame, text="TEXT TO SPEECH", font="arial 24 bold", bg="white", fg="black").place(x=150, y=30)

text_area = Text(root, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)  # to create a textbox to enter the input
text_area.place(x=10, y=150, width=500, height=279)

Label(root, text="VOICE", font="arial 14 bold", bg="#305065", fg="white").place(x=630, y=190)
Label(root, text="SPEED", font="arial 14 bold", bg="#305065", fg="white").place(x=820, y=190)
# to create voice and speed labels

gender_combobox = Combobox(root, values=["MALE", "FEMALE"], font="arial 15", state='r', width=10)
gender_combobox.place(x=600, y=223)
gender_combobox.set("Male")
# adding combobox to choose the gender

speed_combobox = Combobox(root, values=["Fast", "Normal", "Slow"], font="arial 15", state='r', width=10)
speed_combobox.place(x=790, y=223)
speed_combobox.set("Normal")
# adding combobox to choose the face of the speech

image_icon = PhotoImage(file="speak.png")                           # adding speak symbol
btn = Button(root, text="Speak", compound=LEFT, image=image_icon, width=125, height=51, font="arial 14 bold", command=speaknow)
btn.place(x=598, y=310)

image_icon2 = PhotoImage(file="download symbol.png")                # adding download symbol
save = Button(root, text="Save", compound=LEFT, image=image_icon2, width=125, height=49, bg="#39c790", font="arial 14 bold", command=download)
save.place(x=788, y=310)

root.mainloop()
