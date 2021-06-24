# first get what the user wants to do, create password, retrieve password, etc.
import bcrypt

choice = input("Retrieve password (1), Create password (2), Create account (3): ")

def create_account():
    print("Create account")
    username = input("Enter a username: ")
    password = bcrypt.hashpw(bytes(input("Enter a password: "), 'utf-8'), bcrypt.gensalt(12))

    file = open("password_manager_accounts.csv", "a")
    file.write(username + "," + str(password))
    file.close()

    #out = bcrypt.hashpw(b"hello", bcrypt.gensalt(12))
    #if bcrypt.hashpw(b"hello", out) == out:
    #    print("Matchd")

if choice == "1":
    print("Retrieve")
elif choice == "2":
    print("Create password")
elif choice == "3":
    create_account()