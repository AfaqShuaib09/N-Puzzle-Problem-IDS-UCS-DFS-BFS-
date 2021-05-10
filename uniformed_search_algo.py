from Puzzle_board import *
import copy
import heapq

moves = ['Down', 'Left', 'Up', 'Right']


def generate_required_board1(dimension):
    gen_board = []
    for i in range(dimension):
        gen_board.append(list())
    size = dimension * dimension
    for i in range(size):
        gen_board[int(i / dimension)].append(str(i))
    return gen_board


def generate_required_board2(dimension):
    gen_board = []
    for i in range(dimension):
        gen_board.append(list())
    size = dimension * dimension
    for i in range(size):
        gen_board[int(i / dimension)].append(str((i + 1) % size))
    return gen_board


def get_input_from_file(filename):
    file_lines = None
    try:
        file = open(filename, 'r')
        file_lines = file.readlines()
        file.close()
    except Exception as e:
        print("Exception Occured:", str(e))
    finally:
        return file_lines


def write_output_to_file(filename, writing_str, mode='w'):
    try:
        file = open(filename, mode)
        file.write(writing_str)
        file.close()
    except Exception as e:
        print("Failed to write", str(e))


def is_present(board, lst):
    for temp_board in lst:
        if temp_board.is_boards_equal(board):
            return True
    return False


def generate_path_str(path, found):
    os = ''
    if found:
        count = len(path)
        for i in path:
            count = count - 1
            if i == 'D':
                os = os + moves[0]
            elif i == 'R':
                os = os + moves[1]
            elif i == 'U':
                os = os + moves[2]
            elif i == 'L':
                os = os + moves[3]
            if count != 0:
                os = os + '-> '
    else:
        os = os + "No path found"
    return os


def dfs_search(line):
    ls = line.rstrip().split(',')
    ls_visited_states = list()
    ls_new_unvisited_st = list()
    board = Puzzle_board(ls)
    req_board1 = generate_required_board1(int(m.sqrt(len(ls))))
    req_board2 = generate_required_board2(int(m.sqrt(len(ls))))
    ls_new_unvisited_st.append(copy.deepcopy(board)) # maintains the list of non explored state
    ls_visited_states.append(copy.deepcopy(board)) #maintains the list of all discovered states
    path = ''
    if board.is_boards_equal(req_board1) or board.is_boards_equal(req_board2):
        return path
    found = False
    while len(ls_new_unvisited_st) != 0 and not found:
        board = ls_new_unvisited_st.pop() # implementing the stack structure by popping out last element(LIFO)
        temp_board = copy.deepcopy(board)
        temp_board.move_right()
        if not is_present(temp_board.board, ls_visited_states):
            if temp_board.is_boards_equal(req_board1) or temp_board.is_boards_equal(req_board2):
                path = temp_board.path
                found = True
                break
            ls_visited_states.append(copy.deepcopy(temp_board))
            ls_new_unvisited_st.append(copy.deepcopy(temp_board))
        temp_board = copy.deepcopy(board)
        temp_board.move_down()
        if not is_present(temp_board.board, ls_visited_states):
            if temp_board.is_boards_equal(req_board1) or temp_board.is_boards_equal(req_board2):
                path = temp_board.path
                found = True
                break
            ls_visited_states.append(copy.deepcopy(temp_board))
            ls_new_unvisited_st.append(copy.deepcopy(temp_board))
        temp_board = copy.deepcopy(board)
        temp_board.move_left()
        if not is_present(temp_board.board, ls_visited_states):
            if temp_board.is_boards_equal(req_board1) or temp_board.is_boards_equal(req_board2):
                path = temp_board.path
                found = True
                break
            ls_visited_states.append(copy.deepcopy(temp_board))
            ls_new_unvisited_st.append(copy.deepcopy(temp_board))
        temp_board = copy.deepcopy(board)
        temp_board.move_up()
        if not is_present(temp_board.board, ls_visited_states):
            if temp_board.is_boards_equal(req_board1) or temp_board.is_boards_equal(req_board2):
                path = temp_board.path
                found = True
                break
            ls_visited_states.append(copy.deepcopy(temp_board))
            ls_new_unvisited_st.append(copy.deepcopy(temp_board))

    return generate_path_str(path, found)


