import json
import tempfile
from pydoc import text
from tkinter import *
from tkinter import ttk, filedialog
from tkinter import font
import tkinter.messagebox
from tkinter import colorchooser
import os, sys
import win32print
import win32api
root = Tk()
root.geometry("700x500")


class Tkinter(object):
    pass


# class
def entry(args):
    pass


class Window(Frame):
    current_open_file = "no_file"

    # def __init__
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.settings = None
        self.default_path_to_pref = None
        self.editor = None
        self.path = None
        self.entry = None
        self.master = master
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # fileMenu
        fileMenu = Menu(menu)
        fileMenu.add_command(label="Save", command=self.save)
        fileMenu.add_command(label="Save as", command=self.saveas)
        fileMenu.add_command(label="Opain", command=self.opain)
        fileMenu.add_command(label="New Window", command=self.window)
        fileMenu.add_separator()
        fileMenu.add_command(label="Page Setup...", command=self.print)
        fileMenu.add_command(label="Print...", command=self.print)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="File", menu=fileMenu)

        # editMenu
        editMenu = Menu(menu)
        editMenu.add_command(label="Undo     Ctrl+z", command=entry.edit_undo)
        editMenu.add_command(label="Redo     Ctrl+y", command=entry.edit_redo)

        menu.add_cascade(label="Edit", menu=editMenu)

        # Transferring filesMenu
        transferringfilesMenu = Menu(menu)
        transferringfilesMenu.add_command(label="pdf to wrd",command=self.pdf)
        transferringfilesMenu.add_command(label="jpg to png", command=self.jpg)
        transferringfilesMenu.add_command(label="png to jpg", command=self.jpg)
        menu.add_cascade(label="Convert a file", menu=transferringfilesMenu)

        # helpMenu
        helpMenu = Menu(menu)
        helpMenu.add_command(label="View Help", command=self.viewhelp)
        menu.add_cascade(label="Help", menu=helpMenu)


    # def
    # jpg
    def jpg(self):
        from fhhg import root
    # pdf
    def pdf(self):
        from rr import root
    # View Help
    def viewhelp(self):
        tkinter.messagebox.showinfo('View Help', 'Hi, if you need help, read and learn If you want to save the file, go to File, you will find a New window, Save, Save, S, Open, Print, Page Setup, and Exit. If you want to modify, go to Edit')
    # window
    def window(self):
        from text import root

    # print
    def print(self):
        #printnter_name = win32print.GetDefaultPrinter()
        #entry.config(text=printnter_nasme)
        file = text=entry

        if file:
            win32api.ShellExecute(0, 'print', file, None, '.', 0)


    # exitProgram
    def exitProgram(self):
        exit()

    # saveas
    def saveas(self):
        import tkinter.filedialog
        opain = filedialog.asksaveasfilename(defaultextension=".*", title="Save File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"), ("html", "*.html")))
        if opain is None:
            return ()
        entry = self.entry.get(1.0, END)
        opain.write(entry)
        opain.close()
        self.current_open_file = entry.name

    # save
    def save(self, tkFileDialog=None):
        s = {key: self.settings[key].get() for key in self.settings}

        if self.store_last_settings:
            if not ttk.path.exists(self.default_path_to_pref):
                ttk.makedirs(self.default_path_to_pref)
            with open(ttk.path.join(self.default_path_to_pref,
                                    '_last_settings.json'), 'w') as f:
                f.write(json.dumps(s))
            self.store_last_settings = False
        else:
            path_to_pref = filedialog.asksaveasfilename(
                defaultextension='.json', filetypes=[("json files", '*.json')],
                initialdir=self.default_path_to_pref,
                title="Choose filename")
            with open(path_to_pref, 'w') as f:
                f.write(json.dumps(s))
        root.title('New File - TextPad!')

    # opain
    def opain(self):
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select A File",filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
        root.title('file - Notepad pro')



# text
entry = Text(root, height=43, width=170, wrap=WORD, undo=True)
entry.place(x=0, y=0)
app = Window(root)
root.wm_title("Notepad pro")
# icon
photo = PhotoImage(file="62930-clipboard-icon.png")
root.iconphoto(False, photo)
def hi():
    file = text = entry

    if file:
        win32api.ShellExecute(0, 'print', file, None, '.', 0)

root.iconify()
root.deiconify()
root.mainloop()
