import json


def output_json(data):
    file = open('new_json.json', 'w', encoding='UTF-8')
    file.write(json.dumps(data, ensure_ascii=False, indent=4))
    file.close()


def input_json(path = 'new_json.json'):
    file = open(path, 'r', encoding='UTF-8')
    data = file.read()
    file.close()
    return list(json.loads(data))
