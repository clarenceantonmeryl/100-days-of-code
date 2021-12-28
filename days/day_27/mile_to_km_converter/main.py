from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=120)
window.config(padx=30, pady=30)

# Labels

label_equal_to = Label(text="is equal to")
label_equal_to.grid(row=1, column=0)

label_miles = Label(text="Miles")
label_miles.grid(row=0, column=2)

label_km = Label(text="Km")
label_km.grid(row=1, column=2)

label_result = Label(text="0")
label_result.grid(row=1, column=1)

# Entries
entry_input = Entry(width=10)
entry_input.grid(row=0, column=1)


# Buttons
def button_calculate_action():
    miles = int(entry_input.get())
    km = miles * 1.609344
    label_result.config(text=str(km))


button_calculate = Button(text="Calculate", command=button_calculate_action)
button_calculate.grid(row=2, column=1)

window.mainloop()
