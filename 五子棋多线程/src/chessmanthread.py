from chessman import *
import threading


class Chessmanthread(ChessMan):
    def __init__(self):
        self.value = 0
        super().__init__()
        self.con = threading.Condition()

    def do_notify(self):
        self.con.acquire()  # 先要acquire()获取状态才能进行wait()或notify()
        self.con.notify()
        self.con.release()

    def set_pos(self, pos):
        self.pos = pos

    def get_pos(self):
        return self.pos

    # 等待上一个线程
    def do_wait(self):
        self.con.acquire()  # 先要acquire()获取状态才能进行wait()或notify()
        self.con.wait()
        self.con.release()

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color
