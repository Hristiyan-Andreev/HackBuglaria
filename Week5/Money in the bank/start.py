import sql_manager
import hashlib
import getpass
import datetime


def main_menu():
    faillogin = 0
    print("Welcome to our bank service. You are not logged in. \nPlease register or login")
    while True:
        command = input("$$$>")

        if command == 'register':
            username = input("Enter your username: ")
            password = setpass(username)

            sql_manager.register(username, password)

            print("Registration Successfull")

        elif command == 'login':
            username = input("Enter your username: ")
            password = getpass.getpass("Enter your password: ")
            #password = input("Enter your password: ")
            #bytepass = ' '.join(format(x, 'b') for x in bytearray(password))
            hashpass = hashlib.sha1(password.encode())
            logged_user = sql_manager.login(username, hashpass.hexdigest())

            if logged_user:
                logged_menu(logged_user)
            else:
                faillogin += 1
                if faillogin >= 5:
                    failuser = username
                    now = datetime.datetime.now()
                    failmin = now.minute
                print("Login failed")

        elif command == 'help':
            print("login - for logging in!")
            print("register - for creating new account!")
            print("exit - for closing program!")

        elif command == 'exit':
            break
        else:
            print("Not a valid command")


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")

        if command == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')

        elif command == 'changepass':
            new_pass = setpass(logged_user)
            sql_manager.change_pass(new_pass, logged_user)

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)

        elif command == 'show-message':
            print(logged_user.get_message())

        elif command == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")


def setpass(username):
    message = "Your password must be:\n- More than 8 symbol\n -Contain at least one capital letter\
        \n -Contain at east one lower letter\n -Contain at least one special symbol\n -Contain at least one digit"
    print(message)
    Chars = set(["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_"])
    while True:
        password = getpass.getpass("Enter your password: ")

        if (len(password) < 9):
            error = "\nYour password is too short, it must be at least 8 symbols!"
            print(error)

        elif not (c for c in password if c.islower()):
            error = "\nYour password has no lowercase symbols!"
            print(error)

        elif not (c for c in password if c.isupper()):
            error = "\nYour password has no uppercase symbols!"
            print(error)

        elif not any(c in Chars for c in password):
            error = "\nYour password has no sepcial symbols!"
            print(error)

        elif (username in password):
            error = "\nYour password must not contain your username!"
            print(error)

        else:
            break

    #bytepass = ' '.join(format(x, 'b') for x in bytearray(password))
    hashpass = hashlib.sha1(password.encode())
    return hashpass.hexdigest()


def main():
    sql_manager.create_clients_table()
    main_menu()

if __name__ == '__main__':
    main()
