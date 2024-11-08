from interpreter.mouse_interpreter import MouseInterpreter
from interpreter.keyboard_interpreter import KeyboardInterpreter


class Interpreter:
    data: list = None
    mouse_interpreter:MouseInterpreter = None
    keyboard_interpreter:KeyboardInterpreter = None
    def __init__(self):
        if self.mouse_interpreter is None:
            self.mouse_interpreter = MouseInterpreter()
        if self.keyboard_interpreter is None:
            self.keyboard_interpreter = KeyboardInterpreter()
        pass

    def interpret(self, data: list):
        self.data = data
        for operation in data:
            match operation["module"]:
                case "head":
                    pass
                case "mouse":
                    self.mouse_interpreter.interpret(operation)
                case "keyboard":
                    self.keyboard_interpreter.interpret(operation)
                case "browser":
                    pass
