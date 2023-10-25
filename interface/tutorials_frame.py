import tkinter as tk
from database.ModuleDatabase import ModuleDatabase
from Modules import *
from interface.tutorial_frame import TutorialFrame
from User import *

class TutorialsFrame(tk.Frame):
    """
    The class definition for the TutorialsFrame class.
    """

    def __init__(self,master,moduleframe,user_obj:YoungLearner,modules_db:ModuleDatabase,module_selected:Module):
        """
        The constructor for the TutorialsFrame class
        """
        super().__init__(master)
        self.master = master
        self.moduleframe = moduleframe
        self.user_obj = user_obj
        self.modules_db = modules_db
        self.module_selected = module_selected

        # Create a label for the module name
        module_name_label = tk.Label(master=self, text=self.module_selected.get_module_name(), font=("Helvetica", 20, "bold"))
        module_name_label.grid(row=0, column=0, padx=10, pady=10, columnspan=len(self.module_selected.get_tutorials()))

        # Create a list to store the frame widgets
        self.frames = []
        self.tutorials = self.module_selected.get_tutorials()

        # Create frames and add them to the frames list
        for i,tutorial in enumerate(self.tutorials):
            tutorial_frame = tk.Frame(master=self)
            self.frames.append(tutorial_frame)

            circle_canvas = tk.Canvas(master=tutorial_frame, width=50, height=50)
            circle_canvas.grid(row=0, column=0, padx=10, pady=10)

            # Calculate the center coordinates of the canvas
            center_x = int(circle_canvas["width"])/2
            center_y = int(circle_canvas["height"])/2

            # Calculate the radius
            radius = min(center_x,center_y)

            # Calculate the coordinates for the circle (x1, y1, x2, y2)
            x1 = center_x - radius
            y1 = center_y - radius
            x2 = center_x + radius
            y2 = center_y + radius

            # Create circle
            circle_canvas.create_oval(x1,y1,x2,y2 ,fill="black", outline="#FFCC80")

            # Add text number to the center of canvas
            number = i+1
            circle_canvas.create_text(center_x, center_y, text=number, font=("Helvetica", 25, "bold"), fill="white")

            # Create a label for the tutorial name
            tutorial_name_label = tk.Label(master=tutorial_frame, text=tutorial.get_tutorial_name(), font=("Helvetica", 15, "bold"),wraplength=200,width=20,height=3)
            tutorial_name_label.grid(row=1, column=0, padx=10, pady=10,rowspan=2)

            # Create enter tutorial button
            enter_tutorial_button = tk.Button(master=tutorial_frame, text="Enter", font=("Helvetica", 15), width=15,background="#FFCC80",
                                              height=2, borderwidth=2, relief=tk.RAISED,command=lambda tutorial=tutorial: self.enter_tutorial(tutorial))
            enter_tutorial_button.grid(row=3, column=0, padx=10, pady=(30,10))

        # Arrange frames side by side using grid
        for i,frame in enumerate(self.frames):
            frame.grid(row=1,column=i,padx=10,pady=10)

        # Create a Back Button
        back_button = tk.Button(master=self, text="Back", font=("Helvetica", 15,"bold"), width=15,background="#FFCC80", command=self.navigate_to_module,
                                height=2, borderwidth=2, relief=tk.RAISED)
        back_button.grid(row=2, columnspan=len(self.frames), padx=10, pady=10)


    def navigate_to_module(self):
        """
        The function that is called when the user clicks on the "Back" button.
        """
        self.place_forget()
        self.moduleframe.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def enter_tutorial(self,tutorial):
        """
        The function that is called when the user clicks on the "Enter" button.
        """
        self.place_forget()
        self.tutorial_frame = TutorialFrame(self.master,self,self.user_obj,self.modules_db,self.module_selected,tutorial)
        self.tutorial_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

            



        
        


    