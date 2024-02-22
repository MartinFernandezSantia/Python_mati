import tkinter as ttk
from tkinter import simpledialog

def charge_activities(frame, root) :
    frame.grid_forget()
    frame2 = ttk.Frame(root, padx=10,pady=10)
    frame2.grid()
    label = ttk.Label(frame2, text = "Enter an activity")
    label.grid()

root = ttk.Tk()
frm = ttk.Frame(root, padx=10,pady=10)
frm.grid()
ttk.Label(frm, text = "Do you want to enter a new Activity").grid (column = 0, row = 0)
ttk.Button(frm, text = "Yes", command = lambda: charge_activities(frm, root)).grid(column = 1, row = 2)
ttk.Button(frm, text = "No", command = root.destroy).grid(column = 0, row = 2)

root.mainloop()




