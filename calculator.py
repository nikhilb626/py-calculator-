from tkinter import *

root=Tk()

# function handling

def click(event):
    global scvalue

    # we will get the text typed by respective buttons
    text=event.widget.cget("text")
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())

        else:
            value=eval(screen.get())
            scvalue.set(value)
            screen.update()

    elif text=="c":
        scvalue.set("")
        screen.update()


    else:
        scvalue.set(scvalue.get()+text)
        screen.update()



root.geometry("600x650")
root.title("CALCULATOR")

scvalue=StringVar()
scvalue.set("")


screen=Entry(root,textvariable=scvalue,font="lucida 40 bold")

screen.pack(fill=X,ipadx=8,pady=10,padx=10)

f=Frame(root,bg="grey")
b=Button(f,text="9",padx=40,pady=20,font="lucida 35 bold")
b.pack(side=LEFT)
b.bind('<Button-1>',click)

b=Button(f,text="8",padx=40,pady=20,font="lucida 35 bold")
b.pack(side=LEFT)
b.bind('<Button-1>',click)

b=Button(f,text="7",padx=40,pady=20,font="lucida 35 bold")
b.pack(side=LEFT)
b.bind('<Button-1>',click)

b=Button(f,text="6",padx=40,pady=20,font="lucida 35 bold")
b.pack(side=LEFT)
b.bind('<Button-1>',click)

f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="5",padx=40,pady=20,font="lucida 35 bold")
b.pack(side=LEFT)
b.bind('<Button-1>',click)

b=Button(f,text="4",padx=40,pady=20,font="lucida 35 bold")
b.pack(side=LEFT)
b.bind('<Button-1>',click)

b=Button(f,text="3",padx=40,pady=20,font="lucida 35 bold")
b.pack(side=LEFT)
b.bind('<Button-1>',click)

b=Button(f,text="2",padx=40,pady=20,font="lucida 35 bold")
b.pack(side=LEFT)
b.bind('<Button-1>',click)

f.pack()



f=Frame(root,bg="grey")
b=Button(f,text="1",padx=40,pady=20,font="lucida 35 bold")
b.pack(side=LEFT)
b.bind('<Button-1>',click)

b=Button(f,text="0",padx=40,pady=20,font="lucida 35 bold")
b.pack(side=LEFT)
b.bind('<Button-1>',click)

b=Button(f,text="*",padx=43,pady=20,font="lucida 35 bold")
b.pack(side=LEFT)
b.bind('<Button-1>',click)

b=Button(f,text="/",padx=48,pady=20,font="lucida 35 bold")
b.pack(side=LEFT)
b.bind('<Button-1>',click)

f.pack()


f=Frame(root,bg="grey")
b=Button(f,text="-",padx=44,pady=20,font="lucida 35 bold")
b.pack(side=LEFT)
b.bind('<Button-1>',click)

b=Button(f,text="+",padx=40,pady=20,font="lucida 35 bold")
b.pack(side=LEFT)
b.bind('<Button-1>',click)

b=Button(f,text="=",padx=38,pady=20,font="lucida 35 bold")
b.pack(side=LEFT)
b.bind('<Button-1>',click)

b=Button(f,text="c",padx=42,pady=20,font="lucida 35 bold")
b.pack(side=LEFT)
b.bind('<Button-1>',click)

f.pack()


root.mainloop()