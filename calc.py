from tkinter import *
first = True
num_1 = ""
num_2 = ""

def set_numbers(n):
    global first, num_1, num_2
    if(first):
        num_1 = num_1 + str(n)
        screen.insert(0,str(n))
    else:
        num_2 = num_2 + str(n)       
    return

def add_numbers():
    return

def sub_numbers():
    return


root = Tk()
root.title("Basic Calculator")
screen = Entry(root, font = "Helvetica 18", width=25)
screen.grid(row=0, column=0, columnspan=3, padx=10, pady=5)


b1 = Button(root, font = "Helvetica 11 bold", text="1", width=10, command=lambda: set_numbers(1))
b2 = Button(root, font = "Helvetica 11 bold", text="2", width=10, command=lambda: set_numbers(2))
b3 = Button(root, font = "Helvetica 11 bold", text="3", width=10, command=lambda: set_numbers(1))

b4 = Button(root, font = "Helvetica 11 bold", text="4", width=10, command=lambda: set_numbers(4))
b5 = Button(root, font = "Helvetica 11 bold", text="5", width=10, command=lambda: set_numbers(5))
b6 = Button(root, font = "Helvetica 11 bold", text="6", width=10, command=lambda: set_numbers(6))

b7 = Button(root, font = "Helvetica 11 bold", text="7", width=10, command=lambda: set_numbers(7))
b8 = Button(root, font = "Helvetica 11 bold", text="8", width=10, command=lambda: set_numbers(8))
b9 = Button(root, font = "Helvetica 11 bold", text="9", width=10, command=lambda: set_numbers(9))

b1.grid(row=1, column=0, padx=10, pady=5)
b2.grid(row=1, column=1, padx=10, pady=5)
b3.grid(row=1, column=2, padx=10, pady=5)

b4.grid(row=2, column=0, padx=10, pady=5)
b5.grid(row=2, column=1, padx=10, pady=5)
b6.grid(row=2, column=2, padx=10, pady=5)

b7.grid(row=3, column=0, padx=10, pady=5)
b8.grid(row=3, column=1, padx=10, pady=5)
b9.grid(row=3, column=2, padx=10, pady=5)

root.mainloop()
