from tkinter import *

root = Tk()


def send():
    send = 'You =>' + e.get()
    txt.insert(END, '\n' + send)
    if (e.get() == 'hello'):
        txt.insert(END, '\n' + 'Bot => hi')
    elif (e.get() == 'hi'):
        txt.insert(END, '\n' + 'Bot => hello')
    elif (e.get() == 'how are you'):
        txt.insert(END, '\n' + 'Bot => fine, and you?')
    elif (e.get() == 'fine'):
        txt.insert(END, '\n' + 'Bot => nice to hear')
    else:
        txt.insert(END, '\n' + 'Bot => sorry, i don\'t get it')
    e.delete(0, END)


txt = Text(root)
txt.grid(row=0, column=0)
e = Entry(root)
send = Button(root, text='Send', bg='black', fg='white', command=send).grid(row=1, column=1)
e.grid(row=1, column=0)
root.title('ChatBot')
root.mainloop()
