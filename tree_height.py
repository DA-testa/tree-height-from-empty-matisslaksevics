import sys
import threading
import numpy

def compute_height(n, parents):
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
    text = input()
    if 'I' in text:
        n = int(input())
        parents = numpy.array(list(map(int, input().split())))
        print(compute_height(n, parents))

    if 'F' in text:
        filename = input()
        filename = "test/" + filename
        if 'a' not in filename:
            try:
                with open(filename, "r") as file:
                    n = int(file.readline())
                    parents = numpy.array(list(map(int, file.readline().split())))
                    print(compute_height(n, parents))
            except:
                return "File not found"
# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
