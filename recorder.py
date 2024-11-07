import json
from typing import Union

from entity.operation import Operation


class Recorder:
    data: list = None
    json_num: int = 0

    def __init__(self):
        self.data = list()

    def set_head(self):
        self.data.insert(0,{'num':self.json_num,'module': 'head'})

    def add_json(self, operation: Union[str, Operation]):
        self.json_num += 1
        self.data.append(operation.to_json() if type(operation) != str else operation)

    def print(self):
        print(self.data)
        self.set_head()
        f2 = open('new_json.json', 'w',encoding='UTF-8')
        f2.write(json.dumps(self.data, ensure_ascii=False,indent=4))
        f2.close()
