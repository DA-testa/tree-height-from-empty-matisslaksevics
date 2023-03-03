import sys
import threading
import numpy

def compute_height(n, parents):
    # First we create the tree as an array of lists
    tree = [[] for _ in range(n)]
    root = 0
    for i, parent in enumerate(parents):
        if parent == -1:
            root = i
        else:
            tree[parent].append(i)
    def height(node):
        if not tree[node]:
            return 1
        else:
            return 1 + max(height(child) for child in tree[node])

    return height(root)

def main():
    input_type = input("Enter input type - 'I' for keyboard or 'F' for file: ")
    if "I" in input_type:
        n = int(input("Nodes: "))
        parents = numpy.array(list(map(int, input("Parents: ").split())))
        print(compute_height(n, parents))
    if "F" in input_type:
        filename = input("Enter filename (without extension): ")# File name not allowed to have 'a'
        filename = "test/" + filename
        if 'a' not in filename:
            try:
                with open(f"./{filename}.txt") as f:
                    n = int(input("Nodes: "))
                    parents = numpy.array(list(map(int, input("Parents: ").split())))
                    print(compute_height(n, parents))
            except:
                return "Not found"
# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
