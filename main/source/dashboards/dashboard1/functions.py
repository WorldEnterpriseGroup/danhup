def changeOnHover(button, colorOnHover, colorOnLeave):
    # background on entering the widget
    button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover))

    # background on leaving the widget
    button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))


# function to remove current page title and component for being replaced
def delete_pages(title_frame, page_frame):
    for t_frame in title_frame.winfo_children():
        t_frame.destroy()
    for frame in page_frame.winfo_children():
        frame.destroy()


# function to control indicators and pages
def indicator(lb, page, title_frame, page_frame, hide_indicators):
    hide_indicators()
    lb.config(bg="#8ca5e3")
    lb.place(width=173, height=35)
    delete_pages(title_frame, page_frame)
    page()


# function to show or hide pages controllers button on drop down
def show_pages(sidebar_frame):
    global hidden
    if hidden:
        sidebar_frame.place_forget()
    else:
        sidebar_frame.place(x=15, y=85)
        sidebar_frame.pack_propagate(False)
        sidebar_frame.configure(width=200, height=320)
    hidden = not hidden


hidden = True
