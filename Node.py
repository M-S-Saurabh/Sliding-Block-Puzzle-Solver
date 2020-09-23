from enum import Enum

class Actions(Enum):
    UP = "Up"
    DOWN = "Down"
    RIGHT = "Right"
    LEFT = "Left"

class Node:
    state = []
    goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    parent = None
    parent_action = None
    path_cost = 0
    actions = []
    __grid_size = 3

    def child_node(self, action):
        if action not in self.actions:
            raise ValueError('Invalid Action! Allowed actions are:'+str(self.actions))
        new_state = self.state.copy()
        zero_index = self.state.index(0)
        offset_dict = {Actions.UP:3, Actions.DOWN:-3, Actions.LEFT:1, Actions.RIGHT:-1}
        offset = offset_dict[action]
        # Swap 0 with the element at offset
        new_state[zero_index], new_state[zero_index + offset] = new_state[zero_index + offset], new_state[zero_index]
        return Node.fromParent(new_state, self, action)

    def get_string(self):
        return "".join(map(str, self.state))

    def is_goalstate(self):
        return self.state == self.goal_state

    def __init__(self, state, goal_state=None):
        super().__init__()
        self.state = state
        if goal_state is not None:
            self.goal_state = goal_state.copy()
        self.validateActions()

    @classmethod
    def fromParent(cls, state, parent, parent_action, edge_cost=1):
        node = cls(state)
        node.parent = parent
        node.parent_action = parent_action
        node.goal_state = parent.goal_state
        node.path_cost = parent.path_cost + edge_cost
        return node

    def validateActions(self):
        # Using a list instead of a set() to maintain the same order every time search is called.
        self.actions = [action for action in Actions]
        # Remove actions which are not possible in this state
        zero_index = self.state.index(0)
        if(zero_index <= 2):
            self.actions.remove(Actions.DOWN)
        if(zero_index%3 == 0):
            self.actions.remove(Actions.RIGHT)
        if(zero_index%3 == 2):
            self.actions.remove(Actions.LEFT)
        if(zero_index >= 6):
            self.actions.remove(Actions.UP)

    def manhattan_distance(self):
        manhattan = 0
        for index, tile in enumerate(self.state):
            goal_index = self.goal_state.index(tile)
            row_diff = abs(goal_index//3 - index//3)
            col_diff = abs(goal_index - index) % 3
            manhattan += (row_diff + col_diff)
        return manhattan

    def num_wrong_tiles(self):
        wrong_tiles = 0
        for tile, goal_tile in zip(self.state, self.goal_state):
            if goal_tile != tile: wrong_tiles += 1
        return wrong_tiles

    def visualize(self, details=False, message=None):
        if message is not None:
            print('---',message,'---')
        else:
            print("--------------")
        size = 0
        while size < len(self.state):
            print(self.state[size : size+self.__grid_size])
            size += self.__grid_size
        if details:
            print("path_cost: ", self.path_cost)
            print("parent: ", self.parent.state)
            print("actions: ", self.actions)

# To test the Node class, run this file like 'python Node.py'
if __name__ == "__main__":
    parentNode = Node([1, 2, 0, 8, 4, 3, 7, 6, 5])
    parentNode.visualize()
    
    childNode = parentNode.child_node(Actions.UP)
    childNode.visualize()

    childNode = childNode.child_node(Actions.RIGHT)
    childNode.visualize()

    print("is goal state:", childNode.is_goalstate())
    