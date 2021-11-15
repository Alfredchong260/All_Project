from playsound import playsound
from tkinter import messagebox
import multiprocessing
from tkinter import *
import time

root = Tk()
root.geometry('800x600')
root.configure(background='#252323')
root.title('Timer')

sep = Label(root, background='#252323', width=1, height=1).grid(row=1, column=2)

hours = Label(root, text='00', background='#69D6FD', width=12, height=4, font=('', 20))
hours.grid(row=2, column=1)

sep1 = Label(root, background='#252323', width=1, height=5).grid(row=2, column=2)

mins = Label(root, text='00', background='#69D6FD', width=12, height=4, font=('', 20))
mins.grid(row=2, column=3)

sep2 = Label(root, background='#252323', width=10, height=5).grid(row=2, column=4)

secs = Label(root, text='00', background='#69D6FD', width=12, height=4, font=('', 20))
secs.grid(row=2, column=5)

sep3 = Label(root, background='#252323', width=7, height=2).grid(row=3, column=4)

label1 = Label(root, text='Enter time in (HH:MM:SS): ', font=(
    '', 14, 'bold'), padx=10, pady=10, background='#252323', foreground='#FFFFFF', width=23)
label1.grid(row=4, column=1)

times = Entry(root, width=15, font=('', 20), background='#FFFFFF')
times.grid(row=4, column=3)

sep4 = Label(root, background='#252323', width=7, height=2).grid(row=5, column=4)

lst = [hours, mins, secs]

def submit():
    data = times.get().split(':')
    try: 
        t = int(data[0]) * 3600 + int(data[1]) * 60 + int(data[2])
    except:
        pass

    if t <= 11:
        hours.config(background='#FF0000')
        mins.config(background='#FF0000')
        secs.config(background='#FF0000')

    elif t <= 31:
        hours.config(background='#FFFF00')
        mins.config(background='#FFFF00')
        secs.config(background='#FFFF00')

    for d, l in zip(data, lst):
        l.config(text=d)
    times.delete(0, END)

    while t > -1:
        min, sec = divmod(t, 60)
        hour = 0
        if min> 60:
            hour, min = divmod(min, 60)

        hours.config(text="{0:2d}".format(hour))
        mins.config(text="{0:2d}".format(min))
        secs.config(text="{0:2d}".format(sec))

        root.update()
        time.sleep(1)

        t -= 1

        if t <= 10:
            hours.config(background='#FF0000')
            mins.config(background='#FF0000')
            secs.config(background='#FF0000')

        elif t <= 31:
            hours.config(background='#FFFF00')
            mins.config(background='#FFFF00')
            secs.config(background='#FFFF00')

    alarm_start()

def alarm_start():
    top = Toplevel(root)
    top.geometry('250x250')
    p = multiprocessing.Process(target=playsound, args=('./Xxxtentacion Numb Lyrics.mp3', ))
    p.start()
    
    label = Label(top, text="Time's up", font=('', 15, 'bold'))
    label.place(x=90, y=18)

    close_btn = Button(top, text='Stop', font=('', 18), command=lambda x = p: alarm_stop(x, top))
    close_btn.place(x=90, y=90)

def alarm_stop(p, top):
    p.terminate()
    top.destroy()

sub_btn = Button(root, text='Submit', background='#00BBFF',
                 foreground='#114558', font=('', 14), command=submit, width=10)
sub_btn.grid(row=6, column=3)

sep5 = Label(root, background='#252323', width=7, height=2).grid(row=7, column=4)

close_btn = Button(root, text='Quit', background='#00BBFF',
                   foreground='#114558', font=('', 14), command=lambda x=root: x.destroy(), width=10)
close_btn.grid(row=8, column=3)

root.mainloop()
