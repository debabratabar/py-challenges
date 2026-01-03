from openai import OpenAI
import os 
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key= os.getenv("OPEN_AI_KEY"))
                # base_url="https://generativelanguage.googleapis.com/v1beta/openai/") # equivallent api for pulling free data from chrone .


response = client.chat.completions.create(
    model="gpt-4o" , messages= [ {"role" : "user" , "content" : "Hii , who are you ??"  } ] 
)


print(response.choices[0].message.content)