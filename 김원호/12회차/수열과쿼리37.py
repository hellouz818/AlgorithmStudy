import sys
import math

input = sys.stdin.readline


class Node:
    def __init__(self):
        self.odd_num = 0
        self.even_num = 0

    def change_value(self, x):
        if x:
            self.odd_num += 1
            self.even_num -= 1
        else:
            self.odd_num -= 1
            self.even_num += 1
        if self.p != self:
            self.p.change_value(x)

    def __str__(self):
        return f"{self.odd_num}, {self.even_num} |"


N = int(input())
A = [int(x) for x in input().split()]
M = int(input())

x = math.ceil(math.log2(N)) + 1
x = 2 ** x
nodes = [Node() for _ in range(x)]
nodes[0].p = nodes[0]
empty = Node()
for i, node in enumerate(nodes):
    if i * 2 + 1 < x:
        node.left = nodes[i * 2 + 1]
        node.left.p = node
    else:
        node.left = empty
    if i * 2 + 2 < x:
        node.right = nodes[i * 2 + 2]
        node.right.p = node
    else:
        node.right = empty

leaves = []
for a, node in zip(A, nodes[- x // 2:]):
    node.odd_num = a & 1
    node.even_num = node.odd_num ^ 1
    leaves.append(node)
for node in nodes[::-1]:
    left = node.left
    right = node.right
    if left == empty:
        continue
    node.odd_num = left.odd_num + right.odd_num
    node.even_num = left.even_num + right.even_num

for _ in range(M):
    q, l, r = map(int, input().split())
    if q == 1:
        r = r & 1
        leaf = leaves[l - 1]
        if r != leaf.odd_num:
            leaf.change_value(r)
    elif q == 2:
        value = 0
        l = leaves[l - 1]
        r = leaves[r - 1]
        while l != r:
            if l == l.p.right:
                value -= l.p.left.even_num
            if r == r.p.left:
                value -= r.p.right.even_num
            l = l.p
            r = r.p
        value += l.even_num
        print(value)
    elif q == 3:
        value = 0
        l = leaves[l - 1]
        r = leaves[r - 1]
        while l != r:
            if l == l.p.right:
                value -= l.p.left.odd_num
            if r == r.p.left:
                value -= r.p.right.odd_num
            l = l.p
            r = r.p
        value += l.odd_num
        print(value)
