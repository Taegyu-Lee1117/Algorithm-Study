"""오른쪽 큰 수 (Gold)

수열의 각 원소마다 오른쪽에 있으면서 자신보다 큰 첫 번째 수를 출력한다.
존재하지 않으면 -1을 출력한다.

입력: N / 정수 N개
"""

import sys


def solve() -> None:
    input = sys.stdin.readline
    n = int(input())
    numbers = list(map(int, input().split()))
    answer = [-1] * n
    stack = []

    for index, value in enumerate(numbers):
        while stack and numbers[stack[-1]] < value:
            answer[stack.pop()] = value
        stack.append(index)
    print(*answer)


if __name__ == "__main__":
    solve()
