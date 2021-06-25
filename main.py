# first get what the user wants to do, create password, retrieve password, etc.
import bcrypt
import csv
import blowfish
import random
import string

# This can just return true / false, I wouldn't normally do this, but no personal information will be leaked
# If it returns true where passwords don't actually match, the decryption of passwords will be done wrong so return false results.
def check_login(username, password):
    password = bytes(password, 'utf-8')

    try:
        if bcrypt.hashpw(password, get_hashed_pass(username)) == get_hashed_pass(username):
            return True
    except:
        return False

    return False



def create_account():
    username = input("Enter a username: ")
    password = bcrypt.hashpw(bytes(input("Enter a password: "), 'utf-8'), bcrypt.gensalt(12))

    try:
        file = open("password_manager_accounts.csv", "a")
        file.write(username + "," + password.decode('utf-8') + "\n")
        file.close()
        return "Account Created"
    except:
        return "Account Not Created"

def get_hashed_pass(username):
    with open("password_manager_accounts.csv", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if row[0] == username:
                return row[1].encode('utf-8')

    return ""


def return_multiple_of_eight(input):
    len_difference = 0
    if len(input) < 8:
        len_difference = 8 - len(input)
    elif len(input)%8 == 0:
        len_difference = 0
    else:
        len_difference = 8 - (len(input)%8)

    # add on num of chars for len of difference "x" - this function is a bit messy, shouldn't need to use it much though, only for future work

    for i in range(len_difference):
        input += "x"

    return input


def encrypt_blowfish(input, key):
    data_encrypted = ""

    cipher = blowfish.Cipher(key.encode('utf-8'))
    data = input.encode('utf-8')
    data_encrypted = b"".join(cipher.encrypt_ecb(data))

    # return a hex value, that hex can be written to file then converted

    return data_encrypted.hex()

def decrypt_blowfish(input, key):
    data_decrypted = ""

    byte_input = bytes.fromhex(input)

    cipher = blowfish.Cipher(key.encode('utf-8'))
    data_decrypted = b"".join(cipher.decrypt_ecb(byte_input))

    return data_decrypted.decode('utf-8')

def create_password():
    username = input("Enter your username: ")
    master_password_plaintext = input("Enter your master password: ")

    if check_login(username, master_password_plaintext):
        print("Login details correct")
        email = input("Enter the email you'll use: ")
        websiteURL = input("Enter the website URL: ")

        letters = string.ascii_lowercase + string.digits + string.punctuation + string.ascii_uppercase
        result_str = ''.join(random.choice(letters) for i in range(32))

        result_str = return_multiple_of_eight(result_str)  # makes it a multiple of 8 so encryption doesn't break

        encrypted_pass = encrypt_blowfish(result_str, master_password_plaintext)

        file = open("password_manager_passwords.csv", "a", encoding='utf-8')
        file.write(username + "," + email + "," + websiteURL + "," + encrypted_pass + "\n")
        file.close()

        return "Password: " + result_str

    else:
        print("Login details incorrect")
        return "N/A"


def get_encrypted_website_pass(username, website):
    with open("password_manager_passwords.csv", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if row[0] == username and row[2] == website:
                return row[1], row[3]

    return ""

def retrieve_password():
    username = input("Enter your username: ")
    master_password_plaintext = input("Enter your master password: ")

    if check_login(username, master_password_plaintext):
        websiteURL = input("Enter the website URL: ")
        email, encrypted_password = get_encrypted_website_pass(username, websiteURL)
        return "Email: " + email + "\n" + "Password: " + decrypt_blowfish(encrypted_password, master_password_plaintext)

    else:
        print("Login details incorrect")
        return "N/A"


choice = ""
while choice != "9":
    choice = input("Retrieve password (1), Create password (2), Create account (3), Quit (9): ")
    if choice == "1":
        print()
        print(retrieve_password() + "\n")
    elif choice == "2":
        print()
        print(create_password() + "\n")
    elif choice == "3":
        print()
        print(create_account() + "\n")