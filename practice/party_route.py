"""왕복 파티 길 (Gold)

N개 마을 사이에 M개의 단방향 도로가 있다. 모든 학생은 X번 마을의 파티에
갔다가 자신의 마을로 돌아온다. 왕복 최단 시간이 가장 긴 학생의 시간을 구한다.

입력: N M X / M개의 시작 도착 시간
"""

import heapq
import sys


def dijkstra(start: int, graph: list[list[tuple[int, int]]]) -> list[int]:
    distance = [10**18] * len(graph)
    distance[start] = 0
    heap = [(0, start)]
    while heap:
        cost, node = heapq.heappop(heap)
        if cost != distance[node]:
            continue
        for nxt, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < distance[nxt]:
                distance[nxt] = new_cost
                heapq.heappush(heap, (new_cost, nxt))
    return distance


def solve() -> None:
    input = sys.stdin.readline
    n, m, party = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    reverse = [[] for _ in range(n + 1)]
    for _ in range(m):
        start, end, time = map(int, input().split())
        graph[start].append((end, time))
        reverse[end].append((start, time))

    back = dijkstra(party, graph)
    go = dijkstra(party, reverse)
    print(max(go[node] + back[node] for node in range(1, n + 1)))


if __name__ == "__main__":
    solve()
