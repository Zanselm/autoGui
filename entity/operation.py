import json


class Operation:
    """
    操作类
    """
    default_interval = 0.25

    def __init__(self, module, operation, data, description, interval=-1):
        self.module = module
        self.operation = operation
        self.data = dict(data)
        self.description = description
        self.is_operated: bool = False
        if interval < 0:
            self.interval = self.default_interval
        else:
            self.interval = interval

    def to_json(self):
        # return json.dumps(self.__dict__,ensure_ascii=False)
        return self.__dict__


def form_json(json_str: str) -> Operation:
    op = json.loads(json_str)
    # print(type(op),op)
    return Operation(op['module'], op['operation'], op['data'], op['description'], op['interval'])


class MouseMoveTo(Operation):

    def __init__(self, data, description, interval):
        super().__init__('mouse', 'moveTo', data, description, interval)


class MouseClick(Operation):

    def __init__(self, data, description, interval):
        super().__init__('mouse', 'click', data, description, interval)


class MouseScroll(Operation):

    def __init__(self, data, description, interval):
        super().__init__('mouse', 'scroll', data, description, interval)


class KeyboardPress(Operation):

    def __init__(self, data, description, interval):
        super().__init__('keyboard', 'press', data, description, interval)


class KeyboardRelease(Operation):

    def __init__(self, data, description, interval):
        super().__init__('keyboard', 'release', data, description, interval)
