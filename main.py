import sys, time
from Node import Node
from Search import UninformedSearch, InformedSearch

def get_state(state_string):
    return [int(num) for num in state_string]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise IOError("Need input argument for starting state E.g. 'python main.py 120843765'")
    initial_state = get_state(sys.argv[1])
    start_node = Node(initial_state)
    start_node.visualize(message="Initial state")
    print()

    uninformed_search = UninformedSearch(start_node)
    # states, actions = uninformed_search.depth_first()
    # states, actions = uninformed_search.depth_limited(2)
    start_time = time.time()
    states, actions = uninformed_search.iterative_deepening()
    iddfs_time = (time.time() - start_time)
    print("IDDFS solution (path length:{}, time taken:{} secs):".format(len(actions), iddfs_time))
    print(actions)
    print()

    informed_search = InformedSearch(start_node)
    start_time = time.time()
    states, actions = informed_search.astar('manhattan_distance')
    manhattan_time = (time.time() - start_time)
    print("A-star (manhattan) solution (path length:{}, time taken:{} secs):".format(len(actions), manhattan_time))
    print(actions)
    print()

    informed_search = InformedSearch(start_node)
    start_time = time.time()
    states, actions = informed_search.astar('num_wrong_tiles')
    wrong_tiles_time = (time.time() - start_time)
    print("A-star (num_wrong_tiles) solution (path length:{}, time taken:{} secs):".format(len(actions), wrong_tiles_time))
    print(actions)
    