from Node import Node
import copy


def manhattan_dist(state: list, fin_state: list):
    dist = 0
    for number in range(1, 9):
        x_curr_state, y_curr_state, x_final_state, y_final_state = state[number][1][0], state[number][1][1], \
            fin_state[number][1][0], fin_state[number][1][1]
        dist += (abs(x_curr_state - x_final_state) + abs(y_curr_state - y_final_state))

    return dist


def return_move_direction(p_state: list, i_state: list):
    if p_state[0][1][1] > i_state[0][1][1] and p_state[0][1][0] == i_state[0][1][0]:
        return 'U'
    elif p_state[0][1][1] < i_state[0][1][1] and p_state[0][1][0] == i_state[0][1][0]:
        return 'O'
    elif p_state[0][1][1] == i_state[0][1][1] and p_state[0][1][0] > i_state[0][1][0]:
        return 'L'
    elif p_state[0][1][1] == i_state[0][1][1] and p_state[0][1][0] < i_state[0][1][0]:
        return 'R'
    else:  # should never get to here
        return None


def return_neighbors(state: list):
    old_empty_field = state[0][1]  # list[0,0]
    key_old_empty_field = 0
    neighbours = []
    combs_x = [0, 1, 0, -1]
    combs_y = [1, 0, -1, 0]

    for new in range(4):  # here all 4 possible new states from the current one are created, some are not valid however
        new_empty_field = [old_empty_field[0] + combs_x[new], old_empty_field[1] + combs_y[new]]
        try:
            key_new_empty_field = [k for k in range(9) if state[k][1] == new_empty_field][0]
            new_state = copy.deepcopy(state)
            new_state[0][1] = new_empty_field
            new_state[key_new_empty_field][1] = old_empty_field
            neighbours.append(sorted(new_state))
        except IndexError:  # the newly created field does not exist, it's not valid and can be ignored
            continue

    return neighbours  # only valid neighbour states


def find_lowest_f(open_list):  # returns the Node with the lowest f-score out of the open list
    lowest_node = 0
    lowest_f_score = 9999999999999
    for node in open_list:
        node_f_score = node.get_f()
        if node_f_score < lowest_f_score:
            lowest_node = node
            lowest_f_score = node_f_score

    return lowest_node


def is_in(node: Node, t_list: list):  # checks if a Node with the exact state is already in the specified list
    node_state = node.get_state()
    for node_ob in t_list:
        if node_state == node_ob.get_state():
            return True
    return False
