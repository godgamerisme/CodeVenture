from UserInterface import *
from UserDatabase import UserDatabase
from UserAuthenticate import UserAuthenticate
from User import YoungLearner, Educator, Parent

def main():
    """
    This function controls the overall flow of the CodeVenture game.
    """
    #populate user data from file
    db = UserDatabase("./data/users.json")
    data = db.read_data()
    users = db.to_user_array()

    # Create instance of UserAuthenticate class
    auth = UserAuthenticate(db, data,users)

    while True:
        # Display the Home Page
        HomePage.display_on_start()
        menu_input = input("Enter your choice: ")
        
    #TODO: based on choice, register, login, reset pass or exit
        if menu_input == "1":
            #TODO: Decide if we need a design for register page
            register_first_name = input("Enter First Name: ")
            if register_first_name == "q":
                continue
            
            register_last_name = input("Enter Last Name: ")
            if register_last_name == "q":
                continue

            register_password = input("Enter Password (length must be at least 5 and not longer than 15 characters): ")
            if register_password == "q":
                continue

            register_email = input("Enter Email: ")
            if register_email == "q":
                continue

            register_usertype = input("Enter User Type (either one of these: younglearner, educator, parent): ")
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

                password =  input("Please enter your password: ")
                if password == "q":
                    continue

                user = auth.login(username, password)
                
                if isinstance(user, YoungLearner):
                    StudentDashboard.display_dashboard()
                
                elif isinstance(user, Educator):
                    TeacherDashboard.display_dashboard()
                
                elif isinstance(user, Parent):
                    ParentDashboard.display_dashboard()
                    
                else:
                    print("Invalid email/password, please enter correct credentials! ")
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
            break

    # assuming the user has logged in successfully


    return

if __name__ == '__main__':
    main()
