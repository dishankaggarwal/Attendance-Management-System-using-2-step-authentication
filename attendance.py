from contextlib import nullcontext
from tkinter import *
import cv2 
import numpy as np 
import pyzbar.pyzbar as pyzbar
import sys
import time
import pybase64
import sqlite3
import os

root=Tk()
root.title("Mark Attendance")
root.geometry("1300x700")
root.config(bg='#f33f3a')

#Function for Image recognition
def image_recognition():
    print('Image recognition code is running')
    os.system("python main.py")
    Label(root,text="Attendance for "+result+" is marked").pack()


#Function for checking data
def checkData(data,list):
    data=str(data)
    l = data.split("'")
    global result
    result=pybase64.b64decode(l[1]).decode('utf-8')
    #Create a database
    conn = sqlite3.connect('attendance.db')

    #Creating a cursor
    c=conn.cursor()
    
    sql_update_query="""UPDATE students SET qr_code='YES' WHERE enrollment_no=?"""
    update_data=(result,)
    c.execute(sql_update_query,update_data)

    print("table updated successfully")
    Label(root,text='QR code for '+result+' is matched ').pack()

    image_button=Button(root,text="Click here to Recognise Image",font=('Comic Sans MS Bold',20),bg='yellow',command=image_recognition)
    image_button.pack(pady=80)
    list[0]=1
    
    #Commiting the changes
    conn.commit()


    #Closing the connection 
    conn.close()


#Function for qr scanning
def scan_qr():
    
    
    cap=cv2.VideoCapture(0)

    while True:
        _,frame= cap.read()
        decodedObject=pyzbar.decode(frame)
        list=[0]
        for obj in decodedObject:
            

            
            checkData(obj.data,list)
            print(list[0])
            time.sleep(1)
            
 
        cv2.imshow('Frame', frame)
        if list[0]==1:
                cv2.destroyAllWindows()
                break

        #close
        if cv2.waitKey(1) & 0xFF==ord('s'):
            cv2.destroyAllWindows()
            break


Label(root, text="Welcome to Maharaja Surajmal attendance portal",font=('Comic Sans MS Bold',32)).pack()

qr_button=Button(root,text='Click here to scan QR Code',font=('Comic Sans MS Bold',20),bg='yellow',command=scan_qr)
qr_button.pack(pady=60)

root.mainloop()