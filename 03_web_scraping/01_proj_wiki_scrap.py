



"""
 Challenge: Scrape Wikipedia h2 Headers

Use the `requests` and `BeautifulSoup` libraries to fetch the Wikipedia page on Python (programming language).

Your task is to:
1. Download the HTML of the page.
2. Parse all `<h2>` section headers.
3. Store the clean header titles in a list.
4. Print the total count and display the first 10 section titles.

Bonus:
- Remove any trailing "[edit]" from the headers.
- Handle network errors gracefully.

"""

import requests
from bs4 import BeautifulSoup

def extract_h2_tags(url):
    req_header = { "User-Agent": "deb_app" }
    try:
        response = requests.get(url,timeout=10 , headers=req_header)
        response.raise_for_status()       

    except requests.RequestException as e :
        print(f" Oops !! got some error \n {e} " ) 


    soup = BeautifulSoup(response.text,'html.parser')
    h2_tags_data = soup.find_all('h2')
    headers = []



    for i in h2_tags_data:
        if  i.get_text(strip=True) and  i.get_text(strip=True) != 'Contents' :
            headers.append(i.get_text(strip=True))


    return headers
        




def main():
    URL = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
    headers = extract_h2_tags(URL) 

    for i in range(10):
        print(headers[i])




if __name__ == '__main__' :
    main()
