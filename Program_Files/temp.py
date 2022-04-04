import tkinter as tk

root = tk.Tk()
root.title("Message Box")
text1 = tk.Text(root, height=10, width=50)

text1.insert(tk.INSERT, "Line1")
option = input("Enter y/n")
if option == 'y':
    text1.insert(tk.INSERT, "you inserted y")
else:
    text1.insert(tk.INSERT, "you inserted n")

text1.pack()
root.mainloop()

