"""최소 배달 비용 (Gold)

N개 도시와 M개의 단방향 버스가 있다. 출발 도시에서 도착 도시까지 필요한
최소 비용을 구한다. 두 도시 사이에 여러 버스가 있을 수 있다.

입력: N / M / M개의 시작 도착 비용 / 출발 도착
"""

import heapq
import sys


def solve() -> None:
    input = sys.stdin.readline
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    for _ in range(int(input())):
        start, end, cost = map(int, input().split())
        graph[start].append((end, cost))
    start, target = map(int, input().split())

    distance = [10**18] * (n + 1)
    distance[start] = 0
    heap = [(0, start)]
    while heap:
        cost, node = heapq.heappop(heap)
        if cost != distance[node]:
            continue
        if node == target:
            break
        for nxt, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < distance[nxt]:
                distance[nxt] = new_cost
                heapq.heappush(heap, (new_cost, nxt))
    print(distance[target])


if __name__ == "__main__":
    solve()
