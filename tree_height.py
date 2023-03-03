import sys
import threading
import numpy as np

sys.setrecursionlimit(10**7)

def compute_height(parents):
    # create an empty list of children for each node
    children = [[] for _ in range(len(parents))]
    
    # populate the children list
    for i, parent in enumerate(parents):
        if parent == -1:
            root = i
        else:
            children[parent].append(i)
    
    # define a recursive function to compute the height of the tree
    def height(node):
        if len(children[node]) == 0:
            return 1
        else:
            return 1 + max(height(child) for child in children[node])
    
    return height(root)

def main():
    # read input from user
    n = int(input())
    parents = np.fromstring(input(), dtype=int, sep=' ')
    
    # compute and print the height of the tree
    print(compute_height(parents))
    
# use threading to increase the stack size and avoid RecursionError for large inputs
threading.stack_size(2**27)
thread = threading.Thread(target=main)
thread.start()
