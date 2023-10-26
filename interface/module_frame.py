import tkinter as tk
from database.ModuleDatabase import ModuleDatabase
from Modules import *
from interface.tutorials_frame import TutorialsFrame
from User import *
from interface.quiz_frame import QuizFrame

class ModuleFrame(tk.Frame):
    """
    The class definition for the ModuleFrame class.
    """

    def __init__(self,master,modulesframe,user_obj:YoungLearner,modules_db:ModuleDatabase,module_selected:Module):
        """
        The constructor for the ModuleFrame class
        """
        super().__init__(master)
        self.master = master
        self.modulesframe = modulesframe
        self.user_obj = user_obj
        self.modules_db = modules_db
        self.module_selected = module_selected
        
        # Create a label for the module name
        module_name_label = tk.Label(master=self, text=self.module_selected.get_module_name(), font=("Helvetica", 20, "bold"))
        module_name_label.grid(row=0, column=0, padx=10, pady=10)

        # Create a View Tutorials Button
        view_tutorials_button = tk.Button(master=self, text="View Tutorials", font=("Helvetica", 15,"bold"), width=15,background="#FFCC80",
                                          command=self.navigate_to_tutorials,height=2, borderwidth=2, relief=tk.RAISED)
        view_tutorials_button.grid(row=1, column=0, padx=10, pady=10)

        # Create a Take Quiz Button
        take_quiz_button = tk.Button(master=self, text="Take Quiz", font=("Helvetica", 15,"bold"), width=15,background="#FFCC80",command=self.navigate_to_quiz,
                                     height=2, borderwidth=2, relief=tk.RAISED)
        take_quiz_button.grid(row=2, column=0, padx=10, pady=10)

        # Create a Controls Guide Button
        controls_guide_button = tk.Button(master=self, text="Controls Guide", font=("Helvetica", 15,"bold"), width=15,background="#FFCC80",
                                          height=2, borderwidth=2, relief=tk.RAISED)
        controls_guide_button.grid(row=3, column=0, padx=10, pady=10)

        # Create a Back Button
        back_button = tk.Button(master=self, text="Back", font=("Helvetica", 15,"bold"), width=15,background="#FFCC80", command=self.navigate_to_modules,
                                height=2, borderwidth=2, relief=tk.RAISED)
        back_button.grid(row=4, column=0, padx=10, pady=10)


    def navigate_to_modules(self):
        """
        The function that is called when the user clicks on the "Back" button.
        """
        self.place_forget()
        self.modulesframe.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def navigate_to_tutorials(self):
        """
        The function that is called when the user clicks on the "View Tutorials" button.
        """
        self.place_forget()
        self.tutorialsframe = TutorialsFrame(self.master,self,self.user_obj,self.modules_db,self.module_selected)
        self.tutorialsframe.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def navigate_to_quiz(self):
        """
        The function that is called when the user clicks on the "Take Quiz" button.
        """
        self.place_forget()
        self.quizframe = QuizFrame(self.master,self,self.user_obj,self.modules_db,self.module_selected)
        self.quizframe.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


        
