from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk #pillow is image processing in python
from student import Student #connecting student.py
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developers import Developer
from help import Help
from tkinter import messagebox
from time import strftime
from datetime import datetime
import os #direct direcories from where we can import photo

class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0") #0+0 is x and y axis starting point
        self.root.title("Face Recogniton System")
        
        #first image
        img = Image.open(r"college_images\main.jpg")
        img = img.resize((500,130),Image.LANCZOS)    #antilias helps to make image more natural but
        #at now Lanczos is used instead of antilias
        self.photoImg = ImageTk.PhotoImage(img) #making variable as photoImg

        f_lbl = Label(self.root,image=self.photoImg)
        f_lbl.place(x=0,y=0,width=500,height=130) #packing label with x axis and y axis
        
        #second image
        img1 = Image.open(r"college_images\main.jpg")
        img1 = img1.resize((500,130),Image.LANCZOS)   
        self.photoImg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoImg1)
        f_lbl.place(x=500,y=0,width=500,height=130) #x=500 cause mathi ko 500 paxi hamilai yo cahini bayo so 
        
        #third image
        img2 = Image.open(r"college_images\main.jpg")
        img2 = img2.resize((500,130),Image.LANCZOS)    
        self.photoImg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image=self.photoImg2)
        f_lbl.place(x=1000,y=0,width=500,height=130) #duita 500 paxi chaiyo image so
        
        #background image
        img3 = Image.open(r"college_images\background.jpg")
        img3 = img3.resize((1530,710),Image.LANCZOS)   
        self.photoImg3 = ImageTk.PhotoImage(img3) 

        bg_img = Label(self.root,image=self.photoImg3)
        bg_img.place(x=0,y=130,width=1530,height=710) 

        title =  Label(bg_img,text="FACE RECOGNITION SYSTEM",font=("Helvetica",35,"bold"),bg="white",fg="black")
        title.place(x=0,y=0,width=1530,height=45)

        #time
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(title,font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50) 
        time()   

        #student button
        img4 = Image.open(r"college_images\stdnt.jpg")
        img4 = img4.resize((220,190),Image.LANCZOS)   
        self.photoImg4 = ImageTk.PhotoImage(img4)
           #command connects student_details function that open student page
        b1=Button(bg_img,image=self.photoImg4,command=self.student_details, cursor="hand2")
        b1.place(x=150,y=100,width=220,height=190)

        b1_1 =Button(bg_img,text="Student Details",command=self.student_details, cursor="hand2",font=("Helvetica",20,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=150,y=290,width=220,height=30)

        #Recognize face button
        img5 = Image.open(r"college_images\detect.jpg")
        img5 = img5.resize((220,190),Image.LANCZOS)   
        self.photoImg5 = ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoImg5, cursor="hand2",command=self.face_data)
        b1.place(x=450,y=100,width=220,height=190)

        b1_1 =Button(bg_img,text="FaceRecognition", cursor="hand2",command=self.face_data,font=("Helvetica",16,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=450,y=290,width=220,height=30)

        #Attendance button
        img6 = Image.open(r"college_images\attendance.jpg")
        img6= img6.resize((220,190),Image.LANCZOS)   
        self.photoImg6 = ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoImg6, cursor="hand2",command=self.attendance_data,)
        b1.place(x=750,y=100,width=220,height=190)

        b1_1 =Button(bg_img,text="Attendance", cursor="hand2",command=self.attendance_data,font=("Helvetica",20,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=750,y=290,width=220,height=30)

        #Help Desk button
        img7 = Image.open(r"college_images\help.png")
        img7 = img7.resize((220,190),Image.LANCZOS)   
        self.photoImg7 = ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoImg7, cursor="hand2",command=self.help_data)
        b1.place(x=1050,y=100,width=220,height=190)

        b1_1 =Button(bg_img,text="Help Desk", cursor="hand2",command=self.help_data,font=("Helvetica",20,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1050,y=290,width=220,height=30)

        #Train button
        img8 = Image.open(r"college_images\face2.jpg")
        img8 = img8.resize((220,190),Image.LANCZOS)   
        self.photoImg8 = ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoImg8, cursor="hand2",command=self.train_data)
        b1.place(x=150,y=350,width=220,height=190)

        b1_1 =Button(bg_img,text="Train Data", cursor="hand2",command=self.train_data,font=("Helvetica",20,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=150,y=520,width=220,height=30)

        #Photos button
        img9 = Image.open(r"college_images\gallery.png")
        img9 = img9.resize((220,190),Image.LANCZOS)   
        self.photoImg9 = ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoImg9, cursor="hand2",command=self.open_img)
        b1.place(x=450,y=350,width=220,height=190)

        b1_1 =Button(bg_img,text="Photo Gallery", cursor="hand2",command=self.open_img,font=("Helvetica",20,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=450,y=520,width=220,height=30)

        #Developer button
        img10 = Image.open(r"college_images\developer.png")
        img10 = img10.resize((220,190),Image.LANCZOS)   
        self.photoImg10 = ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoImg10, cursor="hand2",command=self.developer_data)
        b1.place(x=750,y=350,width=220,height=190)

        b1_1 =Button(bg_img,text="Developer", cursor="hand2",command=self.developer_data,font=("Helvetica",20,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=750,y=520,width=220,height=30)

         #Exit button
        img11 = Image.open(r"college_images\exit.png")
        img11 = img11.resize((220,190),Image.LANCZOS)   
        self.photoImg11 = ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoImg11, cursor="hand2",command=self.IExit)
        b1.place(x=1050,y=350,width=220,height=190)

        b1_1 =Button(bg_img,text="EXIT", cursor="hand2",command=self.IExit,font=("Helvetica",20,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1050,y=520,width=220,height=30)

    def open_img(self):
        os.startfile("data")

    def IExit(self):
        self.IExit=messagebox.askyesno("Face Recognition","Are you sure you want to exit?",parent=self.root)
        if self.IExit>0:
            self.root.destroy()
        else:
            return


    #function buttons for openening studdent page
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)




         
        

if __name__ == "__main__":
    root=Tk() #calling root
    obj=Face_Recognition_System(root)
    root.mainloop()

    