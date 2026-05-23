"""구간 합 질의 (Silver)

N개의 정수와 M개의 구간 [L, R]이 주어진다.
각 구간에 포함된 수의 합을 한 줄씩 출력한다.

입력: N M / 수열 / M개의 L R (1-indexed)
"""

import sys


def solve() -> None:
    input = sys.stdin.readline
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    prefix = [0] * (n + 1)
    for i, value in enumerate(numbers, 1):
        prefix[i] = prefix[i - 1] + value

    answer = []
    for _ in range(m):
        left, right = map(int, input().split())
        answer.append(str(prefix[right] - prefix[left - 1]))
    print("\n".join(answer))


if __name__ == "__main__":
    solve()
