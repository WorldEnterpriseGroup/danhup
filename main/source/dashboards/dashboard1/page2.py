from tkinter import *
from functions import *

# function to display  page 2 title and content
def page2_content(title_frame, page_frame):
    title2_frame = Frame(title_frame)
    lb_title2 = Label(
        title_frame,
        text="Page 2",
        width=15,
        font=("Bold", 15),
        fg="blue",
        pady=5,
        bd=0,
        bg="#c3c3c3",
    )
    lb_title2.place(relx=0.5, rely=0.5, anchor=CENTER)
    title2_frame.pack(pady=20)

    page2_frame = Frame(page_frame)
    lb_page = Label(page_frame, text="Page 2 Component", font=("Bold", 30))
    lb_page.place(relx=0.5, rely=0.5, anchor=CENTER)
    page2_frame.pack(pady=20)
