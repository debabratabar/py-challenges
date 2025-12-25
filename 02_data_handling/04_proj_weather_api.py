"""
 Challenge: Real-Time Weather Logger (API + CSV)

Build a Python CLI tool that fetches real-time weather data for a given city and logs it to a CSV file for daily tracking.

Your program should:
1. Ask the user for a city name.
2. Fetch weather data using the OpenWeatherMap API.
3. Store the following in a CSV file (`weather_log.csv`):
   - Date (auto-filled as today's date)
   - City
   - Temperature (in °C)
   - Weather condition (e.g., Clear, Rain)
4. Prevent duplicate entries for the same city on the same day.
5. Allow users to:
   - Add new weather log
   - View all logs
   - Show average, highest, lowest temperatures, and most frequent condition

Bonus:
- Format the output like a table
- Handle API failures and invalid city names gracefully
"""



import os, csv , requests 
from datetime import datetime
from tabulate import  tabulate 


weather_file = 'weather_log.csv'
header = ["Date" , 'City' , 'Temp' , 'Condition']
api_key='get your own key' # openweathermap api key 
api_link = f"https://api.openweathermap.org/data/2.5/weather?"




def get_api_data (city):
    # try:
    curr_date = datetime.now().strftime("%Y-%m-%d")
    api_url = f"{api_link}q={city}&appid={api_key}"
    req = requests.get(api_url)
    if req.status_code==200 :
        temparature =  req.json()['main']['temp']
        condition =  req.json()['weather'][0]['main']



        data = [curr_date , city , temparature , condition]
        return data 
    else:
        print(f'Error Message :: {req.json()['message']}')
        return None

    # except Exception as e:
    #     print(e)




def find_data(city,date):
    with open(file=weather_file , mode='r' , encoding='utf-8') as f :
            csvreader = csv.DictReader(f)

            for line in csvreader:
                if line['City'] == city and line['Date'] == date :
                    return True 
                
            return False



def add_weather_log( fileName):
    tmp_file= 'tmp.csv'
    city = input("Please Enter city Name : ").strip().lower()
    curr_date  = datetime.now().strftime("%Y-%m-%d")

    if city:
        if not find_data(city,curr_date):
            city_data = get_api_data(city)
            if city_data:
                with open(file=fileName, mode='a' , encoding='utf-8',newline='') as readfile:
                    csvwriter = csv.writer(readfile)
                    csvwriter.writerow(city_data)

            else:
                print("Wrong input ")
        else:
            print("City is present for today!!!!! check with option 2")
            return 
     

    else:
        print("Please enter city name properly")

        

def show_logs(fileName):
    with open(file=fileName, mode='r' , encoding='utf-8') as readfile:
        csvreader = list(csv.reader(readfile) )
        if len(csvreader) <2:
            print("No Data")
            return

        print(tabulate(csvreader[1:] ,headers=header , tablefmt='psql'))


def get_stats ( fileName) :
    pass 



def  main():
    
    if not os.path.exists(weather_file):
        with open(file=weather_file , mode='w' , encoding='utf-8') as f :
            csvwriter = csv.writer(f)
            csvwriter.writerow(header)
    
   
    while True :
        decorate = "*" * 20
        print(f" {decorate}\nWelcome to Weatgher log CLI tool \n {decorate}\n1. Add Weather Log  \n2. View All Weather logs  \n3. Show Stat \n4. Exit  ")

        choice = input("Please Select your option ( 1-4 ) : ")

        # try:
        match choice:
            
            
            case "1" : 
                add_weather_log(fileName=weather_file )            
            

            case "2":
                show_logs(fileName=weather_file)             
            
            case "3":
                get_stats(fileName=weather_file)                
            
            case "4":
                print("Welcome Back!!!!")
                break              

            case _:
                print("!!!!!!!!!!!!Please Select your option properly !!!!!!!!!!")
               
        # except  Exception as e :
        #     print(e)
            # break






if __name__ == '__main__':
    main()

