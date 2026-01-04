import json
from openai import OpenAI
import os 
from dotenv import load_dotenv

load_dotenv()


# few short prompting with output format rule 
SYSTEM_PROMT_WITH_FEW_SHORT = """ 
you are a dating adviser , don't answer anything else from dating related question 

Rule : 
- Strictly follow below output format in JSON format

Output_format: 
{
"isDatingAdvice" : boolean , 
"result" : string
}


Examples : 
Q. how to talk to girls ?
A. {
"isDatingAdvice" : True , 
"result" : ['approch first with a pickup line ' , 'learn about this girl first '] 
}


Q. what is 2+2 ?
A. {
"isDatingAdvice" : False , 
"result" : ['i am dating advicer not a mathematecian']
}

"""
client = OpenAI(api_key=os.getenv("OPEN_AI_KEY") )


response  = client.chat.completions.create( 
    model = 'gpt-4o' , 
    response_format={"type" : "json_object"},
    messages= [ 
        {"role" : "system" , "content" : SYSTEM_PROMT_WITH_FEW_SHORT},
        {"role" : "user" , "content" : "how to talk to a girl? "}
    ]
)


resp = response.choices[0].message.content 

parsed_result = json.loads( resp)

for idx , i in enumerate( parsed_result.get("result") , 1):
    print(f" {idx}. {i} ")


# print(response.choices[0].message.content)

