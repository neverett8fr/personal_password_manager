# first get what the user wants to do, create password, retrieve password, etc.
import bcrypt
import csv

def create_account():
    print("Create account")
    username = input("Enter a username: ")
    password = bcrypt.hashpw(bytes(input("Enter a password: "), 'utf-8'), bcrypt.gensalt(12))

    file = open("password_manager_accounts.csv", "a")
    file.write(username + "," + password.decode('utf-8') + "\n")
    file.close()

    #out = bcrypt.hashpw(b"hello", bcrypt.gensalt(12))
    #if bcrypt.hashpw(b"hello", out) == out:
    #    print("Matchd")

def get_hashed_pass(username):
    with open("password_manager_accounts.csv", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if row[0] == username:
                return row[1].encode('utf-8')

    return ""

def create_password():
    print("Create_Password")






# This can just return true / false, I wouldn't normally do this, but no personal information will be leaked
# If it returns true where passwords don't actually match, the decryption of passwords will be done wrong so return false results.
def check_login():
    username = input("Enter a username: ")
    password = bytes(input("Enter a password: "), 'utf-8')

    if bcrypt.hashpw(password, get_hashed_pass(username)) == get_hashed_pass(username):
        return True

    return False




choice = ""
while choice != "9":
    choice = input("Retrieve password (1), Create password (2), Create account (3), Quit (9): ")
    if choice == "1":
        check_login()
    elif choice == "2":
        create_password()
    elif choice == "3":
        create_account()