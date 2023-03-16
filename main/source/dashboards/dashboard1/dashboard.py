from tkinter import *
from functions import *
from page1 import *
from page2 import *
from page3 import *
from page4 import *
from page5 import *
from page6 import *
from page7 import *
from page8 import *


def hide_indicators():
    page1_btn_indicator.config(bg="#c3c3c3")
    page1_btn_indicator.place(width=0, height=0)

    page2_btn_indicator.config(bg="#c3c3c3")
    page2_btn_indicator.place(width=0, height=0)

    page3_btn_indicator.config(bg="#c3c3c3")
    page3_btn_indicator.place(width=0, height=0)

    page4_btn_indicator.config(bg="#c3c3c3")
    page4_btn_indicator.place(width=0, height=0)

    page5_btn_indicator.config(bg="#c3c3c3")
    page5_btn_indicator.place(width=0, height=0)

    page6_btn_indicator.config(bg="#c3c3c3")
    page6_btn_indicator.place(width=0, height=0)

    page7_btn_indicator.config(bg="#c3c3c3")
    page7_btn_indicator.place(width=0, height=0)

    page8_btn_indicator.config(bg="#c3c3c3")
    page8_btn_indicator.place(width=0, height=0)


root = Tk()

root.geometry("1920x1080")
root.title("Dashboard")

# set window color
root.configure(bg="#c3c3c3")

# Sidebar frame, a container of pages controller (drop down).
sidebar_frame = Frame(root, bg="#e2e0e0")
# page to show or hide dropdown controllers
show_btn = Button(
    root,
    text="Show pages",
    width=17,
    cursor="hand2",
    font=("Bold", 15),
    bg="#e2e0e0",
    fg="#000000",
    bd=0,
    command=lambda: show_pages(sidebar_frame),
)
show_btn.place(x=15, y=52)

# page one controller button for calling dedicated functon to change page to page 1
page1_btn = Button(
    sidebar_frame,
    text="Page 1",
    width=15,
    cursor="hand2",
    font=("Bold", 15),
    fg="#000000",
    bd=0,
    bg="#c3c3c3",
    command=lambda: indicator(
        page1_btn_indicator,
        lambda: page1_content(title_frame, page_frame),
        title_frame,
        page_frame,
        hide_indicators,
    ),
)
page1_btn.place(x=10, y=5)
changeOnHover(page1_btn, "#8ca5e3", "#c3c3c3")
page1_btn_indicator = Label(
    sidebar_frame, text="Page 1", cursor="hand2", font=("Bold", 15), bg="#c3c3c3"
)
page1_btn_indicator.place(x=10, y=5, width=0, height=0)
page1_btn_indicator.lift()

# page two controller button for calling dedicated functon to change page to page 2
page2_btn = Button(
    sidebar_frame,
    text="Page 2",
    width=15,
    cursor="hand2",
    font=("Bold", 15),
    fg="#000000",
    bd=0,
    bg="#c3c3c3",
    command=lambda: indicator(
        page2_btn_indicator,
        lambda: page2_content(title_frame, page_frame),
        title_frame,
        page_frame,
        hide_indicators,
    ),
)
page2_btn.place(x=10, y=43)
changeOnHover(page2_btn, "#8ca5e3", "#c3c3c3")
page2_btn_indicator = Label(
    sidebar_frame, text="Page 2", cursor="hand2", font=("Bold", 15), bg="#c3c3c3"
)
page2_btn_indicator.place(x=10, y=43, width=0, height=0)

# page three controller button for calling dedicated functon to change page to page 3
page3_btn = Button(
    sidebar_frame,
    text="Page 3",
    width=15,
    cursor="hand2",
    font=("Bold", 15),
    fg="#000000",
    bd=0,
    bg="#c3c3c3",
    command=lambda: indicator(
        page3_btn_indicator,
        lambda: page3_content(title_frame, page_frame),
        title_frame,
        page_frame,
        hide_indicators,
    ),
)
page3_btn.place(x=10, y=81)
changeOnHover(page3_btn, "#8ca5e3", "#c3c3c3")
page3_btn_indicator = Label(
    sidebar_frame, text="Page 3", cursor="hand2", font=("Bold", 15), bg="#c3c3c3"
)
page3_btn_indicator.place(x=10, y=81, width=0, height=0)

