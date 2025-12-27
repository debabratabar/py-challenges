"""
 Challenge: JSON-to-Excel Converter Tool

Create a Python utility that reads structured data (like you'd get from an API) from a `.json` file and converts it to a CSV file that can be opened in Excel.

Your program should:
1. Read from a file named `api_data.json` in the same folder.
2. Convert the JSON content (a list of dictionaries) into `converted_data.csv`.
3. Automatically extract field names as CSV headers.
4. Handle nested structures by flattening or skipping them.

Bonus:
- Provide feedback on how many records   were converted
- Allow user to define which fields to extract
- Handle missing fields gracefully
"""

import json 
import os
import csv 
from tabulate import tabulate

def load_csv_date(input_file):
    if not os.path.exists(input_file):
        print(f"{input_file} not exists ")
        return []
    else:
        with open(input_file , mode='r' , encoding='utf-8') as f :
            csv_data = csv.DictReader(f)
            return list(csv_data)
        

def convert_to_json(csv_data,out_fileName):
    if csv_data:
        # header = list( csv_data[0].keys())

        with open(out_fileName , mode='w' , encoding='utf-8') as f :
            json.dump(csv_data , f ,indent=2)

    else:
        print("Data couldn't be converted to json")


def main():
    input_fileName = 'converted_json_file.csv'
    out_fileName = 'out_json_file.json'

    print("Welcome to Csv to Json converter !!!!")

    csv_data = load_csv_date(input_fileName)
    header = list ( csv_data[0].keys() )
    data = [ list(i.values()) for i in csv_data ]
    convert_to_json(csv_data,out_fileName)
    print(f"{input_fileName} data is converted to {out_fileName} ")
    print("Here is the tabular format")
    # print(header)
    print(tabulate(data , header  , tablefmt='psql'))
    # pprint(json_data)




if __name__ == '__main__':
    main()