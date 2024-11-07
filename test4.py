# # from pynput import keyboard
# #
# # print(keyboard.Key)
#
# import pyautogui as pg
#
#
# # pg.press('enter',presses=2,interval=0.2)
# pg.press('\r')
import time

import jsonIO
from interpreter import  Interpreter

time.sleep(3)
data = jsonIO.input_json()
interpreter = Interpreter()
interpreter.interpret(data)