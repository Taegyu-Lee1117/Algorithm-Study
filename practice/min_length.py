"""가장 짧은 연속 구간 (Gold)

양의 정수 N개가 주어질 때 합이 S 이상인 연속 구간의 최소 길이를 구한다.
그런 구간이 없으면 0을 출력한다.

입력: N S / 정수 N개
"""

import sys


def solve() -> None:
    input = sys.stdin.readline
    n, target = map(int, input().split())
    numbers = list(map(int, input().split()))
    left = 0
    current = 0
    answer = n + 1

    for right, value in enumerate(numbers):
        current += value
        while current >= target:
            answer = min(answer, right - left + 1)
            current -= numbers[left]
            left += 1
    print(0 if answer == n + 1 else answer)


if __name__ == "__main__":
    solve()
