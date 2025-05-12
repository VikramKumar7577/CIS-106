import tkinter as tk

win = tk.Tk()
win.geometry('500x400')
win.title('Gross Pay Calculator')
win.configure(bg="black")  

# Labels
tk.Label(win, text="Enter Last Name", bg="black", fg="white").grid(row=1, column=0, padx=10, pady=5, sticky="e")
tk.Label(win, text="Enter Hours", bg="black", fg="white").grid(row=2, column=0, padx=10, pady=5, sticky="e")
tk.Label(win, text="Enter Pay Rate", bg="black", fg="white").grid(row=3, column=0, padx=10, pady=5, sticky="e")

# Input entries
ent1 = tk.Entry(win)
ent2 = tk.Entry(win)
ent3 = tk.Entry(win)

ent1.grid(row=1, column=1)
ent2.grid(row=2, column=1)
ent3.grid(row=3, column=1)

# Result box
result_box = tk.Text(win, height=10, width=50, bg="black", fg="white")
result_box.grid(row=6, columnspan=2, pady=10)

# Callback function
def print_inputs():
    try:
        last_name = ent1.get()
        hours = float(ent2.get())
        rate = float(ent3.get())
        gross_pay = hours * rate
        result = f"{last_name} earned ${gross_pay:.2f}\n"
        result_box.insert(tk.END, result)

        # Save to file (ONLY addition for Q2)
        with open("gross_pay_output.txt", "a") as f:
            f.write(result)
    except ValueError:
        result_box.insert(tk.END, "Please enter valid numbers for Hours and Pay Rate.\n")

def clear_all():
    ent1.delete(0, tk.END)
    ent2.delete(0, tk.END)
    ent3.delete(0, tk.END)
    result_box.delete('1.0', tk.END)
    ent1.focus_set()

# Buttons
tk.Button(win, text='Compute Gross Pay', command=print_inputs).grid(row=4, column=0, pady=10)
tk.Button(win, text='Clear All', command=clear_all).grid(row=4, column=1, pady=10)

win.mainloop()
