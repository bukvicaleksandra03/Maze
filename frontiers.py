from collections import deque
import heapq
import itertools
from maze import Node

class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier():
    def __init__(self):
        self.frontier = deque()
        
    def add(self, node):
        self.frontier.append(node)
        
    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)
    
    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier.popleft()
            return node
        
class HeapFrontier():
    def __init__(self, goal):
        self.frontier = []
        self.goal = goal
        self.counter = itertools.count()
        
    def calculate_dist_to_goal(self, node: Node) -> int:
        return abs(node.state[0] - self.goal[0]) + abs(node.state[1] - self.goal[1])
        
    def add(self, node: Node):
        count = next(self.counter)
        heapq.heappush(self.frontier, (node.num_steps + self.calculate_dist_to_goal(node), count, node))
        
    def empty(self):
        return len(self.frontier) == 0
    
    def contains_state(self, state):
        return any(node.state == state for dist, count, node in self.frontier)

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            dist, count, node = heapq.heappop(self.frontier)
            return node