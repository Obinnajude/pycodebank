from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Feet to Meter")


def calculate(*args):
    try:
        value = float(feet.get())
        meter.set(int(0.3048 * value * 10000.0 + 0.5) / 10000.0)
    except ValueError:
        pass


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(row=0, column=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(row=1, column=1, sticky=(W, E))

meter = StringVar()
ttk.Label(mainframe, textvariable=meter).grid(row=3, column=1, sticky=(W, E))

ttk.Label(mainframe, text=" Feet").grid(row=1, column=2, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(row=3, column=0, sticky=W)
ttk.Label(mainframe, text="Meters").grid(row=3, column=2, sticky=W)

ttk.Button(mainframe, text="Calculate", command=calculate).grid(row=4, column=2)
feet_entry.focus()
root.mainloop()
