from tkinter import *
from tkinter import messagebox
import scraping2 as ws

root = Tk()
root.title("GUI Demo")
root.geometry("900x600+200+100")
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
root.columnconfigure(4, weight=1)
flag = 0
count=0
def openNewWindow2():



    def check():
        if btn00['text']==btn01['text']==btn02['text']=='O':
            messagebox.showinfo("game ended", 'Player 1 Win')
        elif btn00['text']==btn01['text']==btn02['text']=='X':
            messagebox.showinfo("game ended", 'Player 2 Win')
        elif btn10['text']==btn11['text']==btn12['text']=='O':
            messagebox.showinfo("game ended", 'Player 1 Win')
        elif btn10['text']==btn11['text']==btn12['text']=='X':
            messagebox.showinfo("game ended", 'Player 2 Win')
        elif btn20['text']==btn21['text']==btn22['text']=='O':
            messagebox.showinfo("game ended", 'Player 1 Win')
        elif btn20['text']==btn21['text']==btn22['text']=='X':
            messagebox.showinfo("game ended", 'Player 2 Win')
        elif btn00['text']==btn10['text']==btn20['text']=='O':
            messagebox.showinfo("game ended", 'Player 1 Win')
        elif btn00['text']==btn10['text']==btn20['text']=='X':
            messagebox.showinfo("game ended", 'Player 2 Win')
        elif btn01['text']==btn11['text']==btn21['text']=='O':
            messagebox.showinfo("game ended", 'Player 1 Win')
        elif btn01['text']==btn11['text']==btn21['text']=='X':
            messagebox.showinfo("game ended", 'Player 2 Win')
        elif btn02['text']==btn12['text']==btn22['text']=='O':
            messagebox.showinfo("game ended",'Player 1 Win')
        elif btn02['text']==btn12['text']==btn22['text']=='X':
            messagebox.showinfo("game ended", 'Player 2 Win')
        elif btn00['text']==btn11['text']==btn22['text']=='O':
            messagebox.showinfo("game ended",'Player 1 Win')
        elif btn00['text']==btn11['text']==btn22['text']=='X':
            messagebox.showinfo("game ended",'Player 2 Win')
        elif btn02['text']==btn11['text']==btn20['text']=='O':
            messagebox.showinfo("game ended", 'Player 1 Win')
        elif btn02['text']==btn11['text']==btn20['text']=='X':
            messagebox.showinfo("game ended", 'Player 2 Win')
        else:
            if count==9:
                messagebox.showinfo("game ended", "Draw!")

    
    def btnClick(btn):
        global flag
        global count
        btn.config(text="O", state="disable") if flag==0 else btn.config(text="X", state="disable") # so it alternates between "O" and "X"
        flag = (flag+1)%2
        count+=1
        if count>=5:
            check()


    window = Tk()
    window.title('Demo 02')
    window.geometry("700x600+100+50")
    btn00 = Button(window, width=13, height=5,
                    font ="Arial 20 bold",
                    command=lambda:btnClick(btn00))
    btn00.grid(row=0, column=0, pady=2, padx=2)

    btn01 = Button(window, width=13, height=5,
                    font ="Arial 20 bold",
                    command=lambda:btnClick(btn01))
    btn01.grid(row=0, column=1, pady=2, padx=2)

    btn02 = Button(window, width=13, height=5,
                    font ="Arial 20 bold",
                    command=lambda:btnClick(btn02))
    btn02.grid(row=0, column=2, pady=2, padx=2)

    btn10 = Button(window, width=13, height=5,
                    font ="Arial 20 bold",
                    command=lambda:btnClick(btn10))
    btn10.grid(row=1, column=0, pady=2, padx=2)

    btn11 = Button(window, width=13, height=5,
                    font ="Arial 20 bold",
                    command=lambda:btnClick(btn11))
    btn11.grid(row=1, column=1, pady=2, padx=2)

    btn12 = Button(window, width=13, height=5,
                    font ="Arial 20 bold",
                    command=lambda:btnClick(btn12))
    btn12.grid(row=1, column=2, pady=2, padx=2)

    btn20 = Button(window, width=13, height=5,
                    font ="Arial 20 bold",
                    command=lambda:btnClick(btn20))
    btn20.grid(row=2, column=0, pady=2, padx=2)

    btn21 = Button(window, width=13, height=5,
                    font ="Arial 20 bold",
                    command=lambda:btnClick(btn21))
    btn21.grid(row=2, column=1, pady=2, padx=2)

    btn22 = Button(window, width=13, height=5,
                    font ="Arial 20 bold",
                    command=lambda:btnClick(btn22))
    btn22.grid(row=2, column=2, pady=2, padx=2)

    window.resizable(0,0)
    window.mainloop()

    


 


