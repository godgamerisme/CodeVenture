from typing import List


class Question:
    def __init__(self, question_id, question_text, options, correct_answer):
        self.question_id = question_id
        self.question_text = question_text
        self.options = [Option(opt) for opt in options]
        self.correct_answer = correct_answer

    def get_question_id(self):
        return self.question_id
    
    def get_question(self):
        return self.question_text
    
    def get_options(self):
        return self.options
    
    def get_correct_answer(self):
        "Returns the index of the correct answer"""
        return self.correct_answer


class Quiz:
    def __init__(self, quiz_id, title, questions):
        self.quiz_id = quiz_id
        self.title = title
        self.questions = [Question(**q) for q in questions]

    def get_quiz_id(self):
        return self.quiz_id
    
    def get_quiz_title(self):
        return self.title
    
    def get_questions(self)->List[Question]:
        return self.questions


class Tutorial:
    def __init__(self, tutorial_id, title, content, duration_minutes):
        self.tutorial_id = tutorial_id
        self.title = title
        self.content = content
        self.duration_minutes = duration_minutes

    def get_tutorial_name(self):
        return self.title
    
    def get_tutorial_id(self):
        return self.tutorial_id
    
    def get_tutorial_content(self):
        return self.content
    
    def get_tutorial_duration(self):
        return self.duration_minutes


class Progress:
    def __init__(self, user_id, username, module_id, completed_tutorials, completed_quiz):
        """
        completed_tutorials is a list of tutorial ids
        completed_quiz is a list of quiz ids
        """
        self.user_id = user_id
        self.username = username
        self.module_id = module_id
        self.completed_tutorials = completed_tutorials
        # self.completed_quiz = [quiz for quiz in completed_quiz] if completed_quiz else [] 
        self.completed_quiz = completed_quiz

    def get_user_id(self):
        return self.user_id
    
    def get_username(self):
        return self.username
    
    def get_module_id(self):
        return self.module_id
    
    def get_completed_tutorials(self):
        return self.completed_tutorials
    
    def get_completed_quiz(self):
        return self.completed_quiz
    
    def add_completed_tutorial(self, tutorial_id):
        if tutorial_id not in self.completed_tutorials:
            self.completed_tutorials.append(tutorial_id)

    def add_completed_quiz(self, quiz_id):
        if quiz_id not in self.completed_quiz:
            self.completed_quiz.append(quiz_id)


class Module:
    def __init__(self, module_id, module_name, tutorials, quiz):
        self.module_id = module_id
        self.module_name = module_name
        self.tutorials = [Tutorial(**t) for t in tutorials]
        self.quiz = Quiz(**quiz)
        self.user_progress = []  # A list to store Progress instances

    def get_module_name(self):
        return self.module_name
    
    def get_module_id(self):
        return self.module_id
    
    def get_tutorials(self):
        return self.tutorials
    
    def get_quiz(self)->Quiz:
        return self.quiz
    
    def get_user_progress(self):
        return self.user_progress

    def add_user_progress(self, progress):
        self.user_progress.append(progress)

    def show_user_progress(self, user_id):
        str_progress = ""
        for progress in self.user_progress:
            if progress.user_id == user_id:
                str_progress = f"Module ID: {self.module_id}\nModule Name: {self.module_name}\n"
                # Map the tutorial id to tutorial title
                str_progress += "Completed Tutorials: "
                if not progress.completed_tutorials:  # Check if completed_tutorials list is empty
                    str_progress += "None\n"
                else:
                    for tutorial_id in progress.completed_tutorials:
                        for tutorial in self.tutorials:
                            if tutorial.tutorial_id == tutorial_id:
                                str_progress += tutorial.title + "\n"
                # Check if progress.completed_quiz is null
                if progress.completed_quiz is None:
                    str_progress += "\nCompleted Quiz: None\n"
                else:
                    # Map the quiz id to quiz title
                    str_progress += "Completed Quiz: "
                    for quiz_id in progress.completed_quiz:
                        if quiz_id == self.quiz.quiz_id:
                            str_progress += self.quiz.title + "\n"
        return str_progress
        

class Option:
    def __init__(self, option_text):
        self.option_text = option_text

    def get_option_text(self):
        return self.option_text

# class UserProgress:
#     """This class is used to store the progress of currently login user"""
#     def __init__(self, user_id, username):
#         self.user_id = user_id
#         self.username = username
#         self.module_progress = []
