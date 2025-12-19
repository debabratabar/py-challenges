"""
Building a Caesar Cipher

Challenge: Secret Message Encryptor & Decryptor

Create a Python script that helps you send secret messages to your friend using simple encryption.

Your program should:
1. Ask the user if they want to (E)ncrypt or (D)ecrypt a message.
2. If encrypting:
   - Ask for a message and a numeric secret key.
   - Use a Caesar Cipher (shift letters by the key value).
   - Output the encrypted message.
3. If decrypting:
   - Ask for the encrypted message and key.
   - Reverse the encryption to get the original message.

Rules:
- Only encrypt letters; leave spaces and punctuation as-is.
- Make sure the letters wrap around (e.g., 'z' + 1 → 'a').

Bonus:
- Allow uppercase and lowercase letter handling
- Show a clean interface
"""

def encrypt(msg , secret_key):

    encrypted_msg = ''

    for ch in msg:
        if not ch.isalpha():
            encrypted_msg += ch

        else: 
            upper  = ord('Z') if ch.isupper() else ord('z')
            lower  = ord('A') if ch.isupper() else ord('a')
            ascii_num = ord(ch) + secret_key 
            if ascii_num > upper:
                encrypted_msg += chr( lower+ (ascii_num - upper))
            else:
                encrypted_msg += chr(ascii_num)

    return encrypted_msg 


def decrypt(msg , secret_key):

    decrypted_msg = ''

    for ch in msg:
        if not ch.isalpha():
            decrypted_msg += ch

        else: 
            upper  = ord('Z') if ch.isupper() else ord('z')
            lower  = ord('A') if ch.isupper() else ord('a')
            ascii_num = ord(ch) - secret_key 
            if ascii_num < lower :
                decrypted_msg += chr( upper - (lower- ascii_num))
            else:
                decrypted_msg += chr(ascii_num)


    return decrypted_msg



def main():

    print("What Do you want to do \nE. Encrypt\nD. Decrypt ")
    option = input("Please Choose your option ( E/D): ").strip().upper()
    
    
    if option == 'E':
        msg = input("Please Enter your message to Encrypt : ").strip()
        secret_key = int(input('Please enter secret key between 1 to 25 : '))
        encrypted_msg = encrypt(msg , secret_key )
        print(f"Here is your encrepted message : {encrypted_msg}")
    
    elif  option == 'D':
        msg = input("Please Enter your message to Decrypt : ").strip()
        secret_key = int(input('Please enter secret key between 1 to 25  gitto Decrypt : '))
        decrypted_msg = decrypt(msg , secret_key )
        print(f"Here is your decrypted message : {decrypted_msg}")
    
    
    else:
        print("Please Enter Valid Option ! Thanks ! Visit Again ")

    

if __name__ == '__main__':
    main()