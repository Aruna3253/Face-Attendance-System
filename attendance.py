from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[] #global variable  that is list to get csv data
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0") 
        self.root.title("Face Recogniton System")

        #=====variables======
        self.var_attendId=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_department=StringVar()
        self.var_Time=StringVar()
        self.var_Date=StringVar()
        self.var_attendance=StringVar()

        img_l = Image.open(r"college_images\student.png")
        img_l = img_l.resize((700,180),Image.LANCZOS)    
        self.photoImg_l = ImageTk.PhotoImage(img_l)

        f_lbl = Label(self.root,image=self.photoImg_l)
        f_lbl.place(x=0,y=0,width=700,height=180) 

        img_2 = Image.open(r"college_images\studentss.jpg")
        img_2 = img_2.resize((700,180),Image.LANCZOS)    
        self.photoImg_2 = ImageTk.PhotoImage(img_2)

        f_lbl = Label(self.root,image=self.photoImg_2)
        f_lbl.place(x=705,y=0,width=660,height=180) 

        title = Label(self.root,text="ATTENDANCE MANAGEMENT SYSTEM",font=("Helvetica",25,"bold"),bg="white",fg="darkred")
        title.place(x=0,y=183,width=1530,height=35)

        main_frame=Frame(self.root,bd=2,bg="white",relief=RIDGE) #bd=border
        main_frame.place(x=0,y=220,width=1530,height=475)
        
        #left frame 
        l=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Informatiom",font=("times new roman",12,"bold"))
        l.place(x=0,y=0,width=675,height=465)
                
        img = Image.open(r"college_images\studentss.jpg")
        img = img.resize((675,170),Image.LANCZOS)    
        self.photoImg = ImageTk.PhotoImage(img)

        f_lbl= Label(l,image=self.photoImg)
        f_lbl.place(x=0,y=0,width=675,height=170) 

        l1=LabelFrame(l,bd=2,bg="white",relief=RIDGE)
        l1.place(x=0,y=173,width=674,height=267)
         #1.
        AttendanceId_label=Label(l1,text="AttendanceId:",font=("times new roman",13,"bold"),bg="white")
        AttendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
   
        AttendanceId_entry=ttk.Entry(l1,width=15,textvariable=self.var_attendId,font=("times new roman",13,"bold"))
        AttendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
         #2.
        Roll_label=Label(l1,text="RollNo:",font=("times new roman",13,"bold"),bg="white")
        Roll_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
   
        Roll_entry=ttk.Entry(l1,width=15,textvariable=self.var_roll,font=("times new roman",13,"bold"))
        Roll_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        #3.
        Name_label=Label(l1,text="Name:",font=("times new roman",13,"bold"),bg="white")
        Name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
   
        Name_entry=ttk.Entry(l1,width=15,textvariable=self.var_name,font=("times new roman",13,"bold"))
        Name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        #4.
        Department_label=Label(l1,text="Department:",font=("times new roman",13,"bold"),bg="white")
        Department_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
   
        Department_entry=ttk.Entry(l1,width=15,textvariable=self.var_department,font=("times new roman",13,"bold"))
        Department_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        #5.
        Time_label=Label(l1,text="Time:",font=("times new roman",13,"bold"),bg="white")
        Time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
   
        Time_entry=ttk.Entry(l1,width=15,textvariable=self.var_Time,font=("times new roman",13,"bold"))
        Time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        #6.
        Date_label=Label(l1,text="Date:",font=("times new roman",13,"bold"),bg="white")
        Date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        Date_entry=ttk.Entry(l1,width=15,textvariable=self.var_Date,font=("times new roman",13,"bold"))
        Date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # 7.
        Attendance_label=Label(l1,text="Attendance",font=("times new roman",13,"bold"),bg="white")
        Attendance_label.grid(row=3,column=0,padx=10,sticky=W)
         
        Attendance_combo=ttk.Combobox(l1,font=("times new roman",13,"bold"),width=15,textvariable=self.var_attendance,state="read only")
        Attendance_combo['values']=("Status","Present","Absent")
        Attendance_combo.current(0) 
        Attendance_combo.grid(row=3,column=1,padx=2,pady=20,sticky=W)
        #button
        btn_frame=Frame(l1,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=180,width=675,height=40)

        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=22,font=("times new roman",9,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        export_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=22,font=("times new roman",9,"bold"),bg="blue",fg="white")
        export_btn.grid(row=0,column=1)

        Update_btn=Button(btn_frame,text="Update csv",command=self.update_csv,width=22,font=("times new roman",9,"bold"),bg="blue",fg="white")
        Update_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset csv",command=self.reset_fields,width=22,font=("times new roman",9,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        
        
        #right frame
        r=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        r.place(x=677,y=0,width=675,height=465)

        table_f=Frame(r,bd=2,bg="white",relief=RIDGE)
        table_f.place(x=5,y=5,width=655,height=400)

        #scrolllbar and table
        scroll_x=ttk.Scrollbar(table_f,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_f,orient=VERTICAL)
        
        self.AttendanceReport=ttk.Treeview(table_f,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReport.xview)
        scroll_y.config(command=self.AttendanceReport.yview)

        self.AttendanceReport.heading("id",text="Attendance ID")
        self.AttendanceReport.heading("roll",text="RollNo")
        self.AttendanceReport.heading("name",text="Name")
        self.AttendanceReport.heading("department",text="Department")
        self.AttendanceReport.heading("time",text="Time")
        self.AttendanceReport.heading("date",text="Date")
        self.AttendanceReport.heading("attendance",text="Attendance")
        
        self.AttendanceReport["show"]="headings"

        
      
        #setting width by using column
        columns = self.AttendanceReport["columns"]
        for column in columns:
         self.AttendanceReport.column(column, width=100)

        self.AttendanceReport.pack(fill=BOTH,expand=1)
        self.AttendanceReport.bind("<ButtonRelease>",self.get_cursor) #it binds get_cursor
        # self.fetch_data()
    
    #fetch data

    def fetchData(self,rows):
       self.AttendanceReport.delete(*self.AttendanceReport.get_children())
       for i in rows:
             self.AttendanceReport.insert("",END,values=i)
        

    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open Csv",filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),parent=self.root)#cwd is current working directory built in 
        if fln:
         with open(fln,newline='') as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
             mydata.append(i)
         self.fetchData(mydata)

    #export csv
    def exportCsv(self):
        try:
           if len(mydata)<1:
              messagebox.showerror("No data","No Data Found to export",parent=self.root)
              return False
           fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open Csv",filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),parent=self.root)#cwd is current working directory built in 
           with open(fln,mode="w",newline="") as myfile:
              exp_write=csv.writer(myfile,delimiter=",")
              for i in mydata:
                 exp_write.writerow(i)
              messagebox.showinfo("Data Export","Your data has exported successfully"+os.path.basename(fln)+"successfully")
        except Exception as es:
           messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)


    #
    def get_cursor(self,event):
       cursor_row=self.AttendanceReport.focus()
       content=self.AttendanceReport.item(cursor_row)
       rows=content['values']

       self.var_attendId.set(rows[0])
       self.var_roll.set(rows[1])
       self.var_name.set(rows[2])
       self.var_department.set(rows[3])
       self.var_Time.set(rows[4])
       self.var_Date.set(rows[5])
       self.var_attendance.set(rows[6])
    #update
    def update_csv(self):
        try:
            selected_item = self.AttendanceReport.selection()[0]
            self.AttendanceReport.item(selected_item, values=(self.var_attendId.get(), self.var_roll.get(), self.var_name.get(), self.var_department.get(), self.var_Time.get(), self.var_Date.get(), self.var_attendance.get()))
            for i in range(len(mydata)):
                if mydata[i][0] == self.var_attendId.get():
                    mydata[i] = [self.var_attendId.get(), self.var_roll.get(), self.var_name.get(), self.var_department.get(), self.var_Time.get(), self.var_Date.get(), self.var_attendance.get()]
                    break
            messagebox.showinfo("Success", "Record updated successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)
    

    #reset
    def reset_fields(self):
        self.var_attendId.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_department.set("")
        self.var_Time.set("")
        self.var_Date.set("")
        self.var_attendance.set("Status")


              
              
             
         


if __name__ == "__main__":
    root=Tk() #calling root
    obj=Attendance(root)
    root.mainloop()