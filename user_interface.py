from customtkinter import *

# Create the main window
app = CTk()
app.geometry("600x500")  # Adjust window size
app.title("Ray Finance")





current_scrollable_frame = None # To hold the reference to the scrollable frame






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











def on_button_click():

    selected_option=analysis_dropdown_menu.get()
    # The is made analysis_dropdown_menu global
    # By this line we are getting the option that user has selected

    global current_scrollable_frame
    # If we donot \ explicitly tell the compiler that we are working with global variable
    # Python will treat current_scrollable_frame as a local variable

    if current_scrollable_frame is not None:
        current_scrollable_frame.pack_forget()
        # How CTkScrollableFrame behaves is a problem— destroying it does not remove its visual placeholder entirely until the layout is recalculated.
        # So we needed to call .pack_forget() before destroying the frame. This will remove the reference from the layout manager then we can destroy the frame.


        current_scrollable_frame.destroy()
        current_scrollable_frame=None
        # So that the scrollable frame-from previous gets destroyed.
        # And doesnot occupy screen space so that we can view the current scrollableFrame properly






    if selected_option=="IT Outsoursing":
        #If the user has selected "IT Outsoursing" only then the analysis TCS and it's Competitors will be analysed
        dynamic_label = CTkLabel(master=tabview.tab("Share Market"), text="System is running. Please wait...")
        dynamic_label.pack(pady=10)


        #global current_scrollable_frame
        current_scrollable_frame = CTkScrollableFrame(master=tabview.tab("Share Market"), fg_color="#CD8C67")
        # frame_1_for_label1.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=50, pady=50)

        import WebScraping_IT_Screener
        tablesLablesTogether = WebScraping_IT_Screener.WebScraping_IT_Screener_Method()

        TopRow_CompanyNames = ["", "TCS", "Infosys", "Wipro", "HCL Tech", "TechMahindra", "LTIMindree"]
        # First comum is left blank because there the 10 years, 5 years, 3 years...is displayed

        for oneLabel in tablesLablesTogether:
            print(oneLabel)
            print(tablesLablesTogether[oneLabel])
            print()

            # Title label for the table
            title_label = CTkLabel(master=current_scrollable_frame,
                                   text=oneLabel,
                                   font=("Arial", 16, "bold"),
                                   text_color="white")
            title_label.pack(pady=(20, 5))  # padding for spacing above and below the label

            # Create a frame to hold the table
            table_frame = CTkFrame(master=current_scrollable_frame,
                                   fg_color="transparent")  # transparent to inherit scrollable bg

            table_frame.pack(pady=10, fill="both", expand=True, anchor="center")

            for i, oneCompanyName in enumerate(TopRow_CompanyNames):
                label = CTkLabel(table_frame, text=str(oneCompanyName), corner_radius=5, width=100, height=30)
                label.grid(row=0, column=i, padx=5, pady=2)

            # Display the table
            for i, row in enumerate(tablesLablesTogether[oneLabel]):
                for j, cell in enumerate(row):
                    # enumerate() gives you two values: the index (j) and the corresponding value (cell)

                    label = CTkLabel(table_frame, text=str(cell), corner_radius=5, width=100, height=30,
                                     fg_color="#e0e0e0" if i == 0 else "#f8f8f8", text_color="black")
                    label.grid(row=i + 1, column=j, padx=5, pady=2)

        current_scrollable_frame.pack(fill="both", expand=True, padx=20, pady=20)

        dynamic_label.destroy()















    elif selected_option=="FMCG":
        #If the user has selected "IT Outsoursing" only then the analysis TCS and it's Competitors will be analysed
        dynamic_label = CTkLabel(master=tabview.tab("Share Market"), text="System is running. Please wait...")
        dynamic_label.pack(pady=10)


        current_scrollable_frame = CTkScrollableFrame(master=tabview.tab("Share Market"), fg_color="#CD8C67")
        # frame_1_for_label1.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=50, pady=50)

        import WebScraping_FMCG_Screener
        tablesLablesTogether = WebScraping_FMCG_Screener.WebScraping_FMCG_Screener_Method()

        TopRow_CompanyNames = ["", "HUL", "Marico", "Nestle", "Britannia", "Godrej Consumer", "Patanjali","Dabur","Adani Wilmar","Emami","Colgate-Palmolive","ITC","Reliance"]
        # First comum is left blank because there the 10 years, 5 years, 3 years...is displayed

        for oneLabel in tablesLablesTogether:
            print(oneLabel)
            print(tablesLablesTogether[oneLabel])
            print()

            # Title label for the table
            title_label = CTkLabel(master=current_scrollable_frame,
                                   text=oneLabel,
                                   font=("Arial", 16, "bold"),
                                   text_color="white")
            title_label.pack(pady=(20, 5))  # padding for spacing above and below the label

            # Create a frame to hold the table
            table_frame = CTkFrame(master=current_scrollable_frame,
                                   fg_color="transparent")  # transparent to inherit scrollable bg

            table_frame.pack(pady=10, fill="both", expand=True, anchor="center")

            for i, oneCompanyName in enumerate(TopRow_CompanyNames):
                label = CTkLabel(table_frame, text=str(oneCompanyName), corner_radius=5, width=100, height=30)
                label.grid(row=0, column=i, padx=5, pady=2)

            # Display the table
            for i, row in enumerate(tablesLablesTogether[oneLabel]):
                for j, cell in enumerate(row):
                    # enumerate() gives you two values: the index (j) and the corresponding value (cell)

                    label = CTkLabel(table_frame, text=str(cell), corner_radius=5, width=100, height=30,
                                     fg_color="#e0e0e0" if i == 0 else "#f8f8f8", text_color="black")
                    label.grid(row=i + 1, column=j, padx=5, pady=2)

        current_scrollable_frame.pack(fill="both", expand=True, padx=20, pady=20)

        dynamic_label.destroy()















