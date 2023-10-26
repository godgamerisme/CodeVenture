import tkinter as tk
from User import *
from database.ModuleDatabase import ModuleDatabase
from user_manager import UserManager

class RegisterChildFrame(tk.Frame):
    """
    The class definition for the RegisterChildFrame class.
    """
    def __init__(self, master, parent_dashboard_frame, user_obj:Parent,modules_db:ModuleDatabase):
        """
        The constructor for the RegisterChildFrame class
        """
        super().__init__(master)
        self.master = master
        self.parent_dashboard_frame = parent_dashboard_frame
        self.user_obj = user_obj
        self.modules_db = modules_db

        # Create a label for the title
        title_label = tk.Label(master=self, text="Register Child (Maximum of One)", font=("Helvetica", 25, "bold"),wraplength=300)
        title_label.grid(row=0, column=0, padx=10, pady=10,columnspan=2,rowspan=2)

        # Create a label for Please enter your child's email
        email_label = tk.Label(master=self, text="Please enter your child's email", font=("Helvetica", 15))
        email_label.grid(row=2, column=0, padx=10, pady=10,columnspan=2)

        # Create a Email Entry
        self.email = tk.StringVar()
        self.email_entry = tk.Entry(master=self, textvariable=self.email)
        self.email_entry.grid(row=3, column=0, padx=10, pady=10, sticky="ew",columnspan=2)

        # Create a Register Button
        register_button = tk.Button(master=self, text="Register", font=("Helvetica", 15), width=15, background="#FFCC80",command=self.register_child,
                                    height=2, borderwidth=2, relief=tk.RAISED)
        register_button.grid(row=4, column=0, padx=10, pady=10, sticky=tk.E)

        # Create a Back Button
        back_button = tk.Button(master=self, text="Back", font=("Helvetica", 15), width=15, background="#FFCC80",command=self.navigate_to_parent_dashboard,
                                height=2, borderwidth=2, relief=tk.RAISED)
        back_button.grid(row=5, column=0, padx=10, pady=10, sticky=tk.E)

        # Create a message for registration outcome
        self.register_child_text = tk.StringVar()
        register_child_message = tk.Message(master=self, textvariable=self.register_child_text, font=("Helvetica", 15), width=500)
        register_child_message.grid(row=6, column=0, padx=10, pady=10, columnspan=2)

    def register_child(self):
        """
        The function to handle the action when the user clicks on the "Register" button.
        """
        # Get the email from the entry
        email = self.email.get()

        # Check if email is empty
        if email == "":
            self.register_child_text.set("Please enter your child's email.")
            return
        
        # Try adding child to parent
        self.register_child_text.set(self.user_obj.add_child(email))
        UserManager.get_instance().update_register_child()

    def navigate_to_parent_dashboard(self):
        """
        The function to handle the action when the user clicks on the "Back" button.
        """
        # Navigate to parent dashboard
        self.place_forget()
        self.parent_dashboard_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


        
        

        

        