def IDS_search(line):  #implenting dfs by limiting its depths on each iteration
    ls = line.rstrip().split(',')
    req_board1 = generate_required_board1(int(m.sqrt(len(ls))))
    req_board2 = generate_required_board2(int(m.sqrt(len(ls))))
    found = False
    path = ''
    iter_level = -1
    while not found:
        ls_visited_states = list()
        ls_new_unvisited_st = list()
        board = Puzzle_board(ls)
        if board.is_boards_equal(req_board1) or board.is_boards_equal(req_board2):
            return path
        ls_new_unvisited_st.append((copy.deepcopy(board), 0))
        ls_visited_states.append(copy.deepcopy(board))
        iter_level = iter_level + 1
        level = 0
        level_flag = False
        while len(ls_new_unvisited_st) != 0 and not found:
            board, level = ls_new_unvisited_st.pop()
            if iter_level <= level:
                level_flag = True
            if not level_flag:
                temp_board = copy.deepcopy(board)
                temp_board.move_right()
                if not is_present(temp_board.board, ls_visited_states):
                    if temp_board.is_boards_equal(req_board1) or temp_board.is_boards_equal(req_board2):
                        path = temp_board.path
                        found = True
                        break
                    ls_visited_states.append(copy.deepcopy(temp_board))
                    ls_new_unvisited_st.append((copy.deepcopy(temp_board), level + 1))
                temp_board = copy.deepcopy(board)
                temp_board.move_left()
                if not is_present(temp_board.board, ls_visited_states):
                    if temp_board.is_boards_equal(req_board1) or temp_board.is_boards_equal(req_board2):
                        path = temp_board.path
                        found = True
                        break
                    ls_visited_states.append(copy.deepcopy(temp_board))
                    ls_new_unvisited_st.append((copy.deepcopy(temp_board), level + 1))
                temp_board = copy.deepcopy(board)
                temp_board.move_up()
                if not is_present(temp_board.board, ls_visited_states):
                    if temp_board.is_boards_equal(req_board1) or temp_board.is_boards_equal(req_board2):
                        path = temp_board.path
                        found = True
                        break
                    ls_visited_states.append(copy.deepcopy(temp_board))
                    ls_new_unvisited_st.append((copy.deepcopy(temp_board), level + 1))
                temp_board = copy.deepcopy(board)
                temp_board.move_down()
                if not is_present(temp_board.board, ls_visited_states):
                    if temp_board.is_boards_equal(req_board1) or temp_board.is_boards_equal(req_board2):
                        path = temp_board.path
                        found = True
                        break
                    ls_visited_states.append(copy.deepcopy(temp_board))
                    ls_new_unvisited_st.append((copy.deepcopy(temp_board), level + 1))
            level_flag = False

    return generate_path_str(path, found)


