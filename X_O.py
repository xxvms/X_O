the_board = {'1': '1', '2': '2', '3': '3',
             '4': '4', '5': '5', '6': '6',
             '7': '7', '8': '8', '9': '9'
             }


def print_board(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print("-+-+-")
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print("-+-+-")
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


def take_move():
    victory = False
    while not victory:
        turn = 'X'
        for i in range(9):
            print_board(the_board)
            print('Turn for ' + turn + '. Move on which space?')
            move = input()
            if the_board[move].isnumeric():
                the_board[move] = turn
                if i >= 4:
                    victory = check_victory(turn)
                    if victory:
                        print("player " + turn + " is victorious")
                        break
                    elif i == 8:
                        print("this is a draw")
                        victory = True
                        break
            else:
                print("this slot is taken")
                continue
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'


def check_victory(turn):
    # this is victory
    if (the_board['1'] == turn and the_board['2'] == turn and the_board['3'] == turn) or \
            (the_board['4'] == turn and the_board['5'] == turn and the_board['6'] == turn) or \
            (the_board['7'] == turn and the_board['8'] == turn and the_board['9'] == turn) or \
            (the_board['1'] == turn and the_board['4'] == turn and the_board['7'] == turn) or \
            (the_board['2'] == turn and the_board['5'] == turn and the_board['8'] == turn) or \
            (the_board['3'] == turn and the_board['6'] == turn and the_board['9'] == turn) or \
            (the_board['1'] == turn and the_board['5'] == turn and the_board['9'] == turn) or \
            (the_board['7'] == turn and the_board['5'] == turn and the_board['3'] == turn):
        return True
    else:
        return False


take_move()
