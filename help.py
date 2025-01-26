from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0") 
        self.root.title("Face Recogniton System")

        title = Label(self.root,text="HELP DESK",font=("Helvetica",25,"bold"),bg="white",fg="darkred")
        title.place(x=0,y=0,width=1530,height=35)

        img_top = Image.open(r"college_images\help2.jpg")
        img_top = img_top.resize((1530,720),Image.LANCZOS)   
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=37,width=1530,height=720)
        
        #developer frame
        

        dep_label=Label(f_lbl,text="Email: arunabasaula@gmail.com",font=("times new roman",20,"bold"),bg="blue")
        dep_label.place(x=0,y=5)

        

      
        
if __name__ == "__main__":
    root=Tk() #calling root
    obj=Help(root)
    root.mainloop()