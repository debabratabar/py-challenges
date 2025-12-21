"""
 Challenge: Password Strength Checker & Suggestion Tool

Build a Python script that checks the strength of a password based on:
1. Length (at least 8 characters)
2. At least one uppercase letter
3. At least one lowercase letter
4. At least one digit
5. At least one special character (e.g., @, #, $, etc.)

Your program should:
- Ask the user to input a password.
- Tell them what's missing if it's weak.
- If the password is strong, confirm it.
- Suggest a strong random password if the input is weak.

Bonus:
- Hide password input using `getpass` (no echo on screen).
"""


import getpass
import random , string 


def pass_checker2(pass_str):
    issues =[]

    if len(pass_str)<8:
        issues.append('Password length must be >= 8')
    
    if not any( i.isupper() for i in pass_str):
        issues.append('Please Add atleast one Uppercase Letter')

    if not any( i.islower() for i in pass_str):
        issues.append('Please Add atleast one Uppercase Letter')

    if not any( i.isdigit() for i in pass_str):
        issues.append('Please Add atleast one Digit')

    if not any( i in string.punctuation for i in pass_str):
        issues.append('Please Add atleast one special character ')

    return issues


def pass_checker(pass_str):

    ucase = 0 
    lcase = 0 
    digit = 0 
    spec_ch = 0 

    for  i  in pass_str:
        if 97<=  ord(i)  <= 122:
            lcase+=1
        elif 65 <=  ord(i)  <= 90:
            ucase+=1

        elif 48 <=  ord(i)  <= 57:
            digit+=1
        else:
            spec_ch+=1

    if ucase>=1 and lcase>=1 and digit>=1 and spec_ch >=1 and len(pass_str)>=8:
        print("Your Password is Strong")
    
    else : 
        print("Your Password is Weak \nHere is some suggestion:\n")
        if len(pass_str)<8:
            print('passwoed length must be atleast 8 ')
        if ucase==0:
            print('Please Add atleast one Uppercase Letter')
        if lcase==0:
            print('Please Add atleast one Lowercase Letter')
        if digit==0:
            print('Please Add atleast one Digit Letter')
        if spec_ch==0:
            print('Please Add atleast one Special Character Letter')


def suggested_pass(length =12):
    char_str = string.ascii_letters + string.digits + string.punctuation
    res = ''
    for _ in   range(0,length):
        res+= random.choice(char_str)

    return res


        
def main():

    password = getpass.getpass("Please Enter your passworsd: ")
    issue= pass_checker2(password)

    if len(issue) ==0:
        print('Your password is Strong')
    else:
        print('YOur Password is Weak')
        for i in issue:
            print(i)

        print('\nHere is your random suggested password')
        print(suggested_pass())



    

if __name__ == '__main__':
    main()