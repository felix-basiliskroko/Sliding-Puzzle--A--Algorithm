from Node import Node
from assist_functions import manhattan_dist, return_move_direction, return_neighbors, find_lowest_f, is_in


def a_star(input_state: list, final_state: list):
    # load input node in open list
    open_list = [Node(input_state, 0, 0, 0, [])]
    closed_list = []
    moves = []

    while True:
        node_with_lowest_f: Node = find_lowest_f(open_list)

        closed_list.append(node_with_lowest_f)  # add visited node to closed list
        open_list.remove(node_with_lowest_f)  # remove current node from open list

        if node_with_lowest_f.get_state() == final_state:
            # traverse and return path here...
            current_node = node_with_lowest_f
            current_node_state = node_with_lowest_f.get_state()

            prev_node = current_node.get_prev_node()
            prev_node_state = prev_node.get_state()

            moves.append(return_move_direction(prev_node_state, current_node_state))
            while True:
                current_node = prev_node
                current_node_state = current_node.get_state()

                prev_node = current_node.get_prev_node()
                if type(prev_node) != Node:  # if the previous node is the starting state we have reached the beginning
                    break
                prev_node_state = prev_node.get_state()

                moves.append(return_move_direction(prev_node_state, current_node_state))
            moves.reverse()  # reversed because we want the moves from start-->end not end-->start
            return moves

        neighbours = return_neighbors(node_with_lowest_f.get_state())  # returns all valid neighbours of the current
        # node

        for n in neighbours:
            g = node_with_lowest_f.get_g() + 1
            h = manhattan_dist(n, final_state)
            f = g + h

            n = Node(n, g, h, f, node_with_lowest_f)  # the new Node n
            if is_in(n, closed_list):  # neighbours that have already been looked at don't need to be considered again
                continue
            elif is_in(n, open_list):  # node already exists in open list, maybe the new path is shorter though
                match_in_open: Node = [x for x in open_list if x.get_state() == n.get_state()][0]  # find the
                # matching Node object in the open list

                new_g = node_with_lowest_f.get_g() + 1
                old_h = match_in_open.get_h()  # 'old_h' because nothing has changed concerning the heuristic
                new_f = new_g + old_h

                if new_f < match_in_open.get_f():
                    open_list[
                        [k for k in range(len(open_list) - 1) if open_list[k].get_state() == n.get_state()][0]] = n

            elif not is_in(n, open_list):
                open_list.append(n)


# Example input:
inp = [[0, [1, 2]], [1, [0, 1]], [2, [0, 2]],
       [3, [2, 2]], [4, [2, 1]], [5, [2, 0]],
       [6, [1, 1]], [7, [1, 0]], [8, [0, 0]]]

# Initialize final state
fin = [[0, [1, 1]], [1, [0, 2]], [2, [1, 2]],
       [3, [2, 2]], [4, [2, 1]], [5, [2, 0]],
       [6, [1, 0]], [7, [0, 0]], [8, [0, 1]]]


if __name__ == "__main__":
    print(a_star(inp, fin))
