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
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfile
from PyPDF2 import PdfFileReader



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
        from PIL import Image, ImageTk
          # It will contain open and save dialog boxes

        '''Functions which are being used in the program (To convert JPG to PNG and Vice Versa)'''

        def jpgtopng():
            root.config(bg='#badc57')

            def getjpgfile():
                global pic
                file_path = fd.askopenfilename()
                pic = Image.open(
                    file_path)  # It will open the file and will store it in pic variable (.open and .save are the methods of Image of PIL Module)

            def savepngfile():
                global pic
                export_file_path = fd.asksaveasfilename(defaultextension='.png',
                                                        filetypes=[('Image (.png file)', '.png')])
                pic.save(export_file_path)  # It will save the file to the specified path

            global Head
            imagelabel.destroy()
            f1.destroy()
            Head.destroy()
            Head = Label(text='JPG To PNG Converter', font='Lucida 20 bold', bg='black', fg='#F4C724', padx=5, pady=5)
            Head.pack(pady=10)
            # To get jpg file
            browse_jpg = Button(text="      Import JPG File     ", bg='#BB2CD9', fg='white',
                                font=('helvetica', 15, 'bold'),
                                command=getjpgfile)
            browse_jpg.pack(pady=20)
            # To save jpg file
            save_jpg = Button(text='  Convert JPG To PNG  ', bg='#BB2CD9', fg='white', font=('helvetica', 15, 'bold'),
                              command=savepngfile)
            save_jpg.pack(pady=10)

            # Image in bottom
            bottom_pic = Image.open('Images/jtop.jpg')
            bottom_pic = bottom_pic.resize((400, 250), Image.ANTIALIAS)
            bg_pic = ImageTk.PhotoImage(bottom_pic)
            img_label = Label(root, image=bg_pic)
            img_label.image = bg_pic  # It will make a reference or keep a reference
            img_label.pack(side=BOTTOM, pady=40)

            # Close Button
            close = Button(text='Close', command=root.destroy, bg='black', fg='white', font='11')
            close.place(x=205, y=422)

        def pngtojpg():
            root.config(bg='#67E6DC')

            def getpngfile():
                global pic
                file_location = fd.askopenfilename()
                pic = Image.open(file_location)  # It will store the selected file in pic variable
                pic = pic.convert(
                    'RGB')  # It will covert the file from RGBA to RGB coz PNG files have some transparency or alpha value so we need to remove that to make it a JPG file.

            def savejpgfile():
                global pic
                export_file_location = fd.asksaveasfilename(defaultextension='.jpg')
                pic.save(export_file_location)  # It will save the image to a specified location

            global Head
            imagelabel.destroy()
            f1.destroy()
            Head.destroy()
            Head = Label(text='PNG To JPG Converter', font='Lucida 20 bold', bg='black', fg='#F4C724', padx=5, pady=5)
            Head.pack(pady=10)
            # To get jpg file
            browse_jpg = Button(text="      Import PNG File     ", bg='#2B2B52', fg='white',
                                font=('helvetica', 15, 'bold'),
                                command=getpngfile)
            browse_jpg.pack(pady=20)
            # To save jpg file
            save_jpg = Button(text='  Convert PNG To JPG  ', bg='#2B2B52', fg='white', font=('helvetica', 15, 'bold'),
                              command=savejpgfile)
            save_jpg.pack(pady=10)

            # Image in bottom
            bottom_pic = Image.open('Images/ptoj.jpg')
            bottom_pic = bottom_pic.resize((400, 250), Image.ANTIALIAS)
            bg_pic = ImageTk.PhotoImage(bottom_pic)
            img_label = Label(root, image=bg_pic)
            img_label.image = bg_pic  # It will make a reference or keep a reference
            img_label.pack(side=BOTTOM, pady=40)

            # Close Button
            close = Button(text='Close', command=root.destroy, bg='black', fg='white', font='11')
            close.place(x=205, y=422)

        ''' Events of buttons '''

        def jtopenter(event):
            jtop.config(bg='black', fg='white')

        def jtopleave(event):
            jtop.config(bg='white', fg='black')

        def ptojenter(event):
            ptoj.config(bg='black', fg='white')

        def ptojleave(event):
            ptoj.config(bg='white', fg='black')

        '''Main GUI Program'''

        root = Tk()
        root.title('Image Converter')
        root.wm_iconbitmap('download.jpg')
        root.geometry('450x480')

        '''Creating Main Window :'''

        # Heading of GUI
        Head = Label(text='Image Converter', font='Lucida 20 bold', bg='black', fg='#F4C724', padx=5, pady=5)
        Head.pack(pady=10)

        # Buttons
        f1 = Frame(root)
        jtop = Button(f1, text='JPG To PNG', font='arial 15 bold', command=jpgtopng)
        jtop.pack(side='left', padx=40)
        jtop.bind('<Enter>', jtopenter)
        jtop.bind('<Leave>', jtopleave)
        ptoj = Button(f1, text='PNG To JPG', font='arial 15 bold', command=pngtojpg)
        ptoj.pack(padx=40)
        ptoj.bind('<Enter>', ptojenter)
        ptoj.bind('<Leave>', ptojleave)
        f1.pack(pady=20)

        # Image
        img = Image.open('download.jpg')
        img = img.resize((300, 275), Image.ANTIALIAS)
        bgpic = ImageTk.PhotoImage(img)
        imagelabel = Label(image=bgpic)
        imagelabel.pack(pady=10)

        # Status Bar
        sbar = Label(text='By Logical Coder', font='Helvetica 10 bold', relief=SUNKEN, anchor='w', padx=10)
        sbar.pack(side=BOTTOM, fill=X)

        root.mainloop()
    # pdf
    def pdf(self):


        # =================open file method======================
        def openFile():
            file = askopenfilename(defaultextension=".pdf",
                                   filetypes=[("Pdf files", "*.pdf")])
            if file == "":
                file = None
            else:
                fileEntry.delete(0, END)
                fileEntry.config(fg="blue")
                fileEntry.insert(0, file)

        def convert():
            try:
                pdf = fileEntry.get()
                pdfFile = open(pdf, 'rb')
                # creating a pdf reader object
                pdfReader = PdfFileReader(pdfFile)

                # creating a page object
                pageObj = pdfReader.getPage(0)

                # extracting text from page
                extractedText = pageObj.extractText()
                readPdf.delete(1.0, END)
                readPdf.insert(INSERT, extractedText)

                # closing the pdf file object
                pdfFile.close()
            except FileNotFoundError:
                fileEntry.delete(0, END)
                fileEntry.config(fg="red")
                fileEntry.insert(0, "Please select a pdf file first")
            except:
                pass

        def save2word():
            text = str(readPdf.get(1.0, END))
            wordfile = asksaveasfile(mode='w', defaultextension=".doc",
                                     filetypes=[("word file", "*.doc"),
                                                ("text file", "*.txt"),
                                                ("Python file", "*.py")])

            if wordfile is None:
                return
            wordfile.write(text)
            wordfile.close()
            print("saved")
            fileEntry.delete(0, END)
            fileEntry.insert(0, "pdf Extracted and Saved...")

        # =================== Front End Design
        root = Tk()
        root.geometry("600x350")
        root.config(bg="light blue")
        root.title("PDF Converter [designed by:CID]")
        root.resizable(45, 45)
        try:
            root.wm_iconbitmap("pdf2.ico")
        except:
            print('icon file is not available')
            pass
        file = ""
        defaultText = "\n\n\n\n\t\t Your extracted text will apear here.\n \t\t     you can modify that text too."
        # ==============App Name==============================================================>>
        appName = Label(root, text="PDF to WORD Converter ", font=('arial', 20, 'bold'),
                        bg="light blue", fg='maroon')
        appName.place(x=150, y=5)
        # Select pdf file
        labelFile = Label(root, text="Select Pdf File", font=('arial', 12, 'bold'))
        labelFile.place(x=30, y=50)
        fileEntry = Entry(root, font=('calibri', 12), width=40)
        fileEntry.pack(ipadx=200, pady=50, padx=150)
        # ===========button to access openFile method=================================
        openFileButton = Button(root, text=" Open ", font=('arial', 12, 'bold'), width=30,
                                bg="sky blue", fg='green', command=openFile)
        openFileButton.place(x=150, y=80)
        # ===========button to access convert method=================================
        convert2Text = Button(root, text="Read", font=('arial', 8, 'bold'),
                              bg="RED", fg='WHITE', width=20, command=convert)
        convert2Text.place(x=250, y=120)
        # ======================= Text Box to read pdf file and modify ===================>>
        readPdf = Text(root, font=('calibri', 12), fg='light green', bg='black', width=60, height=30, bd=10)
        readPdf.pack(padx=20, ipadx=20, pady=20, ipady=20)
        readPdf.insert(INSERT, defaultText)
        # ===============================Button to access save2word method=================
        save2Word = Button(root, text="Save to Word File", font=('arial', 10, 'bold'),
                           bg="RED", fg='WHITE', command=save2word)
        save2Word.place(x=255, y=320)

        def tkinter():
            return None

        # ===================halt window=============================>>
        if __name__ == "__main__":
            root.mainloop()
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
        file2 = filedialog.asksaveasfile(initialdir="C:\\Users\\Cakow\\PycharmProjects\\Main",
                                        defaultextension='.txt',
                                        filetypes=[
                                            ("Text file", ".txt"),
                                            ("HTML file", ".html"),
                                            ("All files", ".*"),
                                        ])
        if file2 is None:
            return
        filetext = str(entry.get(1.0, END))
        # filetext = input("Enter some text I guess: ") //use this if you want to use console window
        file2.write(filetext)
        file2.close()


    # save
    def save(self, tkFileDialog=None):
        file = filedialog.asksaveasfile(initialdir="C:\\Users\\Cakow\\PycharmProjects\\Main",
                                        defaultextension='.txt',
                                        filetypes=[
                                            ("Text file", ".txt"),
                                            ("HTML file", ".html"),
                                            ("All files", ".*"),
                                        ])
        if file is None:
            return
        filetext = str(entry.get(1.0, END))
        # filetext = input("Enter some text I guess: ") //use this if you want to use console window
        file.write(filetext)
        file.close()


    # opain
    def opain(self):
        file = filedialog.askopenfile(mode='r',filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
        if file is not None:
            content = file.read()
        entry.insert(INSERT,content)




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
