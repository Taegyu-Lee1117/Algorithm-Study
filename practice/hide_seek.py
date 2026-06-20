"""순간 이동 추적 (Gold)

수빈이는 위치 N에서 K로 이동한다. x→2x는 0초, x→x-1과 x→x+1은 1초다.
K에 도착하는 최소 시간을 구한다. 위치 범위는 0 이상 100000 이하이다.

입력: N K
"""

from collections import deque
import sys


def solve() -> None:
    start, target = map(int, sys.stdin.readline().split())
    limit = 100_000
    distance = [10**9] * (limit + 1)
    distance[start] = 0
    queue = deque([start])

    while queue:
        current = queue.popleft()
        for nxt, cost in ((current * 2, 0), (current - 1, 1), (current + 1, 1)):
            if 0 <= nxt <= limit and distance[nxt] > distance[current] + cost:
                distance[nxt] = distance[current] + cost
                if cost == 0:
                    queue.appendleft(nxt)
                else:
                    queue.append(nxt)
    print(distance[target])


if __name__ == "__main__":
    solve()
