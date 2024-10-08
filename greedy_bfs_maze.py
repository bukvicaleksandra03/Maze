from frontiers import StackFrontier
from maze import Maze, Node

class GreedyBFSMaze(Maze):
    def calculate_dist_to_goal(self, node: Node) -> int:
        return abs(node.state[0] - self.goal[0]) + abs(node.state[1] - self.goal[1])
    
    def solve(self):
        """Finds a solution to maze, if one exists.
            Using Greedy Best-First Search."""

        # Keep track of number of states explored
        self.num_explored = 0

        # Initialize frontier to just the starting position
        start = Node(state=self.start, parent=None, action=None)
        frontier = StackFrontier()
        frontier.add(start)

        # Initialize an empty explored set
        self.explored = set()

        # Keep looping until solution found
        while True:

            # If nothing left in frontier, then no path
            if frontier.empty():
                raise Exception("no solution")

            # Choose a node from the frontier
            node = frontier.remove()
            self.num_explored += 1

            # If node is the goal, then we have a solution
            if node.state == self.goal:
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return

            # Mark node as explored
            self.explored.add(node.state)

            # Add neighbors to frontier
            neighbors_dist = []
            for action, state in self.neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    dist_to_goal = self.calculate_dist_to_goal(child)
                    neighbors_dist.append((child, dist_to_goal))
            
            neighbors_dist.sort(key=lambda x: x[1], reverse=True)

            # We are pushing nodes with the greatest distance to goal to the stack first
            for child, dist_to_goal in neighbors_dist:
                frontier.add(child)