import tkinter
from tkinter import *
import math
import tkinter.messagebox

root=Tk()
root.title("Scientific Calculator By REBELS")
root.geometry("570x795+100+200")
root.resizable(False,False)
root.configure(bg="#17161b")




def btn_1():
    if disp.get()=="0":
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,"1")


def btn_2():
    if disp.get()=="0":
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,"2")


def btn_3():
    if disp.get()=="0":
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,"3")


def btn_4():
    if disp.get()=="0":
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,"4")


def btn_5():
    if disp.get()=="0":
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,"5")


def btn_6():
    if disp.get()=="0":
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,"6")


def btn_7():
    if disp.get()=="0":
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,"7")


def btn_8():
    if disp.get()=="0":
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,"8")


def btn_9():
    if disp.get()=="0":
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,"9")            


def btn_0():
    if disp.get()=="0":
        disp.delete(0,END)
    pos=len(disp.get())
    disp.insert(pos,"0")

def btn_pi():
      if disp.get()=="0":
        disp.delete(0,END)
      pos=len(disp.get())
      disp.insert(pos,str(math.pi))


def btn_a():
    pos=len(disp.get())
    disp.insert(pos,"+")


def btn_s():
    pos=len(disp.get())
    disp.insert(pos,"-")


def btn_m():
    pos=len(disp.get())
    disp.insert(pos,"*")


def btn_d():
    pos=len(disp.get())
    disp.insert(pos,"/")


def pow():
    pos=len(disp.get())
    disp.insert(pos,"**")


def dot():
    pos=len(disp.get())
    disp.insert(pos,".")


def prn1():
    pos=len(disp.get())
    disp.insert(pos,"(")


def prn2():
    pos=len(disp.get())
    disp.insert(pos,")") 


def mod():
    pos=len(disp.get())
    disp.insert(pos,"%")


def cl():
    disp.delete(0,END)    


def back():
    pos=len(disp.get())
    display=str(disp.get())
    if display =='':
        disp.display(0,"0")
    elif display=="":
        disp.insert(0,"0")
    elif display=="0":
        pass
    else:
        disp.delete(0,END) 
        disp.insert(0,display[0:pos-1])   


switch=None
def sin():

    try:
        ans=float(disp.get())
        if switch is True:
            ans=math.sin(math.radians(ans))
        else:
            ans=math.sin(ans)
            disp.delete(0,END) 
            disp.insert(0,str(ans))    
    except EXCEPTION:
        tkinter.messagebox.showerror("Value error!")


def cos():
    try:
        ans=float(disp.get())
        if switch is True:
            ans=math.cos(math.radians(ans))
        else:
            ans=math.cos(ans)
            disp.delete(0,END) 
            disp.insert(0,str(ans))
    except EXCEPTION:
        tkinter.messagebox.showerror("Value error!")


def tan():
    try:
        ans=float(disp.get())
        if switch is True:
            ans=math.tan(math.radians(ans))
        else:
            ans=math.tan(ans)
            disp.delete(0,END) 
            disp.insert(0,str(ans))
    except EXCEPTION:
        tkinter.messagebox.showerror("Value error!")


def log():
    try:
        ans=float(disp.get())
        ans=math.log10(ans)
        disp.delete(0,END) 
        disp.insert(0,str(ans))
    except EXCEPTION:
        tkinter.messagebox.showerror("Value error!")


def sqrt():
    try:
        ans=float(disp.get())
        ans=math.sqrt(ans)
        disp.delete(0,END) 
        disp.insert(0,str(ans))
    except EXCEPTION:
        tkinter.messagebox.showerror("Value error!")

def eq():
    try:
        ans=disp.get()
        ans=eval(ans)
        disp.delete(0,END)
        disp.insert(0,ans)
    except EXCEPTION:
        tkinter.messagebox.showerror("Value error!")        




disp=Entry(root,font=("arial",30),fg="Black",bg="White",bd=2,justify=RIGHT)
disp.insert(0,"0")
disp.pack(expand=TRUE, fill= BOTH)


