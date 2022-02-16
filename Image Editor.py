from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox as messagebox
import os
from tkinter import filedialog
root=Tk()
root.title("Image Editor")
root.geometry("1500x800")
root.configure(bg='gold')

title_L=Label(root,text="Image Editor",font=("architectural",18,"bold"),bg="lightblue")
title_L.place(relx=0.5,rely=0.1,anchor=CENTER)

image_L=Label(root,bg="gold")
image_L.place(relx=0.5,rely=0.55,anchor=CENTER)

img_path=""

def file_open():
    global img_path
    img_path=filedialog.askopenfilename(title="Open Image",filetype=(("Image","*.jpg *.gif *.png *.jpeg"),))
    print(img_path)
    myimage=str(img_path)
    myimage2=ImageTk.PhotoImage(Image.open(myimage))
    print(myimage)
    image_L['image']=myimage2
    image_L['height']=650
    image_L['width']=800
    myimage2.open()
    
    
def turn_image():
    global img_path 
    opened_image.open(img_path)
    opened_image = opened_image.rotate(90)
    rotated_tk = ImageTk.PhotoImage(opened_image)
    image_L['image']=rotated_tk
    image_L['height']=650
    image_L['width']=800
    rotated_tk.open()
    
btn_openfile=Button(root,text="Open File",command=file_open)
btn_openfile.place(relx=0.2,rely=0.5,anchor=CENTER)

btn_turnfile=Button(root,text="Turn File",command=turn_image)
btn_turnfile.place(relx=0.8,rely=0.5,anchor=CENTER)
root.mainloop()