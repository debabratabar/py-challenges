"""
 Challenge: Minutes Alive Calculator

Write a Python script that calculates approximately how many minutes old a person is, based on their age in years.

Your program should:
1. Ask the user for their age in years (accept float values too).
2. Convert that age into:
   - Total days
   - Total hours
   - Total minutes
3. Display the result in a readable format.

Assumptions:
- You can use 365.25 days/year to account for leap years.
- You don't need to handle time zones or exact birthdates in this version.

Example:
Input:
  Age: 25

Output:
  You are approximately:
    - 9,131 days old
    - 219,144 hours old
    - 13,148,640 minutes old

Bonus:
- Add comma formatting for large numbers
- Let the user try again without restarting the program
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

    while True:
        try:
            age = int(input("Enter the age In Years : "))

            days , hours , minutes = calculate_min(age)
            print(f'- {days:,} days old ')
            print(f'- {hours:,} days old ')
            print(f'- {minutes:,} days old ')

            again =input("Do you want to continue  ( y/n) :").strip()
            if again != 'y':
                print('Thank you ! Welcome Back ')
                break
        except Exception as E : 
            print(E)



if __name__ == "__main__" :
    main()

