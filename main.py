from customtkinter import *

app = CTk()
app.geometry("500x500")


set_default_color_theme("green")
# The default color themes can be blue, green, dark green, etc.
# To change the color of the entire window all at once


# Change the tabview colors so that the application looks cool


stocks_links = {
    "Tata Consultancy Services": "https://www.screener.in/company/TCS/consolidated/",
    "Reliance": 24,
    "HDFC Bank": "Male",
    "Pidilite Industries": "Kolkata",
    "Titan": "Kolkata",
    "Nestle Indis": "Kolkata",
"Berger Paints": "Kolkata",
"HDFC Life": "Kolkata",
"ITC": "Kolkata",
"Asian Paints": "Kolkata",
"Bajaj Finance": "Kolkata",
"Hindusthan Unilever": "Kolkata"
}



tabview = CTkTabview(master=app)
tabview.pack(padx=20, pady=20)

tabview.add("Equity Investments")
tabview.add("Bonds and Securities")
tabview.add("Gold")

label_1 = CTkLabel(master=tabview.tab("Equity Investments"), text="This is tab 1")
label_1.pack(padx=20, pady=20)

label_2 = CTkLabel(master=tabview.tab("Bonds and Securities"), text="This is tab 2")
label_2.pack(padx=20, pady=20)

label_3 = CTkLabel(master=tabview.tab("Gold"), text="This is tab 3")
label_3.pack(padx=20, pady=20)

app.mainloop()