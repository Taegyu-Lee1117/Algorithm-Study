"""두 마을로 나누기 (Gold)

N개의 집과 M개의 양방향 도로가 있다. 모든 집이 연결되도록 일부 도로를 고른 뒤
도로 하나를 제거해 두 마을로 나눈다. 남는 도로 유지비의 최솟값을 구한다.

입력: N M / M개의 집A 집B 비용
"""

import sys


def solve() -> None:
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    edges.sort(key=lambda edge: edge[2])
    parent = list(range(n + 1))

    def find(node: int) -> int:
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    total = 0
    largest = 0
    selected = 0
    for a, b, cost in edges:
        root_a, root_b = find(a), find(b)
        if root_a == root_b:
            continue
        parent[root_b] = root_a
        total += cost
        largest = cost
        selected += 1
        if selected == n - 1:
            break
    print(total - largest)


if __name__ == "__main__":
    solve()
