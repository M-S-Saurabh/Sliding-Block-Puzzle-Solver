from collections import deque
from queue import PriorityQueue
from Node import Node

from itertools import count

class MyException(Exception):
    '''Raising my own exception to handle depth limited search max depth reached conditions'''

class UninformedSearch:
    def __init__(self, start_node: Node):
        super().__init__()
        self.start_node = start_node

    def depth_first(self):
        frontier = deque()
        explored_set = set()

        frontier.append(self.start_node)
        while(len(frontier) > 0):
            top = frontier.pop()
            explored_set.add(top.get_string())

            for action in top.actions:
                newNode = top.child_node(action)
                if newNode.get_string() in explored_set:
                    continue
                if newNode.is_goalstate():
                    return newNode.path_to_goal()
                frontier.append(newNode)
        print("DepthFirstSearch failed to reach the given goal state.")
        return [], []

    def depth_limited(self, max_depth):
        frontier = deque()
        frontier.append((self.start_node, 0))
        explored_set = {}
        max_depth_reached = False

        while(len(frontier) > 0):
            top, depth = frontier.pop()
            explored_set[top.get_string()] = depth
            if(depth >= max_depth):
                max_depth_reached = True
                continue
            
            for action in top.actions:
                newNode = top.child_node(action)
                newNode_str = newNode.get_string()
                if newNode_str in explored_set and explored_set[newNode_str] < (depth+1):
                    continue
                if newNode.is_goalstate():
                    return newNode.path_to_goal()
                frontier.append((newNode, depth+1))
        if max_depth_reached:
            raise MyException('Maximum Depth reached while searching. Try again with bigger max_depth.')
        else:
            print("DepthLimitedSearch failed to reach the given goal state.")
            return [], []

    def iterative_deepening(self, stop_depth=31, verbose=False):
        depth = 1
        while depth:
            if(depth > stop_depth): break
            try:
                if verbose: print("Running depth limited search with depth=", depth)
                states, actions = self.depth_limited(depth)
            except MyException as e:
                depth += 1
                continue
            return states, actions
        print("Stopped deepening search after stop_depth is reached. Current stop_depth= ", stop_depth)
        return [], []
            
class InformedSearch:
    valid_metrics = ('manhattan_distance', 'num_wrong_tiles')
    def __init__(self, start_node: Node):
        super().__init__()
        self.start_node = start_node
        self.unique = count()

    def queue_push(self, pqueue, node, distance_metric):
        priority_value = getattr(node, distance_metric)() + node.path_cost
        pqueue.put((priority_value, next(self.unique), node))

    def astar(self, distance_metric='manhattan_distance'):    
        if distance_metric not in self.valid_metrics:
            raise ValueError('Invalid distance metric specified. Valid metrics are:', self.valid_metrics)
        
        frontier = PriorityQueue()
        explored_set = set()

        self.queue_push(frontier, self.start_node, distance_metric)
        while not frontier.empty():
            _, _, top = frontier.get()
            explored_set.add(top.get_string())
            if top.is_goalstate():
                return top.path_to_goal()
            for action in top.actions:
                newNode = top.child_node(action)
                if newNode.get_string() in explored_set:
                    continue
                self.queue_push(frontier, newNode, distance_metric)
        print("A-star search failed to reach the given goal state.")
        return [], []
