"""두 수의 합 (Silver)

서로 다른 N개의 정수 중 두 수를 골라 합이 X가 되는 쌍의 수를 구한다.

입력: N / 정수 N개 / X
"""

import sys


def solve() -> None:
    input = sys.stdin.readline
    n = int(input())
    numbers = sorted(map(int, input().split()))
    target = int(input())
    left, right = 0, n - 1
    count = 0

    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            count += 1
            left += 1
            right -= 1
        elif total < target:
            left += 1
        else:
            right -= 1
    print(count)


if __name__ == "__main__":
    solve()
