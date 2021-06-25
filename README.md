# personal_password_manager
This is a practice personal password manager - It'll be a basic console application.  
Use of a master password (hashed), master password used to encrypt the generated passwords.  
Data stored in CSV file to prevent having to set up SQL DB, etc.  
Won't be the most secure one out there, master password hashed using BCrypt and the password is used to encrypt a randomly generated password (encrypted using Blowfish - ECB) - it'll be stored on a users computer so data won't need to be as secure as otherwise.  

Data / CSV: WebsiteURL, Email, Password.  

Coded in Python, but might make a nicer looking one in C# with forms, etc. / autofilling.  
