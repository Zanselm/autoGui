from pynput.keyboard import Key

special_keys = [
    Key.alt,
    Key.alt_l, Key.alt_r,
    Key.backspace,
    Key.caps_lock,
    Key.ctrl, Key.ctrl_l, Key.ctrl_r,
    Key.delete,
    Key.down,
    Key.end,
    Key.enter,
    Key.esc,
    Key.f1, Key.f2, Key.f3, Key.f4, Key.f5, Key.f6, Key.f7, Key.f8, Key.f9, Key.f10, Key.f11, Key.f12,
    Key.home,
    Key.left,
    Key.page_down,
    Key.page_up,
    Key.right,
    Key.shift, Key.shift_l, Key.shift_r,
    Key.space,
    Key.tab,
    Key.up,
    Key.pause
]

pynput_special_keys = [
    'alt', 'alt_l', 'alt_r',
    'backspace',
    'capslock',
    'ctrl', 'ctrl_l', 'ctrl_r',
    'delete',
    'down',
    'end',
    'enter',
    'esc',
    'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12',
    'home',
    'left',
    'pagedown',
    'pageup',
    'right',
    'shift', 'shift_l', 'shift_r',
    'space',
    'tab',
    'up',
    'pause'
]

pynput_special_keys_withKey = [
    'Key.alt', 'Key.alt_l', 'Key.alt_r',
    'Key.backspace',
    'Key.caps_lock',
    'Key.ctrl', 'Key.ctrl_l', 'Key.ctrl_r',
    'Key.delete',
    'Key.down',
    'Key.end',
    'Key.enter',
    'Key.esc',
    'Key.f1', 'Key.f2', 'Key.f3', 'Key.f4', 'Key.f5', 'Key.f6', 'Key.f7', 'Key.f8', 'Key.f9', 'Key.f10', 'Key.f11', 'Key.f12',
    'Key.home',
    'Key.left',
    'Key.page_down', 'Key.page_up',
    'Key.right',
    'Key.shift', 'Key.shift_l', 'Key.shift_r',
    'Key.space',
    'Key.tab',
    'Key.up',
    'Key.pause'
]

char_keys = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~',
    ' '  # 空格键
]

pyautogui_char_keys = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~',
    ' ' ]

pyautogui_control_keys = [
    'enter', 'esc', 'shift', 'ctrl', 'alt', 'tab', 'backspace', 'delete', 'capslock', 'space', 'up', 'down', 'left', 'right',
    'home', 'end', 'pageup', 'pagedown', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12',
    'pause', 'printscreen', 'scrolllock', 'numlock'
]

key_mapping = {
    'Key.alt': 'alt',
    'Key.alt_l': 'alt',
    'Key.alt_r': 'alt',
    'Key.backspace': 'backspace',
    'Key.caps_lock': 'capslock',
    'Key.ctrl': 'ctrl',
    'Key.ctrl_l': 'ctrl',
    'Key.ctrl_r': 'ctrl',
    'Key.delete': 'delete',
    'Key.down': 'down',
    'Key.end': 'end',
    'Key.enter': 'enter',
    'Key.esc': 'esc',
    'Key.f1': 'f1', 'Key.f2': 'f2', 'Key.f3': 'f3', 'Key.f4': 'f4', 'Key.f5': 'f5',
    'Key.f6': 'f6', 'Key.f7': 'f7', 'Key.f8': 'f8', 'Key.f9': 'f9', 'Key.f10': 'f10',
    'Key.f11': 'f11', 'Key.f12': 'f12',
    'Key.home': 'home',
    'Key.left': 'left',
    'Key.page_down': 'pagedown',
    'Key.page_up': 'pageup',
    'Key.right': 'right',
    'Key.shift': 'shift',
    'Key.shift_l': 'shift',
    'Key.shift_r': 'shift',
    'Key.space': 'space',
    'Key.tab': 'tab',
    'Key.up': 'up',
    'Key.pause': 'pause'
}