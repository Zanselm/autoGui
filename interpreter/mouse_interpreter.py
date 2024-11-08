import time

import pyautogui as pg

pg.PAUSE = 0


class MouseInterpreter:

    def __init__(self):
        pass

    def interpret(self, operation):
        match operation["operation"]:
            case "moveTo":
                self._moveTo(operation)
            case "click":
                self._click(operation)
            case "scroll":
                self._scroll(operation)

    def _moveTo(self, operation):
        data = operation["data"]
        pg.moveTo(data["x"], data["y"], operation["interval"])

    def _click(self, operation):
        data = operation["data"]
        button = str(data["button"]).split(".")[1]
        is_down = data["is_down"]
        pg.moveTo(data["x"], data["y"])
        if is_down:
            pg.mouseDown(x=data["x"], y=data["y"], duration=0, button=button)
        else:
            pg.mouseUp(x=data["x"], y=data["y"], duration=0, button=button)
        time.sleep(operation["interval"])

    def _scroll(self, operation):
        data = operation["data"]
        dy = data["dy"]
        pg.moveTo(data["x"], data["y"])
        pg.scroll(dy * 120)
        time.sleep(operation["interval"])



