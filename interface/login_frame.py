import tkinter as tk
from database.UserDatabase import UserDatabase
from authentication.UserAuthenticate import UserAuthenticate
from User import *
from interface.student_dashboard_frame import StudentDashboardFrame
from interface.reset_password_frame import ResetPasswordFrame

class LoginFrame(tk.Frame):
    """
    The class definition for the LoginFrame class.
    """

    def __init__(self, master, homepage_frame):
        """
        The constructor for the LoginFrame class
        :param master: The parent widget.
        :param homepage_frame: The homepage frame.
        
        """
        super().__init__(master)
        self.master = master
        self.homepage_frame = homepage_frame

        self.auth = self.setUpAuthenticate()
        
        # Create a Login Title
        login_title = tk.Label(master=self, text="Good to see you!", font=("Helvetica", 24,"bold"))
        login_title.grid(row=0,columnspan=2,padx=10,pady=10)

        # Create a Username Label
        username_label = tk.Label(master=self, text="Username",font=("Helvetica", 12))
        username_label.grid(row=1,column=0,padx=10,pady=(10,0),sticky="w")

        # Create a Username Entry
        self.username = tk.StringVar()
        self.username_entry = tk.Entry(master=self, textvariable=self.username)
        self.username_entry.grid(row=2,column=0,padx=10,pady=(0,10),sticky="ew",columnspan=2)

        # Create a Password Label
        password_label = tk.Label(master=self, text="Password",font=("Helvetica", 12))
        password_label.grid(row=3,column=0,padx=10,pady=(10,0),sticky="w")

        # Create a Password Entry
        self.password = tk.StringVar()
        self.password_entry = tk.Entry(master=self, textvariable=self.password,show="●")
        self.password_entry.grid(row=4,column=0,padx=10,pady=(0,10),sticky="ew",columnspan=2)

        # Create a Reset Password Button
        reset_password_button = tk.Button(master=self, text="Reset Password",background="#FFCC80",font=("Helvetica", 15),width=15,height=1,borderwidth=2,relief=tk.RAISED,
                                          command=self.navigate_to_reset_password)
        
        reset_password_button.grid(row=5, column=0,padx=10,pady=10)

        # Create a Login Button
        login_button = tk.Button(master=self, text="Login",background="#FFCC80",font=("Helvetica", 15),width=15,height=1,borderwidth=2,relief=tk.RAISED,
                                 command=self.authenticate_login)
        login_button.grid(row=5,column=1,padx=10,pady=10)

        # Create a Back Button
        back_button = tk.Button(master=self, text="Back",background="#FFCC80",font=("Helvetica", 15),width=15,height=1,borderwidth=2,relief=tk.RAISED,
                                command=self.navigate_to_homepage)
        back_button.grid(row=6,columnspan=2,padx=10,pady=10)

        # Create a Login outcome message
        self.login_text = tk.StringVar()
        login_message = tk.Message(master=self, textvariable=self.login_text, width=150,font=("Helvetica", 9))
        login_message.grid(row=7,columnspan=2,padx=10,pady=10)

    def authenticate_login(self):
        """
        The function to authenticate the login.
        """
        # Authenticate user
        user = self.auth.login(self.username.get(), self.password.get())
        modules_db = self.auth.get_module_db()

        if isinstance(user, User):
            # Clear entries upon successful login
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)

            # Remove login page from display
            self.place_forget()
            if isinstance(user, YoungLearner):
                # Create and display the YoungLearner Dashboard
                student_dashboard_frame = StudentDashboardFrame(self.master, self, user,modules_db)
                student_dashboard_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def navigate_to_homepage(self):
        """
        The function to navigate to the homepage.
        """
        self.place_forget()
        self.homepage_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def navigate_to_reset_password(self):
        """
        The function to reset the password.
        """
        self.place_forget()
        reset_password_frame = ResetPasswordFrame(self.master, self,self.auth)
        reset_password_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def setUpAuthenticate(self):
        # Create instance of UserAuthenticate class
        auth = UserAuthenticate()
        return auth
        