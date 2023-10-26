import tkinter as tk

from interface.homepageframe import HomePageFrame


class Interface(tk.Tk):
    """
    Class definition for the Interface class
    """
    def __init__(self, title, width=960, height=650):
        """
        Constructor for the Interface class,
        the main window for CodeVenture.
        :param title: str
        :param width: int - default 960 pixels
        :param height: int - default 650 pixels
        """
        super().__init__()
        self.title(title)
        self.configure(bg="white")
        self.geometry(f"{width}x{height}")
        self.homepage =HomePageFrame(self)
        
        #position at the top center
        self.homepage.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        

if __name__ == "__main__":
    # DO NOT MODIFY THIS
    codeventure = Interface("CodeVenture")

    codeventure.mainloop()
    print("--- End of program execution ---")
