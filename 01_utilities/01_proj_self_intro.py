"""
 Challenge: Self-Intro Script Generator

Create a Python script that interacts with the user and generates a personalized self-introduction.

Your program should:
1. Ask the user for their name, age, city, profession, and favorite hobby.
2. Format this data into a warm, friendly paragraph of self-introduction.
3. Print the final paragraph in a clean and readable format.

Example:
If the user inputs:
  Name: Priya
  Age: 22
  City: Jaipur
  Profession: Software Developer
  Hobby: playing guitar

Your script might output:
  "Hello! My name is Priya. I'm 22 years old and live in Jaipur. I work as a Software Developer and I absolutely enjoy playing guitar in my free time. Nice to meet you!"

Bonus:
- Add the current date to the end of the paragraph like: "Logged on: 2025-06-14"
- Wrap the printed message with a decorative border of stars (*)
"""



import datetime 

def personalized_output(user_data):

    curr_date =datetime.date.today()
    log_str = f'Logged on : {curr_date}'
    intro_msg = f"""
    Hello !! My Name is {user_data['Name']} , I'm  {user_data['Age']}  years old and live in {user_data['City']}. I work as a {user_data['Profession']} and 
    I absolutely enjoy {user_data['Hobby']} in my free time . Nice to meet you!
    {log_str}
    """

    decorator = "*" * 80

    final_msg = f'\n{decorator}\n {intro_msg} \n {decorator}'

    return final_msg


def main():
    user_data = {}
    user_inp =  ['Name' , 'Age' , 'City' , 'Profession' , 'Hobby']

    for inp in user_inp :
        user_input = input(f"Enter your {inp}:").strip()
        user_data[inp] = user_input

    print(personalized_output(user_data))


if __name__ == "__main__" :
    main()