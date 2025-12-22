"""
 Challenge: CLI Contact Book (CSV-Powered)

Create a terminal-based contact book tool that stores and manages contacts using a CSV file.

Your program should:
1. Ask the user to choose one of the following options:
   - Add a new contact
   - View all contacts
   - Search for a contact by name
   - Exit
2. Store contacts in a file called `contacts.csv` with columns:
   - Name
   - Phone
   - Email
3. If the file doesn't exist, create it automatically.
4. Keep the interface clean and clear.

Example:
Add Contact
View All Contacts
Search Contact
Exit

Bonus:
- Format the contact list in a table-like view
- Allow partial match search
- Prevent duplicate names from being added
"""

import os
from datetime import datetime
import csv 


HEADER = ['name' , 'email' , 'ph_no']


def delete_contact(file_name, name):

    
    if os.path.exists(file_name):
        tmp_file = 'tmp_file.csv'
        chk = False


        with open(file=file_name, mode='r' , encoding='utf-8',newline='') as readfile:
            csv_reader = csv.DictReader(readfile)

            for line in csv_reader:
                if line['name'] == name :
                    chk = True
                    break

        if chk :
            with open(file=file_name, mode='r' , encoding='utf-8',newline='') as readfile , open(file=tmp_file, mode='w' , encoding='utf-8',newline='') as writefile  :

                csv_reader = csv.DictReader(readfile)
                csv_writer = csv.writer(writefile)

                csv_writer.writerow(HEADER)

                for line in csv_reader:
                    if line['name'] != name :
                        val =  [ item for item in line.values() ] 
                        csv_writer.writerow(val)

            os.replace(tmp_file , file_name)
            print("Contact Deleted  ")

        else:
            print(f" {name} is not found ")
    else:
        print(f" {file_name} Not exists " )


def update_contacts(file_name, name):
    
    # header = [ item for item in name.keys() ] 
    if os.path.exists(file_name):
        tmp_file = 'tmp_file.csv'
        chk = False


        with open(file=file_name, mode='r' , encoding='utf-8',newline='') as readfile:
            csv_reader = csv.DictReader(readfile)

            for line in csv_reader:
                if name['name'] == line['name']:
                    chk = True
                    break

        if chk :
            with open(file=file_name, mode='r' , encoding='utf-8',newline='') as readfile , open(file=tmp_file, mode='w' , encoding='utf-8',newline='') as writefile  :

                csv_reader = csv.DictReader(readfile)
                csv_writer = csv.writer(writefile)

                csv_writer.writerow(HEADER)

                for line in csv_reader:
                    if line['name'] ==name['name']:
                        val =  [ item for item in name.values() ] 
                        csv_writer.writerow(val)

                    else:
                        val =  [ item for item in line.values() ] 
                        csv_writer.writerow(val)

            os.replace(tmp_file , file_name)
            print("Contact Updated ")

        else:
            print(f" {name['name']  } is not found ")
    else:
        print(f" {file_name} Not exists " )
    





def search_contacts(file_name, name ) :

    if os.path.exists(file_name):
        with open(file=file_name, mode='r' , encoding='utf-8') as f :

            csvreader = csv.DictReader(f)
            for line in csvreader:
                if line['name'] == name:
                    # print(line) 
                    # break
                    return [ True , line]

            # print("No Contact Found")
            return [False]
    else:
        return [False]



def add_contacts (contacts , file_name):
    header = [ item for item in contacts.keys() ] 
    data = [ item for item in contacts.values() ] 

    if os.path.exists(file_name):
        with open(file=file_name, mode='a' , encoding='utf-8',newline='') as f :

            csvwriter = csv.writer(f)     
            # csvwriter.writerow(header)
            csvwriter.writerow(data)
    else:
        with open(file=file_name, mode='a' , encoding='utf-8' , newline='') as f :

            csvwriter = csv.writer(f)     
            csvwriter.writerow(header)
            csvwriter.writerow(data)

    print("!!!!!!!!Contact added !!!!!!!!!!!!!!!")
        



def view_contacts(file_name):

    if os.path.exists(file_name):
        with open(file=file_name, mode='r' , encoding='utf-8') as f :

            csvreader = csv.DictReader(f)
            for line in csvreader:
                print(line)

    else:
        print("No Contact Founds")





def contact_book_manager():

    contact_file = 'contacts.csv'
    
    while True :
        # tasks = load_task(task_file)
        decorate = "*" * 20
        print(f" {decorate}\nWelcome to Contact List Manager\n {decorate}\n1. Add a New Contact  \n2. View All Contacts  \n3. Search a Contact \n4. Update a contact \n5. Delete a contact \n6. Exit  ")

        choice = input("Please Select your option ( 1-6 ) : ")

        try:
            match choice:
                
                
                case "1" : #Add contact 
                    items  = ['name' , 'email' , 'ph_no']
                    items_dict={}
                    for item in items: 
                        inp = input(f"please enter your {item}: ").strip()
                        items_dict[item]= inp  

                    # print(items_dict)

                    if not search_contacts(contact_file , items_dict['name']  )[0]:
                        add_contacts(items_dict , contact_file)
                    else:
                        print(f" {items_dict['name']} is already present in contact book ")

                
                
                
                
                case "2":
                    view_contacts(file_name=contact_file)

                
                
                
                
                case "3":
                    name = input("Please enter the person Name : ").strip()
                    result =     search_contacts(contact_file , name )[0]
                    if result[0]:
                        print(f"Contact Found -- {result[1]}")
                    else:
                        print("No Contact Found")

                
                
                
                case "4":
                    name = input(f"please enter your name you want to update : ").strip()

                    items  = ['email' , 'ph_no']
                    items_dict={}
                    items_dict['name'] = name
                    for item in items: 
                        inp = input(f"please enter your {item}: ").strip()
                        items_dict[item]= inp  


                    update_contacts(contact_file , items_dict)



                case "5":
                    del_name = input(f"PLease Enter the contact name you want to delete: ").strip()
                    # print(del_name)

                    if del_name:
                        delete_contact(contact_file , del_name)
                    else:
                        print("Please Enter a Valid Name ")


                case  "6":
                    print("Welcome Back!!!!")
                    break              


                case _:
                    print("!!!!!!!!!!!!Please Select your option properly !!!!!!!!!!")
               
        except  Exception as e :
            print(e)
            break


                


           
def main():

    contact_book_manager()


if __name__ == '__main__':
    main()