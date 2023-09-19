from UserInterface import *
from UserDatabase import UserDatabase
from UserAuthenticate import UserAuthenticate
from User import YoungLearner, Educator, Parent
from ModuleDatabase import ModuleDatabase


def main():
    """
    This function controls the overall flow of the CodeVenture game.
    """
    # Populate user data from file
    db = UserDatabase("./data/users.json")
    data = db.read_data()
    users = db.to_user_array()

    # Populate module data from file
    db_module = ModuleDatabase("./data/modules.json")
    data_module = db_module.read_data()
    modules = db_module.to_module_array(data_module)

    # Create instance of UserAuthenticate class
    auth = UserAuthenticate(db, data, users)

    while True:
        # Display the Home Page
        HomePage.display_on_start()
        menu_input = input("Enter your choice: ")
        
    # TODO: based on choice, register, login, reset pass or exit
        if menu_input == "1":
            # TODO: Decide if we need a design for register page
            register_first_name = input("Enter First Name: ")
            if register_first_name == "q":
                continue

            register_last_name = input("Enter Last Name: ")
            if register_last_name == "q":
                continue

            register_password = input("Enter Password (5 to 15 characters): ")
            if register_password == "q":
                continue

            register_email = input("Enter Email: ")
            if register_email == "q":
                continue

            register_usertype = input("Enter User Type (younglearner, educator, parent): ")
            if register_usertype == "q":
                continue

            auth.register(register_first_name, register_last_name, register_password, register_email, register_usertype)

        elif menu_input == "2":
            LoginPage.display_on_start()
            login_menu_option = input("Select one of these: ")
            if login_menu_option == "1":

                username = input("Please enter your username: ")
                if username == "q":
                    continue

                password = input("Please enter your password: ")
                if password == "q":
                    continue

                user = auth.login(username, password)
                is_logout = False
                
                while not is_logout:
                    if isinstance(user, YoungLearner):
                        StudentDashboard.display_dashboard()
                        student_option = input("Select one of these: ")
                        if student_option == "1":
                            # List all modules
                            ModulesPage.display_on_start(module_array=modules)
                            module_option = int(input("Select one of these: "))
                            if module_option <= len(modules):
                                current_module = modules[module_option-1]
                                print("You have selected " + current_module.module_name)
                                print("Loading module...")
                                ModulePage.display_on_start()
                                module_page_option = input("Select one of these: ")

                                if module_page_option == "1":  # View tutorials
                                    for tutorial in range(len(current_module.tutorials)):
                                        # Display all tutorials title
                                        print(f"{tutorial+1}. {current_module.tutorials[tutorial].title}")
                                    tutorial_option = int(input("Select one of these: "))
                                    if tutorial_option <= len(current_module.tutorials):
                                        current_tutorial = current_module.tutorials[tutorial_option-1]
                                        print("You have selected " + current_tutorial.title)
                                        print("Loading tutorial...")
                                        print(current_tutorial.content)
                                        # Prompt user to check if they want to complete the tutorial
                                        while True:
                                            complete_tutorial = input("Do you want to complete this tutorial? (y/n): ").lower()  # Case-insensitivity
                                            if complete_tutorial == "y":
                                                # Update the progress in module
                                                # Search for the progress in the module
                                                for progress in current_module.user_progress:
                                                    if progress.user_id == user.id:
                                                        progress.completed_tutorials.append(current_tutorial.tutorial_id)
                                                        # Update data in file
                                                        # Search in data_module and append the tutorial id to the completed tutorial
                                                        for user_progress in data_module["users"]:
                                                            if user_progress["user_id"] == progress.user_id:
                                                                # Search for the module id in the module progress
                                                                for module_progress in user_progress["module_progress"]:
                                                                    if module_progress["module_id"] == current_module.module_id:
                                                                        module_progress["completed_tutorials"].append(current_tutorial.tutorial_id)
                                                                        break
                                                        break  # Exit the loop if the user input 'y'
                                            elif complete_tutorial == "n":
                                                break  # Exit the loop if the user input 'n'
                                            else:
                                                print("Please enter 'y' or 'n' to indicate your choice.")

                                elif module_page_option == "2":  # Take quiz
                                    print("You have selected " + current_module.quiz.title)
                                    print("Loading quiz...")
                                    # Display all questions
                                    for question in range(len(current_module.quiz.questions)):
                                        print(f"Question{question+1}. {current_module.quiz.questions[question].question_text}")
                                        for option in range(len(current_module.quiz.questions[question].options)):
                                            print(f"Option{option+1}. {current_module.quiz.questions[question].options[option].option_text}")
                                        # Prompt user to select an option
                                        selected_option = input("Select one of the answer: ")
                                        if selected_option == current_module.quiz.questions[question].correct_answer:                                         
                                            print("You have selected the correct answer!")
                                        else:
                                            print("You have selected the wrong answer!")
                                    # Prompt user to check if they want to complete the quiz
                                    while True:
                                        complete_quiz = input("Do you want to complete this quiz? (y/n): ").lower()
                                        if complete_quiz == "y":
                                            # Update the progress in module
                                            # Search for the progress in the module
                                            for progress in current_module.user_progress:
                                                if progress.user_id == user.id:
                                                    progress.completed_quiz.append(current_module.quiz.quiz_id)
                                                    # Update data in file
                                                    # Search in data_module and append the quiz id to the completed quiz
                                                    for user_progress in data_module["users"]:
                                                        if user_progress["user_id"] == progress.user_id:
                                                            # Search for the module id in the module progress
                                                            for module_progress in user_progress["module_progress"]:
                                                                if module_progress["module_id"] == current_module.module_id:
                                                                    module_progress["completed_quiz"].append(current_module.quiz.quiz_id)
                                                                    break
                                                            break
                                            break  # Exit the loop if the user input 'y'
                                        elif complete_quiz == "n":
                                            break  # Exit the loop if the user input 'n'
                                        else:
                                            print("Please enter 'y' or 'n' to indicate your choice.")

                                elif module_page_option == "3":  # Back to dashboard
                                    continue
                                else:   
                                    print("Invalid input, please try again")
                                    continue

                        elif student_option == "2":  # Check progress
                            ProgressPage.display_page()
                            # Prompt user to select a progress to view
                            progress_option = input("Select one of the option: ")
                            if progress_option == "1":
                                # Go through all the modules and display the progress
                                for module in modules:
                                    print(module.show_user_progress(user.id))
                            elif progress_option == "2":
                                # Back to dashboard
                                continue
                        elif student_option == "3":  # Logout
                            is_logout = True         
                            db.write_data(data)
                            db_module.write_data(data_module)
                    
                    elif isinstance(user, Educator):
                        TeacherDashboard.display_dashboard()
                        # TODO: IMPLEMENT LATER
                        break
                    
                    elif isinstance(user, Parent):
                        ParentDashboard.display_dashboard()
                        # TODO: IMPLEMENT LATER
                        break
                        
                    else:
                        print("Invalid email/password, please enter correct credentials! ")
                        break
                        
            elif login_menu_option == "2":
                print("Reset Password")
                email = input("Please enter your email: ")
                if email == "q":
                    continue
                password = input("Please enter your new password: ")
                if password == "q":
                    continue
                auth.reset_password(email, password)

        else:
            print("Exiting...")
            print("Shut down completed.")
            # TODO: save data to file
            
            break

    # assuming the user has logged in successfully

    return


if __name__ == '__main__':
    main()
