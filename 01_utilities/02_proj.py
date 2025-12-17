"""
Challenge: Stylish Bio Generator for Instagram/Twitter

Create a Python utility that asks the user for a few key details and generates a short, stylish bio that could be used for social media profiles like Instagram or Twitter.

Your program should:
1. Prompt the user to enter their:
   - Name
   - Profession
   - One-liner passion or goal
   - Favorite emoji (optional)
   - Website or handle (optional)

2. Generate a stylish 2-3 line bio using the inputs. It should feel modern, concise, and catchy.

3. Add optional hashtags or emojis for flair.

Example:
Input:
  Name: Riya
  Profession: Designer
  Passion: Making things beautiful
  Emoji: 🎨
  Website: @riya.design

Output:
  🎨 Riya | Designer  
  💡 Making things beautiful  
  🔗 @riya.design

Bonus:
- Let the user pick from 2-3 different layout styles.
- Ask the user if they want to save the result into a `.txt` file.
"""


def write_to_file(filename , content):

    decorate = "*" * 50
    final_content = decorate +"\n" +content +"\n" +decorate

    with open(filename ,'w' , encoding="utf-8") as f : 
        f.write(final_content)



def bio_generate(user_data , option):

    if option == "1":

        return f'{user_data['emoji']} {user_data['Name']} | {user_data['Profession']} \n {user_data['Passion']} \n  {user_data['website'] } '

    elif option == "2":
        return f'{user_data['emoji']} {user_data['Name']} \n{user_data['Profession']}  🔥\n{user_data['Passion']} \n{user_data['website'] }  🔥'

    elif option == "3":
        return f'{user_data['emoji']*3} \n{user_data['Name']} - {user_data['Profession']} \n{user_data['Passion']} \n{user_data['website'] } \n{user_data['emoji']*3}  '



def main():
    user_data = {}
    user_inp =  ['Name' , 'Profession' , 'Passion' , 'emoji' , 'website']

    for inp in user_inp :
        user_input = input(f"Enter your {inp}:").strip()
        user_data[inp] = user_input

    print("Choose your option:")
    print("\n1. Simple Lines ")
    print("\n1. Vertical Flair ")
    print("\n1. emoji sandwich ")

    option= input("\n Choose your style ( 1/2/3 ) :  ").strip()

    bio = bio_generate(user_data,option)
    print(bio)

    iswrite= input("Do you want to write the bio in a file? (y/n) : ").lower().strip()
    
    if iswrite == 'y':
        fileName = user_data['Name'].lower().replace(' ' , '_') + '_bio.txt'
        write_to_file(fileName , bio )
        print('FIle Written Successfully')
    
    print("Thank you ! welcome back ")




if __name__ == "__main__" :
    main()

