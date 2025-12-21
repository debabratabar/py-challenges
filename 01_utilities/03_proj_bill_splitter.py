"""
 Challenge: Simple Bill Splitter

Write a Python script that helps split a bill evenly between friends.

Your program should:
1. Ask how many people are in the group.
2. Ask for each person's name.
3. Ask for the total bill amount.
4. Calculate each person's share of the bill.
5. Display how much each person owes in a clean, readable format.

Example:
Total bill: ₹1200  
People: Aman, Neha, Ravi

Each person owes: ₹400

Final output:
  Aman owes ₹400  
  Neha owes ₹400  
  Ravi owes ₹400

Bonus:
- Round to 2 decimal places
- Print a decorative summary box
"""


def main():

    head_cnt = int(input("Enter the total no. of peaple: "))
    people= []
    for i in range(1,head_cnt+1):
        people.append(input(f"Please Enter  peron name #{i}: ").capitalize().strip())

    tot_amt = int(input("Enter the total bill amount :  "))
    person_split = round ( tot_amt / head_cnt  , 2 )

    print("*" * 50)
    print(f"\nTotal Bill : र{tot_amt} \nPeople: { " , ".join(people)} \n\nEach person owes : {person_split} \n\nFinal Output:")

    for i in people:
        print(f"  {i} owes र{person_split}")
    print("*" * 50)


if __name__ == "__main__" :
    main()

