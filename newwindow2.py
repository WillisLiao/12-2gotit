from tkinter import *
from tkinter import messagebox
import scraping as ws

root = Tk()
root.title("GUI Demo")
root.geometry("600x500+200+100")
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.rowconfigure(6, weight=1)
root.rowconfigure(7, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

def openNewWindow():
    root.withdraw()
    newWindow = Toplevel(root)
    newWindow.title("New Window")
    newWindow.geometry("400x300")
    Label(newWindow, text="This is a new Window").pack()
    btn = Button(newWindow,
                 text="Close",
                 command = lambda:newWindowClose(newWindow))
    btn.pack(pady = 5)

def newWindowClose(self):
    root.deiconify()
    self.destroy()

def getWordList(text):
    wordList = ws.start_scrapting()
    text.configure( state='normal')
    for item in wordList:
        for i in item:
            for k in i:
                text.insert(INSERT, k)
            text.insert(INSERT, '\n')
    text.configure(state='disabled')

def cleanText(text):
    text.configure( state='normal')
    text.delete("1.0", 'end')
    text.configure( state='disable')

content = Text(root, font=("Monaco", 14, "bold"),
               state='disabled',
               background="#99ffff")
content.grid( row=1, column=0, rowspan=7, columnspan=4, sticky=NSEW)


lab1 = Label(root, text="This is the main window")
lab1.pack(pady = 10)
btn = Button(root, 
             text="Click to open a new window",
             command = openNewWindow)
btn.pack(pady = 10)

root.mainloop()