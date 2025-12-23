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
import json  


def search_movies(file_name ) :
    inp = input("Please enter your movie or genre name = ").strip().lower()

    if os.path.exists(file_name):
        with open(file=file_name, mode='r' , encoding='utf-8') as f :

            json_data = json.load(f)
            movie_data = [ 
                movie for movie in json_data if movie['Title'] == inp or movie['Genre'] == inp
            ]

            if len(movie_data) ==0 :
                print("No Movie Found!!!")
            else:
                for line in movie_data :
                    print(f"Movie Found --{line} " )

    else:
        print("No File found")



def add_movies (file_name):
    try:
        Title = input("Enter Movie Title: ").strip()
        genre = input("Enter Movie genre: ").strip()
        rating = int(input("Enter Movie rating ( 1-10): "))

        if rating < 0 or rating > 10 :
            print("Please enter proper Ratinf ( 0-10 ) ")
            return
        

        with open(file=file_name, mode='r' , encoding='utf-8',newline='') as readfile:
            json_data = json.load(readfile)
            for line in readfile:
                if line['Title'] == Title:
                    print(f"Movie - {Title} is already present ")
                    return 

        movie = {'Title' : Title  , 'Genre' : genre , 'rating' : rating }
        # json_data = list
        json_data.append(movie)

        tmp_file = 'tmp.json'

        with open(file=tmp_file, mode='a' , encoding='utf-8',newline='') as writefile  :

            json.dump(json_data , writefile)
        
        os.replace(tmp_file , file_name)

        print("!!!!!!!!Movie  added !!!!!!!!!!!!!!!")
    except Exception as e : 
        print(e)

    
        



def view_movies(file_name):

    if os.path.exists(file_name):
        with open(file=file_name, mode='r' , encoding='utf-8') as f :

            json_data = json.load(f)
            for line in json_data:
                print(line)

    else:
        print("No Movie Founds")





def movie_tracker():

    movie_filename = 'movies.json'

    if not os.path.exists(movie_filename):
        with open(file=movie_filename , mode='w' , encoding='utf-8') as f :
            json.dump([]  , f)
    
    while True :
        # tasks = load_task(task_file)
        decorate = "*" * 20
        print(f" {decorate}\nWelcome to Personal Movie Tracker\n {decorate}\n1. Add a Movie  \n2. View All Movies  \n3. Search Movies by title or genre \n4. Exit the app  \n{decorate} ")

        choice = input("Please Select your option ( 1-4 ) : ")

        try:
            match choice:
                case "1" : #Add movie  
                    add_movies(movie_filename)
                case "2":
                    view_movies(file_name=movie_filename) 
                case "3":
                    search_movies(movie_filename )
                case  "4":
                    print("Welcome Back!!!!")
                    break              
                case _:
                    print("!!!!!!!!!!!!Please Select your option properly !!!!!!!!!!")
               
        except  Exception as e :
            print(e)
            break             


def main():

    movie_tracker()


if __name__ == '__main__':
    main()