def openNewWindow():
    #root.withdraw()
    #newWindow = Toplevel(root)
    #newWindow.title("New Window")
    #newWindow.geometry("400x300")
    #Label(newWindow, text="This is a new Window").pack()
    #btn = Button(newWindow,
    #             text="Close",
    #             command = lambda:newWindowClose(newWindow))
    #btn.pack(pady = 5)


    op=0
    v1=0
    opFlag=False

    def chageText(num):
        if lab['text'] != '0' and opFlag==False:
            if num == '.' :
                if '.' not in lab['text'] :
                    lab['text']=lab['text']+num
            else:
                lab['text']=lab['text']+num
        else:
            lab['text'] = num

    def opset(opValue):
        global op
        global v1
        global opFlag
        opFlag=True
        v1=float(lab['text'])
        op=opValue

    def compute():
        v2=float(lab['text'])
        global op
        global opFlag
        if op== 1:
            lab['text']=str(v1+v2)
        elif op== 2:
            lab['text']=str(v1-v2)
        elif op== 3:
            lab['text']=str(v1*v2)
        elif op== 4:
            lab['text']=str(v1/v2)
        opFlag=False

    window= Tk()
    window.title("Digital Keyboard")
    window.geometry("400x500+200+100")
    window.rowconfigure(1,weight=1)
    window.rowconfigure(2,weight=1)
    window.rowconfigure(3,weight=1)
    window.rowconfigure(4,weight=1)
    window.columnconfigure(0,weight=1)
    window.columnconfigure(1,weight=1)
    window.columnconfigure(2,weight=1)
    window.columnconfigure(3,weight=1)

    lab=Label(window, text='0', justify=RIGHT, anchor=E,
            font=("MOnaco",26,"bold"), bg="#ccddee")
    lab.grid(row=0, column=0, columnspan=4, sticky=EW)

    btn7=Button(window, text="7", font=("Monaco",30,"bold"),
                command=lambda:chageText('7'))
    btn7.grid(row=1, column=0 ,sticky=NSEW)
    btn8=Button(window, text="8", font=("Monaco",30,"bold"),
                command=lambda:chageText('8'))
    btn8.grid(row=1, column=1 ,sticky=NSEW)
    btn9=Button(window, text="9", font=("Monaco",30,"bold"),
                command=lambda:chageText('9'))
    btn9.grid(row=1, column=2 ,sticky=NSEW)
    btnDiv=Button(window,text="/",font=("Monaco",30,"bold"),
                command=lambda:opset('4'))
    btnDiv.grid(row=1, column=3 ,sticky=NSEW)

    btn4=Button(window, text="4", font=("Monaco",30,"bold"),
                command=lambda:chageText('4'))
    btn4.grid(row=2, column=0 ,sticky=NSEW)
    btn5=Button(window, text="5", font=("Monaco",30,"bold"),
                command=lambda:chageText('5'))
    btn5.grid(row=2, column=1 ,sticky=NSEW)
    btn6=Button(window, text="6", font=("Monaco",30,"bold"),
                command=lambda:chageText('6'))
    btn6.grid(row=2, column=2 ,sticky=NSEW)
    btnMulti=Button(window,text="*",font=("Monaco",30,"bold"),
                    command=lambda:opset(3))
    btnMulti.grid(row=2, column=3 ,sticky=NSEW)

    btn1=Button(window, text="1", font=("Monaco",30,"bold"),
                command=lambda:chageText('1'))
    btn1.grid(row=3, column=0 ,sticky=NSEW)
    btn2=Button(window, text="2", font=("Monaco",30,"bold"),
                command=lambda:chageText('2'))
    btn2.grid(row=3, column=1 ,sticky=NSEW)
    btn3=Button(window, text="3", font=("Monaco",30,"bold"),
                command=lambda:chageText('3'))
    btn3.grid(row=3, column=2 ,sticky=NSEW)
    btnMulti=Button(window,text="-",font=("Monaco",30,"bold"),
                    command=lambda:opset(2))
    btnMulti.grid(row=3, column=3 ,sticky=NSEW)

    btn0=Button(window, text="0", font=("Monaco",30,"bold"))
    btn0.grid(row=4, column=0 ,sticky=NSEW)
    btnDot=Button(window, text=".", font=("Monaco",30,"bold"))
    btnDot.grid(row=4, column=1 ,sticky=NSEW)
    btnEq=Button(window, text="=", font=("Monaco",30,"bold"),
                command=compute)
    btnEq.grid(row=4, column=2 ,sticky=NSEW)
    btnAdd=Button(window,text="+",font=("Monaco",30,"bold"),
                command=lambda:opset(1))
    btnAdd.grid(row=4, column=3 ,sticky=NSEW)
    window.mainloop()

        
   
  

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
content.grid( row=1, column=0, rowspan=7, columnspan=5, sticky=NSEW)

btnGetWordlist = Button(root, text="Get Wordlist",
                        font=("Monaco", 20, "bold"),
                        command=lambda:getWordList(content))
btnGetWordlist.grid( row=0, column=0, sticky=NSEW)

btnClean = Button( root, text="Clean",
                   foreground="#224399",
                   command=lambda:cleanText(content),
                   font=("Monaco", 20, "bold"))
btnClean.grid( row=0, column=1, sticky=NSEW)

btnCalculator = Button( root, text="Calculator",
                        font=("Monaco", 20, "bold"),
                        command = openNewWindow,
                        foreground="#993333")
btnCalculator.grid( row=0, column=2, sticky=NSEW)
btnTicTacToe = Button( root, text="TicTacToe",
                        font=("Monaco", 20, "bold"),
                        command = openNewWindow2,
                        foreground="#66CDAA")
btnTicTacToe.grid( row=0, column=3, sticky=NSEW)

btnExit = Button( root,
                  text="EXIT",
                  font=("Monaco", 20, "bold"),
                  foreground="#ee4433",
                  command = root.destroy)
btnExit.grid( row=0, column=4, sticky=NSEW)
'''
lab1 = Label(root, text="This is the main window")
lab1.pack(pady = 10)
btn = Button(root, 
             text="Click to open a new window",
             command = openNewWindow)
btn.pack(pady = 10)
'''
root.mainloop()