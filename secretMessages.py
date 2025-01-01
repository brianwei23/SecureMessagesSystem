import bcrypt   #used for hashing
import pwinput  #used for masking passwords when typing

optionExists = False

while optionExists == False:
    option = input("Please enter (1) if you want to send a message. Enter (2) if you want to receive a message. Enter (3) if you want to delete the message from our secure system.\n")
    if option not in ("1", "2", "3"):
        print("Input invalid. Try again.\n")
    else:
        optionExists = True

if option == "1":
    username = input("Please enter a username.\n")
   
    passExist = True
    while passExist:
        passcode = pwinput.pwinput("Please enter a passcode.\n").encode('utf-8')
        
        is_unique = True    
        with open("user_code.txt", "r") as file:
            for line in file:
                _, hashedPass, _ = line.strip().split(" ", 2)
                if bcrypt.checkpw(passcode, hashedPass.encode('utf-8')):
                    print("Password is not unique. Try again.\n")
                    is_unique = False
                    break
        if is_unique:
            passExist = False
                                      
    firstSalt = bcrypt.gensalt() #generates random value
    hashedPass = bcrypt.hashpw(passcode, firstSalt).decode('utf-8') #hashes passcode with the salt for security
    plainMessage = input("Please enter your message. \n")
    secondSalt = bcrypt.gensalt()
    secMessage = bcrypt.hashpw(plainMessage.encode('utf-8'), secondSalt).decode('utf-8')
    with open("user_code.txt", "a") as file:
        file.write(f"{username} {hashedPass} {secMessage}\n")
    thirdSalt = bcrypt.gensalt()
    secondHashPass = bcrypt.hashpw(passcode, thirdSalt).decode('utf-8')
    with open("messages.txt", "a") as file:
        file.write(f"{secondHashPass} {plainMessage}\n")
    print("You have sent your message. Thank you!") 

if option == "2":
    found = False
    username = input("Please enter the username of the user that the message is from. \n")
    passcode = pwinput.pwinput("Please enter the password to access the message.\n").encode('utf-8')
    with open("user_code.txt", "r") as file:
        for line in file:
            listedUser, listHashPass, storedSecMessage = line.strip().split(' ')
            if username == listedUser:
                if bcrypt.checkpw(passcode, listHashPass.encode('utf-8')):
                    found = True
    if found == True:
        print("Your attempt has been successful!\n")
        with open("messages.txt", "r") as file:
            for line in file:
                listedHash, listedMessage = line.strip().split(" ", 1)
                if bcrypt.checkpw(passcode, listedHash.encode('utf-8')):
                    print("Message: " + listedMessage)
    else:
        print("Message retrieval unsuccessful.")

       
if option == "3":
    match = False
    username = input("Enter username associated with message you want to delete.\n")
    passcode = pwinput.pwinput("Enter passcode associated with message you want to delete.\n").encode('utf-8')
    
    with open("user_code.txt", "r") as file:
        lines = file.readlines()
        
    neededLines = []
    
    for line in lines:
        deleteUser, deletePass, _ = line.strip().split(" ", 2)
        if not username == deleteUser or not bcrypt.checkpw(passcode, deletePass.encode('utf-8')):
            neededLines.append(line)
        else:
            match = True
            
    with open("user_code.txt", "w") as file:
        file.writelines(neededLines)
    
    if match:    
        with open("messages.txt", "r") as file:
            lines = file.readlines()
        
        neededLines = []
    
        for line in lines:
            deletePass, _ = line.strip().split(" ", 1)
            if not bcrypt.checkpw(passcode, deletePass.encode('utf-8')):
                neededLines.append(line)
            
        with open("messages.txt", "w") as file:
            file.writelines(neededLines)
    
        print("The message associated with the username and passcode exists, and it has been removed. Thank you!")
    
    if not match:
        print("Message associated with the username and passcode provided does not exist.")    