row1=Frame(root,bg="#000000")
row1.pack(expand=TRUE,fill=BOTH)

clrbtn=Button(row1,text="C", width=5, height=1,font=("arial",30,"bold"),relief=GROOVE,bd=1,fg="#fff",bg="#3697f5",command=cl).pack(side=LEFT,expand=TRUE,fill=BOTH)
powbtn=Button(row1,text="x²",width=5, height=1,font=("arial",30,"bold"),relief=GROOVE, bd=1,fg="#fff",bg="#2a2d36",command=pow).pack(side=LEFT,expand=TRUE,fill=BOTH)
sqrtbtn=Button(row1,text="√x",width=5, height=1,font=("arial",30,"bold"),relief=GROOVE, bd=1,fg="#fff",bg="#2a2d36" ,command=sqrt).pack(side=LEFT,expand=TRUE,fill=BOTH)
backbtn=Button(row1,text="⌫",width=5, height=1,font=("arial",30,"bold"),relief=GROOVE, bd=1,fg="#fff",bg="#2a2d36" ,command=back).pack(side=LEFT,expand=TRUE,fill=BOTH)


row2=Frame(root)
row2.pack(expand=TRUE,fill=BOTH)
sinbtn=Button(row2,text="Sin",width=5, height=1,font=("arial",30,"bold"),relief=GROOVE, bd=1,fg="#fff",bg="#2a2d36" ,command=sin).pack(side=LEFT,expand=TRUE,fill=BOTH)
cosbtn=Button(row2,text="Cos",width=5, height=1,font=("arial",30,"bold"),relief=GROOVE, bd=1,fg="#fff",bg="#2a2d36" ,command=cos).pack(side=LEFT,expand=TRUE,fill=BOTH)
tanbtn=Button(row2,text="Tan",width=5, height=1,font=("arial",30,"bold"),relief=GROOVE, bd=1,fg="#fff",bg="#2a2d36" ,command=tan).pack(side=LEFT,expand=TRUE,fill=BOTH)
modbtn=Button(row2,text="%",width=5, height=1,font=("arial",30,"bold"),relief=GROOVE, bd=1,fg="#fff",bg="#2a2d36",command=mod).pack(side=LEFT,expand=TRUE,fill=BOTH)


row3=Frame(root)
row3.pack(expand=TRUE,fill=BOTH)
logbtn=Button(row3,text="log10",width=5, height=1,font=("arial",30,"bold"),relief=GROOVE, bd=1,fg="#fff",bg="#2a2d36" ,command=log).pack(side=LEFT,expand=TRUE,fill=BOTH)
prn1btn=Button(row3,text="(",width=5, height=1,font=("arial",30,"bold"),relief=GROOVE, bd=1,fg="#fff",bg="#2a2d36" ,command=prn1).pack(side=LEFT,expand=TRUE,fill=BOTH)
prn2btn=Button(row3,text=")",width=5, height=1,font=("arial",30,"bold"),relief=GROOVE, bd=1,fg="#fff",bg="#2a2d36" ,command=prn2).pack(side=LEFT,expand=TRUE,fill=BOTH)
divbtn=Button(row3,text="/",width=5, height=1,font=("arial",30,"bold"),relief=GROOVE, bd=1,fg="#fff",bg="#2a2d36",command=btn_d).pack(side=LEFT,expand=TRUE,fill=BOTH)


