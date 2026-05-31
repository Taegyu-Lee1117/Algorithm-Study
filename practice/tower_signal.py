"""왼쪽 신호탑 (Gold)

높이가 서로 다를 수 있는 N개의 탑이 왼쪽을 향해 신호를 보낸다.
각 탑의 신호를 처음 수신하는, 자신보다 높거나 같은 왼쪽 탑의 번호를 출력한다.
수신하는 탑이 없으면 0을 출력한다.

입력: N / 탑 높이 N개
"""

import sys


def solve() -> None:
    input = sys.stdin.readline
    n = int(input())
    heights = list(map(int, input().split()))
    stack = []
    answer = []

    for index, height in enumerate(heights, 1):
        while stack and stack[-1][1] < height:
            stack.pop()
        answer.append(stack[-1][0] if stack else 0)
        stack.append((index, height))
    print(*answer)


if __name__ == "__main__":
    solve()