def show_new_ui():
    """Display a new frame after successful login."""
    # Create a tabbed interface
    global tabview
    #Since this Tabview will be used outside this function

    tabview = CTkTabview(master=app, fg_color="gray20")
    # Change dimensions
    # Change fg_color for background

    tabview.pack(expand=True, fill="both", padx=20, pady=20)
 # Adds padding around the tab view.
    # Use pack(expand=True, fill="both") instead of fixed padx/pady
    # This stretches it to full window
    # expand=True lets it grow, fill="both" fills both horizontally and vertically.

    tabview.add("Share Market")
    tabview.add("Gold market")
    tabview.add("Debt Investing")
    # Add three tabs to the tabbed interface




    ll = CTkLabel(master=tabview.tab("Share Market"), text="Select any one sector for Analysis", font=('Arial', 16), text_color="#FFCC70")
    ll.pack(padx=5, pady=5)

    # Frame to hold both widgets
    container_frame = CTkFrame(master=tabview.tab("Share Market"), fg_color="gray20")
    container_frame.pack(pady=10)


    global analysis_dropdown_menu
    analysis_dropdown_menu = CTkComboBox(master=container_frame, values=["IT Outsoursing", "FMCG","Banks and NBFC","Paints","Reliance and Compititors"])
    # You can change fg_color, dropdown_fg_color, border_color and corner_radius
    analysis_dropdown_menu.pack(side="left",padx=10)


    button_1 = CTkButton(master=container_frame, text="Run Analysis", command=on_button_click)
    button_1.pack(side="right",padx=10)















    frame_1_for_label2 = CTkScrollableFrame(master=tabview.tab("Gold market"), fg_color="#CD8C67")
    frame_1_for_label2.pack(fill="both", expand=True, padx=50, pady=50)


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

CTkLabel(master=frame_3, text="Welcome to Ray Finace", font=("Arial Bold", 20), justify="left").pack(expand=True, pady=(30, 15))
username_entry = CTkEntry(master=frame_3, placeholder_text="Enter your username", width=400)
username_entry.pack(expand=True, pady=15, padx=20)
password_entry = CTkEntry(master=frame_3, placeholder_text="Enter your password", width=400, show="*")
password_entry.pack(expand=True, pady=15, padx=20)
login_button = CTkButton(master=frame_3, text="Login", command=check_login)
login_button.pack(expand=True, fill="both", pady=(30, 15), padx=30)
error_label = CTkLabel(master=frame_3, text="", font=("Arial", 14))







app.mainloop()
