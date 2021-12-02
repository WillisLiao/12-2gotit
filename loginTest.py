from tkinter import *
import sys, hashlib

s256 = hashlib.sha256()
btnLabs = ["7", "8", "9", "/",
           "4", "5", "6", "*",
           "1", "2", "3", "-",
           "0", ".", "(", "+",
           ")", "c", "exit", "="]
def login():
    idData = entryID.get()
    pwData = entryPW.get()
    if len(idData) > 0 and len(pwData) > 0:
        s256.update(pwData.encode("utf-8"))
        pwHash = s256.hexigest()
        # print(pwHash)
        if idData == "h304" and pwHash == "5515f0912ec4ca5c9537a9c29ed62372869e0f2332c58eb312bd7ca7de850456":
            root.deiconify()
            top.destroy()
        else:
            entryID.delete(0, "end")
            entryID.insert(0, "")
            entryPW.delete(0, "end")
            entryPW.insert(0, "")
    else:
        entryID.delete(0, "end")
        entryID.insert(0, "")
        entryPW.delete(0, "end")
        entryPW.insert(0, "")

def quitProgram():
    top.destroy()
    root.destroy()
    sys.exit()

def btnClick(btnStr):
    #print(btnStr)
    if btnStr == "exit":
        root.destroy()
        sys.exit()
    elif btnStr in ["+", "-", "*", ]




































root = Tk()
top = Toplevel(root)

top.rowconfigure(0, weight=1)
top.rowconfigure(1, weight=1)
top.rowconfigure(2, weight=1)
top.columnconfigure(0, weight=1)
top.columnconfigure(1, weight=1)
root.geometry("300x400+200+100")
top.geometery("300x100+200+100")
labelID = Label(top, text="ID", justify=RIGHT, anchor=E, font="Times 20 bold")
labelPwd = Label(top, text="Password", justify=RIGHT, anchor=E, font="Times 20 bold")
entryID = Entry(top)
entryPW = Entry(top, show="*")
btnLogin = Button(top, text="Login", command=login)
btnQuit = Button(top, text="Quit", command=quitProgram)
labelID.grid(row=0, column=0, sticky=NSEW)
entryID.grid(row=0, column=1, sticky=NSEW)
labelPwd.grid(row=1, column=0, sticky=NSEW)
entryPW.grid(row=1, column=1, sticky=NSEW)
btnLogin.grid(row=2, column=0, sticky=NSEW)
btnQuit.grid(row=2, column=1, sticky=NSEW)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

lab = Label(root, text="0", bg="#ccddff", font=("Times", 20), anchor=E, justify=RIGHT)
lab.grid(row=0, column=0, sticky=NSEW, coplumnspan=4)
i=0
btns=[]
for btnLab in btnLabs:
    btn = Button(root, text=btnLab, command=click(btnLab), font=("Times", 20, "bold"))
    btns.append(btn)
    btn.grid(row=i // 4 + 1, column=i%4, sticky=NSEW)
    i+=1

root.withdraw()
root.mainloop()