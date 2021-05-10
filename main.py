from uniformed_search_algo import *


def run_NPuzzle_program():
    mode = 'w'
    file_input = get_input_from_file('input.txt')
    for line in file_input:
        ls = line.rstrip().split(',')
        state = ''
        for i in ls:
            state = state + str(i) + ','
        state = state.rstrip(',')
        print(state)
        bfs_path = "BFS: " + bfs_search(line)
        print(bfs_path)
        ucs_path = "UCS: " + UCS_search(line)
        print(ucs_path)
        ids_path = "IDS: " + IDS_search(line)
        print(ids_path)
        dfs_path = "DFS: " + dfs_search(line)
        print(dfs_path)
        write_output_to_file('output.txt', bfs_path + '\n' + ucs_path + '\n' + ids_path + '\n' + dfs_path +
                             '\n', mode)
        mode = 'a'


# Main function Calling
run_NPuzzle_program()
