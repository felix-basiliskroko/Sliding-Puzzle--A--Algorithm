class Node:  # each Node represents one state of the Puzzle
    def __init__(self, state: list, g_score: int, h_score: int, f_score: int, prev_node):
        self.state = sorted(state)
        self.g_score = g_score
        self.h_score = h_score
        self.f_score = f_score
        self.prev_node = prev_node

    def get_g(self):
        return self.g_score

    def get_h(self):
        return self.h_score

    def get_f(self):
        return self.f_score

    def get_state(self):
        return self.state

    def get_prev_node(self):
        return self.prev_node

    def set_g(self, score):
        self.g_score = score

    def set_h(self, score):
        self.h_score = score

    def set_f(self, score):
        self.f_score = score