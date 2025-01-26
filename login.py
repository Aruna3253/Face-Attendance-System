from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System


def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()

class login_window():
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0") #0+0 is x and y axis starting point
        self.root.title("LOGIN")
        
        img = Image.open(r"college_images\main.jpg")
        img = img.resize((1530,790),Image.LANCZOS)    #antilias helps to make image more natural but
        self.photoImg = ImageTk.PhotoImage(img) #making variable as photoImg

        f_lbl = Label(self.root,image=self.photoImg)
        f_lbl.place(x=0,y=0,width=1530,height=790)

        main_frame=Frame(self.root,bg="white") 
        main_frame.place(x=600,y=170,width=325,height=420)

        
        img2 = Image.open(r"college_images\back.jpg")
        img2 = img2.resize((325,420),Image.LANCZOS)    #antilias helps to make image more natural but
        self.photoImg2 = ImageTk.PhotoImage(img2) #making variable as photoImg

        f_lbl2 = Label(main_frame,image=self.photoImg2)
        f_lbl2.place(x=0,y=0,width=325,height=420)

        Current_f=Label(f_lbl2,bd=2,bg="black",fg="white",text="Get Started",font=("times new roman",20,"bold"))
        Current_f.place(x=75,y=55,width=200,height=30)

        Username=Label(f_lbl2,text="Email",font=("times new roman",15,"bold"),bg="black",fg="white")
        Username.place(x=60,y=120)

        self.email_entry=ttk.Entry(f_lbl2,width=15,font=("times new roman",15,"bold"))
        self.email_entry.place(x=40,y=150,width=270)

        Password=Label(f_lbl2,text="Password",font=("times new roman",15,"bold"),bg="black",fg="white")
        Password.place(x=60,y=185)

        self.Password_entry=ttk.Entry(f_lbl2,width=15,font=("times new roman",15,"bold"))
        self.Password_entry.place(x=40,y=210,width=270)

        save_btn=Button(f_lbl2,command=self.login,text="Login",width=22,font=("times new roman",14,"bold"),bg="red",fg="white")
        save_btn.place(x=70,y=260,width=200)

        save_btn2=Button(f_lbl2,text="Sign Up",command=self.register_window,width=22,font=("times new roman",10,"bold"),borderwidth=0,bg="black",fg="white")
        save_btn2.place(x=70,y=310,width=200)

        save_btn3=Button(f_lbl2,text="Forgot Password",command=self.forgot_password,width=22,font=("times new roman",10,"bold"),borderwidth=0,bg="black",fg="white")
        save_btn3.place(x=70,y=340,width=210)
    
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=RegisterWindow(self.new_window)

    def login(self):
        if self.email_entry.get()=="" or self.Password_entry.get()=="":
            messagebox.showerror("Error","All fields must be required",parent=self.root)
        elif self.email_entry.get()=="Aruna" and self.Password_entry.get()=="12345":
            messagebox.showinfo("Success","Welcome to face recognition system",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Arun@poi098",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(

                                                                                        self.email_entry.get(),
                                                                                        self.Password_entry.get()
                                                                                     ))
            row = my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username and password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return 
            
            conn.commit()
            conn.close()
    #reset password 
    def reset_password(self):
        if self.Search_combo.get()=="Select":
            messagebox.showerror("Error","select the security question")
        elif self.answer_entry.get()=="":
            messagebox.showerror("Error","please enter the answer")
        elif self.password_new_entry.get()=="":
            messagebox.showerror("Error","Please enter the new password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Arun@poi098",database="face_recognizer")
            my_cursor=conn.cursor()
            qury=("select *  from register where email=%s and securityQ=%s and securityA=%s")
            value = (self.email_entry.get(),self.Search_combo.get(), self.answer_entry.get())
            my_cursor.execute(qury,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please,enter the correct answer",parent=self.root)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.password_new_entry.get(),self.email_entry.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","You Password has been reset,please login",parent=self.root)
                self.root2.destroy()



    #forgot password window
    def forgot_password(self):
        if self.email_entry.get()=="":
            messagebox.showerror("Error","Please enter your Email",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Arun@poi098",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select *from register where email=%s")
            value=(self.email_entry.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("Error","Please enter the valid user name",parent=self.root)
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("450x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="black",fg="white")
                l.place(x=0,y=10,relwidth=1)

                security=Label(self.root2,bd=2,bg="white",fg="black",text=" Select Security Questions",font=("times new roman",15,"bold"))
                security.place(x=50,y=80)
                self.Search_combo=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),width=15,state="read only")
                self.Search_combo['values']=("Select","Your Birth Place","You nickname","Your pet name")
                self.Search_combo.current(0)
                self.Search_combo.place(x=50,y=110,width=250)
                
                answer=Label(self.root2,bd=2,bg="white",fg="black",text="Security Answer",font=("times new roman",15,"bold"))
                answer.place(x=50,y=150)
                self.answer_entry=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.answer_entry.place(x=50,y=180,width=250)

                password_new=Label(self.root2,bd=2,bg="white",fg="black",text=" New Password",font=("times new roman",15,"bold"))
                password_new.place(x=50,y=230)
                self.password_new_entry=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.password_new_entry.place(x=50,y=260,width=250)

                reset_btn=Button(self.root2,text="Reset",command=self.reset_password,font=("times new roman",15,"bold"),bg="red",fg="white")
                reset_btn.place(x=100,y=310,width=250)

              




            

              


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

        login_btn=Button(main_frame,command=self.return_login,image=self.photoImgLogin,borderwidth=0,cursor="hand2")
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

    def return_login(self):
        self.root.destroy()

          



if __name__ == "__main__":
    main()