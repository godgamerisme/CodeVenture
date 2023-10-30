import tkinter as tk
from database.ModuleDatabase import ModuleDatabase
from Modules import *
from User import *

class QuizFrame(tk.Frame):
    """
    The class definition for the QuizFrame class.
    """

    def __init__(self, master, module_frame, user_obj:YoungLearner, modules_db:ModuleDatabase, module_selected:Module,current_question:int=0):
        """
        The constructor for the QuizFrame class
        """
        super().__init__(master)
        self.master = master
        self.module_frame = module_frame
        self.user_obj = user_obj
        self.modules_db = modules_db
        self.module_selected = module_selected
        self.current_question = current_question

        # Set the background colour of the frame to follow main window
        self.configure(bg="white")

        # Get quiz question from module selected
        self.quiz = self.module_selected.get_quiz()
        self.questions = self.quiz.get_questions()

        # Create a label for the quiz title
        quiz_title_label = tk.Label(master=self, text="Take Quiz", font=("Helvetica", 20, "bold"), bg="white")
        quiz_title_label.grid(row=0, column=0, padx=30, pady=15,columnspan=2)

        # Create a label for the quiz question
        self.quiz_question_label = tk.Label(master=self, text=self.questions[self.current_question].get_question(), font=("Helvetica", 18, "bold"),wraplength=700,justify=tk.LEFT, bg="white")
        self.quiz_question_label.grid(row=1, column=0, padx=10, pady=10,columnspan=2)

        # Create option buttons
        self.option_buttons = []
        self.options = self.questions[self.current_question].get_options()
        for i,option in enumerate(self.options):
            option_button = tk.Button(master=self, text=option.get_option_text(), font=("Helvetica", 15), width=20,background="white",command=lambda i=i, option=option: self.select_option(i,option.get_option_text()),
                                      height=2, borderwidth=2, relief=tk.RAISED,wraplength=200)
            if i%2 == 0:
                option_button.grid(row=int(i//2)+2, column=0, padx=50, pady=30)
            else:
                option_button.grid(row=int(i//2)+2, column=1, padx=50, pady=30)
            self.option_buttons.append(option_button)

        # Create a label for the quiz outcome
        self.quiz_outcome_text = tk.StringVar()
        quiz_outcome_message = tk.Message(master=self, textvariable=self.quiz_outcome_text, font=("Helvetica", 15), width=500, bg="white")
        quiz_outcome_message.grid(row=5, column=0, padx=10, pady=10, columnspan=2,rowspan=2)

        # Create a Back Button
        back_button = tk.Button(master=self, text="Back", font=("Helvetica", 15, "bold"), width=15, background="#FFCC80",
                                command=self.navigate_to_module_or_quiz,
                                height=1, borderwidth=2, relief=tk.RAISED)
        back_button.grid(row=7, column=0, padx=10, pady=10, sticky=tk.W)

        # Check if current question is the last question
        if self.current_question == len(self.questions)-1:
            # Create a Submit Button
            submit_button = tk.Button(master=self, text="Submit Quiz", font=("Helvetica", 15, "bold"), width=15, background="#FFCC80",
                                    command=self.submit_quiz,
                                    height=1, borderwidth=2, relief=tk.RAISED)
            submit_button.grid(row=7, column=1, padx=10, pady=10, sticky=tk.E)
        else:
            # Create a Next Button
            next_button = tk.Button(master=self, text="Next Question", font=("Helvetica", 15, "bold"), width=15, background="#FFCC80",
                                    command=self.next_question,
                                    height=1, borderwidth=2, relief=tk.RAISED)
            next_button.grid(row=7, column=1, padx=10, pady=10, sticky=tk.E)

        # Create a label to show quiz submission status
        self.quiz_submission_status_text = tk.StringVar()
        quiz_submission_status_message = tk.Message(master=self, textvariable=self.quiz_submission_status_text, font=("Helvetica", 15), width=500, bg="white")
        quiz_submission_status_message.grid(row=8, column=0, padx=10, pady=10, columnspan=2)
            
    def select_option(self,button_index,option_selected:str):
        """
        The function that is called when the user clicks on an option button.
        """
        # Check if the option selected is the correct answer
        print("Button index: "+str(button_index))
        if button_index == self.questions[self.current_question].get_correct_answer():
            self.quiz_outcome_text.set("You have selected the correct answer!")
            # Change the button color to green for 1 s
            self.change_color(button_index,"green")

        else:
            #set the quiz outcome text to show option_selected
            print("Option selected: "+option_selected)
            self.quiz_outcome_text.set("You have selected the wrong answer!\nCorrect answer: "+self.options[self.questions[self.current_question].get_correct_answer()].get_option_text())
            # Change the button color to red for 1 s
            self.change_color(button_index,"red")

    def change_color(self,button_index,new_color:str):
        """
        The function that is called to change the color of the button
        """
        #get the button with button index
        button = self.option_buttons[button_index]
        original_color = button.cget("background")
        button.config(background=new_color)
        button.after(1000,lambda: button.config(background=original_color))

    def navigate_to_module_or_quiz(self):
        """
        The function that is called when the user clicks on the "Back" button.
        """
        # Check if its the first question, if it is then go back to module frame, else go back to quiz frame
        if self.current_question == 0:
            self.place_forget()
            self.module_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        else:
            self.place_forget()
            self.quizframe = QuizFrame(self.master,self.module_frame,self.user_obj,self.modules_db,self.module_selected,self.current_question-1)
            self.quizframe.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def next_question(self):
        """
        The function that is called when the user clicks on the "Next Question" button.
        """
        self.place_forget()
        self.quizframe = QuizFrame(self.master,self.module_frame,self.user_obj,self.modules_db,self.module_selected,self.current_question+1)
        self.quizframe.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def submit_quiz(self):
        """
        The function that is called when the user clicks on the "Submit Quiz" button.
        """
        # Save to completed quizzes
        self.modules_db.complete_quiz(self.user_obj.get_id(),self.module_selected.get_module_id(),self.quiz.get_quiz_id())
        # Set quiz submission status text
        self.quiz_submission_status_text.set("Quiz Submitted! Navigating back to module...")
        # Go back to module frame after 3 seconds
        self.after(3000,self.navigate_to_module)

    def navigate_to_module(self):
        """
        The function that is called after submission
        """
        self.place_forget()
        self.module_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
