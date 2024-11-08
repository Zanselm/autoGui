import json
from typing import Union

import util.jsonIO
from entity.operation import Operation


class Recorder:
    data: list = None
    json_num: int = 0

    def __init__(self):
        self.data = list()

    def set_head(self, data: dict):
        if self.data[0]["module"] != "head":
            self.data.insert(0, {'num': self.json_num, 'module': 'head'})
        for key in data.keys():
            self.data[0][key] = data[key]

    def add_json(self, operation: Union[str, Operation]):
        self.json_num += 1
        self.data.append(operation.to_json() if type(operation) != str else operation)

    def print(self):
        """
        打印记录数据至控制台
        :return: None
        """
        print(self.data)

    def output(self, data: dict):
        self.set_head(data)
        util.jsonIO.output_json(self.data)
