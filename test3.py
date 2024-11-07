# from pynput import keyboard
#
#
# def on_press(key):
#     try:
#         # 如果按下的是字母或数字键，则输出其字符标识
#         if hasattr(key, 'char') and key.char is not None:
#             print(f"按下了字符键：{key.char}")
#         else:
#             # 输出其他特殊键的标识符
#             print(f"按下了特殊键：{key}")
#     except AttributeError:
#         # 对于特殊按键（如 Shift、Ctrl 等），直接输出它们的名称1234456789/*11123456789
#
#         print(f"按下了特殊键：{key}")
#
#
# # 设置键盘监听
# with keyboard.Listener(on_press=on_press) as listener:
#     listener.join()
import time

import jsonIO
import interpreter

import mouse_listener

ml = mouse_listener.MouseListener()

ml.start()
ml.record()
ml.join()

# import json
# a = {
#     "name": "dabao",
#     "id":123,
#     "hobby": {
#         "sport": "basketball",
#         "book": "python study"
#     }
# }
# b = json.dumps(a)
# f2 = open('new_json.json', 'w')
# f2.write(b)
# f2.close()
# data = jsonIO.input_json()
# print(data,type(data),data[0],type(data[1]))

# data = jsonIO.input_json()
# interpreter = interpreter.Interpreter()
# interpreter.interpret(data)