from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Own Image Viewer')

img = ImageTk.PhotoImage(Image.open('../scrap/lenglui/20200514155238.jpg'))
img1 = ImageTk.PhotoImage(Image.open('../scrap/lenglui/20200514155235.jpg'))
img2 = ImageTk.PhotoImage(Image.open('../scrap/lenglui/20200514155236.jpg'))
img3 = ImageTk.PhotoImage(Image.open('../scrap/lenglui/20200514155237.jpg'))
img_list = [img1, img2, img3]

my_label = Label(image=img)
my_label.grid(row=0, column=0, columnspan=3)

status = Label(root, text=f'Image 1 of {len(img_list)}', bd=1, relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def next(num):
    global my_label
    global button_next
    global button_back

    my_label.grid_forget()
    my_label = Label(image=img_list[num - 1])
    button_next = Button(root, text='>>', command=lambda: next(num + 1))
    button_back = Button(root, text='<<',command=lambda: back(num - 1))

    if num == len(img_list):
        button_next = Button(root, text='>>', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_next.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

    status = Label(root, text=f'Image {num} of {len(img_list)}', bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def back(num):
    global my_label
    global button_next
    global button_back

    my_label.grid_forget()
    my_label = Label(image=img_list[num - 1])
    button_next = Button(root, text='>>', command=lambda: next(num + 1))
    button_back = Button(root, text='<<',command=lambda: back(num - 1))
    if num == 1:
        button_back = Button(root, text='<<', state=DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    button_next.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

    status = Label(root, text=f'Image {num} of {len(img_list)}', bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

button_next = Button(root, text='>>', command=lambda: next(2))
button_back = Button(root, text='<<', command=lambda: back, state=DISABLED)
button_quit = Button(root, text='Exit program', command=root.quit)
button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_next.grid(row=1, column=2, pady=10)

root.mainloop()
# print(len(img_list))
