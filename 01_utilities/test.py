
from datetime import datetime
import string
import csv ,os 


data = ['Deb',999,'gmail']
header = ['Name','ph','email']

file_name  = 'contact.csv'

# if os.path.exists(file_name):
#     with open(file=file_name, mode='a' , encoding='utf-8') as f :

#         csvwriter = csv.writer(f)     
#         # csvwriter.writerow(header)
#         csvwriter.writerow(data)
# else:
#     with open(file=file_name, mode='a' , encoding='utf-8') as f :

#         csvwriter = csv.writer(f)     
#         csvwriter.writerow(header)
#         csvwriter.writerow(data)


# with open(file=file_name, mode='r' , encoding='utf-8') as f :
#     csv_obj = csv.DictReader(f)
#     csv_writerf = csv.DictWriter(f)

#     for i in csv_obj:
#         print(i)


dict = {'name': 'de', 'email': 'e', 'ph_no': 'ph_deno'}

print(list(dict.keys()))
print(dict.values())


obj = 'deb'

if obj:
    print("heyy")
else:
    print("NOO")