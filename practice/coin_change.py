"""동전 최소 개수 (Silver)

N종류의 동전을 각각 원하는 만큼 사용할 수 있다. 가치의 합을 K로 만드는 데 필요한
동전의 최소 개수를 구한다. 만들 수 없으면 -1을 출력한다.

입력: N K / 동전 가치 N줄
"""

import sys


def solve() -> None:
    input = sys.stdin.readline
    n, target = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    dp = [target + 1] * (target + 1)
    dp[0] = 0
    for coin in coins:
        for value in range(coin, target + 1):
            dp[value] = min(dp[value], dp[value - coin] + 1)
    print(-1 if dp[target] == target + 1 else dp[target])


if __name__ == "__main__":
    solve()
