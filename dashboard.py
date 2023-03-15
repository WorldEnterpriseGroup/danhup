from tkinter import *

ws = Tk()
ws.geometry('1920x1080')
ws.title("Dashboard")


def  Page_Switch(pageNumber):
    if pageNumber == "page1":
        ws.destroy()
        import page_1
    elif pageNumber == "page2":
        ws.destroy()
        import page_2
    elif pageNumber == "page3":
        ws.destroy()
        import page_3
    elif pageNumber == "page4":
        ws.destroy()
        import page_4
    elif pageNumber == "page5":
        ws.destroy()
        import page_5
    elif pageNumber == "page6":
        ws.destroy()
        import page_6
    elif pageNumber == "page7":
        ws.destroy()
        import page_7
    elif pageNumber == "page8":
        ws.destroy()
        import page_8


button_1 = Button(ws, text="Page 1", font=('Arial',24), padx=23, pady=23, command=lambda: Page_Switch("page1"))
button_2 = Button(ws, text="Page 2", font=('Arial',24), padx=23, pady=23, command=lambda: Page_Switch("page2"))
button_3 = Button(ws, text="Page 3", font=('Arial',24), padx=23, pady=23, command=lambda: Page_Switch("page3"))
button_4 = Button(ws, text="Page 4", font=('Arial',24), padx=23, pady=23, command=lambda: Page_Switch("page4"))
button_5 = Button(ws, text="Page 5", font=('Arial',24), padx=23, pady=23, command=lambda: Page_Switch("page5"))
button_6 = Button(ws, text="Page 6", font=('Arial',24), padx=23, pady=23, command=lambda: Page_Switch("page6"))
button_7 = Button(ws, text="Page 7", font=('Arial',24), padx=23, pady=23, command=lambda: Page_Switch("page7"))
button_8 = Button(ws, text="Page 8", font=('Arial',24), padx=23, pady=23, command=lambda: Page_Switch("page8"))


button_1.grid(row=0, column=1)
button_2.grid(row=0, column=2)
button_3.grid(row=0, column=3)
button_4.grid(row=0, column=4)
button_5.grid(row=1, column=1)
button_6.grid(row=1, column=2)
button_7.grid(row=1, column=3)
button_8.grid(row=1, column=4)

ws.mainloop()