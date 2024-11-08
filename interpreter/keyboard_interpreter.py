import time

import pyautogui as pg

pg.PAUSE = 0


class KeyboardInterpreter:

    def __init__(self):
        pass

    def interpret(self, operation):
        match operation["operation"]:
            case "press":
                self._press(operation)
            case "release":
                self._release(operation)

    def _press(self, operation):
        data = operation["data"]
        pg.keyDown(data["key"])
        time.sleep(operation["interval"])

    def _release(self, operation):
        data = operation["data"]
        pg.keyUp(data["key"])
        time.sleep(operation["interval"])




