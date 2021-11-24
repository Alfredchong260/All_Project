from tkinter import *
import datetime
import time


root = Tk()
root.geometry('500x300+100+100')

time_str = str(datetime.datetime.today())[:-7]

time_var = StringVar()

label = Label(root, textvariable=time_var, font=('', 20)).pack()

while True:
    root.update()
    time.sleep(1)
    time_str = str(datetime.datetime.today())[:-7]
    time_var.set(time_str)

# root.mainloop()
