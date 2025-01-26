from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0") 
        self.root.title("Face Recogniton System")

      #   ====VAriables declaration=======
        self.var_dep=StringVar()
        self.var_sem=StringVar()
        self.var_year=StringVar()
        self.var_course=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_Email=StringVar()
        self.var_phone=StringVar()
        self.var_div=StringVar()
        self.var_address=StringVar()
        self.var_roll=StringVar()
        self.var_dob=StringVar()
        self.var_radio1=StringVar()
       


        #first image
        img = Image.open(r"C:\Users\Redstone\OneDrive\Desktop\Face Recognition System\college_images\studentss.jpg")
        img = img.resize((500,130),Image.LANCZOS)   
        self.photoImg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoImg)
        f_lbl.place(x=0,y=0,width=500,height=130) 
        
        #second image
        img1 = Image.open(r"C:\Users\Redstone\OneDrive\Desktop\Face Recognition System\college_images\studentss.jpg")
        img1 = img1.resize((500,130),Image.LANCZOS)   
        self.photoImg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoImg1)
        f_lbl.place(x=500,y=0,width=500,height=130) 

        #third image
        img2 = Image.open(r"C:\Users\Redstone\OneDrive\Desktop\Face Recognition System\college_images\studentss.jpg")
        img2 = img2.resize((500,130),Image.LANCZOS)    
        self.photoImg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image=self.photoImg2)
        f_lbl.place(x=1000,y=0,width=500,height=130) 

        #background image
        img3 = Image.open(r"C:\Users\Redstone\OneDrive\Desktop\Face Recognition System\college_images\back.jpg")
        img3 = img3.resize((1530,710),Image.LANCZOS)   
        self.photoImg3 = ImageTk.PhotoImage(img3) 

        bg_img =Label(self.root,image=self.photoImg3)
        bg_img.place(x=0,y=130,width=1530,height=710) 

        title =Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("Helvetica",35,"bold"),bg="white",fg="darkgreen")
        title.place(x=0,y=0,width=1530,height=45)

        #making frame
        main_frame=Frame(bg_img,bd=2,bg="white") #bd=border
        main_frame.place(x=15,y=50,width=1325,height=480)
        
        #left frame #labelframe ma text halna milxa
        l=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        l.place(x=10,y=10,width=675,height=455)

        img_l = Image.open(r"C:\Users\Redstone\OneDrive\Desktop\Face Recognition System\college_images\studentss.jpg")
        img_l = img_l.resize((660,115),Image.LANCZOS)    
        self.photoImg_l = ImageTk.PhotoImage(img_l)

        f_lbl = Label(l,image=self.photoImg_l)
        f_lbl.place(x=5,y=0,width=660,height=115) 

        #1.current course
        Current_f=LabelFrame(l,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        Current_f.place(x=5,y=120,width=660,height=115)

          #department in current course
        dep_label=Label(Current_f,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
           #combo box is like drop down list
        dep_combo=ttk.Combobox(Current_f,textvariable=self.var_dep,font=("times new roman",10,"bold"),width=15,state="read only")
        dep_combo['values']=("Select Department","computer","IT","Civil","Mechanical")
        dep_combo.current(0) #tuple ko indexing 0 bata start hunxa so select department jailay dekhosh banera 0 rakhko
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course in current course
        course_label=Label(Current_f,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
           #combo box is like drop down list
        course_combo=ttk.Combobox(Current_f,textvariable=self.var_course,font=("times new roman",10,"bold"),width=15,state="read only")
        course_combo['values']=("Select Course","Python","Java","C","Dot net")
        course_combo.current(0) #tuple ko indexing 0 bata start hunxa so select department jailay dekhosh banera 0 rakhko
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year in current course
        year_label=Label(Current_f,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
           #combo box is like drop down list
        year_combo=ttk.Combobox(Current_f,textvariable=self.var_year,font=("times new roman",10,"bold"),width=15,state="read only")
        year_combo['values']=("Select Year","2020-2","2020-3","2021-2","2021-3")
        year_combo.current(0) #tuple ko indexing 0 bata start hunxa so select department jailay dekhosh banera 0 rakhko
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester in current course
        semester_label=Label(Current_f,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
           #combo box is like drop down list
        semester_combo=ttk.Combobox(Current_f,textvariable=self.var_sem,font=("times new roman",10,"bold"),width=15,state="read only")
        semester_combo['values']=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4")
        semester_combo.current(0) #tuple ko indexing 0 bata start hunxa so select department jailay dekhosh banera 0 rakhko
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #2.class student information
        Class_f=LabelFrame(l,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        Class_f.place(x=5,y=240,width=660,height=190)
          #2.a Labelstudent id
        StudentId_label=Label(Class_f,text="StudentId:",font=("times new roman",9,"bold"),bg="white")
        StudentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

           #entry field is like input field
        studentId_entry=ttk.Entry(Class_f,textvariable=self.var_id,width=15,font=("times new roman",9,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #2.b Labelstudent name
        StudentName_label=Label(Class_f,text="StudentName:",font=("times new roman",9,"bold"),bg="white")
        StudentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

           #entry field is like input field
        studentName_entry=ttk.Entry(Class_f,textvariable=self.var_name,width=15,font=("times new roman",9,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #2.c Labelclass division
        StudentDiv_label=Label(Class_f,text="ClassDivision:",font=("times new roman",9,"bold"),bg="white")
        StudentDiv_label.grid(row=0,column=4,padx=10,pady=5,sticky=W)

           #entry field is like input field
        div_combo=ttk.Combobox(Class_f,textvariable=self.var_div,font=("times new roman",10,"bold"),width=7,state="read only")
        div_combo['values']=("Select","A","B","C")
        div_combo.current(0) #tuple ko indexing 0 bata start hunxa so select department jailay dekhosh banera 0 rakhko
        div_combo.grid(row=0,column=5,padx=10,pady=5,sticky=W)
         #2.d Label RollNo
        StudentRoll_label=Label(Class_f,text="RollNo:",font=("times new roman",9,"bold"),bg="white")
        StudentRoll_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

           #entry field is like input field
        studentRoll_entry=ttk.Entry(Class_f,textvariable=self.var_roll,width=15,font=("times new roman",9,"bold"))
        studentRoll_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

         #2.e Label Gender
        StudentDiv_label=Label(Class_f,text="Gender:",font=("times new roman",9,"bold"),bg="white")
        StudentDiv_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

           #cpmbo box field is like input field
    
        gender_combo=ttk.Combobox(Class_f,textvariable=self.var_gender,font=("times new roman",10,"bold"),width=11,state="read only")
        gender_combo['values']=("Select Gender","Male","Female","Other")
        gender_combo.current(0) #tuple ko indexing 0 bata start hunxa so select department jailay dekhosh banera 0 rakhko
        gender_combo.grid(row=1,column=3,padx=10,pady=5,sticky=W)

         #2.f Label Email
        StudentEmail_label=Label(Class_f,text="Email:",font=("times new roman",9,"bold"),bg="white")
        StudentEmail_label.grid(row=1,column=4,padx=10,pady=5,sticky=W)

           #entry field is like input field
        studentEmail_entry=ttk.Entry(Class_f,textvariable=self.var_Email,width=10,font=("times new roman",9,"bold"))
        studentEmail_entry.grid(row=1,column=5,padx=10,pady=5,sticky=W)

         #2.g Label Phone No
        StudentPhone_label=Label(Class_f,text="Phone No:",font=("times new roman",9,"bold"),bg="white")
        StudentPhone_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

           #entry field is like input field
        studentPhone_entry=ttk.Entry(Class_f,textvariable=self.var_phone,width=15,font=("times new roman",9,"bold"))
        studentPhone_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

         #2.h Address
        StudentAddress_label=Label(Class_f,text="Address:",font=("times new roman",9,"bold"),bg="white")
        StudentAddress_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

           #entry field is like input field
        studentAddress_entry=ttk.Entry(Class_f,textvariable=self.var_address,width=15,font=("times new roman",9,"bold"))
        studentAddress_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #2.i DOB
        StudentDob_label=Label(Class_f,text="DateOfBirth:",font=("times new roman",9,"bold"),bg="white")
        StudentDob_label.grid(row=2,column=4,padx=10,pady=5,sticky=W)

           #entry field is like input field
        studentDob_entry=ttk.Entry(Class_f,textvariable=self.var_dob,width=10,font=("times new roman",9,"bold"))
        studentDob_entry.grid(row=2,column=5,padx=10,pady=5,sticky=W)
        
        #2.j radio Button 
        radiobtn1=ttk.Radiobutton(Class_f,variable=self.var_radio1,text="Take photo Sample",value="Yes")
        radiobtn1.grid(row=3,column=0)

        radiobtn2=ttk.Radiobutton(Class_f,variable=self.var_radio1,text="No photo Sample",value="No")
        radiobtn2.grid(row=3,column=1)
        #button Frame
        btn_frame=Frame(Class_f,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=115,width=655,height=40)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=22,font=("times new roman",9,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=22,font=("times new roman",9,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=22,font=("times new roman",9,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=22,font=("times new roman",9,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(Class_f,bd=2,relief=RIDGE)
        btn_frame1.place(x=0,y=145,width=655,height=35)

        takePhoto_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=45,font=("times new roman",9,"bold"),bg="blue",fg="white")
        takePhoto_btn.grid(row=0,column=0)

        updatePhoto_btn=Button(btn_frame1,text="Update Photo Sample",width=45,font=("times new roman",9,"bold"),bg="blue",fg="white")
        updatePhoto_btn.grid(row=0,column=1)

 
        #right frame #labelframe ma text halna milxa
        r=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        r.place(x=695,y=10,width=600,height=455)

        img_r = Image.open(r"C:\Users\Redstone\OneDrive\Desktop\Face Recognition System\college_images\studentss.jpg")
        img_r = img_r.resize((585,115),Image.LANCZOS)    
        self.photoImg_r = ImageTk.PhotoImage(img_r)

        f_lbl = Label(r,image=self.photoImg_r)
        f_lbl.place(x=5,y=0,width=585,height=115) 

        #search system
        Search_f=LabelFrame(r,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_f.place(x=5,y=114,width=585,height=60)

        Search_label=Label(Search_f,text="Search By:",font=("times new roman",9,"bold"),bg="darkred",fg="white")
        Search_label.grid(row=0,column=0,padx=9,pady=5,sticky=W)

        Search_combo=ttk.Combobox(Search_f,font=("times new roman",10,"bold"),width=15,state="read only")
        Search_combo['values']=("Select","Roll_No","Phone_No")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=2,pady=9,sticky=W)

        search_entry=ttk.Entry(Search_f,width=15,font=("times new roman",10,"bold"))
        search_entry.grid(row=0,column=2,padx=9,pady=5,sticky=W)

        search_btn=Button(Search_f,text="Search",width=14,font=("times new roman",10,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=3)

        showAll_btn=Button(Search_f,text="Show All",width=14,font=("times new roman",10,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=3)

      #   table Frame 
        table_f=LabelFrame(r,bd=2,bg="white",relief=RIDGE,text="Details Table",font=("times new roman",12,"bold"))
        table_f.place(x=0,y=177,width=585,height=200)

        scroll_x=ttk.Scrollbar(table_f,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_f,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_f,column=("dep","sem","id","year","gender","Email","name","div","address","phone","course","dob"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="division")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("Email",text="email")
        self.student_table.heading("phone",text="PhoneNumber")
        self.student_table.heading("dob",text="DOB")
        self.student_table["show"]="headings"
        
      
        #setting width by using column
        columns = self.student_table["columns"]
        for column in columns:
         self.student_table.column(column, width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor) #it binds get_cursor
        self.fetch_data()

     #function  declaration to add data
    def add_data(self): #data validation
     if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()==""   :
        messagebox.showerror("Error","All fields must be filled",parent=self.root) #kailay kai message box arko window m jana sakxa so esmai dekhauna lainwe add parent
     else:
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="Arun@poi098",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                         self.var_dep.get(),
                                                                                                         self.var_sem.get(),
                                                                                                         self.var_id.get(),
                                                                                                         self.var_year.get(),
                                                                                                         self.var_gender.get(),
                                                                                                         self.var_Email.get(),
                                                                                                         self.var_name.get(),
                                                                                                         self.var_div.get(),
                                                                                                         self.var_address.get(),
                                                                                                         self.var_phone.get(),
                                                                                                         self.var_course.get(),
                                                                                                         self.var_dob.get(),
                                                                                                         self.var_roll.get(),
                                                                                                         self.var_radio1.get(),
                                                                                                         
                                                                                                         
                                                                                                         ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("success","student details are filled successfully",parent=self.root)
        except Exception as es:
           messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    #fetching data from database to our right frame
    def fetch_data(self):
       conn=mysql.connector.connect(host="localhost",username="root",password="Arun@poi098",database="face_recognizer")
       my_cursor=conn.cursor()
       my_cursor.execute("select * from student")
       data=my_cursor.fetchall()


       if len(data)!=0:
          self.student_table.delete(*self.student_table.get_children())
          for i in data:
             self.student_table.insert("",END,values=i)
          conn.commit()
       conn.close()



    #====== get cursor=====
    def get_cursor(self,event=""):
       cursor_focus=self.student_table.focus()
       content=self.student_table.item(cursor_focus)
       data=content["values"]

       self.var_dep.set(data[0]),
       self.var_sem.set(data[1]),
       self.var_id.set(data[2]),
       self.var_year.set(data[3]),
       self.var_gender.set(data[4]),
       self.var_Email.set(data[5]),
       self.var_name.set(data[6]),
       self.var_div.set(data[7]),
       self.var_address.set(data[8]),
       self.var_phone.set(data[9]),
       self.var_course.set(data[10]),
       self.var_dob.set(data[11]),
       self.var_roll.set(data[12]),
       self.var_radio1.set(data[13])

     #Update Function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()==""   :
         messagebox.showerror("Error","All fields must be filled",parent=self.root)
        else:
           try:
              Update=messagebox.askyesno("Update","Do you want to update the details?",parent=self.root)
              if Update>0:
                 conn=mysql.connector.connect(host="localhost",username="root",password="Arun@poi098",database="face_recognizer")
                 my_cursor=conn.cursor()
                 my_cursor.execute("update student set Dep=%s,Semester=%s,Year=%s,Gender=%s,Email=%s,Name=%s,Division=%s,Address=%s,Phone=%s,Course=%s,DateOfBirth=%s,RollNo=%s,PhotoSample=%s where StudentId=%s",(
                                                                                                         self.var_dep.get(),
                                                                                                         self.var_sem.get(),
                                                                                                         self.var_year.get(),
                                                                                                         self.var_gender.get(),
                                                                                                         self.var_Email.get(),
                                                                                                         self.var_name.get(),
                                                                                                         self.var_div.get(),
                                                                                                         self.var_address.get(),
                                                                                                         self.var_phone.get(),
                                                                                                         self.var_course.get(),
                                                                                                         self.var_dob.get(),
                                                                                                         self.var_roll.get(),
                                                                                                         self.var_radio1.get(),
                                                                                                         self.var_id.get()
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                                                                                       ))
              else:
                 if not Update:
                    return
              messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
              conn.commit()
              self.fetch_data()
              conn.close()
           except Exception as es:
              messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
            
    #Delete function
    def delete_data(self):
       if self.var_id.get()=="":
          messagebox.showerror("Error","Student Id must be required",parent=self.root)
       else:
          try:
             delete=messagebox.askyesno("Delete","Do you want to delete the student details?",parent=self.root)
             if delete>0:
                 conn=mysql.connector.connect(host="localhost",username="root",password="Arun@poi098",database="face_recognizer")
                 my_cursor=conn.cursor()
                 sql="delete from student where StudentId=%s"
                 val=(self.var_id.get(),)
                 my_cursor.execute(sql,val)
             else:
               if not delete:
                  return
             conn.commit()
             self.fetch_data()
             conn.close()
             messagebox.showinfo("Delete","successfully deleted the details",parent=self.root)
          except Exception as es:
              messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #Reset Function
    def reset_data(self):
       self.var_dep.set("Select Department")
       self.var_sem.set("Select Semester"),
       self.var_id.set(""),
       self.var_year.set("Select Year"),
       self.var_gender.set("Select Gender"),
       self.var_Email.set(""),
       self.var_name.set(""),
       self.var_div.set(""),
       self.var_address.set(""),
       self.var_phone.set(""),
       self.var_course.set("Select Course"),
       self.var_dob.set(""),
       self.var_roll.set(""),
       self.var_radio1.set("") 


     #Generate data set to take photo sample
    def generate_dataset(self):
       if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()==""   :
         messagebox.showerror("Error","All fields must be filled",parent=self.root)
       else:
           try:
              
            conn=mysql.connector.connect(host="localhost",username="root",password="Arun@poi098",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from student")
            myresult=my_cursor.fetchall()
            user_id=0
            for x in myresult:
               user_id+=1
            my_cursor.execute("update student set Dep=%s,Semester=%s,Year=%s,Gender=%s,Email=%s,Name=%s,Division=%s,Address=%s,Phone=%s,Course=%s,DateOfBirth=%s,RollNo=%s,PhotoSample=%s where StudentId=%s",(
                                                                                                         self.var_dep.get(),
                                                                                                         self.var_sem.get(),
                                                                                                         self.var_year.get(),
                                                                                                         self.var_gender.get(),
                                                                                                         self.var_Email.get(),
                                                                                                         self.var_name.get(),
                                                                                                         self.var_div.get(),
                                                                                                         self.var_address.get(),
                                                                                                         self.var_phone.get(),
                                                                                                         self.var_course.get(),
                                                                                                         self.var_dob.get(),
                                                                                                         self.var_roll.get(),
                                                                                                         self.var_radio1.get(),
                                                                                                         self.var_id.get()==user_id+1
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                                                                                       ))
            conn.commit()
            self.fetch_data()
            self.reset_data()
            conn.close()
            # load predifined cascade algorithm features: face frontals from opencv
            face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            def face_cropped(img):
               gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converting rgb images to gray image at initial
               faces=face_classifier.detectMultiScale(gray,1.3,5) #scaling factor=1.3(bydefault hunxa),Minimum neighbour=5

               #we need to make rectangle.x-axis,y-axis,width,height
               for(x,y,w,h) in faces:
                  face_cropped=img[y:y+h,x:x+w] #face cropped garni formula
                  return face_cropped
             #lets open camera , web camera ko 0 hunxa, aru ko 1
            cap=cv2.VideoCapture(0)
            img_id=0 #image capture bayepaxi calculate bayera img_id ma store hunca by default 0 rakhdiyem
            while True: #image ko sample collect garna lai loop chalako
               ret,my_frame=cap.read() #image capture bako read garxa
               
               if face_cropped(my_frame) is not None:  #image xa baney
                  img_id+=1 #image xa baney image ko sample plus hudai janxa
                  face=cv2.resize(face_cropped(my_frame),(450,450)) #fheri liyeko image in my_frame lai fheri cropped yaa resize garni
                  face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY) #ava tyo image (rectangle image sano sano) color ma hunxa fheri teslai gray ma convert garni
                  file_name_path="data/user."+str(user_id)+"."+str(img_id)+".jpg" #image ko sample jati data banni file ma with user.1.1 esari save hunxa.
                  #that is mailay sample diye banye suru ma mero id=1 hunxa and ek choti garexu so img_id pani 1 hunxa so it will save with name user.1.1
                  cv2.imwrite(file_name_path,face) #file lai then we pass faces through file path
                  cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2) #by default around the face ko mathi rectangle draw garxam tara esma cropped gareko data ko image store gareko xam so rectangle chaiyena
                                                                     #2 is font scale,(0,255,255)samma ko color hunxa, ani last ko 2 is thickness

                  cv2.imshow("Cropped Face",face) #then image lai show garxam camera lai

               if cv2.waitKey(1)==13 or int(img_id)==100: #face capture garera 100 sample ma rokkosh banera loop lagayem and wait key lay key pressed garyo ki nai banera wait garxa yedi garena baney -1 return gardinxa
                  break
            cap.release() #capture gareko release garxa
            cv2.destroyAllWindows() #This function destroys all of the windows created by OpenCV. It should be called after you're done with displaying images or videos to clean up resources and avoid memory leaks.
            messagebox.showinfo("Result","Generating data sets completed!!")
           except Exception as es:
              messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

           



if __name__ == "__main__":
    root=Tk() #calling root
    obj=Student(root)
    root.mainloop()
