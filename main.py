from tkinter import *
from tkinter import filedialog
from pypdf import *

app = Tk()
app.title('Python File Reader')
heading = Label(text="File Reader", bg='grey', fg='white', font=12, width=500, height=3)
heading.pack()  # to make the heading in center
app.geometry("650x1200")
app.configure(bg="#D8E9E6")

# Create Open file button function
def open_txt():
    file = filedialog.askopenfilename(title="Open Text File", filetypes=(("Text Files", "*.txt"),))
    name = file
    name = name.replace(".txt", "")

    file = open(file, 'r')
    stuff = file.read()

    my_text.insert(END, stuff)
    file.close()

    app.title(f'{name} - Textpad')

# Create Save button function
def save_txt():
    file = filedialog.askopenfilename(title="Open Text File", filetypes=(("Text Files", "*.txt"),))
    file = open(file, 'w')
    file.write(my_text.get(1.0, END))

my_frame = Frame(app)
my_frame.pack(pady=15)

# Create scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

my_text = Text(my_frame, width=80, height=25, font=("Sylfaen",10 ),bg='white', fg="black",
               yscrollcommand=text_scroll.set, undo=True)
my_text.pack()

# Configure our scrollbar
text_scroll.config(command=my_text.yview())

open_button = Button(app, text="Open Text File", command=open_txt)
open_button.pack(pady=20)

save_button = Button(app, text="Save File", command=save_txt)
save_button.pack(pady=20)

app.mainloop()
