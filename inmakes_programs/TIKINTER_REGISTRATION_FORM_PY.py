from tkinter import  *
root=Tk()
l1 = Label(root,text ="Username")
l2 = Label(root,text ="Mobile number")
l3 = Label(root,text="E.mail id")
l4 = Label(root,text="Age")
l5 = Label(root,text="Password")
l6 = Label(root,text="Confirm Password")

button1=Button(root,text="Sign up",fg="white",bg="dark green")
button.
button2=Button(root,text="Cancel",fg="white",bg="dark red")

entry1 = Entry(root,bg="light blue")
entry2 = Entry(root,bg="light blue")
entry3 = Entry(root,bg="light blue")
entry4 = Entry(root,bg="light blue")
entry5 = Entry(root,bg="light blue")
entry6 = Entry(root,bg="light blue")

l1.grid(row=0,column=0)
entry1.grid(row=0,column=1)
l2.grid(row=1,column=0)
entry2.grid(row=1,column=1)
l3.grid(row=2,column=0)
entry3.grid(row=2,column=1)
l4.grid(row=3,column=0)
entry4.grid(row=3,column=1)
l5.grid(row=4,column=0)
entry5.grid(row=4,column=1)
l6.grid(row=5,column=0)
entry6.grid(row=5,column=1)
button1.grid(row=6,column=0)
button2.grid(row=6,column=1)

root.mainloop()
