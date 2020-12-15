from tkinter import *
from tkinter import messagebox

root = Tk()
root.withdraw()

result = messagebox.askquestion('Delete', 'Delete all?', icon='warning')
if result.lower() == 'yes':
    print('ok done')
else:
    print('ok won\'t do that')

result = messagebox.askokcancel('Delete', 'Delete all?', icon='warning')
if result is True:
    print('ok done')
else:
    print('cancelled')

result = messagebox.askretrycancel('Warning', "Operation Failed, try again?")
if result is True:
    print("OK, trying again...")
else:
    print('Operation cancelled')