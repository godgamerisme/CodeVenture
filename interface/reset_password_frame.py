import tkinter as tk
from authentication.UserAuthenticate import UserAuthenticate

class ResetPasswordFrame(tk.Frame):
    """
    The class definition for the ResetPasswordFrame class.
    """
    
    def __init__(self,master,login_frame,auth:UserAuthenticate):
        """
        The constructor for the ResetPasswordFrame class
        :param master: The parent widget.
        :param login_frame: The login frame.
        :param auth: The UserAuthenticate object.
        """
        super().__init__(master)
        self.master = master
        self.login_frame = login_frame
        self.auth = auth

        # Set the background colour of the frame to follow main window
        self.configure(bg="white")

        # Create a Reset Password Title
        reset_password_title = tk.Label(master=self, text="Forgot Password?", font=("Helvetica", 24,"bold"),bg="white")
        reset_password_title.grid(row=0,columnspan=2,padx=10,pady=(50,10))

        # Create a email Label
        email_label = tk.Label(master=self, text="Email",font=("Helvetica", 12),bg="white")
        email_label.grid(row=1,column=0,padx=10,pady=(10,0),sticky="w")

        # Create a email Entry
        self.email = tk.StringVar()
        self.email_entry = tk.Entry(master=self, textvariable=self.email)
        self.email_entry.grid(row=2,column=0,padx=10,pady=(0,10),sticky="ew",columnspan=2)

        # Create a new password Label
        new_password_label = tk.Label(master=self, text="New Password",font=("Helvetica", 12),bg="white")
        new_password_label.grid(row=3,column=0,padx=10,pady=(10,0),sticky="w")

        # Create a new password Entry
        self.new_password = tk.StringVar()
        self.new_password_entry = tk.Entry(master=self, textvariable=self.new_password,show="●")
        self.new_password_entry.grid(row=4,column=0,padx=10,pady=(0,10),sticky="ew",columnspan=2)

        # Create a Reset Password Button
        reset_password_button = tk.Button(master=self, text="Reset Password",background="#FFCC80",font=("Helvetica", 15),width=15,height=1,borderwidth=2,relief=tk.RAISED,
                                          command=self.reset_password)
        reset_password_button.grid(row=5,columnspan=2,padx=10,pady=10,sticky="ew")

        # Create a Back Button
        back_button = tk.Button(master=self, text="Back",background="#FFCC80",font=("Helvetica", 15),width=15,height=1,borderwidth=2,relief=tk.RAISED,
                                command=self.navigate_to_login)
        back_button.grid(row=6,columnspan=2,padx=10,pady=10,sticky="ew")

        # Create a Reset Password outcome message
        self.reset_password_text = tk.StringVar()
        reset_password_message = tk.Message(master=self, textvariable=self.reset_password_text, width=150,font=("Helvetica", 9),bg="white")
        reset_password_message.grid(row=7,columnspan=2,padx=10,pady=10)

    def reset_password(self):
        """
        The function that is called when the user clicks on the "Reset Password" button.
        """
        is_reset = self.auth.reset_password(self.email.get(),self.new_password.get())
        self.email_entry.delete(0,tk.END)
        self.new_password_entry.delete(0,tk.END)

        if is_reset:
            self.reset_password_text.set("Password reset successful!")
        else:
            self.reset_password_text.set("Password reset failed!")

    def navigate_to_login(self):
        """
        The function that is called when the user clicks on the "Back" button.
        """
        self.place_forget()
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


    




        