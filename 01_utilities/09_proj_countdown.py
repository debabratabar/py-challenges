"""
Challenge: Set a Countdown Timer

Create a Python script that allows the user to set a timer in seconds. The script should:

1. Ask the user for the number of seconds to set the timer.
2. Show a live countdown in the terminal.
3. Notify the user when the timer ends with a final message and sound (if possible).

Bonus:
- Format the remaining time as MM:SS
- Use a beep sound (`\a`) at the end if the terminal supports it
- Prevent negative or non-integer inputs
"""

import time 

def main():
    try:
        sec = int(input("Please enter a value in seconds "))
        if sec >= 1:
            for i in range(sec,0,-1):
                mins , secs = divmod( i , 60)
                time_format = f"{mins:02}:{secs:02}"
                print(f"times remaining {time_format}",end='\r')
                time.sleep(1)
        else:
            print('please give a non-negative number ')
    except Exception as e :
        print("Exception !! {e}")

    

if __name__ == '__main__':
    main()