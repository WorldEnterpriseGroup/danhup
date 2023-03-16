from tkinter import *
from functions import *

# function to display  page 6 title and content
def page6_content(title_frame, page_frame):
    title6_frame = Frame(title_frame)
    lb_title6 = Label(
        title_frame,
        text="Page 6",
        width=15,
        font=("Bold", 15),
        fg="blue",
        pady=5,
        bd=0,
        bg="#c3c3c3",
    )
    lb_title6.place(relx=0.5, rely=0.5, anchor=CENTER)
    title6_frame.pack(pady=20)

    page6_frame = Frame(page_frame)
    lb_page = Label(page_frame, text="Page 6 Component", font=("Bold", 30))
    lb_page.place(relx=0.5, rely=0.5, anchor=CENTER)
    page6_frame.pack(pady=20)
