from queue import Queue
import queue
import time
from typing import List, Set

class BFSAgent:
    def __init__(self, initial_State):
        self.explored = set()
        self.path = []
        self.parent = {}
        self.goal = 12345678
        self.initial_State = self.prepare_initial_State(initial_State)

    def get_children(self, state: int) -> list[tuple[int, str]]:
        children = []
        state = str(state)
        if len(state) != 9:
            state = '0' + state
        zero_index = state.index('0')
        if zero_index != 0 and zero_index != 1 and zero_index != 2:
            children.append((int(self.swap(state, zero_index, zero_index - 3)),'UP'))
        if zero_index != 6 and zero_index != 7 and zero_index != 8:
            children.append((int(self.swap(state, zero_index, zero_index + 3)),'DOWN'))
        if zero_index != 0 and zero_index != 3 and zero_index != 6:
            children.append((int(self.swap(state, zero_index, zero_index - 1)),"LEFT"))
        if zero_index != 2 and zero_index != 5 and zero_index != 8:
            children.append((int(self.swap(state, zero_index, zero_index + 1)),"RIGHT"))
        return children
    
    def swap(self, state: str, i: int, j: int) -> str:
        state = list(state)
        state[i], state[j] = state[j], state[i]
        return ''.join(state)
    
 
    def get_path(self, state: int):
        if state not in self.parent:
            return
        self.get_path(self.parent[state][0])  
        self.path.append((state, self.parent[state][1])) 

    def prepare_initial_State(self ,initial_State : list[list[int]]) -> int:
        k = 8
        intial = 0
        for i in range(3):
            for j in range(3):
                intial += initial_State[i][j] * (10 ** k)
                k -= 1
        return intial
    
    def BFS (self):
        start_time = time.time()
        frontier_set = set()
        frontier = Queue()
        frontier.put(self.initial_State)
        frontier_set.add(self.initial_State)
        parent ={}
        while(not frontier.empty()):
            state = frontier.get()
            self.explored.add(state)
            if state== self.goal:
                self.get_path(state)
                end_time = time.time()
                return self.path , len(self.path), len(self.explored) , end_time-start_time
            
            children = self.get_children(state)
            for child in children:
                if child[0] not in self.explored and child[0] not in frontier_set:
                    frontier.put(child[0])
                    frontier_set.add(child[0])
                    self.parent[child[0]] = (state,child[1])
        end_time = time.time()
       
        return None , None, None,end_time-start_time





l = BFSAgent(
[[1, 2, 3],
 [4, 5, 6],
 [7, 0, 8]]
)
res =l.BFS()
print("SOLVABLE")
print("path : " ,res[0])
print("cost : ",res[1])
print("expanded nodes : " ,res[2])
print("time elapsed : ",res[3])

k = BFSAgent(
[[2, 1, 3],
 [4, 5, 6],
 [7, 8, 0]]
)
res2= k.BFS()
print("UNSOLVABLE")
print("path : " ,res2[0])
print("cost : ",res2[1])
print("expanded nodes : " ,res2[2])
print("time elapsed : ",res2[3])