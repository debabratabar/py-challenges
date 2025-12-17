"""
 Challenge: Emoji Enhancer for Messages

Create a Python script that takes a message and adds emojis after specific keywords to make it more expressive.

Your program should:
1. Ask the user to input a message.
2. Add emojis after certain keywords (like "happy", "love", "code", "tea", etc.).
3. Print the updated message with emojis.

Example:
Input:
  I love to code and drink tea when I'm happy.

Output:
  I love ❤️ to code 💻 and drink tea 🍵 when I'm happy 😊.

Bonus:
- Make it case-insensitive (match "Happy" or "happy")
- Handle punctuation (like commas or periods right after keywords)

"""

def calculate_min(age):

    tot_day_in_yr = 365.25
    tot_hr_in_day = 24
    tot_min_in_hr = 60

    tot_days = tot_day_in_yr * age
    tot_hrs = tot_days * tot_hr_in_day
    tot_mins = tot_hrs * tot_min_in_hr

    return round(tot_days , 2) , round(tot_hrs  , 2) , round(tot_mins,2)  


def main():

    try:
        emoji_dict = { 'work' : '🏢' ,
                      'smile' : '😊',
                      'fire' : '🔥',
                      'code' :  '🧑‍💻'  ,
                            'love' : "❤️"      }
        
        inp_str =input("Please enter your String : ")

        int_str_split = inp_str.split(' ')

        res_str = ''

        for i in int_str_split:
            i = i.lower().strip('.,I ?')
            if emoji_dict.get(i.lower().strip(),0):

                res_str+= f" {i}  {emoji_dict[i]} "

            else:

                res_str+= f" {i} "

        print(res_str)

    except Exception as e : 
        print(e)




        print(res_str)




if __name__ == "__main__" :
    main()

