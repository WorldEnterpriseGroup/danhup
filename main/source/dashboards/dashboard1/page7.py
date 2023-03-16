from tkinter import *
from functions import *

# function to display  page 7 title and content
def page7_content(title_frame, page_frame):
    title7_frame = Frame(title_frame)
    lb_title7 = Label(
        title_frame,
        text="Page 7",
        width=15,
        font=("Bold", 15),
        fg="blue",
        pady=5,
        bd=0,
        bg="#c3c3c3",
    )
    lb_title7.place(relx=0.5, rely=0.5, anchor=CENTER)
    title7_frame.pack(pady=20)

    page7_frame = Frame(page_frame)
    lb_page = Label(page_frame, text="Page 7 Component", font=("Bold", 30))
    lb_page.place(relx=0.5, rely=0.5, anchor=CENTER)
    page7_frame.pack(pady=20)
