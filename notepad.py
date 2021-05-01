from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    file = None
    root.title("Untitled - Notepad")
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension = ".txt", filetypes = [("all files", "*.*"), ("text document ", "*.txt")])

    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) +"- Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad by SK", "This is the Notepad by Shubham")
if __name__ == '__main__':
    root = Tk()
    root.title("NotePad by SK")
    root.geometry("588x600")
    TextArea= Text(root, font = "lucida 14")
    file = None

    TextArea.pack(expand = TRUE, fill = BOTH)

    menuBar = Menu(root)

    fileMenu = Menu(menuBar ,tearoff=0)

    fileMenu.add_command(label = "New", command= newFile)
    fileMenu.add_command(label = "Open", command = openFile)
    fileMenu.add_command(label = "Save", command = saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label = "Exit", command = quitApp)

    menuBar.add_cascade(label= "File", menu = fileMenu)

    editMenu = Menu(menuBar, tearoff = 0)
    editMenu.add_command(label = "Cut", command = cut)
    editMenu.add_command(label = "Copy", command = copy)
    editMenu.add_command(label = "Paste", command= paste)

    menuBar.add_cascade(label = "Edit", menu = editMenu)

    helpMenu = Menu(menuBar, tearoff = 0)
    helpMenu.add_command(label = "About", command = about)

    menuBar.add_cascade(label = "Help", menu = helpMenu)

    root.config(menu = menuBar)

    scroll = Scrollbar(TextArea)
    scroll.pack(side = RIGHT, fill = Y)
    scroll.config(command = TextArea.yview)
    TextArea.config(yscrollcommand = scroll.set)


    root.mainloop()