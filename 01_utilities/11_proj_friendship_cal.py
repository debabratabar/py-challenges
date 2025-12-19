"""
 Challenge: Friendship Compatibility Calculator

Build a Python script that calculates a fun "compatibility score" between two friends based on their names.

Your program should:
1. Ask for two names (friend A and friend B).
2. Count shared letters, vowels, and character positions to create a compatibility score (0-100).
3. Display the percentage with a themed message like:
   "You're like chai and samosa — made for each other!" or 
   "Well... opposites attract, maybe?"

Bonus:
- Use emojis in the result
- Give playful advice based on the score range
- Capitalize and center the final output in a framed box
"""


def calculate_score(name1 , name2 ):

    score = 0 

    shared_characters = set(name1) & set(name2) 
    vowels = set('aeiou') & shared_characters
    score += len(shared_characters) *5  
    score +=  len(vowels) * 5 

    return min(score , 100)


def create_themed_msg( score):

    
    content = ''
    if score > 80 :
        content = f'You\'re like chai and samosa — made for each other!'
    
    elif score >50 :
        content = f'You can work on it '

    else:
        content = f'Well... opposites attract, maybe?'

    decorate  = "*" * (len(content)+4)

    print(f'\n{decorate}\n*  {content}  *\n{decorate} ' )



def main():

    print("🧑‍🤝‍🧑 Welcome to  Friendship Compatibility Calculator 🧑‍🤝‍🧑")
    name1  = input("Please type your Friend 1 Name : ").strip().lower()
    name2  = input("Please type your Friend 2 Name : ").strip().lower()

    friendship_score = calculate_score(name1 , name2)
    print(f"Here is your Friendship score {friendship_score}")

    create_themed_msg(friendship_score)




if __name__=='__main__':
    main()