# page four controller button for calling dedicated functon to change page to page 4
page4_btn = Button(
    sidebar_frame,
    text="Page 4",
    width=15,
    cursor="hand2",
    font=("Bold", 15),
    fg="#000000",
    bd=0,
    bg="#c3c3c3",
    command=lambda: indicator(
        page4_btn_indicator,
        lambda: page4_content(title_frame, page_frame),
        title_frame,
        page_frame,
        hide_indicators,
    ),
)
page4_btn.place(x=10, y=119)
changeOnHover(page4_btn, "#8ca5e3", "#c3c3c3")
page4_btn_indicator = Label(
    sidebar_frame, text="Page 4", cursor="hand2", font=("Bold", 15), bg="#c3c3c3"
)
page4_btn_indicator.place(x=10, y=119, width=0, height=0)

# page five controller button for calling dedicated functon to change page to page 5
page5_btn = Button(
    sidebar_frame,
    text="Page 5",
    width=15,
    cursor="hand2",
    font=("Bold", 15),
    fg="#000000",
    bd=0,
    bg="#c3c3c3",
    command=lambda: indicator(
        page5_btn_indicator,
        lambda: page5_content(title_frame, page_frame),
        title_frame,
        page_frame,
        hide_indicators,
    ),
)
page5_btn.place(x=10, y=157)
changeOnHover(page5_btn, "#8ca5e3", "#c3c3c3")
page5_btn_indicator = Label(
    sidebar_frame, text="Page 6", cursor="hand2", font=("Bold", 15), bg="#c3c3c3"
)
page5_btn_indicator.place(x=10, y=157, width=0, height=0)

# page six controller button for calling dedicated functon to change page to page 6
page6_btn = Button(
    sidebar_frame,
    text="Page 6",
    width=15,
    cursor="hand2",
    font=("Bold", 15),
    fg="#000000",
    bd=0,
    bg="#c3c3c3",
    command=lambda: indicator(
        page6_btn_indicator,
        lambda: page6_content(title_frame, page_frame),
        title_frame,
        page_frame,
        hide_indicators,
    ),
)
page6_btn.place(x=10, y=195)
changeOnHover(page6_btn, "#8ca5e3", "#c3c3c3")
page6_btn_indicator = Label(
    sidebar_frame, text="Page 6", cursor="hand2", font=("Bold", 15), bg="#c3c3c3"
)
page6_btn_indicator.place(x=10, y=195, width=0, height=0)

# page seven controller button for calling dedicated functon to change page to page 7
page7_btn = Button(
    sidebar_frame,
    text="Page 7",
    width=15,
    cursor="hand2",
    font=("Bold", 15),
    fg="#000000",
    bd=0,
    bg="#c3c3c3",
    command=lambda: indicator(
        page7_btn_indicator,
        lambda: page7_content(title_frame, page_frame),
        title_frame,
        page_frame,
        hide_indicators,
    ),
)
page7_btn.place(x=10, y=233)
changeOnHover(page7_btn, "#8ca5e3", "#c3c3c3")
page7_btn_indicator = Label(
    sidebar_frame, text="Page 7", cursor="hand2", font=("Bold", 15), bg="#c3c3c3"
)
page7_btn_indicator.place(x=10, y=233, width=0, height=0)

# page eight controller button for calling dedicated functon to change page to page 8
page8_btn = Button(
    sidebar_frame,
    text="Page 8",
    width=15,
    cursor="hand2",
    font=("Bold", 15),
    fg="#000000",
    bd=0,
    bg="#c3c3c3",
    command=lambda: indicator(
        page8_btn_indicator,
        lambda: page8_content(title_frame, page_frame),
        title_frame,
        page_frame,
        hide_indicators,
    ),
)
page8_btn.place(x=10, y=271)
changeOnHover(page8_btn, "#8ca5e3", "#c3c3c3")
page8_btn_indicator = Label(
    sidebar_frame, text="Page 8", cursor="hand2", font=("Bold", 15), bg="#c3c3c3"
)
page8_btn_indicator.place(x=10, y=271, width=0, height=0)
sidebar_frame.place(x=15, y=85)
sidebar_frame.pack_propagate(False)
sidebar_frame.configure(width=200, height=320)

# Title frame, a container of pages title.
title_frame = Frame(root, bg="#e2e0e0")
title_label = Label(
    title_frame,
    text="Page 1",
    width=15,
    font=("Bold", 15),
    fg="blue",
    pady=5,
    bd=0,
    bg="#c3c3c3",
)
title_label.place(relx=0.5, rely=0.5, anchor=CENTER)
title_frame.pack(side=TOP)
title_frame.pack_propagate(False)
title_frame.configure(width=1270, height=50)

# Pages frame, a container of pages content.
page_frame = Frame(root, bg="#c3c3c3")
page_frame.pack(side=RIGHT)
page_frame.pack_propagate(False)
page_frame.place(x=200, y=52)
page_frame.configure(width=1070, height=600)
lb_page = Label(page_frame, text="Page 1 Component", font=("Bold", 30))
lb_page.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()
