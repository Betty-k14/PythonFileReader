import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import font
import pandas as pd
import os
from PyPDF2 import PdfReader

app = Tk()
app.title('Python File Reader')
heading = Label(text="File Reader", bg='grey', fg='white', font=12, width=500, height=3)
heading.pack()  #to make the heading in center
app.geometry("650x1200")
app.configure(bg = "#D8E9E6")

# Labels
NumPages_txt = Label(text="Num of Pages: ")
viewPage_txt = Label(text="Enter the page number to view: ")
newFile_txt = Label(text="Enter new file name to copy data to: ")

# placing labels on ui
NumPages_txt.place(x=15,y=600)
viewPage_txt.place(x=15,y=630)
newFile_txt.place(x=15,y=660)

# Variables
pageNum = IntVar()
viewPage = IntVar()
newFile = StringVar()

# entry boxes to take values
pageNum_e = Label( width=25)
viewPage_e = Entry(textvariable=viewPage, width=25)
newFile_e = Entry(textvariable=newFile, width=30)

# placing entry boxes on ui
pageNum_e.place(x=230,y=600)
viewPage_e.place(x=230,y=630)
newFile_e.place(x=230,y=660)

def clear_text():
    my_text.delete(1.0, END)

def open_file():
    file = filedialog.askopenfilename(title="Open Text File", filetypes=[("All files", "*.*")])
    pdfReader = PdfReader(file)

    # printing number of pages in pdf file
    length= len(pdfReader.pages)
    # creating a page object
    pageObj = pdfReader.pages[viewPage.get()]

    # extracting text from page
    my_text.insert(END, pageObj.extract_text())
    pageNum_e.config(text=str(length))

def save_txt():
    text_file = newFile.get()+str(".txt")
    print(text_file)
    text_file = open(text_file, 'w')
    text_file.write(my_text.get(1.0, END))

my_frame = Frame(app)
my_frame.pack(pady=50)

# Create scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

my_text = Text(my_frame, width=50, height=15, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black",
			   yscrollcommand=text_scroll.set, undo=True)
my_text.pack()

# Configure our scrollbar
text_scroll.config(command=my_text.yview)
#
# Buttons
open_button = Button(app, text="Open File", command=open_file).place(x=180,y=520)
save_button = Button(app, text="Save File", command=save_txt).place(x=280,y=520)
clear_button = Button(app, text="Clear Textbox", command=clear_text).place(x=380,y=520)


app.mainloop()
