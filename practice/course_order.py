"""선수 과목 순서 (Gold)

N개 과목과 M개의 선수 조건 A→B가 주어진다. 조건을 모두 지키는 수강 순서를
출력한다. 가능한 과목이 여러 개면 번호가 작은 과목을 먼저 선택한다.

입력: N M / M개의 A B
"""

import heapq
import sys


def solve() -> None:
    input = sys.stdin.readline
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for _ in range(m):
        before, after = map(int, input().split())
        graph[before].append(after)
        indegree[after] += 1

    heap = [node for node in range(1, n + 1) if indegree[node] == 0]
    heapq.heapify(heap)
    answer = []
    while heap:
        node = heapq.heappop(heap)
        answer.append(node)
        for nxt in graph[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                heapq.heappush(heap, nxt)
    print(*answer)


if __name__ == "__main__":
    solve()
