from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0") 
        self.root.title("Face Recogniton System")

        title = Label(self.root,text="DEVELOPER",font=("Helvetica",25,"bold"),bg="white",fg="darkred")
        title.place(x=0,y=0,width=1530,height=35)

        img_top = Image.open(r"college_images\dev2.jpg")
        img_top = img_top.resize((1530,720),Image.LANCZOS)   
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=37,width=1530,height=720)
        
        #developer frame
        main_frame=Frame(f_lbl,bd=2,bg="white") #bd=border
        main_frame.place(x=880,y=0,width=460,height=530)
        
        img_low = Image.open(r"college_images\dev.jpg")
        img_low = img_low.resize((200,200),Image.LANCZOS)   
        self.photoimg_low = ImageTk.PhotoImage(img_low)

        f_lbl = Label(main_frame,image=self.photoimg_low)
        f_lbl.place(x=300,y=0,width=200,height=200)

        dep_label=Label(main_frame,text="Developer Info",font=("times new roman",20,"bold"),bg="white")
        dep_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="I am Aruna",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=0,y=40)

        img_lo = Image.open(r"college_images\trainface3.jpg")
        img_lo = img_lo.resize((500,320),Image.LANCZOS)   
        self.photoimg_lo = ImageTk.PhotoImage(img_lo)

        f_lbl = Label(main_frame,image=self.photoimg_lo)
        f_lbl.place(x=0,y=220,width=500,height=320)

       
     

if __name__ == "__main__":
    root=Tk() #calling root
    obj=Developer(root)
    root.mainloop()