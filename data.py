from datetime import datetime
import json


def generate_new_user(id):
    data = get_data_person()
    data[id] = {}
    out = data[id]

    out["name"] = ''
    out["citizen"] = 100
    out["gold"] = 100
    out["exp"] = 0
    out["need_exp"] = 10
    out["lvl"] = 1
    out["power"] = 1
    update_data(data)

def update_data(new):
    with open("BD.json", "w") as f:
        json.dump(new, f,
                  ensure_ascii=False,
                  sort_keys=False,
                  indent=4,
                  separators=(',', ': ')
                  )
def get_data_person():
    with open("BD.json", "r") as f:
        data = json.load(f)
    return data

def check_person(id):
    data = get_data_person()
    try:
        x = data[str(id)]
        return True
    except:
        return False
