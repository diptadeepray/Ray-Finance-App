#This program will run whenever the computer starts
from pip._internal.cli.cmdoptions import python

#python -c "import sys; print(sys.executable)"

import customtkinter as ctk



# Function to Get Selected Options
def get_selected():
    selected = [text for text, var in checkboxes.items() if var.get()]
    print("Selected:", selected)

app = ctk.CTk()
app.geometry("300x300")

checkboxes = {}
options = ["Tata Consultancy Services Ltd", "Reliance Industries Ltd", "Titan Company Ltd","HDFC Bank Ltd"]

for i, option in enumerate(options):
    var = ctk.StringVar(value="")  # Store selection
    cb = ctk.CTkCheckBox(app, text=option, variable=var, onvalue=option, offvalue="")
    cb.pack(anchor="w")
    checkboxes[option] = var

button = ctk.CTkButton(app, text="Get Selected", command=get_selected)
button.pack()

app.mainloop()

