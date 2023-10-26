import tkinter as tk
from interface.register_frame import RegisterFrame
from interface.login_frame import LoginFrame
from authentication.UserAuthenticate import UserAuthenticate


class HomePageFrame(tk.Frame):
    """
    The class definition for the HomePageFrame class.
    """
    def __init__(self, master):
        """
        Constructor for the HomePageFrame class.
        :param master: Tk object; the main window that the
                       home page frame is to be contained.
        """
        super().__init__(master=master)
        self.master = master

        # Set up authentication
        self.auth = UserAuthenticate()

        self.grid_columnconfigure(0, weight=1, minsize=20)

        home_page_title = tk.Label(self, text="Welcome to CodeVenture", font=("Helvetica", 24,"bold"))
        home_page_title.grid(row=0,columnspan=3)
        
        
        # Create a canvas for the image
        self.home_canvas = tk.Canvas(master=self, width=400, height=400)
        self.home_canvas.grid(row=1, column=0, sticky=tk.W,padx=15,pady=20)

        # Load and display an image on the canvas
        image_path = "img/home.png"
        self.home_image = tk.PhotoImage(file=image_path)
        self.display_image()
        
        
        # Create a frame for the "Login" and "Register" buttons
        button_frame = tk.Frame(master=self)
        button_frame.grid(row=1, column=1, sticky=tk.W,columnspan=2)

        # Create a "Login" button
        login_button = tk.Button(master=button_frame, text="Login",background="#FFCC80",font=("Helvetica", 15),width=15,height=2,borderwidth=2,relief=tk.RAISED,
                                 command=self.navigate_to_login)
        login_button.grid(row=0, column=0, padx=10, pady=50)

        # Create a "Register" button
        register_button = tk.Button(master=button_frame, text="Register", background="#FFCC80",font=("Helvetica", 15),width=15,height=2,borderwidth=2,relief=tk.RAISED,
                                    command=self.navigate_to_register)
        register_button.grid(row=1, column=0, padx=10, pady=10)


    def display_image(self):
        # Get the original image dimensions
        original_width = self.home_image.width()
        original_height = self.home_image.height()

        # Get the canvas dimensions
        canvas_width = self.home_canvas.winfo_width()
        canvas_height = self.home_canvas.winfo_height()

        # Calculate the zoom factor for both width and height
        zoom_factor_width = canvas_width / original_width
        zoom_factor_height = canvas_height / original_height

        # Use the minimum zoom factor to maintain the aspect ratio
        zoom_factor = min(zoom_factor_width, zoom_factor_height)

        # Create and display the image with the adjusted size
        self.home_canvas.create_image(0, 0, anchor=tk.NW, image=self.home_image, tags='img')
        self.home_canvas.scale('img', 0, 0, zoom_factor, zoom_factor)

    
    def navigate_to_login(self):
        """
        Function to handle the action when the "Login" button is clicked.
        """
        self.place_forget()
        login_frame = LoginFrame(self.master, self,self.auth)
        login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
                

    def navigate_to_register(self):
        """
        Function to handle the action when the "Register" button is clicked.
        """
        self.place_forget()
        register_frame = RegisterFrame(self.master, self,self.auth)
        register_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
