"""트리 거리 질의 (Gold)

가중치가 있는 N개 정점의 트리가 주어진다. 두 정점 사이의 거리 M개를 출력한다.

입력: N / N-1개의 A B 가중치 / M / M개의 A B
"""

from collections import deque
import sys


def solve() -> None:
    input = sys.stdin.readline
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b, weight = map(int, input().split())
        graph[a].append((b, weight))
        graph[b].append((a, weight))

    log = n.bit_length()
    parent = [[0] * (n + 1) for _ in range(log)]
    depth = [-1] * (n + 1)
    distance = [0] * (n + 1)
    depth[1] = 0
    queue = deque([1])
    while queue:
        node = queue.popleft()
        for nxt, weight in graph[node]:
            if depth[nxt] != -1:
                continue
            depth[nxt] = depth[node] + 1
            distance[nxt] = distance[node] + weight
            parent[0][nxt] = node
            queue.append(nxt)

    for level in range(1, log):
        for node in range(1, n + 1):
            parent[level][node] = parent[level - 1][parent[level - 1][node]]

    def lca(a: int, b: int) -> int:
        if depth[a] < depth[b]:
            a, b = b, a
        difference = depth[a] - depth[b]
        for level in range(log):
            if difference & (1 << level):
                a = parent[level][a]
        if a == b:
            return a
        for level in range(log - 1, -1, -1):
            if parent[level][a] != parent[level][b]:
                a = parent[level][a]
                b = parent[level][b]
        return parent[0][a]

    answer = []
    for _ in range(int(input())):
        a, b = map(int, input().split())
        ancestor = lca(a, b)
        answer.append(str(distance[a] + distance[b] - 2 * distance[ancestor]))
    print("\n".join(answer))


if __name__ == "__main__":
    solve()