def bfs_search(line):
    ls = line.rstrip().split(',')
    req_board1 = generate_required_board1(int(m.sqrt(len(ls))))
    req_board2 = generate_required_board2(int(m.sqrt(len(ls))))
    ls_visited_states = list()
    ls_new_unvisited_st = list()
    board = Puzzle_board(ls)
    ls_new_unvisited_st.append(copy.deepcopy(board))
    ls_visited_states.append(copy.deepcopy(board))
    path = ''
    if board.is_boards_equal(req_board1) or board.is_boards_equal(req_board2):
        return path
    found = False
    while len(ls_new_unvisited_st) != 0 and not found:
        board = ls_new_unvisited_st[0]
        ls_new_unvisited_st.pop(0) #implenting the stack structure by popping the first Element
        temp_board = copy.deepcopy(board)
        temp_board.move_down()
        if not is_present(temp_board.board, ls_visited_states):
            if temp_board.is_boards_equal(req_board1) or temp_board.is_boards_equal(req_board2):
                path = temp_board.path
                found = True
                break
            ls_visited_states.append(copy.deepcopy(temp_board))
            ls_new_unvisited_st.append(copy.deepcopy(temp_board))
        temp_board = copy.deepcopy(board)
        temp_board.move_right()
        if not is_present(temp_board.board, ls_visited_states):
            if temp_board.is_boards_equal(req_board1) or temp_board.is_boards_equal(req_board2):
                path = temp_board.path
                found = True
                break
            ls_visited_states.append(copy.deepcopy(temp_board))
            ls_new_unvisited_st.append(copy.deepcopy(temp_board))
        temp_board = copy.deepcopy(board)
        temp_board.move_up()
        if not is_present(temp_board.board, ls_visited_states):
            if temp_board.is_boards_equal(req_board1) or temp_board.is_boards_equal(req_board2):
                path = temp_board.path
                found = True
                break
            ls_visited_states.append(copy.deepcopy(temp_board))
            ls_new_unvisited_st.append(copy.deepcopy(temp_board))
        temp_board = copy.deepcopy(board)
        temp_board.move_left()
        if not is_present(temp_board.board, ls_visited_states):
            if temp_board.is_boards_equal(req_board1) or temp_board.is_boards_equal(req_board2):
                path = temp_board.path
                found = True
                break
            ls_visited_states.append(copy.deepcopy(temp_board))
            ls_new_unvisited_st.append(copy.deepcopy(temp_board))
    return generate_path_str(path, found)


def UCS_search(line):
    path = ''
    found = False
    ls = line.rstrip().split(',')
    req_board1 = generate_required_board1(int(m.sqrt(len(ls))))
    req_board2 = generate_required_board2(int(m.sqrt(len(ls))))
    ls_visited_states = []
    ls_new_unvisited_st = []
    board = Puzzle_board(ls)
    if board.is_boards_equal(req_board1) or board.is_boards_equal(req_board2):
        return path
    level_no = 0
    heapq.heappush(ls_new_unvisited_st, (level_no, copy.deepcopy(board)))
    ls_visited_states.append(copy.deepcopy(board))
    while len(ls_new_unvisited_st) != 0 and not found:
        level_no, board = heapq.heappop(ls_new_unvisited_st) #get the board state from queue on the basis of level no.
        temp_board = copy.deepcopy(board)
        temp_board.move_down()
        if not is_present(temp_board.board, ls_visited_states):
            if temp_board.is_boards_equal(req_board1) or temp_board.is_boards_equal(req_board2):
                path = temp_board.path
                found = True
                break
            ls_visited_states.append(copy.deepcopy(temp_board))
            heapq.heappush(ls_new_unvisited_st, (level_no + 1, copy.deepcopy(temp_board)))
        temp_board = copy.deepcopy(board)
        temp_board.move_right()
        if not is_present(temp_board.board, ls_visited_states):
            if temp_board.is_boards_equal(req_board1) or temp_board.is_boards_equal(req_board2):
                path = temp_board.path
                found = True
                break
            ls_visited_states.append(copy.deepcopy(temp_board))
            heapq.heappush(ls_new_unvisited_st, (level_no + 1, copy.deepcopy(temp_board)))
        temp_board = copy.deepcopy(board)
        temp_board.move_up()
        if not is_present(temp_board.board, ls_visited_states):
            if temp_board.is_boards_equal(req_board1) or temp_board.is_boards_equal(req_board2):
                path = temp_board.path
                found = True
                break
            ls_visited_states.append(copy.deepcopy(temp_board))
            heapq.heappush(ls_new_unvisited_st, (level_no + 1, copy.deepcopy(temp_board)))
        temp_board = copy.deepcopy(board)
        temp_board.move_left()
        if not is_present(temp_board.board, ls_visited_states):
            if temp_board.is_boards_equal(req_board1) or temp_board.is_boards_equal(req_board2):
                path = temp_board.path
                found = True
                break
            ls_visited_states.append(copy.deepcopy(temp_board))
            heapq.heappush(ls_new_unvisited_st, (level_no + 1, copy.deepcopy(temp_board)))
    return generate_path_str(path, found)

