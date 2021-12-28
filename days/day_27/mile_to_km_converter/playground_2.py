from tkinter import *

window = Tk()
window.title("Window")
window.minsize(width=800, height=500)
window.config(padx=30, pady=30)

#
# label = tkinter.Label(text="Label", font=("Courier", 24, "bold"))
# label.pack()
# label.config(text="new text")
#
#
# def button_click():
#     label.config(text=text.get("2.0", tkinter.END))
#
#
# button = tkinter.Button(text="Button text", command=button_click)
# button.pack()
#
# input_entry = tkinter.Entry(width=10)
# input_entry.insert(tkinter.END, string="Enter text")
# input_entry.pack()
#
# text = tkinter.Text(height=5, width=50)
# text.focus()
# text.pack()
#
#
# def spin_box_used():
#     label.config(text=spinbox.get())
#
#
# spinbox = tkinter.Spinbox(from_=0, to=10, width=10, command=spin_box_used)
# spinbox.pack()
#
#
# def scale_used(value):
#     label.config(text=value)
#
#
# scale = tkinter.Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
#
# def checkbox_used():
#     label.config(text=checkbox_state.get())
#
#
# checkbox_state = tkinter.IntVar()
# checkbox = tkinter.Checkbutton(text="Is On", variable=checkbox_state, command=checkbox_used)
# checkbox.pack()
#
#
# def radio_button_used():
#     label.config(text=radio_state.get())
#
#
# radio_state = tkinter.IntVar()
# radio_button_1 = tkinter.Radiobutton(text="Option 1", value=10, variable=radio_state, command=radio_button_used)
# radio_button_2 = tkinter.Radiobutton(text="Option 2", value=20, variable=radio_state, command=radio_button_used)
# radio_button_1.pack()
# radio_button_2.pack()
#
# fruits = ['apple', 'orange', 'mango', 'pear']
#
#
# def list_box_used(event):
#     label.config(text=list_box.get(list_box.curselection()))
#
#
# list_box = tkinter.Listbox(height=4)
# for item in fruits:
#     list_box.insert(fruits.index(item), item)
#
# list_box.bind("<<ListboxSelect>>", list_box_used)
# list_box.pack()

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.grid(row=0, column=0)

#Buttons
def action():
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.grid(row=1, column=1)

#calls action() when pressed
button1 = Button(text="Click Me", command=action)
button1.grid(row=0, column=2)

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.grid(row=2, column=3)


window.mainloop()
