# personal_password_manager
This is a practice personal password manager - It'll be a basic console application.
  
## How it works  
It links accounts with passwords. The Users main account is stored as a 'username' and hashed master password.  
The master password is used to encrypt a randomly generated password consisting of Upper-Case, Lower-Case, Symbols and Numbers.  

## How to use it  
Create an account  
Create a password for an account - this requires you to log in, where the hash is checked and then creates a randomly generated password (stored encrypted using master password)  
Retrieve password for an account - this requires you to log in, the hash is checked, then asks you for the website you want details for. The application returns the email you used, as well as the password created (decrypted using your master password)  
  
## Notes  
- The data is stored in CSV file to prevent users from having to set up SQL DB, etc.  
- This won't be the most secure one out there.  
- - it'll be stored on a users computer so data won't need to be as secure as otherwise.  
- Master password hashed using BCrypt  
- Master password is used to encrypt a randomly generated password  
- Website passwords are encrypted using Blowfish - ECB  
  

Coded in Python, but might make a nicer looking one in C# with forms, etc. / autofilling.  

![image](https://user-images.githubusercontent.com/43852724/123477692-50406280-d5f6-11eb-817e-7c05fa6fb8bc.png)  
![image](https://user-images.githubusercontent.com/43852724/123477748-651cf600-d5f6-11eb-934c-9befafaeaa7e.png)  
![image](https://user-images.githubusercontent.com/43852724/123477885-9c8ba280-d5f6-11eb-8520-3da4fb975b19.png)  

