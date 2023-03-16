from tkinter import *
import time
import os


global key
key = True
root = Tk()
root.geometry("1920x1080")
root.title("Welcome")

f = ("Times bold", 14)


def authMember():
    print(key)
    if key:
        root.destroy()
        os.system("python main/source/dashboards/dashboard1/dashboard.py")


Label(
    root, text="Checking License...", padx=20, pady=20, fg="gray", bg="white", font=f
).pack(expand=True, fill=BOTH)
root.after(1000, authMember)


root.mainloop()
