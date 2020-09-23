from collections import deque
from Node import Node

class MyException(Exception):
    '''Raising my own exception to handle depth limited search max depth reached conditions'''

class UninformedSearch:
    def __init__(self, start_node: Node):
        super().__init__()
        self.start_node = start_node

    def path_to_goal(self, goal):
        states = []
        actions = []
        while goal.parent is not None:
            states.append(goal.get_string())
            actions.append(goal.parent_action.value)
            goal = goal.parent
        states.reverse()
        actions.reverse()
        return states, actions

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
                    return self.path_to_goal(newNode)
                frontier.append(newNode)
        print("DepthFirstSearch failed to reach the given goal state.")
        return [], []

    def depth_limited(self, max_depth):
        frontier = deque()
        frontier.append((self.start_node, 0))
        max_depth_reached = False

        while(len(frontier) > 0):
            top, depth = frontier.pop()
            if(depth >= max_depth):
                max_depth_reached = True
                continue
            
            for action in top.actions:
                newNode = top.child_node(action)
                if newNode.is_goalstate():
                    return self.path_to_goal(newNode)
                frontier.append((newNode, depth+1))
        if max_depth_reached:
            raise MyException('Maximum Depth reached while searching. Try again with bigger max_depth.')
        else:
            print("DepthLimitedSearch failed to reach the given goal state.")
            return [], []

    def iterative_deepening(self, stop_depth=25):
        depth = 1
        while depth:
            if(depth > stop_depth): break
            try:
                print("Running depth limited search with depth= ", depth)
                states, actions = self.depth_limited(depth)
            except MyException as e:
                depth += 1
                continue
            return states, actions
        print("Stopped deepening search after stop_depth is reached. Current stop_depth= ", stop_depth)
        return [], []
            
class InformedSearch:
    valid_metrics = ('manhattan_distance', 'num_wrong_tiles')

    def astar(self, distance_metric='manhattan_distance'):    
        if distance_metric not in self.valid_metrics:
            raise ValueError('Invalid distance metric specified. Valid metrics are:', self.valid_metrics)
        # TODO
