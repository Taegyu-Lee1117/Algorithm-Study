"""중요 문서 출력 (Silver)

문서마다 중요도가 있다. 큐의 맨 앞 문서보다 중요한 문서가 남아 있으면
맨 앞 문서를 뒤로 보낸다. 지정한 문서가 몇 번째로 출력되는지 구한다.

입력: T / 각 테스트의 N M / 중요도 N개
"""

from collections import deque
import sys


def solve() -> None:
    input = sys.stdin.readline
    answer = []
    for _ in range(int(input())):
        n, target = map(int, input().split())
        priorities = list(map(int, input().split()))
        queue = deque(enumerate(priorities))
        order = 0

        while queue:
            index, priority = queue.popleft()
            if any(other > priority for _, other in queue):
                queue.append((index, priority))
                continue
            order += 1
            if index == target:
                answer.append(str(order))
                break
    print("\n".join(answer))


if __name__ == "__main__":
    solve()
