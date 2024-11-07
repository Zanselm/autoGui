import mouse_interpreter


class Interpreter:
    data: list = None
    mouse_interpreter = None

    def __init__(self):
        self.mouse_interpreter = mouse_interpreter.MouseInterpreter()
        pass

    def interpret(self, data:list):
        self.data = data
        for operation in data:
            match operation["module"]:
                case "head":
                    pass
                case "mouse":
                    self.mouse_interpreter.interpret(operation)
