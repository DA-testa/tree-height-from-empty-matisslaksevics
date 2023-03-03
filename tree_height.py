import sys
import threading
import numpy as np

def compute_height(parents):
    children = [[] for _ in range(len(parents))]
    for i, parent in enumerate(parents):
        if parent == -1:
            root = i
        else:
            children[parent].append(i)
    def height(node):
        if len(children[node]) == 0:
            return 1
        else:
            return 1 + max(height(child) for child in children[node])
    return height(root)
def main():
    n = int(input())
    parents = np.fromstring(input(), dtype=int, sep=' ')
    print(compute_height(parents))
#threading.stack_size(2**27)
#sys.setrecursionlimit(10**7)
#thread = threading.Thread(target=main).start()