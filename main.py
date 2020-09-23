import sys
from Node import Node
from Search import UninformedSearch

def get_state(state_string):
    return [int(num) for num in state_string]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise IOError("Need input argument for starting state E.g. 'python main.py 120843765'")
    initial_state = get_state(sys.argv[1])
    start_node = Node(initial_state)
    start_node.visualize(message="Initial state")

    uninformed = UninformedSearch(start_node)
    # states, actions = uninformed.depth_first()
    # states, actions = uninformed.depth_limited(2)
    states, actions = uninformed.iterative_deepening()
    print(states)
    print(actions)
    