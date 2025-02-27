# keyboard-names.py
# 2025 (C) DAREKPAGES
# NOTE: the tk window must be active when pressing the keys.
# Code reading is in the terminal: event.keysym, event.keycode, event.char.

from tkinter import Tk, Canvas
col = False
    
def key_return(event):
    global col
    ec = event.char
    if ec == '':
        ec = '(no char)'
    print(event.keysym, event.keycode, ec)
    sign = lambda f: cnvs.create_oval(50, 50, 150, 150, width= 0, fill= f)
    if col == False:
        col = True
        sign('firebrick1')
    else:
        col = False
        sign('firebrick')

root = Tk()
root.geometry('200x200')
cnvs = Canvas(bg= 'white')
cnvs.pack()
root.bind("<Key>", key_return)
root.mainloop()