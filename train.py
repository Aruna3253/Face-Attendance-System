from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0") 
        self.root.title("Face Recogniton System")

        title = Label(self.root,text="TRAIN DATA SET",font=("Helvetica",25,"bold"),bg="white",fg="darkred")
        title.place(x=0,y=0,width=1530,height=35)

        img_top = Image.open(r"college_images\trainface.jpg")
        img_top = img_top.resize((1530,240),Image.LANCZOS)   
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1530,height=240)

        btn=Button(self.root,text="TRAIN DATA",command=self.train_classifier,width=1530,font=("times new roman",25,"bold"),bg="red",fg="white")
        btn.place(x=0,y=287,width=1530,height=30)

        img_bottom = Image.open(r"college_images\train.jpg")
        img_bottom = img_bottom.resize((1530,450),Image.LANCZOS)   
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=315,width=1530,height=450)
    
    def train_classifier(self): #now,we use LBPH algorithm in this function
        data_dir=("data") #file ko path
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)] #passing path in listcomprehensive in OS

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') #converting into grayscale image
            imageNp=np.array(img,'uint8') #using numpy array for image and coverting into grid (unsigned int as data types)
            id=int(os.path.split(image)[1].split('.')[1])
        #     C:\Users\Redstone\OneDrive\Desktop\Face Recognition System\data\user.1.1
        #      C bata index 0 start hunxa upto data. then,index=1 from user tyei bayera image[1] banera lekheko, then 
        # again user.1.1 bata neh 0 index garda user=0 index ma parxa array ma, then suru ko .1 is id which is located at index 1 so split 1 gareko
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids) #id lai numpy array ma lageko

        #==train the classifier and save
        clf = cv2.face.LBPHFaceRecognizer.create()
        clf.train(faces,ids)
        clf.write("classifier.xml") #image train garepaxi file ma save gareko, file ko name j rakhda neh hunxa
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training data sets completed")

        #----note---- we just trained our data over here, now we will recognized face in face_recognizer



if __name__ == "__main__":
    root=Tk() #calling root
    obj=Train(root)
    root.mainloop()