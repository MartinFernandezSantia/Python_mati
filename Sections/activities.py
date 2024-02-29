import tkinter as ttk
from tkinter import simpledialog

activity_list = []


def charge_activities(frame, root):
    frame.grid_forget()
    frame2 = ttk.Frame(root, padx=10, pady=10)
    frame2.grid()
    # label = ttk.Label(frame2, text="Enter an activity")
    # label.grid()
    # # Carga de datos
    # etiqueta1 = ttk.Label(frame2, text="Write Here ").grid(column=0, row=1)
    # entrada1 = ttk.Entry(frame2, activity).grid(column=2, row=1)
    # ttk.Button(frame2, text="guardar").grid(column=0, row=3)

    entry1 = ttk.Entry(frame2)
    entry1.grid(row=0, column=0)
    b1 = ttk.Button(
        frame2, text="Guardar", command=lambda: Guardar_datos(entry1.get())
    ).grid(row=1, column=0)

    ttk.Label(frame2, text="entry1")


def Mostrar():
    # k = 0
    # while k < len(activity_list):
    #     print(activity_list[k])
    #     k + 1
    print(activity_list)
    for activity in activity_list:
        print(activity)


def Guardar_datos(entry1):
    activity_list.append(entry1)
    Mostrar()


root = ttk.Tk()
frm = ttk.Frame(root, padx=10, pady=10)
frm.grid()
ttk.Label(frm, text="Do you want to enter a new Activity").grid(column=0, row=0)
ttk.Button(frm, text="Yes", command=lambda: charge_activities(frm, root)).grid(
    column=1, row=2
)
ttk.Button(frm, text="No", command=root.destroy).grid(column=0, row=2)


root.mainloop()
