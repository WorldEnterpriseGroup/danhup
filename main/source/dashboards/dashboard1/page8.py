from tkinter import *
from functions import *

# function to display  title and content
def page8_content(title_frame, page_frame):
    title8_frame = Frame(title_frame)
    lb_title8 = Label(
        title_frame,
        text="Page 8",
        width=15,
        font=("Bold", 15),
        fg="blue",
        pady=5,
        bd=0,
        bg="#c3c3c3",
    )
    lb_title8.place(relx=0.5, rely=0.5, anchor=CENTER)
    title8_frame.pack(pady=20)

    page8_frame = Frame(page_frame)
    lb_page = Label(page_frame, text="Page 8 Component", font=("Bold", 30))
    lb_page.place(relx=0.5, rely=0.5, anchor=CENTER)
    page8_frame.pack(pady=20)
