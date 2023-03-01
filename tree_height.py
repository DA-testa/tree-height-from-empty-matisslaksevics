# python3

import sys
import threading
import numpy
def compute_height(n, parents):
    depths = [0] * n
    def compute_depth(node):
        if depths[node] != 0:
            return depths[node]
        if parents[node] == -1:
            depths[node] = 1
        else:
            depths[node] = compute_depth(parents[node]) + 1
        return depths[node]
    max_depth = 0
    for i in range(n):
        depth = compute_depth(i)
        if depth > max_depth:
            max_depth = depth
    return max_depth
def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))
    pass
sys.setrecursionlimit(10**7) 
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))