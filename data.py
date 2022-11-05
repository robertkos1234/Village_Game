from datetime import datetime
import json


def generate_new_user(id):
    data = get_data()
    data[id] = {}
    out = data[id]

    out["name"] = ''
    out["human"] = 10
    out["gold"] = 500
    out["tax"] = 2
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


def get_data():
    with open("BD.json", "r") as f:
        data = json.load(f)
    return data


def check_person(id):
    data = get_data()
    try:
        x = data[str(id)]
        return True
    except:
        return False


def set_name(id, name):
    data = get_data()
    data[str(id)]["name"] = name

    update_data(data)


def get_data_person(id):
    data = get_data()

    return data[str(id)]


def add_gold(id, amount):
    data = get_data()
    data[str(id)]["gold"] += amount

    update_data(data)