from pynput import mouse, keyboard


# 移动监听
def on_move(x, y):
    print('鼠标移动到了：{}'.format((x, y)))


# 点击监听
def on_click(x, y, button, pressed):
    print('鼠标按键：{}，在位置处 {}, {} '.format(button, (x, y), '按下了' if pressed else '释放了'))


# 滚动监听
def on_scroll(x, y, dx, dy):
    print('滚动中... {} 至 {}'.format('向下：' if dy < 0 else '向上：', (x, y)))


# # 构造监听器对象，方式1: （监听哪几种类型事件）
# with mouse.Listener(
#         on_move=on_move,
#         on_click=on_click,
#         on_scroll=on_scroll) as listener:


# 构造监听器对象，方式2（可替换上面with）（监听哪几种类型事件）
listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)

# 开始监听
# listener.start()


# listener.join()


def on_press(key):
    print('{} 按下了'.format(key))
    # try:
    #     print('字母键： {} 被按下'.format(key.char))
    # except AttributeError:
    #     print('特殊键： {} 被按下'.format(key))


def on_release(key):
    print('{} 释放了'.format(key))
    if key == keyboard.Key.esc:
        # 释放了esc 键，停止监听a
        return False


# 方式1：构造监听器对象listener
# with keyboard.Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:


# 方式2：构造监听器对象listener
listener2 = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)

# 开始监听
# 监听启动方式1：阻断式

# 监听启动方式2：非阻断式
listener2.start()

listener2.join()
