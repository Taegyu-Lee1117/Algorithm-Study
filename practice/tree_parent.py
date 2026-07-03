"""트리의 부모 찾기 (Silver)

1번 정점을 루트로 하는 트리가 주어진다. 2번부터 N번 정점까지 각 부모를 구한다.

입력: N / N-1개의 간선
"""

from collections import deque
import sys


def solve() -> None:
    input = sys.stdin.readline
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    parent = [0] * (n + 1)
    parent[1] = -1
    queue = deque([1])
    while queue:
        node = queue.popleft()
        for child in graph[node]:
            if parent[child] == 0:
                parent[child] = node
                queue.append(child)
    print("\n".join(map(str, parent[2:])))


if __name__ == "__main__":
    solve()
