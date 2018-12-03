from chessboard import *
from chessman import *
from engine import *
from chessmanthread import *
from gothread import *






def test6():
    while True:
        chessboard = ChessBoard()
        chessboard.init_board()
        engine = Engine(chessboard)
        engine.judge()
        i = int(input('是否继续是（1）否（0）:'))
        if i == 0 :
            break
def main_thread():
    c = input('选择先后,a黑子(x)先，b白子(o):')
    if c == 'x':
        print('已选择')
    chessboard = ChessBoard()
    chessboard.init_board()
    engine = Engine(chessboard)
    chessman_pc = Chessmanthread()
    chessman_user = Chessmanthread()
    t1 = ComputerGoThread(chessman_pc,engine)
    t2 = UserGoThread(chessman_user,engine)
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    while True:
        chessman_user.do_wait()

        pos = chessman_user.get_pos()
        chessboard.set_chess(pos, 'x')
        chessboard.print_board()

        chessman_pc.do_notify()
        chessman_pc.do_wait()

        pos = chessman_pc.get_pos()
        chessboard.set_chess(pos, 'o')
        chessboard.print_board()

        l = engine.is_womm('x')
        if l == True:
            break
        chessman_user.do_notify()

if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    # test4()
    #test5()
    #test6()
    main_thread()

