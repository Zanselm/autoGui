import time

import pyautogui
from pynput import keyboard

import key_list
from entity.operation import *
from recorder import Recorder


class KeyboardListener(keyboard.Listener):
    """
    键盘监听类
    """
    _data: dict = None  # 数据
    _can_record: bool = False  # 可记录标志
    _keyboard: keyboard.Controller = None  # 键盘控制器
    _recorder: Recorder = Recorder()  # 记录器
    _key_map: list = None  # 按键映射

    def __init__(self):
        super().__init__(on_press=self._on_press,
                         on_release=self._on_release)
        self._data = dict()
        self._keyboard = keyboard.Controller()
        self._key_map: dict = key_list.key_mapping

    # 按下监听
    def _on_press(self, key):
        if self._can_record:
            key = self._get_key_str(key)
            print('{} 按下了'.format(key))
            self._recorder.add_json(
                KeyboardPress({'key': key}, f'{key} 按下', self._get_time_distance()))
            # try:
            #     print('字母键： {} 被按下'.format(key.char))
            # except AttributeError:
            #     print('特殊键： {} 被按下'.format(key))

    def _on_release(self, key):
        if key == keyboard.Key.esc:
            # 释放了esc 键，停止监听a
            self.end_record()
        if self._can_record:
            key = self._get_key_str(key)
            print('{} 释放了'.format(key))
            self._recorder.add_json(
                KeyboardPress({'key': key}, f'{key} 释放', self._get_time_distance()))

    def _get_time_distance(self) -> float:
        """
        获取操作间隔时间
        :return: 时间
        """
        last_time = self._data["last_time"]
        now_time = time.time()
        self._data["last_time"] = now_time
        return round(now_time - last_time, 3)

    def _get_key_str(self, key_str) -> str:
        strip_str = str(key_str).strip("'")
        # if len(strip_str)>1:
        #     return self._key_map[strip_str]
        # else:
        #     return strip_str
        return self._key_map[strip_str] if len(strip_str) > 1 else strip_str

    def record(self):
        """
        开始记录
        :return: None
        """
        self._can_record = True
        # self._data["last_position"] = self._mouse.position
        self._data["last_time"] = round(time.time(), 3)
        self._data["start_time"] = round(time.time(), 3)

    def end_record(self):
        """
        结束记录
        :return: None
        """
        self._can_record = False
        self._data["all_time"] = round(time.time() - self._data["start_time"], 3)
        self._recorder.output(self._data)
        self.stop()


if __name__ == '__main__':
    # time.sleep(3)
    # s = time.time()
    ky = KeyboardListener()
    ky.start()
    ky.record()
    ky.join()
    # print(time.time() - s)
    # a
    # pyautogui.keyDown('ctrl')
    # pyautogui.press("\x01")
    # pyautogui.keyUp('ctrl')

    # pyautogui.keyDown("win")
    # pyautogui.keyUp("win")

    # print(str("'a'").strip("'").split(".")[0])
    pass
