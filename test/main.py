import atexit
import signal
import win32api
import win32con

def on_exit():
    file = open('test.txt', 'w')
    file.write('exiting')
    file.close()

def on_exit2(event):
    if event == win32con.WM_CLOSE:
        on_exit()

atexit.register(on_exit)
signal.signal(signal.SIGTERM, on_exit)
win32api.SetConsoleCtrlHandler(on_exit2, True)

input('hello world')
