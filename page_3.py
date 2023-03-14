from tkinter import *

ws = Tk()
ws.geometry('700x500')
ws.title('Welcome')
ws['bg']='#ffbf00'
 
def welcomePage():
    ws.destroy()
    import index

def dashPage():
    ws.destroy()
    import dashboard

Label(
    ws,
    text="Page 3",
    padx=20,
     font=('Arial',48),
    pady=20,
    bg='#6fbf00',
).pack(expand=True, fill=BOTH)

Button(
    ws, 
    text="Back to Home", 
    command=welcomePage
    ).pack(fill=X, expand=TRUE, side=LEFT)
Button(
    ws, 
    text="Back To Dashboard", 
    command=dashPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()