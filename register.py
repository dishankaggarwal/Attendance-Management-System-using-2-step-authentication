import sqlite3

from tkinter import * 

root=Tk()
root.geometry("448x500")
root.title("Register")
root.configure(bg='#c6f5d0')

#register function
def register():
    first=first_name_entry.get()
    last=last_name_entry.get()
    enroll=enrollment_entry.get()

    first_name_entry.delete(0,'end')
    last_name_entry.delete(0,'end')
    enrollment_entry.delete(0,'end')

    
    #Create a database
    conn = sqlite3.connect('attendance.db')

    #Creating a cursor
    c=conn.cursor()

    c.execute("INSERT INTO students(first_name,last_name,enrollment_no) VALUES (?,?,?)",(first,last,enroll))

    #Commiting the changes
    conn.commit()


    #Closing the connection 
    conn.close()






def show():
    #Create a database
    conn = sqlite3.connect('attendance.db')

    #Creating a cursor
    c=conn.cursor()

    c.execute("SELECT * FROM students")
    item=c.fetchall()
    for items in item:
        print(items)
    #Commiting the changes
    conn.commit()


    #Closing the connection 
    conn.close()





Label(root,text="Register Student",bg='grey',font=('Comic Sans MS Bold',32) ).pack()

Label(root,text="First Name").pack(pady=20)

first_name_entry=Entry(root)
first_name_entry.pack()

Label(root,text="Last Name").pack(pady=20)

last_name_entry=Entry(root)
last_name_entry.pack()
Label(root,text="Enrollment No.").pack(pady=20)

enrollment_entry=Entry(root)
enrollment_entry.pack()


my_button=Button(root,text='Register',command=register).pack(pady=30)

display_button=Button(root,text="show details",command=show).pack()

#Create a table
# c.execute("""CREATE TABLE students(
#      first_name text,
#      last_name text,
#      enrollment_no text PRIMARY KEY,
#      qr_code text DEFAULT 'NO',
#      image_recog text DEFAULT 'NO',
#      attendance text DEFAULT 'NO'
#      )""")





root.mainloop()