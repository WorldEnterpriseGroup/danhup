from tkinter import *
from functions import *
# function to display  page 1 title and content
def page1_content(title_frame, page_frame):
    title1_frame =Frame(title_frame)
    lb_title1= Label(title_frame, text="Page 1", width=15, font=(
    'Bold', 15), fg='blue', pady=5, bd=0, bg='#c3c3c3')
    lb_title1.place(relx=0.5, rely=0.5, anchor=CENTER)
    title1_frame.pack(pady =20)

    page1_frame =Frame(page_frame)
    lb_page= Label(page_frame, text='Page 1 Component', font = ('Bold', 30))
    lb_page.place(relx=0.5, rely=0.5, anchor=CENTER)
    page1_frame.pack(pady =20)