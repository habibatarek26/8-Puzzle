import heapq
import math
import sys


class PuzzleState:
    def __init__(self, state_str, moves=0, previous=None, heuristic_type='manhattan'):
        self.state_str = state_str
        self.moves = moves
        self.previous = previous
        self.heuristic_type = heuristic_type

    def __lt__(self, other):
        return self.f() < other.f()

    def __eq__(self, other):
        return self.state_str == other.state_str

    def f(self):
        return self.moves + self.heuristic()

    def get_zero_position(self):
        pos = self.state_str.index('0')
        return divmod(pos, 3)

    def heuristic(self):
        if self.heuristic_type == 'manhattan':
            return self.manhattan_distance()
        elif self.heuristic_type == 'euclidean':
            return self.euclidean_distance()
        return 0

    def manhattan_distance(self):
        total_distance = 0
        for i, digit in enumerate(self.state_str):
            if digit != '0':
                current_row, current_col = divmod(i, 3)
                target_value = int(digit)
                target_row, target_col = divmod(target_value, 3)
                total_distance += abs(target_row - current_row) + abs(target_col - current_col)
        return total_distance

    def euclidean_distance(self):
        total_distance = 0
        for i, digit in enumerate(self.state_str):
            if digit != '0':
                current_row, current_col = divmod(i, 3)
                target_value = int(digit)
                target_row, target_col = divmod(target_value, 3)
                total_distance += math.sqrt((target_row - current_row) ** 2 + (target_col - current_col) ** 2)
        return total_distance

    def get_neighbors(self):
        neighbors = []
        zero_idx = self.state_str.index('0')
        row, col = divmod(zero_idx, 3)

        moves = [
            (-1, 0) if row > 0 else None,
            (1, 0) if row < 2 else None,
            (0, -1) if col > 0 else None,
            (0, 1) if col < 2 else None
        ]

        for move in moves:
            if move is None:
                continue

            new_row = row + move[0]
            new_col = col + move[1]
            new_idx = new_row * 3 + new_col

            new_state_list = list(self.state_str)
            new_state_list[zero_idx], new_state_list[new_idx] = new_state_list[new_idx], new_state_list[zero_idx]
            new_state_str = ''.join(new_state_list)

            neighbors.append(PuzzleState(
                new_state_str,
                self.moves + 1,
                self,
                self.heuristic_type
            ))

        return neighbors


def board_to_string(board):
    return ''.join(str(cell) for row in board for cell in row)


def string_to_board(state_str):
    return [[int(state_str[i * 3 + j]) for j in range(3)] for i in range(3)]


def a_star(initial_board, heuristic_type='manhattan'):
    initial_state_str = board_to_string(initial_board)
    initial_state = PuzzleState(initial_state_str, 0, None, heuristic_type)

    open_set = []
    heapq.heappush(open_set, initial_state)
    closed_set = set()

    while open_set:
        current_state = heapq.heappop(open_set)

        if current_state.state_str == "012345678":
            path = []
            while current_state:
                path.append(current_state.state_str)
                current_state = current_state.previous
            return path[::-1], len(path) - 1

        if current_state.state_str in closed_set:
            continue

        closed_set.add(current_state.state_str)

        for neighbor in current_state.get_neighbors():
            if neighbor.state_str not in closed_set:
                heapq.heappush(open_set, neighbor)

    return None, 0


