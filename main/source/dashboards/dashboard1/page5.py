from tkinter import *
from functions import *

# function to display  page 4 title and content
def page5_content(title_frame, page_frame):
    title5_frame = Frame(title_frame)
    lb_title5 = Label(
        title_frame,
        text="Page 5",
        width=15,
        font=("Bold", 15),
        fg="blue",
        pady=5,
        bd=0,
        bg="#c3c3c3",
    )
    lb_title5.place(relx=0.5, rely=0.5, anchor=CENTER)
    title5_frame.pack(pady=20)

    page5_frame = Frame(page_frame)
    lb_page = Label(page_frame, text="Page 5 Component", font=("Bold", 30))
    lb_page.place(relx=0.5, rely=0.5, anchor=CENTER)
    page5_frame.pack(pady=20)
