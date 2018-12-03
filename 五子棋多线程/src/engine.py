from chessboard import *
from chessman import *
import random
from math import *


class Engine(object):
    # 初始化 需要把棋盘对象传入
    def __init__(self, chessboard):
        self.__chessboard = chessboard

    # 电脑下棋的策略
    # 告诉棋子的颜色 返回下棋的位置
    # 传入chessman对象的时候 把棋子的颜色写入
    # 该方法中负责填写棋子的位置

    def computer_go(self, chessman):
        if not isinstance(chessman, ChessMan):
            raise RuntimeError('类型不对 第1个参数必须为ChessMan对象')

        while True:
            # pos_x和pos_y在1~15之间随机生成一个数
            pos_x = random.randint(1, 15)  # [1,15]
            pos_y = random.randint(1, 15)
            if self.__chessboard.get_chess((pos_x, pos_y)) == '+':
                print('电脑下棋的位置:%d,%s' % (pos_x,chr(pos_y + 96)))
                # 把pos_x和pos_y写入chessman对象中
                chessman.set_pos((pos_x, pos_y))
                # 退出while循环
                break

    # 用户在终端下棋
    # 提示用户 传入用户输入的字符串 并解释该字符串对应的位置
    # 传入chessman对象的时候 把棋子的颜色写入
    # 该方法中负责填写棋子的位置
    # 比如3,b 表示第3行第2列
    def parse_user_input(self,inpu,chessman):
        if not isinstance(chessman, ChessMan):
            raise RuntimeError('类型不对 第1个参数必须为ChessMan对象')
        im = inpu
        ret = im.split(',')
        value1 = ret[0]  # '3'
        value2 = ret[1]  # 'b'
        # 转换成坐标
        pos_x = int(value1)
        pos_y = ord(value2) - ord('a') + 1
        # print(pos_y)
        chessman.set_pos((pos_x, pos_y))

    # 判断胜负
    # 判断胜负
    # 判断chessman对象的棋子放置后 胜负是否已分
    # 调用is_won()并返回它的返回值即可
    def is_wonman(self, chessman):
        if not isinstance(chessman, ChessMan):
            raise RuntimeError('类型不对 第1个参数必须为ChessMan对象')
        pos = chessman.get_pos()
        color = chessman.get_color()
        return self.is_won(pos, color)
















    def judge(self):
        chessboard = ChessBoard()
        chessboard.init_board()
        c = input('选择先后,a黑子(x)先，b白子(o):')
        if c == 'b':
            chessman1 = ChessMan()
            chessman1.set_color('o')
            chessman2 = ChessMan()
            chessman2.set_color('x')
            while True:
                engine = Engine(chessboard)
                engine.computer_go(chessman2)
                chessboard.set_chessman(chessman2)
                chessboard.print_board()
                engine.parse_user_input(chessman1)
                chessboard.set_chessman(chessman1)
                chessboard.print_board()
                #l = chessboard.is_wo('o')
                l = engine.is_womm('o')
                if l == True:
                    break
        else:
            chessman1 = ChessMan()
            chessman1.set_color('o')
            chessman2 = ChessMan()
            chessman2.set_color('x')
            while True:
                engine = Engine(chessboard)
                engine.parse_user_input(chessman2)
                chessboard.set_chessman(chessman2)
                engine.computer_go(chessman1)
                chessboard.set_chessman(chessman1)
                chessboard.print_board()
                #l = chessboard.is_wo('x')
                l = engine.is_womm('x')
                if l == True:
                    break
    def is_womm(self, color):
        c = []
        for i in range(1,16):
            for j in range(1,16):
                chess = self.__chessboard.get_chess((i, j))
                if chess == color:
                    l = []
                    l.append(i)
                    l.append(j)
                    c.append(l)
        for i in range(len(c) - 1):
            for l in range(i + 1, len(c)):
                x = abs((c[i][0] - c[l][0]) ** 2 + (c[i][1] - c[l][1]) ** 2)
                if sqrt(x) == sqrt(16):
                    if (c[i][0] - c[l][0]) == 0:
                        if c[l - 1][1] == c[l][1] - 1 and c[l - 2][1] == c[l][1] - 2 and c[l - 3][1] == c[l][1] - 3:
                            print('你赢了')
                            return True
                    elif (c[i][1] - c[l][1]) == 0:
                        if c[l - 1][0] == c[l][0] - 1 and c[l - 2][0] == c[l][0] - 2 and c[l - 3][0] == c[l][0] - 3:
                            print('你赢了')
                            return True
                    else:
                        continue
                if sqrt(x) == sqrt(32):
                    if c[l][0] + c[l][1] > c[i][0] + c[i][1]:
                        q = [c[i][0] + 1, c[i][1] + 1]
                        w = [c[i][0] + 2, c[i][1] + 2]
                        e = [c[i][0] + 3, c[i][1] + 3]
                        if q == c[i + 1] and w == c[i + 2] and e == c[i + 3]:
                            print('你赢了')
                            return True
                    else:
                        t = c[i][0] + c[i][1]
                        if c[i + 1][0] + c[i + 1][1] == t and c[i + 2][0] + c[i + 2][1] == t and c[i + 3][0] + c[i + 3][
                            1] == t:
                            print('你赢了')
                            return True

