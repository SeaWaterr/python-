import threading
import random


class UserGoThread(threading.Thread):
    def __init__(self, chessmanthread, engine):
        super().__init__()
        self.engine = engine
        self.chessmanthread = chessmanthread

    def run(self):
        while True:
            im = input('请下棋:')
            self.engine.parse_user_input(im, self.chessmanthread)
            self.chessmanthread.do_notify()
            self.chessmanthread.do_wait()


class ComputerGoThread(threading.Thread):
    def __init__(self, chessmanthread, engine):
        super().__init__()
        self.chessmanthread = chessmanthread
        self.engine = engine

    def run(self):
        while True:
            self.chessmanthread.do_wait()
            self.engine.computer_go(self.chessmanthread)
            self.chessmanthread.do_notify()
