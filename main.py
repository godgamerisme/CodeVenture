from UserInterface import *
from UserDatabase import UserDatabase
from UserAuthenticate import UserAuthenticate

def main():
    """
    This function controls the overall flow of the CodeVenture game.
    """

     

    #populate user data from file
    db = UserDatabase("./data/users.json")
    data = db.read_data()

    # Create instance of UserAuthenticate class
    auth = UserAuthenticate(db, data)

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
            select_option = input("Select one of these: ")
            if(select_option == "1"):

                email = input("Please enter your email address: ")
                if email == "q":
                    continue

                password =  input("Please enter your password: ")
                if password == "q":
                    continue

                role = auth.login(email, password)
                
                if(role == "younglearner"):
                    StudentDashboard.display_dashboard()
                
                elif(role == "educator"):
                    TeacherDashboard.display_dashboard()
                
                elif(role == "parent"):
                    ParentDashboard.display_dashboard()
                    
                else:
                    print("Invalid email/password, please enter correct credentials! ")
            
        else:
            print("Exiting...")
            break

    # assuming the user has logged in successfully


    return

if __name__ == '__main__':
    main()
