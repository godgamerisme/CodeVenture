import tkinter as tk
from User import *
from database.ModuleDatabase import ModuleDatabase
from interface.modules_frame import ModulesFrame

class StudentDashboardFrame(tk.Frame):
    """
    The class definition for the StudentDashboardFrame class.
    """
    
    def __init__(self, master, login_frame, user_obj:YoungLearner,modules_db:ModuleDatabase):
        """
        The constructor for the StudentDashboardFrame class
        """
        super().__init__(master)
        self.master = master
        self.login_frame = login_frame
        self.user_obj = user_obj
        self.modules_db = modules_db

        # for row_count in range(5):
        #     self.master.rowconfigure(row_count, weight=1, uniform="row")

        # self.master.columnconfigure(0, weight=1, uniform="col")

        # Create a container to hold the widgets
        container = tk.Frame(master=self)
        container.grid(row=0, column=0, padx=10, pady=10)

        # Create a welcome message
        welcome_message = tk.Label(master=container, text="Welcome back,",
                                   font=("Helvetica", 24, "bold"))
        welcome_message.grid(row=0, column=0, padx=10, pady=10)

        # Create a username label
        username_label = tk.Label(master=container, text=f"{self.user_obj.get_firstname()}!",font=("Helvetica", 24, "bold"))
        username_label.grid(row=1, column=0, padx=10, pady=(5,10))

        # Create a view modules button
        view_modules_button = tk.Button(master=container, text="View Modules", font=("Helvetica", 15), width=15,background="#FFCC80",command=self.navigate_to_modules,
                                        height=2, borderwidth=2, relief=tk.RAISED)
        view_modules_button.grid(row=2, column=0, padx=10, pady=20)

        # Create a check progress button
        check_progress_button = tk.Button(master=container, text="Check Progress", font=("Helvetica", 15), width=15,background="#FFCC80",
                                          height=2, borderwidth=2, relief=tk.RAISED)
        check_progress_button.grid(row=3, column=0, padx=10, pady=20)

        # Create a logout button
        logout_button = tk.Button(master=container, text="Logout", font=("Helvetica", 15), width=15,background="#FFCC80", command=self.logout,
                                  height=2, borderwidth=2, relief=tk.RAISED)
        logout_button.grid(row=4, column=0, padx=10, pady=20)

        # Create a canvas for the image
        self.student_dashboard_canvas = tk.Canvas(master=self, width=400, height=450)
        self.student_dashboard_canvas.grid(row=0, column=1, columnspan=3, rowspan=3)

        # Insert the image onto the canvas
        image_path = "img/studentdashboard.png"
        self.student_dashboard_image = tk.PhotoImage(file=image_path)
        self.display_image()
        # self.student_dashboard_canvas.create_image(0, 0, anchor=tk.NW, image=self.student_dashboard_image)

    def navigate_to_modules(self):
        """
        The function to navigate to the modules frame.
        """
        self.place_forget()
        self.modules_frame = ModulesFrame(self.master,self,self.user_obj,self.modules_db)
        self.modules_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)



    def display_image(self):
        # Get the original image dimensions
        original_width = self.student_dashboard_image.width()
        original_height = self.student_dashboard_image.height()

        # Get the canvas dimensions
        canvas_width = self.student_dashboard_canvas.winfo_width()
        canvas_height = self.student_dashboard_canvas.winfo_height()

        # Calculate the zoom factor for both width and height
        zoom_factor_width = canvas_width / original_width
        zoom_factor_height = canvas_height / original_height

        # Use the minimum zoom factor to maintain the aspect ratio
        zoom_factor = min(zoom_factor_width, zoom_factor_height)

        # Create and display the image with the adjusted size
        self.student_dashboard_canvas.create_image(0, 0, anchor=tk.NW, image=self.student_dashboard_image, tags='img')
        self.student_dashboard_canvas.scale('img', 0, 0, zoom_factor, zoom_factor)

    def logout(self):
        """
        The function to handle the action when the user clicks on the "Logout" button.
        """
        self.place_forget()
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # def set_up_modules(self):
    #     """
    #     The function to set up the modules for the student.
    #     """
    #     return self.modules_db.get_module_array()