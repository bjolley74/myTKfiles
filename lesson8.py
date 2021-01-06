# lesson 8

from tkinter import *

root = Tk()
root.geometry("200x200")

def do_status(printout):
    status = Label(root, text=printout, bd=1, relief=SUNKEN, anchor=W)
    status.pack(side=BOTTOM, fill=X)

do_status('READY')

x = 4
y = 5
z = x * y
output = f'{x} x {y} = {z}'
do_status(output)

root.mainloop()