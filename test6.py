import customtkinter as ctk

# Set appearance and theme

#ctk.set_appearance_mode("Light")
#ctk.set_appearance_mode("System")
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# Create app window
app = ctk.CTk()
app.title("CustomTkinter Table")
app.geometry("400x250")

# Data is given as lists of lists
data = [
    ["ID", "Name", "Age"],
    [1, "Alice", 22],
    [2, "Bob", 25],
    [3, "Charlie", 23],
    [4, "Diptadeep", 24],
]

# Create a frame to hold the table
table_frame = ctk.CTkFrame(app)
table_frame.pack(pady=20, padx=20, fill="both", expand=True)

# Display the table
for i, row in enumerate(data):
    for j, cell in enumerate(row):
        # enumerate() gives you two values: the index (j) and the corresponding value (cell)

        label = ctk.CTkLabel(table_frame, text=str(cell), corner_radius=5, width=100, height=30,
                             fg_color="#e0e0e0" if i == 0 else "#f8f8f8", text_color="black")
        label.grid(row=i, column=j, padx=5, pady=2)

app.mainloop()
