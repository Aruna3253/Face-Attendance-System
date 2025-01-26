# Face-Attendance-System
This project is an advanced face recognition system designed to automate student attendance. It utilizes Python's OpenCV library for real-time face detection and recognition, streamlining the process of recording attendance in educational settings.

Features
User Authentication: Secure login system with username and password protection.
Student Management: Add, update, delete, and manage student records.
Photo Capture: Capture and store photo samples for each student.
Training Module: Train the system with collected photo samples for accurate recognition.
Attendance Recording: Automatically mark attendance upon recognizing a student's face.
Attendance Reports: Generate and export attendance reports in Excel format and store them in a MySQL database.
Developer Information: Access details about the developer.
Help Desk: Assistance and guidance for users.

Technologies Used
Programming Language: Python 3.8.5
Libraries: OpenCV (for object detection and face recognition)
Database: MySQL
GUI Framework: Tkinter

Setup Instructions
Install Python 3.8.5: Ensure Python 3.8.5 is installed on your system.
Install Required Libraries: Use pip to install the necessary libraries:
bash
Copy
Edit
pip install opencv-python
pip install mysql-connector-python

Database Configuration: Set up a MySQL database and update the database connection settings in the project code.
Run the Application: Execute the main Python file to launch the application.

Usage
Login: Enter your username and password to access the system.
Student Management: Navigate to the student management section to add or update student information and capture photo samples.
Train System: Use the training module to process the photo samples for face recognition.
Take Attendance: Start the attendance module; the system will recognize faces in real-time and mark attendance accordingly.
Generate Reports: Access the attendance report section to view and export attendance records.

#More Detailed demonstration
#main.py
The main file consists of the home page with all the features on.

#student.py
Create the required database as mentioned in the file in mysql.
we have used haarscascade algorithm from open cv to take and upload photo sample, so the haarscascade xml file in haarscascadefrontface zip file, so extract it.I have collected 100 sample, you can change it, if you want. The data is then created and successfully saved in data folder.

#train.py
I have used LBPH algorithm from openCv to train the dataset, the trained file is availble in zip file of classifier.xml.

#Facerecognition.py
then, the face is recognized through this page.

#attendance.py
when attendance is completed it is saved in attendance.csv

The final interface of project:
![Screenshot (352)](https://github.com/user-attachments/assets/dcc5bb1e-2261-4e70-b9e9-23a2a41ac116)

The face recognition demonstration:
![Screenshot (351)](https://github.com/user-attachments/assets/58faeb27-ecfb-427c-831a-c371b164005c)


