# python3

import sys
import threading
import numpy

def compute_height(n, parents):
    heights = [0] * n
    root = -1
    for i in range(n):
        if parents[i] == -1:
            root = i
    def dfs(node):
        nonlocal heights
        for child in range(n):
            if parents[child] == node:
                if heights[child] == 0:
                    dfs(child)
                heights[node] = max(heights[node], heights[child] + 1)
    dfs(root)
    return heights[root]

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    height = compute_height(n, parents)
    print(height)

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()