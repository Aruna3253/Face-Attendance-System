from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class RegisterWindow():
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0") 
        self.root.title("REGISTER")
        #variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()
        

        # Load the image
        self.original_image = Image.open(r"college_images\bg.jpg")

        # Resize the image to fit the window
        self.bg_image = self.original_image.resize((1530, 790), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.bg_image)

        # Create a label with the background image
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        #next image
        img2 = Image.open(r"college_images\reg.jpg")
        img2 = img2.resize((440,500),Image.LANCZOS)    #antilias helps to make image more natural but
        self.photoImg2 = ImageTk.PhotoImage(img2) #making variable as photoImg

        f_lbl2 = Label(self.root,image=self.photoImg2)
        f_lbl2.place(x=50,y=100,width=440,height=500)

        main_frame=Frame(self.root,bg="white") 
        main_frame.place(x=492,y=100,width=800,height=500)

        register=Label(main_frame,bd=2,bg="white",fg="darkgreen",text="REGISTER HERE",font=("times new roman",20,"bold"))
        register.place(x=20,y=20)
           #row 1
        name=Label(main_frame,bd=2,bg="white",fg="black",text=" First Name",font=("times new roman",15,"bold"))
        name.place(x=50,y=70)
        name_entry=ttk.Entry(main_frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        name_entry.place(x=50,y=100,width=250)

        l_name=Label(main_frame,bd=2,bg="white",fg="black",text=" Last Name",font=("times new roman",15,"bold"))
        l_name.place(x=350,y=70)
        self.l_name_entry=ttk.Entry(main_frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.l_name_entry.place(x=350,y=100,width=250)

        #row 2
        contact=Label(main_frame,bd=2,bg="white",fg="black",text=" Contact No.",font=("times new roman",15,"bold"))
        contact.place(x=50,y=140)
        self.contact_entry=ttk.Entry(main_frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.contact_entry.place(x=50,y=170,width=250)

        email=Label(main_frame,bd=2,bg="white",fg="black",text="Email",font=("times new roman",15,"bold"))
        email.place(x=350,y=140)
        self.email_entry=ttk.Entry(main_frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.email_entry.place(x=350,y=170,width=250)
        #row 3
        security=Label(main_frame,bd=2,bg="white",fg="black",text=" Select Security Questions",font=("times new roman",15,"bold"))
        security.place(x=50,y=220)
        Search_combo=ttk.Combobox(main_frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),width=15,state="read only")
        Search_combo['values']=("Select","Your Birth Place","You nickname","Your pet name")
        Search_combo.current(0)
        Search_combo.place(x=50,y=250,width=250)
        
        answer=Label(main_frame,bd=2,bg="white",fg="black",text="Security Answer",font=("times new roman",15,"bold"))
        answer.place(x=350,y=220)
        self.answer_entry=ttk.Entry(main_frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.answer_entry.place(x=350,y=250,width=250)

        #row4
        password=Label(main_frame,bd=2,bg="white",fg="black",text=" Password",font=("times new roman",15,"bold"))
        password.place(x=50,y=290)
        self.password_entry=ttk.Entry(main_frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.password_entry.place(x=50,y=320,width=250)

        confirm=Label(main_frame,bd=2,bg="white",fg="black",text="Confirm Password",font=("times new roman",15,"bold"))
        confirm.place(x=350,y=290)
        self.confirm_entry=ttk.Entry(main_frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.confirm_entry.place(x=350,y=320,width=250)

        #checkbutton
        checkbtn=Checkbutton(main_frame,variable=self.var_check,text="I agree the terms and condition",font=("times new roman",15,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=370)

        img3 = Image.open(r"college_images\register.jpg")
        img3 = img3.resize((250,50),Image.LANCZOS)   
        self.photoImg3 = ImageTk.PhotoImage(img3)

        register_btn=Button(main_frame,command=self.register_data,image=self.photoImg3,borderwidth=0,cursor="hand2")
        register_btn.place(x=10,y=420,width=250)
        #login button
        imgLogin = Image.open(r"college_images\login.jpg")
        imgLogin = imgLogin.resize((250,70),Image.LANCZOS)   
        self.photoImgLogin = ImageTk.PhotoImage(imgLogin)

        login_btn=Button(main_frame,image=self.photoImgLogin,borderwidth=0,cursor="hand2")
        login_btn.place(x=300,y=420,width=250)

        #function declaration
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All Field must be required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","passwords and confirm passwords must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","please agree our terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Arun@poi098",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists,please try another email")

            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                         self.var_fname.get(),
                                                                                                         self.var_lname.get(),
                                                                                                         self.var_contact.get(),
                                                                                                         self.var_email.get(),
                                                                                                         self.var_securityQ.get(),
                                                                                                         self.var_securityA.get(),
                                                                                                         self.var_pass.get(),
                                                                                      )) 

                conn.commit()
                
                conn.close()
                messagebox.showerror("success","Register successfully")




if __name__ == "__main__":
    root = Tk()  # calling root
    obj = RegisterWindow(root)
    root.mainloop()
