import json
import uuid

def read_json(data_path: str):
        with open(data_path, "r", encoding='utf-8') as database:
            return json.load(database)

def write_json(data_path: str, payload: list[dict]):
    with open(data_path, 'a') as file:

        new_data = {'id' :  str(uuid.uuid4()) ,'name' : payload["name"],'price': payload["price"]}
        json.dump(new_data, file, indent=2)

########### Utilizei uuid pois na entrega diz apenas que precisa ser um id não repetido #############