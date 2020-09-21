class Node:
    state = [1, 2, 0, 8, 4, 3, 7, 6, 5]
    parent = None
    path_cost = 0
    actions = {'R', 'L', 'U', 'D'}
    grid_size = 3

    def child_node(self, action):
        if action not in self.actions:
            raise ValueError('Invalid Action! Allowed actions are:'+str(self.actions))
        new_state = self.state.copy()
        zero_index = self.state.index(0)
        offset_dict = {'U':3, 'D':-3, 'L':1, 'R':-1}
        offset = offset_dict[action]
        # Swap 0 with the element at offset
        new_state[zero_index], new_state[zero_index + offset] = new_state[zero_index + offset], new_state[zero_index]
        return Node.withParent(new_state, self)

    def is_goalstate(self):
        return self.state == [1, 2, 3, 8, 0, 4, 7, 6, 5]

    def get_pathcost(self):
        # TODO
        return 1

    def __init__(self):
        super().__init__()
        self.validateActions()

    @classmethod
    def withParent(cls, state, parent, edge_cost=1):
        node = cls()
        node.state = state
        node.parent = parent
        node.validateActions()

        if edge_cost is None:
            node.path_cost = get_pathcost(node.state)
        else:
            node.path_cost = parent.path_cost + edge_cost
        return node

    def validateActions(self):
        self.actions = {'R', 'L', 'U', 'D'}
        # Remove actions which are not possible in this state
        zero_index = self.state.index(0)
        if(zero_index <= 2):
            self.actions.remove('D')
        if(zero_index%3 == 0):
            self.actions.remove('R')
        if(zero_index%3 == 2):
            self.actions.remove('L')
        if(zero_index >= 6):
            self.actions.remove('U')

    def visualize(self, details=False):
        print("--------------")
        size = 0
        while size < len(self.state):
            print(self.state[size : size+self.grid_size])
            size += self.grid_size
        if details:
            print("path_cost: ", self.path_cost)
            print("parent: ", self.parent.state)
            print("actions: ", self.actions)

# To test the Node class, run this file like 'python Node.py'
if __name__ == "__main__":
    parentNode = Node()
    parentNode.visualize()
    
    childNode = parentNode.child_node('U')
    childNode.visualize()

    childNode = childNode.child_node('R')
    childNode.visualize()

    print("is goal state:", childNode.is_goalstate())
    