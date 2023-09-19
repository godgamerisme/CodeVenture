class HomePage:
    @staticmethod
    def display_on_start():
        print("------------------------")
        print("Welcome to the Home Page")
        print("------------------------")
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
        print("-------------------------")
        print("Welcome to the Login Page")
        print("-------------------------")
        LoginPage.display_menu()

    @staticmethod
    def display_menu():
        print("You have the following options:")
        print("\t1. Login")
        print("\t2. Reset Password")


class StudentDashboard:
    @staticmethod
    def display_dashboard():
        print("--------------------------------")
        print("Welcome to the Student Dashboard")
        print("--------------------------------")
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
        print("--------------------------------")
        print("Welcome to the Teacher Dashboard")
        print("--------------------------------")
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
        print("--------------------------------")
        print("Welcome to the Parent Dashboard")
        print("--------------------------------")
        ParentDashboard.display_menu()

    @staticmethod
    def display_menu():
        print("You have the following options:")
        print("\t1. Check Child's Progress")
        print("\t2. Log Out")


class ModulesPage:
    @staticmethod
    def display_on_start(module_array):
        print("---------------------------")
        print("Welcome to All Modules Page")
        print("---------------------------")
        print("Please select a module to view: ")
        ModulesPage.display_all_modules(module_array)

    def display_all_modules(module_array):
        for module in range(len(module_array)):
            print(f"{module+1}. {module_array[module].module_name}")


class ModulePage:
    @staticmethod
    def display_on_start():
        print("---------------------------")
        print("Welcome to the Modules Page")
        print("---------------------------")
        ModulePage.display_menu()

    @staticmethod
    def display_menu():
        print("You have the following options:")
        print("\t1. View Tutorials")
        print("\t2. Take Quiz")
        print("\t3. Back to Dashboard")


class ProgressPage:
    @staticmethod
    def display_page():
        print("----------------------------")
        print("Welcome to the Progress Page")
        print("----------------------------")
        ProgressPage.display_menu()
        # Display student's progress information here
        # You can fetch and display progress data for the student

    @staticmethod
    def display_menu():
        print("You have the following options:")
        print("\t1. View Overall Progress")
        print("\t2. Back to Dashboard")
