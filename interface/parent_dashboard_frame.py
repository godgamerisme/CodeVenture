import tkinter as tk
from User import *
from database.ModuleDatabase import ModuleDatabase
from interface.register_child_frame import RegisterChildFrame
from interface.check_progress_frame import CheckProgressFrame
from user_manager import UserManager

class ParentDashboardFrame(tk.Frame):
    """
    The class definition for the ParentDashboardFrame class.
    """

    def __init__(self, master, login_frame, user_obj:Parent,modules_db:ModuleDatabase):
        """
        The constructor for the ParentDashboardFrame class
        """
        super().__init__(master)
        self.master = master
        self.login_frame = login_frame
        self.user_obj = user_obj
        self.modules_db = modules_db

        # Set the background colour of the frame to follow main window
        self.configure(bg="white")

        # Create a container to hold the widgets
        container = tk.Frame(master=self, bg="white")
        container.grid(row=0, column=0, padx=10, pady=10)

        # Create a welcome message
        welcome_message = tk.Label(master=container, text="Welcome back,",
                                   font=("Helvetica", 24, "bold"), bg="white")
        welcome_message.grid(row=0, column=0, padx=10, pady=10)

        # Create a username label
        username_label = tk.Label(master=container, text=f"{self.user_obj.get_firstname()}!",font=("Helvetica", 24, "bold"), bg="white")
        username_label.grid(row=1, column=0, padx=10, pady=(5,10))

        # Create a register child button
        register_child_button = tk.Button(master=container, text="Register Child", font=("Helvetica", 15), width=15,background="#FFCC80",wraplength=150,
                                        command=self.navigate_to_register_child,height=2, borderwidth=2, relief=tk.RAISED)
        register_child_button.grid(row=2, column=0, padx=10, pady=20)

        # Create a view chil progress button
        view_child_progress_button = tk.Button(master=container, text="View Child Progress", font=("Helvetica", 15), width=15,background="#FFCC80",wraplength=150,
                                        command=self.view_child_progress,height=2, borderwidth=2, relief=tk.RAISED)
        view_child_progress_button.grid(row=3, column=0, padx=10, pady=20)

        # Create a logout button
        logout_button = tk.Button(master=container, text="Logout", font=("Helvetica", 15), width=15,background="#FFCC80", command=self.logout,
                                  height=2, borderwidth=2, relief=tk.RAISED)
        logout_button.grid(row=4, column=0, padx=10, pady=20)

         # Create a message for View Child Progress outcome
        self.view_child_progress_text = tk.StringVar()
        view_child_progress_message = tk.Message(master=self, textvariable=self.view_child_progress_text, font=("Helvetica", 15), width=500, bg="white")
        view_child_progress_message.grid(row=5, column=0, padx=10, pady=10, columnspan=2)

        # Create a canvas for the image
        self.parent_dashboard_canvas = tk.Canvas(master=self, width=400, height=450,background="white",highlightthickness=0)
        self.parent_dashboard_canvas.grid(row=0, column=1, columnspan=3, rowspan=3)

        # Insert the image onto the canvas
        image_path = "img/parent.png"
        self.parent_dashboard_image = tk.PhotoImage(file=image_path)
        self.parent_dashboard_canvas.create_image(200, 200, anchor=tk.CENTER, image=self.parent_dashboard_image)

       


    def logout(self):
        """
        The function to handle the action when the user clicks on the "Logout" button.
        """
        self.place_forget()
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def navigate_to_register_child(self):
        """
        The function to navigate to the register child frame.
        """
        self.place_forget()
        self.register_child_frame = RegisterChildFrame(self.master,self,self.user_obj,self.modules_db)
        self.register_child_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def view_child_progress(self):
        """
        The function to navigate to the view child progress frame.
        """
        if len(self.user_obj.get_children()) == 0:
            self.view_child_progress_text.set("You have not registered any child yet.")
            return
        self.place_forget()
        children_obj = UserManager.get_instance().get_children(self.user_obj)
        self.view_child_progress_frame = CheckProgressFrame(self.master,self,children_obj[0],self.modules_db)
        self.view_child_progress_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)