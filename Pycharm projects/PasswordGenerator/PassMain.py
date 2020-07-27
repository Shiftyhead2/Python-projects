import string
import random
import secrets
import time

#Main function for generating passwords
def PasswordGenerator(s,nop,special,letters_count,digital_count,special_count):
    #Creation of generic variables
    print("Password generator booting up")
    i = 0
    final_passwords = []
    fin_pass = ''
     #Checks if the size of the passwords if less or equal to 64
    time.sleep(1)
    print("Generating passwords")
    time.sleep(1)
    if(s <= 64):
        while i < nop:
            i += 1
            for j in range(s):
                    ran_password = ''.join(secrets.choice(string.ascii_letters) for i in range(letters_count))
                    ran_password += ''.join(secrets.choice(string.digits) for i in range(digital_count))
                    # Checks if the user wants any special characters
                    if special == 1:
                        ran_password += ''.join(secrets.choice(string.punctuation) for i in range(special_count))
                    # Checks if the user has entered a number that is higher than 1 in which case it stops the
                    # function from generating any passwords and stops the program
                    elif special > 1:
                        print("Invalid response detected! Restart the application to get your new passwords. Passwords will not be generated!")
                        return
                    # Passwords are generated and stored in a list
                    current_pass = list(ran_password)
                    random.shuffle(current_pass)
                    fin_pass = ''.join(current_pass)
            final_passwords.append(fin_pass)
            time.sleep(0.05)
            print("Your password[",i,"]", "is:" , fin_pass)
                #Checks the lenght of the stored passwords list
        time.sleep(0.5)
        if len(final_passwords) > 1:
            print("These are the generated passwords:", final_passwords)
        elif len(final_passwords) == 1:
            print("This is the generated password:", final_passwords)
        else:
            print("There are no generated passwords")
    else:
        print("The number size is higher than 64")
        return
    time.sleep(1)
    print("Generator shutting down!")


def checkcharactersize(s,chars):
    if(chars > s):
        print("--WARNING: the character count is higher than the size of the passwords! The program will not generate passwords if you continue--")


size = int(input("Enter a password size number: "))
number_of_pass = int(input("Enter how many passwords do you want to generate: "))
wants_special_characters = int(input("Do you want special characters(0 for no , 1 for yes)? "))
character_count = 0
number_of_let = int(input("Enter how many characters you want to have: "))
time.sleep(0.5)
character_count += number_of_let
print("Current character count is: ", character_count)
checkcharactersize(size,character_count)
number_of_dig = int(input("Enter how many digits you want to have: "))
time.sleep(0.5)
character_count += number_of_dig
print("Current character count is: ", character_count)
checkcharactersize(size,character_count)
time.sleep(0.5)
if(wants_special_characters == 1):
    number_of_specials = int(input("Enter how many special characters you want to have: "))
    character_count += number_of_specials
    time.sleep(0.5)
    print("Current character count is: ", character_count)
    time.sleep(0.5)
    print("Checking if everything is alright...")
    time.sleep(2)
    if(character_count > size):
        time.sleep(0.5)
        print("The character count is higher than the password size!")
    else:
        time.sleep(0.5)
        print("Everything is fine")
        time.sleep(0.5)
        PasswordGenerator(size, number_of_pass, wants_special_characters , number_of_let,number_of_dig , number_of_specials)
else:
    time.sleep(0.5)
    print("Checking if everything is alright...")
    if (character_count > size):
        time.sleep(0.5)
        print("The character count is higher than the password size!")
    else:
        time.sleep(0.5)
        print("Everything is fine")
        time.sleep(0.5)
        PasswordGenerator(size, number_of_pass, wants_special_characters, number_of_let, number_of_dig, 0)