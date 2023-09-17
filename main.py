from HomePage import HomePage
from UserDatabase import UserDatabase
from LoginPage import LoginPage
from UserAuthenticate import UserAuthenticate

def main():
    """
    This function controls the overall flow of the CodeVenture game.
    """
    # Display the Home Page
    HomePage.display_on_start()

    #populate user data from file
    db = UserDatabase("./data/users.json")
    data = db.read_data()
    users = db.to_user_array(data)

    

    while True:
        # display the Home Page Menu
        HomePage.display_menu()
        menu_input = input("Enter your choice: ")
    #TODO: based on choice, register, login, reset pass or exit
        if menu_input == "1":
            #TODO: Decide if we need a design for regiser page
            print("Register")
            UserAuthenticate.register(data)
        elif menu_input == "2":
            LoginPage.display_on_start()
        else:
            print("Exiting...")
            break

    return

if __name__ == '__main__':
    main()
