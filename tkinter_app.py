import tkinter as ttk

def nombre_func():
    print("algo")

root = ttk.Tk()
root.configure(bg="blue")
frm = ttk.Frame(root, padx= 10,pady=10)
frm.configure(bg="white")
frm.grid()
ttk.Label(frm, text = "Hello world ").grid(column = 0, row = 0)
ttk.Button(frm, text = "Hello", command = nombre_func).grid(column = 1, row = 2)
ttk.Button(frm, text = "Quit", command = root.destroy).grid(column = 0, row = 2)

root.mainloop()