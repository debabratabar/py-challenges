from openai import OpenAI
import os 
from dotenv import load_dotenv

load_dotenv()

SYSTEM_PROMT = """ 
you are a dating adviser , don't answer anything else from dating related question 
"""


client = OpenAI(api_key=os.getenv("OPEN_AI_KEY") )


response  = client.chat.completions.create( 
    model = 'gpt-4o' , messages= [ 
        {"role" : "system" , "content" : SYSTEM_PROMT},
        {"role" : "user" , "content" : "how to warm up milk for baby  "}
    ]
)


print(response.choices[0].message.content)

