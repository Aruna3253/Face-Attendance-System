from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0") 
        self.root.title("Face Recogniton System")

        title_lbl = Label(self.root,text="FACE RECOGNITION",font=("Helvetica",25,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=35)

        img_top = Image.open(r"college_images\trainface2.jpg")
        img_top = img_top.resize((700,600),Image.LANCZOS)   
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=40,width=700,height=600)

        img_bottom = Image.open(r"college_images\trainface3.jpg")
        img_bottom = img_bottom.resize((700,600),Image.LANCZOS)   
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=703,y=40,width=700,height=600)
        
        #button in second image
        btn=Button(self.root,text="Face recognizer",command=self.face_recog,width=150,font=("times new roman",20,"bold"),bg="darkgreen",fg="white")
        btn.place(x=900,y=590,width=300,height=35)

    #attendance

    def mark_attendance(self,i,r,n,d):
        with open("Attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.strip().split(",")
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)) :
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")   
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},present")


    #Face recognition
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbour,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbour)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w]) #clf rreturns id and predict the confidence score ( distance between the closesttrained image and the test image.)
                confidence=int((100*(1-predict/300))) #convert preicted distnace into confidence percentage. 300 is threshold value. and predict/300 finds normalizatio 
                
                conn=mysql.connector.connect(host="localhost",username="root",password="Arun@poi098",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("SELECT Name FROM student WHERE StudentId=%s", (id,))
                n = my_cursor.fetchone()
                if n is not None:
                    n = "+".join(n)
                else:
                    n = "Unknown"

                my_cursor.execute("SELECT RollNo FROM student WHERE StudentId=%s", (id,))
                r = my_cursor.fetchone()
                if r is not None:
                    r = "+".join(r)
                else:
                    r = "Unknown"

                my_cursor.execute("SELECT Dep FROM student WHERE StudentId=%s", (id,))
                d = my_cursor.fetchone()
                if d is not None:
                    d = "+".join(d)
                else:
                    d = "Unknown"

                my_cursor.execute("SELECT StudentId FROM student WHERE StudentId=%s", (id,))
                i = my_cursor.fetchone()
                if i is not None:
                    i = "+".join(i)
                else:
                    i = "Unknown"


                if confidence>80: #we can give confidence on our own. 
                    cv2.putText(img,f"Id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,25,255),3) #nachineko face aayo baney

                coord=[x,y,w,h]
            return coord
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)    
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml") #uta train ko file ma yo file write garethem yeta read

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("welcome to face recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()




if __name__ == "__main__":
    root=Tk() #calling root
    obj=Face_Recognition(root)
    root.mainloop()