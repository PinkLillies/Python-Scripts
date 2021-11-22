from tkinter import *
import tkinter.messagebox as box



window=Tk()
window.title('Listbox example')


frame = Frame(window)


listbox = Listbox(frame)
listbox.insert(1, 'html5 in easy steps')
listbox.insert(2, 'css3 in easy stesps')
listbox.insert(3, ' javascript in easy steps')



def dialog():
    box.showinfo('selection','your choice: ' + \
    listbox.get(listbox.curselection()))

btn = Button(frame, text ='Choose', command = dialog)

btn.pack(side = RIGHT, padx = 5)
listbox.pack(side = LEFT)
frame.pack(padx = 30, pady = 30)


window.mainloop()
                         
