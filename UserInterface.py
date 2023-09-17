class HomePage:
    @staticmethod
    def display_on_start():
        print("Welcome to the Home Page")
        HomePage.display_menu()

    @staticmethod
    def display_menu():
        print("You have the following options:")
        print("\t1. Register")
        print("\t2. Login")
        print("\t3. Shut Down")


class LoginPage:
    @staticmethod
    def display_on_start():
        print("Welcome to the Login Page")
        LoginPage.display_menu()

    @staticmethod
    def display_menu():
        print("You have the following options:")
        print("\t1. Login")
        print("\t2. Forgot Password")
        print("\t3. Reset Password")
        print("\t4. Exit")


class StudentDashboard:
    @staticmethod
    def display_dashboard():
        print("Welcome to the Student Dashboard")
        StudentDashboard.display_menu()

    @staticmethod
    def display_menu():
        print("You have the following options:")
        print("\t1. View Modules")
        print("\t2. Check Progress")
        print("\t3. Log Out")


class TeacherDashboard:
    @staticmethod
    def display_dashboard():
        print("Welcome to the Teacher Dashboard")
        TeacherDashboard.display_menu()

    @staticmethod
    def display_menu():
        print("You have the following options:")
        print("\t1. Create Module")
        print("\t2. View All Student Progress")
        print("\t3. View One Student's Progress")
        print("\t4. Log Out")


class ParentDashboard:
    @staticmethod
    def display_dashboard():
        print("Welcome to the Parent Dashboard")
        ParentDashboard.display_menu()

    @staticmethod
    def display_menu():
        print("You have the following options:")
        print("\t1. Check Child's Progress")
        print("\t2. Log Out")


class ModulesPage:
    @staticmethod
    def display_page():
        print("Welcome to the Modules Page")
        ModulesPage.display_menu()

    @staticmethod
    def display_menu():
        print("You have the following options:")
        print("\t1. View Tutorials")
        print("\t2. Take Quiz")
        print("\t3. Start Challenges")
        print("\t4. Back to Dashboard")


class ProgressPage:
    @staticmethod
    def display_page():
        print("Welcome to the Progress Page")
        # Display student's progress information here
        # You can fetch and display progress data for the student

    @staticmethod
    def display_menu():
        print("You have the following options:")
        print("\t1. View Tutorial Progress")
        print("\t2. View Quiz Progress")
        print("\t3. View Challenge Progress")
        print("\t4. Back to Dashboard")
