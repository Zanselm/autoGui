"""
用于json文件输出读取
"""
import json
import tkinter as tk
from tkinter import filedialog


def output_json(data: list, path: str = '../new_json.json'):
    """
    输出json文件
    :param data: 数据列表
    :param path: 被输出文件的路径
    :return: None
    """
    file = open(path, 'w', encoding='UTF-8')
    file.write(json.dumps(data, ensure_ascii=False, indent=4))
    file.close()


def input_json(path: str = 'new_json.json') -> list:
    """
    获取json文件
    :param path: 被读取文件的路径
    :return: 数据列表
    """
    file = open(path, 'r', encoding='UTF-8')
    data = file.read()
    file.close()
    return list(json.loads(data))


def select_file_path():
    # 创建 tkinter 根窗口并隐藏它
    root = tk.Tk()
    root.withdraw()
    # 隐藏主窗口
    # 打开文件选择对话框
    file_path = filedialog.asksaveasfilename(defaultextension=".json",
                                             filetypes=[("JSON files", "*.json")])
    return file_path

#
# if __name__ == '__main__':
#     print(select_file_path())
