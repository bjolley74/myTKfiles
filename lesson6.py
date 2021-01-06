import tkinter

def func():
    x = 4
    y = 5
    print('function click')
    print(f'answer of {x} x {y} is {x*y}')

if __name__ == '__main__':
    root = tkinter.Tk()
    root.title('Hello World')
    root.geometry('500x400')
    btn = tkinter.Button(root, text='Hello', command=func)
    btn.place(x=0, y=0)
    root.mainloop()