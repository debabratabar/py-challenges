from openai import OpenAI
import os 
from dotenv import load_dotenv

load_dotenv()

SYSTEM_PROMT = """ 
You are a math professor , you only answer to a math question , anything elsr other than math don't answer , just say sorry



"""


client = OpenAI(api_key=os.getenv("OPEN_AI_KEY") )


response  = client.chat.completions.create( 
    model = 'gpt-4o' , messages= [ 
        {"role" : "system" , "content" : SYSTEM_PROMT},
        {"role" : "user" , "content" : "give me basics of trigonmetry"}
    ]
)


print(response.choices[0].message.content)

