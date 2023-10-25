import tkinter as tk
from database.ModuleDatabase import ModuleDatabase
from Modules import *
from User import *

class TutorialFrame(tk.Frame):
    """
    The class definition for the TutorialFrame class.
    """

    def __init__(self, master, tutorialsframe,user_obj:YoungLearner, modules_db: ModuleDatabase, module_selected: Module,
                 tutorial_selected: Tutorial):
        """
        The constructor for the TutorialFrame class
        """
        super().__init__(master)
        self.master = master
        self.tutorialsframe = tutorialsframe
        self.user_obj = user_obj
        self.modules_db = modules_db
        self.module_selected = module_selected
        self.tutorial_selected = tutorial_selected

        # Create a label for the tutorial name
        tutorial_name_label = tk.Label(master=self, text=self.tutorial_selected.get_tutorial_name(),
                                       font=("Helvetica", 20, "bold"))
        tutorial_name_label.grid(row=0, column=0, padx=10, pady=10,columnspan=2)

        # Create a label for the tutorial content
        tutorial_content_label = tk.Label(master=self, text=self.tutorial_selected.get_tutorial_content(),
                                          font=("Helvetica", 15), wraplength=700, justify=tk.LEFT)
        tutorial_content_label.grid(row=1, column=0, padx=10, pady=10)

        # Create a Back Button
        back_button = tk.Button(master=self, text="Back", font=("Helvetica", 15, "bold"), width=15, background="#FFCC80",
                                command=self.navigate_to_tutorials,
                                height=1, borderwidth=2, relief=tk.RAISED)
        back_button.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        # Create a Complete Tutorial Button
        complete_tutorial_button = tk.Button(master=self, text="Complete Tutorial", font=("Helvetica", 15, "bold"),
                                             width=15, background="#FFCC80",command=self.complete_tutorial,
                                             height=1, borderwidth=2, relief=tk.RAISED)
        complete_tutorial_button.grid(row=2, column=1, padx=10, pady=10,sticky=tk.W)

        # Create a Complete Tutorial Outcome text
        self.complete_tutorial_text = tk.StringVar()
        complete_tutorial_message = tk.Message(master=self, textvariable=self.complete_tutorial_text, font=("Helvetica", 15), width=200)
        complete_tutorial_message.grid(row=3, column=0, padx=10, pady=10, columnspan=2)


    def navigate_to_tutorials(self):
        """
        The function that is called when the user clicks on the "Back" button.
        """
        self.place_forget()
        self.tutorialsframe.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def complete_tutorial(self):
        """
        The function that is called when the user clicks on the "Complete Tutorial" button.
        """
        self.modules_db.complete_tutorial(self.user_obj.get_id(),self.module_selected.get_module_id(),self.tutorial_selected.get_tutorial_id())
        self.tutorialsframe.place(relx=0.5, rely=0.5, anchor=tk.CENTER)



        