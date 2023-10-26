import tkinter as tk
from User import *
from database.ModuleDatabase import ModuleDatabase
from module_manager import ModuleManager

class CheckProgressFrame(tk.Frame):
    """
    The class definition for the CheckProgressFrame class.
    """

    def __init__(self,master,studentdashboardframe,user_obj:YoungLearner,modules_db:ModuleDatabase):
        """
        The constructor for the CheckProgressFrame class
        """
        super().__init__(master)
        self.master = master
        self.studentdashboardframe = studentdashboardframe
        self.user_obj = user_obj
        self.modules_db = modules_db

        # populate user progress
        self.user_obj.populate_user_progress(self.modules_db.get_module_array())

        # Get all tutorials completed and all quizzes completed
        self.all_tutorials_completed = self.user_obj.get_all_tutorials_completed()
        self.all_quizzes_completed = self.user_obj.get_all_quizzes_completed()

        self.tutorial_completion_percentage = self.__calculate_percentage_completion(len(self.all_tutorials_completed),ModuleManager.get_instance().calculate_number_of_tutorials())
        self.quiz_completion_percentage = self.__calculate_percentage_completion(len(self.all_quizzes_completed),ModuleManager.get_instance().calculate_number_of_quizzes())

        # Create a container to hold the widgets
        container = tk.Frame(master=self)
        container.grid(row=0, column=0, padx=10, pady=10)

        # Create a canvas for the image
        self.check_progress_canvas = tk.Canvas(master=container, width=200, height=200)
        self.check_progress_canvas.grid(row=0, column=0, padx=10, pady=10)

        # Insert the image onto the canvas
        image_path = "img/progress.png"
        self.check_progress_img = tk.PhotoImage(file=image_path)
        self.check_progress_canvas.create_image(100,100, image=self.check_progress_img)

        # Create a label for the title
        title_label = tk.Label(master=container, text="Progress Tracking", font=("Helvetica", 25, "bold"))
        title_label.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        # Create another container to hold the widgets ,which is tutorial progress frame and quiz progress frame
        container2 = tk.Frame(master=self)
        container2.grid(row=1, column=0, padx=10, pady=10)

        # Create a frame for tutorial Progress below the container
        tutorial_progress_frame = tk.Frame(master=container2,background="#F6F0FF")
        tutorial_progress_frame.grid(row=0, column=0, padx=10, pady=10,sticky=tk.W)

        # Create a label for the tutorial progress title
        tutorial_progress_title_label = tk.Label(master=tutorial_progress_frame, text="Tutorial Progress", font=("Helvetica", 20, "bold"))
        tutorial_progress_title_label.grid(row=0, column=0, padx=10, pady=10,columnspan=2)

        # Create a label for the tutorial progress percentage
        tutorial_progress_percentage_label = tk.Label(master=tutorial_progress_frame, text=f"{self.tutorial_completion_percentage}%", font=("Helvetica", 30, "bold"))
        tutorial_progress_percentage_label.grid(row=1, column=0, padx=20, pady=10,rowspan=2,sticky=tk.W)

        # Create a label beside tutorial progress percentage to show the number of tutorials completed
        tutorial_progress_number_label = tk.Label(master=tutorial_progress_frame, text=f"{len(self.all_tutorials_completed)} of {ModuleManager.get_instance().calculate_number_of_tutorials()} tutorials completed", font=("Helvetica", 15),wraplength=100)
        tutorial_progress_number_label.grid(row=1, column=2, padx=10, pady=10,rowspan=2,sticky=tk.W)

        # Create a frame for quiz Progress below the container beside the tutorial progress frame
        quiz_progress_frame = tk.Frame(master=container2,background="#F6F0FF")
        quiz_progress_frame.grid(row=0, column=1, padx=10, pady=10,sticky=tk.W)

        # Create a label for the quiz progress title
        quiz_progress_title_label = tk.Label(master=quiz_progress_frame, text="Quiz Progress", font=("Helvetica", 20, "bold"))
        quiz_progress_title_label.grid(row=0, column=0, padx=10, pady=10,columnspan=2)

        # Create a label for the quiz progress percentage
        quiz_progress_percentage_label = tk.Label(master=quiz_progress_frame, text=f"{self.quiz_completion_percentage}%", font=("Helvetica", 30, "bold"))
        quiz_progress_percentage_label.grid(row=1, column=0, padx=20, pady=10,rowspan=2,sticky=tk.W)

        # Create a label beside quiz progress percentage to show the number of quizzes completed
        quiz_progress_number_label = tk.Label(master=quiz_progress_frame, text=f"{len(self.all_quizzes_completed)} of {ModuleManager.get_instance().calculate_number_of_quizzes()} quizzes completed", font=("Helvetica", 15),wraplength=100)
        quiz_progress_number_label.grid(row=1, column=2, padx=10, pady=10,rowspan=2,sticky=tk.W)

        # Create a Back Button position in the center
        back_button = tk.Button(master=self, text="Back", font=("Helvetica", 15, "bold"), width=15, background="#FFCC80",
                                command=self.navigate_to_dashboard,
                                height=1, borderwidth=2, relief=tk.RAISED)
        back_button.grid(row=2, column=0, padx=10, pady=10, sticky=tk.N, columnspan=2)

    def navigate_to_dashboard(self):
        """
        The function that is called when the user clicks on the "Back" button.
        """
        self.place_forget()
        self.studentdashboardframe.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


    def __calculate_percentage_completion(self,completed,total):
        """
        Calculate the percentage of tutorials/quizzes completed
        """
        return round((completed/total)*100,0)

        
        



