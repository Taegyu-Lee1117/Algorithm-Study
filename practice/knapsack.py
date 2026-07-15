"""제한 무게 배낭 (Gold)

N개의 물건은 각각 무게와 가치가 있다. 각 물건을 최대 한 번 선택할 수 있을 때,
총 무게가 K 이하인 조합의 최대 가치를 구한다.

입력: N K / N개의 무게 가치
"""

import sys


def solve() -> None:
    input = sys.stdin.readline
    n, limit = map(int, input().split())
    dp = [0] * (limit + 1)

    for _ in range(n):
        weight, value = map(int, input().split())
        for current in range(limit, weight - 1, -1):
            dp[current] = max(dp[current], dp[current - weight] + value)
    print(dp[limit])


if __name__ == "__main__":
    solve()
