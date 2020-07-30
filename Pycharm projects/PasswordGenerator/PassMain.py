import string
import random
import secrets
import time
import json

#Main function for generating passwords
def PasswordGenerator(s,nop,letters_count,digital_count,special_count):
    #Creation of generic variables
    print("Password generator booting up")
    i = 0
    key = "password"
    final_passwords = []
    saved_password = { }
    saved_password.setdefault(key,[])
    fin_pass = ''
     #Checks if the size of the passwords if less or equal to 64
    time.sleep(1)
    print("Generating passwords")
    time.sleep(1)
    if(s <= 64):
        while i < nop:
            for j in range(s):
                    ran_password = ''.join(secrets.choice(string.ascii_letters) for i in range(letters_count))
                    ran_password += ''.join(secrets.choice(string.digits) for i in range(digital_count))
                    ran_password += ''.join(secrets.choice(string.punctuation) for i in range(special_count))
                    # Passwords are generated and stored in a list
                    current_pass = list(ran_password)
                    random.shuffle(current_pass)
                    fin_pass = ''.join(current_pass)
            final_passwords.append(fin_pass)
            time.sleep(0.05)
            print("Your password[",i,"]", "is:" , fin_pass)
            i += 1
        #Checks the lenght of the stored passwords list
        time.sleep(0.5)
        if len(final_passwords) == 0:
            print("There are no generated passwords!")
            return
        time.sleep(0.5)
        save = (int)(input("Which password do you want to save(0 - size of the password list. \nType in a number higher or equal to the password list to save all of them)? "))
        if save >= len(final_passwords):
            print("Saving your passwords")
        else:
            print("Saving your password")
        time.sleep(0.5)
        if(save >= len(final_passwords)):
            for y in range(len(final_passwords)):
                saved_password[key].append(final_passwords[y])
        else:
            saved_password[key].append(final_passwords[save])
        #print(saved_password)
        json_object = json.dumps(saved_password,sort_keys=True,ensure_ascii=False,indent=4)
        with open("passwords.dat","w") as outfile:
            outfile.write(json_object)
        time.sleep(0.1)
        print("Saving completed")

    else:
        print("The number size is higher than 64")
        return


def checkcharactersize(s,chars):
    if(chars > s):
        print("--WARNING: the character count is higher than the size of the passwords! The program will not generate passwords if you continue--")


size = int(input("Enter a password size number(max 64): "))
number_of_pass = int(input("Enter how many passwords do you want to generate: "))
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
    PasswordGenerator(size, number_of_pass, number_of_let,number_of_dig , number_of_specials)
time.sleep(1)
print("Generator shutting down!")
exit = input("Press any key to exit the application")