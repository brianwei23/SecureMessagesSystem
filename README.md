# SecureMessagesSystem
Allows users to send and receive messages securely. Usernames and passwords are used to ensure security. Passwords and messages are salted and then hashed.

To send a message, the sender must make up a username and a unique passcode. Passcode must not be used before in the system. The username, hashed passcode, and hashed message is placed in user_code.txt. The hashed password and plain message is placed in messages.txt. The receiver must input the correct sender's username and correct passcode. If validated, the receiver can get the message. 

To delete a message that is stored in the secure message system, the user must input the sender's username and passcode. If both match, then the associated message is deleted. 

Hashing is used by using bcrypt. Before hashing, a salt is generated. A salt is a random value added to the text that will be hashed. Salt is important so that if you have duplicate texts, different hashes would still be generated. Pwinput is used to mask the passwords into "*" during password input.

secretMessages.py contains the code. user_code.txt and messages.txt are sample text files. In reality, both of these txt files would be kept secret.

# How to run code:
In Visual Studio Code:
1. We will set up the virtual environment to use bcrypt and pwinput. In the terminal, put in "python -m venv myenv".
2. Then we will activate the virtual environment. If you are on Windows, do "myenv\Scripts\activate". If you are on macOS or Linux, do "source myenv/bin/activate" in the terminal.
3. Then, do "pip install bcrypt pwinput" in terminal.
4. Type in "python secretMessages.py".
5. Follow instructions listed in the terminal.
