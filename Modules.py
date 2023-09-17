class Question:
    def __init__(self, question_id, question_text, options, correct_answer):
        self.question_id = question_id
        self.question_text = question_text
        self.options = [Option(opt) for opt in options]
        self.correct_answer = correct_answer

class Quiz:
    def __init__(self, quiz_id, title, questions):
        self.quiz_id = quiz_id
        self.title = title
        self.questions = [Question(**q) for q in questions]

class Tutorial:
    def __init__(self, tutorial_id, title, content, duration_minutes):
        self.tutorial_id = tutorial_id
        self.title = title
        self.content = content
        self.duration_minutes = duration_minutes

class Progress:
    def __init__(self, user_id, username, module_id,completed_tutorials, completed_quiz):
        self.user_id = user_id
        self.username = username
        self.module_id = module_id
        self.completed_tutorials = completed_tutorials
        self.completed_quiz = completed_quiz

class Module:
    def __init__(self, module_id, module_name, tutorials, quiz):
        self.module_id = module_id
        self.module_name = module_name
        self.tutorials = [Tutorial(**t) for t in tutorials]
        self.quiz = Quiz(**quiz)
        self.user_progress = []  # A list to store Progress instances

    def add_user_progress(self, progress):
        self.user_progress.append(progress)

class Option:
    def __init__(self, option_text):
        self.option_text = option_text
