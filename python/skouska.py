from tkinter import *
from PIL import ImageTk, Image
root=Tk()
root.iconbitmap("C:/Users/kamji/Downloads/GitHubDesktopSetup-x64.exe")
root.title("MECUBE")

obr1 = ImageTk.PhotoImage(Image.open("C:/Users/kamji/Pictures/apple.png"))
obr2 = ImageTk.PhotoImage(Image.open("C:/Users/kamji/Pictures/pikachu_uses_growth__by_vale98pm_d9degey-fullview.png"))
obr3 = ImageTk.PhotoImage(Image.open("C:/Users/kamji/Pictures/h.png"))
obr4 = ImageTk.PhotoImage(Image.open("C:/Users/kamji/Pictures/thumb-22359.png"))
obr5 = ImageTk.PhotoImage(Image.open("C:/Users/kamji/Pictures/unnamed.png"))

my_label = Label(image=obr1)
my_label.grid(row=0, column=0, columnspan=3) 

def forward(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget() 
    my_label = Label(image=obr_list[image_number-1])
    my_label.grid(row=0, column=0, columnspan=3) 


def back():
    global my_label
    global button_forward
    global button_back
obr_list = list[obr1, obr2, obr3, obr4, obr5]



button_forward = Button(root, text=">>", padx=10,command=lambda:forward(2))
button_exit = Button(root, text="EXIT", padx=20, command=exit)
button_back = Button(root, text="<<",padx=10, command=lambda:back())


button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()