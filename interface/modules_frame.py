import tkinter as tk
from database.ModuleDatabase import ModuleDatabase
from User import *
from interface.module_frame import ModuleFrame

class ModulesFrame(tk.Frame):
    """
    The class definition for the ModulesFrame class.
    """
    
    def __init__(self,master,studentdashboardframe,user_obj:YoungLearner,modules_db:ModuleDatabase):
        """
        The constructor for the ModulesFrame class
        """
        super().__init__(master)
        self.master = master
        self.studentdashboardframe = studentdashboardframe
        self.user_obj = user_obj
        self.modules_db = modules_db

        self.modules_array = self.modules_db.get_module_array()

        # Create a list to store the frame widgets
        self.frames = []

        # Create frames and add them to the frames list
        for module in self.modules_array:
            module_frame = tk.Frame(master=self)
            self.frames.append(module_frame)

            circle_canvas = tk.Canvas(master=module_frame, width=50, height=50)
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
            number = module.get_module_id()
            circle_canvas.create_text(center_x, center_y, text=number, font=("Helvetica", 25, "bold"), fill="white")

            # Create label for module name
            module_name_label = tk.Label(master=module_frame, text=module.get_module_name(), font=("Helvetica", 20, "bold"))
            module_name_label.grid(row=1, column=0, padx=10, pady=10,rowspan=2)

            # Create button for entering module
            enter_module_button = tk.Button(master=module_frame, text="Enter", font=("Helvetica", 15), width=15,background="#FFCC80",
                                            height=2, borderwidth=2, relief=tk.RAISED,command=lambda module=module: self.enter_module(module))
            enter_module_button.grid(row=3, column=0, padx=10, pady=(30,10))

        # Arrange frames side by side using grid
        for i,frame in enumerate(self.frames):
            frame.grid(row=0,column=i,padx=10,pady=10)

        # Create a return to dashboard button below the frames
        return_to_dashboard_button = tk.Button(master=self, text="Return to Dashboard", font=("Helvetica", 15), width=20,background="#FFCC80",
                                                height=2, borderwidth=2, relief=tk.RAISED,command=self.return_to_dashboard)
        return_to_dashboard_button.grid(row=1, columnspan=len(self.frames), padx=10, pady=(50,10))
        

    def enter_module(self,module):
        """
        The function that is called when the user clicks on the "Enter" button.
        """
        self.place_forget()
        self.module_frame = ModuleFrame(self.master,self,self.user_obj,self.modules_db,module)
        self.module_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def return_to_dashboard(self):
        """
        The function that is called when the user clicks on the "Return to Dashboard" button.
        """
        self.place_forget()
        self.studentdashboardframe.place(relx=0.5, rely=0.5, anchor=tk.CENTER)