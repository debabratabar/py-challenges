"""
 Challenge: Offline Notes Locker

Create a terminal-based app that allows users to save, view, and search personal notes securely in an encrypted file.

Your program should:
1. Let users add notes with title and content.
2. Automatically encrypt each note using Fernet (AES under the hood).
3. Store all encrypted notes in a single `.vault` file (JSON format).
4. Allow listing of titles and viewing/decrypting selected notes.
5. Support searching by title or keyword.

Bonus:
- Add timestamps to notes.
- Use a master password to unlock vault (optional).


"""

import os , json 
from cryptography.fernet import Fernet 
from datetime import datetime
import base64

keyfile = 'secret.key'
vault_file = 'notes_vault.json'


def load_or_create_key():

    if not os.path.exists(keyfile):
        key = Fernet.generate_key()
        with open(keyfile , 'wb') as f :
            f.write(key)

    else:
        with open(keyfile , mode='r') as f :
            key = f.read()

    return Fernet(key)


Fernet = load_or_create_key()

def load_json_data():

    if not os.path.exists(vault_file):
        # print(f" {vault_file} Not exists ")
        return []
    
    with open(vault_file ,mode='r' ) as f:
        data = json.load(f)

    return data



def save_json(json_data):

    with open(vault_file ,mode='w' ) as f:
        json.dump( json_data ,f  ,indent=2)




def add_notes () :

    title = input("Please enter the notes title : ").strip().lower()
    content = input("Please enter the notes content : ").strip().lower()

    encrypted_content = Fernet.encrypt(content.encode()).decode()



    data = load_json_data()
    data.append ( 
        {
            "title" : title ,
            'content' : encrypted_content,
            'timestamp'  : datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    )

    save_json(data)

    print(" Notes added to the notes manager ")

    

def list_notes():
    notes = load_json_data()
    if not notes:
        print("No notes to show")

    else:
        for idx , line in enumerate(notes,1):
            print(f"{idx}. {line['title']} - {line['timestamp']}")

    
def view_notes():

    list_notes()

    inp = int(input("please enter a index= "))-1
    data = load_json_data()
    
    if   0 <= inp <len(data) : 
        decrypted_content= Fernet.decrypt( data[inp]['content'].encode()).decode()

        print (f"title= {data[inp]['title']} | content = {decrypted_content} | timestamp = {data[inp]['timestamp']} ")

        
    else:
        print("Invalid input")





def search_notes () :
    search = input("Please enter the topic you want to search = ").strip().lower()
    data =load_json_data()

    result = [ line for line in data if search in line['title']]


    if not result:
        print("Not Found")
        
    else:
        for line in result:
            print(f" {line['title']} - {line['timestamp']}")

    






def main():
     

    while True:
        decorate = "*" * 20
        print(f" {decorate}\nWelcome to offline notes vault Manager\n {decorate}\n1. Add Notes  \n2. View Notes  \n3. List Notes  \n4. Search Notes \n5. Exit  ")

        choice = input("Please Enter your choice ( 1-5): ")
        
        match choice:

            case "1":
                add_notes()
            case "2":
                view_notes()

            case "3":
                list_notes()

            case "4":
                search_notes()
                
            case "5":
                print("welcome back")
                break 


            case _ :
                print("Please Enter the correct choice !!!!")



if __name__== '__main__':
    main()