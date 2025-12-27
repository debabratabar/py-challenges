import requests
from datetime import datetime
from pprint import pprint 
import csv , base64



str1 = 'debabrata'

dcode_vali = str1.encode()

print(dcode_vali)
print(type(dcode_vali))


print(base64.b64encode(dcode_vali))

