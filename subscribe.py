from tkinter import *

ws = Tk()
ws.geometry('1920x1080')
ws.title('Welcome')
ws['bg']='#ffbf00'

f = ("Times bold", 14)
 
def welcomePage():
    ws.destroy()
    import index

def subscribePage():
    ws.destroy()
    import subscribe

Label(
    ws,
    text="Subscribe",
    padx=20,
    pady=20,
    bg='#ffbf00',
    font=f
).pack(expand=True, fill=BOTH)

Button(
    ws, 
    text="Back to Home", 
    font=f,
    command=welcomePage
    ).pack(fill=X, expand=TRUE, side=LEFT)
Button(
    ws, 
    text="Subscribe", 
    font=f,
    command=subscribePage
    ).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()