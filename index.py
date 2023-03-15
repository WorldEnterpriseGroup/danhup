from tkinter import *

ws = Tk()
ws.geometry('1920x1080')
ws.title('Welcome')
ws['bg']='#5d8a82'

f = ("Times bold", 14)
global userkey
userkey = "1234"
def  authMember(key):
     if key.get() ==  userkey:
        ws.destroy()
        import dashboard
     else :
        ws.destroy()
        import subscribe
def checkMember():
    key = Entry(ws,
        width=15,
        font=('Arial',16),
        text="click Me!",
        fg="black",
        bg="white")
    key.pack(pady=10)
    key.insert(0, "Enter your key")
    Button(
        ws, 
        text="Check Membership", 
        fg='white',
        bg='gray',
        font=f,
        command=lambda: authMember(key)
    ).pack(pady=10)
     
   
Label(
    ws,
    text="WELCOME SCREEN",
    padx=20,
    pady=20,
    fg='gray',
    bg='white',
    font=f
).pack(expand=True, fill=BOTH)


check = Button(
    ws, 
    padx=20,
    text="Go To Dashboard", 
    fg='white',
    bg='gray',
    font=f,
    command=checkMember
    ).pack(pady=10)

ws.mainloop()