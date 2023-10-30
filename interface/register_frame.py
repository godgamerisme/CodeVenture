import tkinter as tk
from authentication.UserAuthenticate import UserAuthenticate

class RegisterFrame(tk.Frame):
    """
    The class definition for the RegisterFrame class.
    """
    
    def __init__(self,master,homepage_frame,auth:UserAuthenticate):
        """
        The constructor for the LoginFrame class
        :param master: The parent widget.
        :param homepage_frame: The homepage frame.
        """
        super().__init__(master)
        self.master = master
        self.homepage_frame = homepage_frame
        self.auth = auth

        # Set the background colour of the frame to follow main window
        self.configure(bg="white")

        # Create a Register Title
        register_title = tk.Label(master=self, text="Create Account", font=("Helvetica", 24,"bold"),bg="white")
        register_title.grid(row=0,columnspan=2,padx=10,pady=(50,10))

        # Create a First Name Label
        first_name_label = tk.Label(master=self, text="First Name",font=("Helvetica", 12),bg="white")
        first_name_label.grid(row=1,column=0,padx=10,pady=(10,0),sticky="w")

        # Create a First Name Entry
        self.first_name = tk.StringVar()
        self.first_name_entry = tk.Entry(master=self, textvariable=self.first_name)
        self.first_name_entry.grid(row=2,column=0,padx=10,pady=(0,10),sticky="ew",columnspan=2)

        # Create a Last Name Label
        last_name_label = tk.Label(master=self, text="Last Name",font=("Helvetica", 12),bg="white")
        last_name_label.grid(row=3,column=0,padx=10,pady=(10,0),sticky="w")

        # Create a Last Name Entry
        self.last_name = tk.StringVar()
        self.last_name_entry = tk.Entry(master=self, textvariable=self.last_name)
        self.last_name_entry.grid(row=4,column=0,padx=10,pady=(0,10),sticky="ew",columnspan=2)

        # Create a Password Label
        password_label = tk.Label(master=self, text="Password",font=("Helvetica", 12),bg="white")
        password_label.grid(row=5,column=0,padx=10,pady=(10,0),sticky="w")

        # Create a Password Entry
        self.password = tk.StringVar()
        self.password_entry = tk.Entry(master=self, textvariable=self.password,show="●")
        self.password_entry.grid(row=6,column=0,padx=10,pady=(0,10),sticky="ew",columnspan=2)

        # Create a Email Label
        email_label = tk.Label(master=self, text="Email",font=("Helvetica", 12),bg="white")
        email_label.grid(row=7,column=0,padx=10,pady=(10,0),sticky="w")

        # Create a Email Entry
        self.email = tk.StringVar()
        self.email_entry = tk.Entry(master=self, textvariable=self.email)
        self.email_entry.grid(row=8,column=0,padx=10,pady=(0,10),sticky="ew",columnspan=2)

        # Create a User Type Label
        user_type_label = tk.Label(master=self, text="User Type",font=("Helvetica", 12),bg="white")
        user_type_label.grid(row=9,column=0,padx=10,pady=(10,0),sticky="w")

        # Create a Dropdown Menu
        self.user_type = tk.StringVar()
        self.user_type.set("YoungLearner")
        user_type_dropdown = tk.OptionMenu(self,self.user_type,"YoungLearner","Parent","Educator")
        user_type_dropdown.grid(row=10,column=0,padx=10,pady=(0,10),sticky="ew",columnspan=2)

        # Create a Register Button
        register_button = tk.Button(master=self, text="Register",command=self.register, background="#FFCC80",font=("Helvetica", 15),width=15,height=1,borderwidth=2,relief=tk.RAISED)
        register_button.grid(row=11,columnspan=2,padx=10,pady=10,sticky="ew")

        # Create a back button
        back_button = tk.Button(master=self, text="Back",command=self.navigate_to_homepage, background="#FFCC80",font=("Helvetica", 15),width=15,height=1,borderwidth=2,relief=tk.RAISED)
        back_button.grid(row=12,columnspan=2,padx=10,pady=10,sticky="ew")

        # Create a Register Text
        self.register_text = tk.StringVar()
        register_message = tk.Message(master=self, textvariable=self.register_text,width=150,font=("Helvetica", 9),bg="white")
        register_message.grid(row=13,columnspan=2,padx=10,pady=10)

        # Create a UserName Message
        self.username_text = tk.StringVar()
        username_message = tk.Message(master=self, textvariable=self.username_text,width=150,font=("Helvetica", 9),bg="white")
        username_message.grid(row=14,columnspan=2,padx=10,pady=0)

    def register(self):
        """
        Frontend function for the authentication procedure.
        This is invoked when the register button is clicked.
        :return: None
        """ 
        self.register_text.set("Register Successful")
        # Create instance of UserAuthenticate class
        user = self.auth.register(self.first_name.get(),self.last_name.get(),self.password.get(),self.email.get(),self.user_type.get())
        if(user): 
            self.register_text.set("Register Successful")
            self.username_text.set("Your username is " + user.username)
        else:
            self.register_text.set("Register Failed")

    def navigate_to_homepage(self):
        """
        Function to handle the action when the "Back" button is clicked.
        """
        self.place_forget()
        self.homepage_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)



