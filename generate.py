from MyQR import myqr
import os
import base64
import sqlite3
from tkinter import *

root=Tk()
root.title("Generate QR codes")
root.geometry("1000x500")
root.config(bg='#f34376')

def reset():
    #Create a database
    conn = sqlite3.connect('attendance.db')

    #Creating a cursor
    c=conn.cursor()

    c.execute("""UPDATE students SET qr_code='NO',image_recog='NO',attendance='NO'""")
    
    #Commiting the changes
    conn.commit()


    #Closing the connection 
    conn.close()
    Label(root,text='Attendance reset Done!').pack(pady=10)

def generate():
    #Create a database
    conn = sqlite3.connect('attendance.db')

    #Creating a cursor
    c=conn.cursor()
    names=[]
    c.execute("SELECT * FROM students")
    name=c.fetchall()
    for items in name:
        names.append(items[2])
    print(names)

    #Commiting the changes
    conn.commit()
    #Closing the connection 
    conn.close()

    for item in names:
        data=item.encode()
        name = base64.b64encode(data)

        version, level , qr_name=myqr.run(
            str(name),
            level='H',
            version=1,


            #background

            picture= 'maharaja.jpg',
            contrast=1.0,
            brightness=1.0,
            colorized= True,

            save_name = str(item+'.bmp'),
            save_dir= os.getcwd()
        )

Label(root,text='Welcome to Maharaja Surajmal QR generation portal',font=("Comic Sans MS",24)).pack()

my_button=Button(root,text="Click here to generate QR codes",font=("Comic Sans MS",20),bg='yellow',command=generate)
my_button.pack(pady=70)

my_button2=Button(root,text="Click here to reset attendance",font=("Comic Sans MS",20),bg='yellow',command=reset)
my_button2.pack()

root.mainloop()
