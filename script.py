from tkinter import *
from datetime import date
from datetime import datetime
from Matrix import *

def determinant(rows, cols, matrix, root):
    window = Toplevel(root)
    window.title("Matrix")
    entries = []

    for i in range(rows):
        for j in range(cols):
            entry = Entry(window, width=5)
            entry.grid(row=i, column=j)
            entries.append(entry)
    
    def showEntries():
        matrix = setMatrix()
        answer = LabelFrame(window, text='Answer')
        answer.grid(row=3, column=3)
        Label(answer, text=det(matrix)).grid(row=3, column=4)
    def setMatrix():
        total = len(entries)
        i = 0
        temp_matrix = []
        curr_row = -1
        for e in entries:
            if i % rows == 0: # We need to reset the row.
                temp_matrix.append([])
                curr_row += 1
                temp_matrix[curr_row].append(int(e.get()))
            else:
                temp_matrix[curr_row].append(int(e.get()))
            i+=1
        return temp_matrix
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
    matrix = []
    btn = Button(labelframe, text='Go', command = lambda: determinant(int(rows_input.get()), int(cols_input.get()), matrix, ROOT))
    btn.pack()
    ROOT.mainloop()

if __name__ == "__main__":
    start()