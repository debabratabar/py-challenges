



""" 

Challenge: Hacker News Top Posts Scraper

Build a Python script that:
1. Fetches the HN homepage (news.ycombinator.com).
2. Extracts the top 20 post titles and URLs.
3. Saves the results into a CSV file (`hn_top20.csv`) with columns:
   - Title
   - URL
4. Handles network errors and uses a clean CSV structure.

"""

import requests
from bs4 import BeautifulSoup
import csv

def extract_hacker_news(url):
    req_header = { "User-Agent": "deb_app" }
    try:
        response = requests.get(url,timeout=10 , headers=req_header)
        response.raise_for_status()       

    except requests.RequestException as e :
        print(f" Oops !! got some error \n {e} " ) 

    


    soup = BeautifulSoup(response.text,'html.parser')
    a_tags_data = soup.select('span.titleline > a')
    headers = []

    for idx,i in enumerate(a_tags_data , start=1):

        headers.append({"Id" : idx , "Title" : i.get_text().strip() , "URL" : i.get('href').strip()})




    return headers
        

def write_to_csv(csv_data, csv_file):


    if not csv_data : 
        print("No Data , GO back Simon ")



    with open(file=csv_file , mode="w" , encoding="utf-8" , newline='') as f :
        csvwriter = csv.DictWriter(f, fieldnames=["Id" , "Title" , "URL" ] )

        csvwriter.writeheader()

        for line in csv_data:
            csvwriter.writerow(line)


def main():
    URL = 'https://news.ycombinator.com/'
    CSV_FILENAME = 'hn_top20.csv'
    csv_data = extract_hacker_news(URL) 
    write_to_csv(csv_data , CSV_FILENAME)

    



if __name__ == '__main__' :
    main()
