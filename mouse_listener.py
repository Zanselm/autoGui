import time

from pynput import mouse
from entity.operation import *
from recorder import Recorder


class MouseListener(mouse.Listener):
    """
    鼠标监听类
    """
    _data: dict = None
    _can_record: bool = False
    _mouse: mouse.Controller = None
    _record_distance: int = 0
    _recorder: Recorder = Recorder()

    def __init__(self, record_move=True, record_click=True, record_scroll=True, record_distance=30):
        super().__init__(on_move=self._on_move,
                         on_click=self._on_click if record_click else None,
                         on_scroll=self._on_scroll if record_scroll else None)
        self._record_distance = record_distance
        self._data = dict()
        self._mouse = mouse.Controller()
        self.record_move = record_move

    def _on_move(self, x, y):
        if self._can_record:
            if x < 5 and y > 1075:
                self._recorder.print()
                self.stop()
            elif self.record_move:
                point = self._data.get("last_position")
                lx = point[0]
                ly = point[1]
                # print(x,y,lx,ly,(x - lx) ** 2 + (y - ly) ** 2)
                if (x - lx) ** 2 + (y - ly) ** 2 > self._record_distance ** 2:
                    self._data["last_position"] = (x, y)
                    # print('鼠标移动到了：{}'.format((x, y)))
                    self._recorder.add_json(
                        MouseMoveTo({'x': x, 'y': y}, '鼠标移至{}'.format((x, y)), self._get_distance()))

    # 点击监听
    def _on_click(self, x, y, button, pressed):
        if self._can_record:
            # print('鼠标按键：{}，在位置处 {}, {} '.format(button, (x, y), '按下了' if pressed else '释放了'))
            self._recorder.add_json(
                MouseClick({'x': x, 'y': y, 'button': str(button), 'is_down': True if pressed else False},
                           '{}在{}{} '.format(button, (x, y), '按下' if pressed else '释放'),
                           self._get_distance()))

    # 滚动监听
    def _on_scroll(self, x, y, dx, dy):
        if self._can_record:
            # print('滚动中... {} 至 {}'.format('向下：' if dy < 0 else '向上：', (x, y)))
            self._recorder.add_json(
                MouseScroll({'x': x, 'y': y, 'dy': dy, 'dx': dx},
                            '{}滚动至{}'.format('向下：' if dy < 0 else '向上：', (x, y)),
                            self._get_distance()))

    def _get_distance(self):
        last_time = self._data["last_time"]
        now_time = time.time()
        self._data["last_time"] = now_time
        return round(now_time - last_time, 2)

    def record(self):
        self._can_record = True
        self._data["last_position"] = self._mouse.position
        self._data["last_time"] = time.time()
        self._data["start_time"] = time.time()

    def end_record(self):
        self._can_record = False