row4=Frame(root)
row4.pack(expand=TRUE,fill=BOTH)
btn7=Button(row4,text="7",width=5, height=1,font=("arial",30,"bold"),relief=GROOVE, bd=1,fg="#fff",bg="#2a2d36" ,command=btn_7).pack(side=LEFT,expand=TRUE,fill=BOTH)
btn8=Button(row4,text="8",width=5, height=1,font=("arial",30,"bold"),relief=GROOVE, bd=1,fg="#fff",bg="#2a2d36" ,command=btn_8).pack(side=LEFT,expand=TRUE,fill=BOTH)
btn9=Button(row4,text="9",width=5, height=1,font=("arial",30,"bold"),relief=GROOVE, bd=1,fg="#fff",bg="#2a2d36" ,command=btn_9).pack(side=LEFT,expand=TRUE,fill=BOTH)
mulbtn=Button(row4,text="X",width=5, height=1,font=("arial",30,"bold"),relief=GROOVE, bd=1,fg="#fff",bg="#2a2d36" ,command=btn_m).pack(side=LEFT,expand=TRUE,fill=BOTH)


row5=Frame(root)
row5.pack(expand=TRUE,fill=BOTH)
btn4=Button(row5,text="4",width=5, height=1,font=("arial",30,"bold"),relief=GROOVE, bd=1,fg="#fff",bg="#2a2d36" ,command=btn_4).pack(side=LEFT,expand=TRUE,fill=BOTH)
btn5=Button(row5,text="5",width=5, height=1,font=("arial",30,"bold"),relief=GROOVE, bd=1,fg="#fff",bg="#2a2d36" ,command=btn_5).pack(side=LEFT,expand=TRUE,fill=BOTH)
btn6=Button(row5,text="6",width=5, height=1,font=("arial",30,"bold"),relief=GROOVE, bd=1,fg="#fff",bg="#2a2d36" ,command=btn_6).pack(side=LEFT,expand=TRUE,fill=BOTH)
minbtn=Button(row5,text="-",width=5, height=1,font=("arial",30,"bold"),relief=GROOVE, bd=1,fg="#fff",bg="#2a2d36" ,command=btn_s).pack(side=LEFT,expand=TRUE,fill=BOTH)


row6=Frame(root)
row6.pack(expand=TRUE,fill=BOTH)
btn1=Button(row6,text="1",width=5, height=1,font=("arial",30,"bold"),relief=GROOVE, bd=1,fg="#fff",bg="#2a2d36" ,command=btn_1).pack(side=LEFT,expand=TRUE,fill=BOTH)
btn2=Button(row6,text="2",width=5, height=1,font=("arial",30,"bold"),relief=GROOVE, bd=1,fg="#fff",bg="#2a2d36" ,command=btn_2).pack(side=LEFT,expand=TRUE,fill=BOTH)
btn3=Button(row6,text="3",width=5, height=1,font=("arial",30,"bold"),relief=GROOVE, bd=1,fg="#fff",bg="#2a2d36" ,command=btn_3).pack(side=LEFT,expand=TRUE,fill=BOTH)
posbtn=Button(row6,text="+",width=5, height=1,font=("arial",30,"bold"),relief=GROOVE, bd=1,fg="#fff",bg="#2a2d36" ,command=btn_a).pack(side=LEFT,expand=TRUE,fill=BOTH)


row7=Frame(root)
row7.pack(expand=TRUE,fill=BOTH)
btn0=Button(row7,text="0",width=5, height=1,font=("arial",30,"bold"),relief=GROOVE, bd=1,fg="#fff",bg="#2a2d36" ,command=btn_0).pack(side=LEFT,expand=TRUE,fill=BOTH)
dotbtn=Button(row7,text=".",width=5, height=1,font=("arial",30,"bold"),relief=GROOVE, bd=1,fg="#fff",bg="#2a2d36" ,command=dot).pack(side=LEFT,expand=TRUE,fill=BOTH)
pibtn=Button(row7,text="π",width=5, height=1,font=("arial",30,"bold"),relief=GROOVE, bd=1,fg="#fff",bg="#2a2d36" ,command=btn_pi).pack(side=LEFT,expand=TRUE,fill=BOTH)
eqbtn=Button(row7,text="=",width=5, height=1,font=("arial",30,"bold"),relief=GROOVE, bd=1,fg="#fff",bg="#fe9037" ,command=eq).pack(side=LEFT,expand=TRUE,fill=BOTH)


root.mainloop()