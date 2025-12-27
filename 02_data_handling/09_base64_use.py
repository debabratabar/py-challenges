"""
Challenge: Offline Credential Manager

Create a CLI tool to manage login credentials (website, username, password) in an encoded local file (`vault.txt`).

Your program should:
1. Add new credentials (website, username, password)
2. Automatically rate password strength (weak/medium/strong)
3. Encode the saved content using Base64 for simple offline obfuscation
4. View all saved credentials (decoding them)
5. Update password for any existing website entry (assignment)

Bonus:
- Support searching for a website entry
- Mask password when showing in the list
"""


import os ,string , getpass
import base64
from tabulate import tabulate

Filename = 'vault.txt'


def decode(text):
    return base64.b64decode(text.encode()).decode()

def encode(text):
    return base64.b64encode(text.encode()).decode()


def passworkChecker(password):
    length = len(password)
    upper = any(c.isupper() for c in password)
    lower = any(c.islower() for c in password)
    digit =  any(c.isdigit() for c in password)
    spec_char = any(i in string.punctuation for i in password )
    res = sum([length>=8 , upper , lower, spec_char ,digit])

    return ['Weak' , 'Moderate' , 'Strong'][min(sum , 2)]



def add_credentials():
    website = input("Please write your website= ").strip().lower()
    user_name = input("Please write your username= ").strip().lower()
    password = getpass.getpass("Please write your password =").strip().lower()
    # password = input("Please write your password =").strip().lower()

    actual_url = f"{website}||{user_name}||{password}"

    encoded_str = encode(actual_url)

    with open(file=Filename , mode='a' , encoding='utf-8',newline="\n") as f:
        f.write(encoded_str +"\n")

    print(" Encoded string added" )



def show_credentials():

    if not os.path.exists(Filename):
        print("No file found")
        return
    

    with open(file=Filename , mode='r' , encoding='utf-8') as f:
        data = []
        for line in f : 
            decodded_str = decode(line)
            website , user_name , password = decodded_str.split('||')
            sudo_pass = "*" * len(password)

            data.append((website , user_name , sudo_pass))

            # print(f" website : {website} \nusername : {user_name} \npassword : {sudo_pass}")
        print(tabulate(data , headers=['website' , 'username' , 'password' ] , tablefmt='psql'))


    # print(" Encoded string added" )
    


def update_credentials():

    if not os.path.exists(Filename):
        print("No file found")
        return
    
    new_website = input("Please write your Existing  website= ").strip().lower()
    new_user_name = input("Pleasr write your Existing username= ").strip().lower()
    new_password = getpass.getpass("Pleasr write your New password =").strip().lower()
    
    tmp_file = 'tmp.txt'
    updated = False

    with open(file=Filename , mode='r' , encoding='utf-8') as readfile ,  open(file=tmp_file , mode='w' , encoding='utf-8') as writefile:

        for line in readfile : 
            decodded_str = decode(line)
            website , user_name , password = decodded_str.split('||')

            if website == new_website or user_name == new_user_name :

                actual_url = f"{website}||{user_name}||{new_password}"
                encoded_str = encode(actual_url)

                writefile.write(encoded_str)
                updated = True
                             
            else:
                writefile.write(line)
                

    os.replace(tmp_file , Filename)
    if updated:
        print(" Password updated")
    else:
        print("Either user_name or website not found ")





def main():

    while True:
        decorate = "*" * 20
        print(f" {decorate}\nWelcome to password vault Manager\n {decorate}\n1. Add New Credentials  \n2. show all credentials  \n3. Update Credentials  \n4. Exit  ")

        choice = input("Please Enter your choice ( 1-4): ")
        
        match choice:

            case "1":
                add_credentials()
            case "2":
                show_credentials()

            case "3":
                update_credentials()

            case "4":
                print("welcome back")
                break 

            case _ :
                print("Please Enter the correct choice !!!!")




if __name__ == '__main__':
    main()