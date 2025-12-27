"""
Challenge : JSON Flattener

{
  "user": {
    "id": 1,
    "name": "Riya",
    "email": "riya@example.com",
    "address": {
      "city": "Delhi",
      "pincode": 110001
    }
  },
  "roles": ["admin", "editor"],
  "is_active": true
}

Flatten this to:

{
  "user.id": 1,
  "user.name": "Riya",
  "user.email": "riya@example.com",
  "user.address.city": "Delhi",
  "user.address.pincode": 110001,
  "roles.0": "admin",
  "roles.1": "editor",
  "is_active": true
}


"""

import json ,os



inp_file = 'raw_data.json'
out_file = 'flattened_data.json'

def flatten_json(data , parent_key  = '' , sep='.' , ):

    items = {}

    if isinstance( data , dict) :
        for key , value in data.items():
            full_key = f"{parent_key}{sep}{key}" if parent_key else key
            items.update(flatten_json(value , full_key , sep))

    elif isinstance(data, list):
        
        for id , item  in enumerate(data):
            full_key = f"{parent_key}{sep}{id}" if parent_key else str(id)
            items.update(flatten_json(item, full_key , sep))

    else:
        items[parent_key] = data


    return items 




def main():
    


    if not os.path.exists(inp_file):
        print(f' {inp_file} is not present ')
    else:
        try:
            sep= input("please Enter the separater = ") or '.'

            with open(file=inp_file , mode='r' , encoding='utf-8') as f :
                data = json.load(f)

            flatten_data = flatten_json( data=data ,parent_key='' ,  sep=sep )
            # print(flatten_data)
            with open(file=out_file , mode='w' , encoding='utf-8' ) as f :
                json.dump(flatten_data , f , indent=2 )

        except Exception as e:
            print(e)





if __name__ == '__main__':
    main()



