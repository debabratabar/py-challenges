
from datetime import datetime
import string

curr_time = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")

print(curr_time)

print(string.punctuation)

print(string.ascii_letters)

print(chr(122))

name1 = "debabrata"
name2 = 'bar'

shared_characters = set(name1) & set(name2) 
    
print(shared_characters)
print(set('aeiou'))