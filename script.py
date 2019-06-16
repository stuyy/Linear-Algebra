from tkinter import *
from datetime import date
from datetime import datetime

def create(rows, cols, root):
    window = Toplevel(root)
    window.title("Matrix")
    entries_list = []

    for i in range(rows):
        for j in range(cols):
            entry = Entry(window, width=5)
            entry.grid(row=i, column=j)
            entries_list.append(entry)
        
    def showEntries():
        for i in entries_list:
            print(i.get())

    
    btn = Button(window, text='Go', command=lambda: showEntries())

    btn.grid()
    window.transient(root)
    window.grab_set()
    root.wait_window(window)

def start():
    ROOT = Tk()
    ROOT.title('Machine Learning')
    LOGO = PhotoImage(file='C:\\Users\\Anson\\Desktop\\neural.png')
    Title = Label(ROOT, text='Intro to Machine Learning').pack()
    Label(ROOT, image=LOGO).pack()


    Date = Label(ROOT, text="Today is {}".format(datetime.now().strftime("%B %d, %Y"))).pack()
    Time = Label(ROOT, text="The current time is {}".format(datetime.now().strftime("%I:%M %p"))).pack()

    labelframe = LabelFrame(ROOT, text='Matrix Calculator')
    labelframe.pack()

    rows = Label(labelframe, text='Enter Rows')
    cols = Label(labelframe, text='Enter Columns')

    rows_input = Entry(labelframe)
    rows.pack()

    rows_input.pack()
    cols.pack()

    cols_input = Entry(labelframe)
    cols_input.pack()
    
    btn = Button(labelframe, text='Go', command=lambda: create(int(rows_input.get()), int(cols_input.get()), ROOT))
    btn.pack()
    ROOT.mainloop()

if __name__ == "__main__":
    start()