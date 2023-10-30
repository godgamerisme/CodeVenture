import tkinter as tk
from User import *
from database.ModuleDatabase import ModuleDatabase
from interface.view_student_progress_frame import ViewStudentProgressFrame


class EducatorDashboardFrame(tk.Frame):
    """
    The class definition for the EducatorDashboardFrame class.
    """

    def __init__(self, master, login_frame, user_obj:Educator,modules_db:ModuleDatabase):
        """
        The constructor for the StudentDashboardFrame class
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

        # Create a view student progress button
        view_student_progress_button = tk.Button(master=container, text="View Student Progress", font=("Helvetica", 15), width=15,background="#FFCC80",wraplength=150,
                                        command=self.navigate_to_view_student_progress,height=2, borderwidth=2, relief=tk.RAISED)
        view_student_progress_button.grid(row=2, column=0, padx=10, pady=20)

        # Create a logout button
        logout_button = tk.Button(master=container, text="Logout", font=("Helvetica", 15), width=15,background="#FFCC80", command=self.logout,
                                  height=2, borderwidth=2, relief=tk.RAISED)
        logout_button.grid(row=3, column=0, padx=10, pady=20)

        # Create a canvas for the image
        self.educator_dashboard_canvas = tk.Canvas(master=self, width=400, height=450,background="white",highlightthickness=0)
        self.educator_dashboard_canvas.grid(row=0, column=1, columnspan=3, rowspan=3)

        # Insert the image onto the canvas
        image_path = "img/teacher.png"
        self.educator_dashboard_image = tk.PhotoImage(file=image_path)
        self.educator_dashboard_canvas.create_image(200, 200, anchor=tk.CENTER, image=self.educator_dashboard_image)

    def logout(self):
        """
        The function to handle the action when the user clicks on the "Logout" button.
        """
        self.place_forget()
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def navigate_to_view_student_progress(self):
        """
        The function to navigate to the view student progress frame.
        """
        self.place_forget()
        self.view_student_progress_frame = ViewStudentProgressFrame(self.master,self,self.user_obj,self.modules_db)
        self.view_student_progress_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)