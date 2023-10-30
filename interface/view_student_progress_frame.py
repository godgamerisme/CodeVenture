import tkinter as tk
from User import *
from database.ModuleDatabase import ModuleDatabase
from user_manager import UserManager
from interface.check_progress_frame import CheckProgressFrame

class ViewStudentProgressFrame(tk.Frame):
    """
    The class definition for the ViewStudentProgressFrame class.
    
    """

    def __init__(self, master, educator_dashboard_frame, user_obj:Educator,modules_db:ModuleDatabase,current_student:int=0):
        """
        The constructor for the ViewStudentProgressFrame class
        """
        super().__init__(master)
        self.master = master
        self.educator_dashboard_frame = educator_dashboard_frame
        self.user_obj = user_obj
        self.modules_db = modules_db
        self.current_student = current_student

        # Set the background colour of the frame to follow main window
        self.configure(bg="white")

        # Get all the young learners
        self.all_young_learners = UserManager.get_instance().get_all_young_learners()

        # Slice the array to get 6 young learners to display
        self.young_learners = self.all_young_learners[self.current_student:self.current_student+6]

        # Create a label for select student
        select_student_label = tk.Label(master=self, text="Select Student", font=("Helvetica", 20, "bold"), bg="white")
        select_student_label.grid(row=0, column=0, padx=10, pady=10,columnspan=3)

        # Create a Frame to hold the buttons
        student_buttons_frame = tk.Frame(master=self, bg="white")
        student_buttons_frame.grid(row=1, column=0, padx=10, pady=10,columnspan=4)

        # Create buttons for each young learner, each button will display the young learner's full name,
        # each row display two buttons, beside each button there is a canvas(a circle) to show the number
        self.student_buttons = []
        for i, young_learner in enumerate(self.young_learners):
            # Create a canvas for the circle, the circle is on the left of the button
            student_circle_canvas = tk.Canvas(master=student_buttons_frame, width=50, height=50, bg="white",highlightthickness=0)
            student_circle_canvas.grid(row=int(i//2)+1, column=(i%2)*2, padx=10, pady=10)

            # Calculate the center coordinates of the canvas
            center_x = int(student_circle_canvas["width"])/2
            center_y = int(student_circle_canvas["height"])/2

            # Calculate the radius
            radius = min(center_x,center_y)

            # Calculate the coordinates for the circle (x1, y1, x2, y2)
            x1 = center_x - radius
            y1 = center_y - radius
            x2 = center_x + radius
            y2 = center_y + radius

            # Create circle
            student_circle_canvas.create_oval(x1,y1,x2,y2 ,fill="black", outline="#FFCC80")

            # Add text number to the center of canvas
            number = i+1+self.current_student
            student_circle_canvas.create_text(center_x, center_y, text=number, font=("Helvetica", 25, "bold"), fill="white")

            student_button = tk.Button(master=student_buttons_frame, text=young_learner.get_fullname(), font=("Helvetica", 15), width=20,background="#FFCC80",
                                       command=lambda young_learner=young_learner: self.select_student(young_learner),
                                      height=2, borderwidth=2, relief=tk.RAISED,wraplength=200)
            student_button.grid(row=int(i//2)+1, column=(i%2)*2+1, padx=10, pady=10)
            self.student_buttons.append(student_button)

        # Create a Back Button
        back_button = tk.Button(master=self, text="Back", font=("Helvetica", 15, "bold"), width=15, background="#FFCC80",
                                command=self.navigate_to_view_student_progress_or_educator_dashboard,
                                height=1, borderwidth=2, relief=tk.RAISED)
        back_button.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

        # Check if its the last page
        if self.current_student+6 < len(self.all_young_learners):
            # Create a Next Button
            next_button = tk.Button(master=self, text="Next Page", font=("Helvetica", 15, "bold"), width=15, background="#FFCC80",
                                    command=self.navigate_to_next_page,
                                    height=1, borderwidth=2, relief=tk.RAISED)
            next_button.grid(row=3, column=3, padx=20, pady=10, sticky=tk.E)
        else:
            # Create a Back to Dashboard Button
            back_to_dashboard_button = tk.Button(master=self, text="Back to Dashboard", font=("Helvetica", 15, "bold"), width=15, background="#FFCC80",
                                    command=self.navigate_to_educator_dashboard,
                                    height=1, borderwidth=2, relief=tk.RAISED)
            back_to_dashboard_button.grid(row=3, column=3, padx=20, pady=10, sticky=tk.E)

    def navigate_to_educator_dashboard(self):
        """
        The function to navigate to the educator dashboard frame.
        """
        self.place_forget()
        self.educator_dashboard_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def navigate_to_next_page(self):
        """
        The function to navigate to the next page.
        """
        self.place_forget()
        self.view_student_progress_frame = ViewStudentProgressFrame(self.master,self.educator_dashboard_frame,self.user_obj,self.modules_db,self.current_student+6)
        self.view_student_progress_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


    def select_student(self,student:YoungLearner):
        """
        The function to handle the action when the user clicks on the student button.
        """
        self.place_forget()
        # based on student selected, navigate to check progress frame
        self.check_progress_frame = CheckProgressFrame(self.master,self,student,self.modules_db)
        self.check_progress_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        

    def navigate_to_view_student_progress_or_educator_dashboard(self):
        """
        The function that is called when the user clicks on the "Back" button.
        """
        self.place_forget()
        if self.current_student == 0:
            self.educator_dashboard_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        else:
            self.view_student_progress_frame = ViewStudentProgressFrame(self.master,self.educator_dashboard_frame,self.user_obj,self.modules_db,self.current_student-6)
            self.view_student_progress_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)