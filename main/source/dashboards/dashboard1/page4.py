from tkinter import *
from functions import *

# function to display  page 4 title and content
def page4_content(title_frame, page_frame):
    title4_frame = Frame(title_frame)
    lb_title4 = Label(
        title_frame,
        text="Page 4",
        width=15,
        font=("Bold", 15),
        fg="blue",
        pady=5,
        bd=0,
        bg="#c3c3c3",
    )
    lb_title4.place(relx=0.5, rely=0.5, anchor=CENTER)
    title4_frame.pack(pady=20)

    page4_frame = Frame(page_frame)
    lb_page = Label(page_frame, text="Page 4 Component", font=("Bold", 30))
    lb_page.place(relx=0.5, rely=0.5, anchor=CENTER)
    page4_frame.pack(pady=20)
