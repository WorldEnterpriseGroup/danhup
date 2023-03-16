from tkinter import *
from functions import *

# function to display  page 3 title and content
def page3_content(title_frame, page_frame):
    title3_frame = Frame(title_frame)
    lb_title3 = Label(
        title_frame,
        text="Page 3",
        width=15,
        font=("Bold", 15),
        fg="blue",
        pady=5,
        bd=0,
        bg="#c3c3c3",
    )
    lb_title3.place(relx=0.5, rely=0.5, anchor=CENTER)
    title3_frame.pack(pady=20)

    page3_frame = Frame(page_frame)
    lb_page = Label(page_frame, text="Page 3 Component", font=("Bold", 30))
    lb_page.place(relx=0.5, rely=0.5, anchor=CENTER)
    page3_frame.pack(pady=20)
