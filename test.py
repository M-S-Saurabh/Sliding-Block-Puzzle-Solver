import random, time
import numpy as np
from Node import Node
from Search import UninformedSearch, InformedSearch
import matplotlib.pyplot as plt

def generate_start_node():
    node = Node([1, 2, 3, 8, 0, 4, 7, 6, 5])
    explored_set = set()
    for step in range(31):
        explored_set.add(node.get_string())
        while(node.get_string() in explored_set):
            action = random.choice(node.actions)
            node = node.child_node(action)
    return Node(node.state.copy())

def plot_bar_chart(iddfs_times, astar_times):
    N = len(iddfs_times)

    fig, ax = plt.subplots()

    ind = np.arange(N)    # the x locations for the groups
    width = 0.35         # the width of the bars
    p1 = ax.bar(ind, iddfs_times, width)
    p2 = ax.bar(ind + width, astar_times, width)

    ax.set_title('Search times (secs) by algorithm')
    ax.set_xlabel('Random initial states')
    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels([str(index) for index in ind])

    ax.legend((p1[0], p2[0]), ('IDDFS', 'A-star'))
    ax.autoscale_view()
    plt.show()

if __name__ == "__main__":
    # start_node = Node([8,0,6,5,4,7,2,3,1], goal_state=[0,1,2,3,4,5,6,7,8]) # worst case TC
    iddfs_times = []
    astar_times = []
    random.seed(0)
    for test_case in range(30):
        print("Test case #", test_case)
        start_node = generate_start_node()
        start_node.visualize(message="Initial state")

        uninformed_search = UninformedSearch(start_node)
        start_time = time.time()
        states, actions = uninformed_search.iterative_deepening()
        iddfs_time = time.time() - start_time
        iddfs_times.append(iddfs_time)
        #print(states)
        print("IDDFS solution (length:{}, time:{}):".format(len(actions), iddfs_time))
        print(actions)

        informed_search = InformedSearch(start_node)
        start_time = time.time()
        states, actions = informed_search.astar('num_wrong_tiles')
        astar_time = time.time() - start_time
        astar_times.append(astar_time)
        # print(states)
        print("A star solution (length:{}, time:{}):".format(len(actions), astar_time))
        print(actions)
        print()

    print("iddfs times:", iddfs_times)
    print("astar times:", astar_times)
    plot_bar_chart(iddfs_times, astar_times)