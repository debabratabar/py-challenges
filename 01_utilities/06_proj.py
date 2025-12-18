"""
 Challenge: Daily Learning Journal Logger

Build a Python script that allows you to maintain a daily learning journal. Each entry will be saved into a `.txt` file along with a timestamp.

Your program should:
1. Ask the user what they learned today.
2. Add the entry to a file called `learning_journal.txt`.
3. Each entry should include the date and time it was written.
4. The journal should **append** new entries rather than overwrite.

Bonus:
- Add an optional rating (1-5) for how productive the day was.
- Show a confirmation message after saving the entry.
- Make sure the format is clean and easy to read when opening the file.

Example:
📅 2025-06-14 — 10:45 AM
Today I learned about how list comprehensions work in Python!
Productivity Rating: 4/5
"""

from datetime import datetime


def write_to_file(filename , content):

    curr_time = "📅 " + datetime.now().strftime("%Y-%m-%d - %I:%M: %p")
    decorate = "*" * 50
    final_content =  curr_time+"\n" + decorate +"\n" +content +"\n" +decorate +"\n"

    with open(filename ,'a' , encoding="utf-8") as f : 
        f.write(final_content)




def main():

    try:
        
        usr_inp  =input("What did you learn today ( use ',' for mutiple items ) : ").strip()
        prductivity = input("Tell me how productive were you today out of 5  : ").strip()

        int_str_split = usr_inp.split(',')

        content = 'Today I learnt about \n'

        for i in int_str_split:
            content+= f"-> {i.strip()}\n"

        content+=f"Productivity rating : {prductivity}/5" 

        

        write_to_file("learning_journet.txt" , content)

        print("Entry saved to the file successfully ")

    except Exception as e : 
        print(e)



if __name__ == "__main__" :
    main()

