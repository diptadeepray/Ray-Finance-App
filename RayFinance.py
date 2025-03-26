from customtkinter import *

# Create the main window
app = CTk()
app.geometry("600x500")  # Adjust window size
app.title("Login System")


dropdown_value="Not yet selected"

def func(value):
    global dropdown_value
    dropdown_value=value

# Dummy credentials
USERNAME = "admin"
PASSWORD = "1234"

def check_login():
    """Check login credentials and update UI."""
    if username_entry.get() == USERNAME and password_entry.get() == PASSWORD:
        frame_3.destroy()  # Remove login frame
        show_new_ui()      # Load new UI
    else:
        error_label.configure(text="Invalid credentials!", text_color="red")

def on_button_click(tab_name):
    print(f"Button clicked in {tab_name}")
def show_new_ui():
    """Display a new frame after successful login."""
    # Create a tabbed interface
    tabview = CTkTabview(master=app, fg_color="gray20", width=400, height=500)
    # Change dimensions
    # Change fg_color for background

    tabview.pack(padx=20, pady=20)  # Adds padding around the tab view.

    tabview.add("Share Market")
    tabview.add("Gold market")
    tabview.add("Debt Investing")
    # Add three tabs to the tabbed interface

    label_1 = CTkLabel(master=tabview.tab("Share Market"), text="This is tab 1")
    label_1.pack(padx=20, pady=20)
    # Used for Dropdown menu
    combobox = CTkComboBox(master=tabview.tab("Share Market"), values=["Option 1", "Option 2"], command=func)
    # You can change fg_color, dropdown_fg_color, border_color and corner_radius
    combobox.pack(padx=10, pady=10)
    button_1 = CTkButton(master=tabview.tab("Share Market"), text="Click Me", command=lambda: on_button_click("Tab 1"))
    button_1.pack(pady=10)

    label_2 = CTkLabel(master=tabview.tab("Gold market"), text="This is tab 2")
    label_2.pack(padx=20, pady=20)
    frame_1 = CTkScrollableFrame(master=tabview.tab("Gold market"), fg_color="#CD8C67")
    frame_1.pack(fill="both", expand=True, padx=50, pady=50)

    label_3 = CTkLabel(master=tabview.tab("Debt Investing"), text="This is tab 3")
    label_3.pack(padx=20, pady=20)
    frame = CTkFrame(master=tabview.tab("Debt Investing"), fg_color="#8D6F3A", border_color="#FFCC70", border_width=2)
    # CTkScrollableFrame can be used for multiple widgets that scrolling can have orientation "horizontal" or "vertical"
    # You can also change scrollbar_button_color="#FFCC70"

    frame.pack(expand=True)
    label = CTkLabel(master=frame, text="This is a frame")
    entry = CTkEntry(master=frame, placeholder_text="Type something...")
    btn = CTkButton(master=frame, text="Submit")
    label.pack(expand=True, pady=10, padx=30)
    entry.pack(expand=True,  pady=10, padx=30)
    btn.pack(expand=True,  pady=10, padx=30)



# Create login frame
# Configure the grid to center the frame
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)
app.grid_rowconfigure(2, weight=1)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=1)

# Create login frame
frame_3 = CTkFrame(master=app, fg_color="#4EAC7D", width=500, height=350)
frame_3.grid(row=1, column=1, padx=20, pady=20)  # Place it in the center

CTkLabel(master=frame_3, text="Section 3", font=("Arial Bold", 20), justify="left").pack(expand=True, pady=(30, 15))
username_entry = CTkEntry(master=frame_3, placeholder_text="Enter your username", width=400)
username_entry.pack(expand=True, pady=15, padx=20)
password_entry = CTkEntry(master=frame_3, placeholder_text="Enter your password", width=400, show="*")
password_entry.pack(expand=True, pady=15, padx=20)
login_button = CTkButton(master=frame_3, text="Login", command=check_login)
login_button.pack(expand=True, fill="both", pady=(30, 15), padx=30)
error_label = CTkLabel(master=frame_3, text="", font=("Arial", 14))


app.mainloop()
