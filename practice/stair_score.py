"""계단 점수 (Silver)

계단마다 점수가 있다. 한 번에 한 칸 또는 두 칸 오를 수 있지만 세 계단을 연속으로
밟을 수 없고 마지막 계단은 반드시 밟아야 한다. 얻는 점수의 최댓값을 구한다.

입력: N / 계단 점수 N줄
"""

import sys


def solve() -> None:
    input = sys.stdin.readline
    n = int(input())
    score = [0] + [int(input()) for _ in range(n)]
    if n == 1:
        print(score[1])
        return

    dp = [0] * (n + 1)
    dp[1] = score[1]
    dp[2] = score[1] + score[2]
    for stair in range(3, n + 1):
        dp[stair] = max(dp[stair - 2], dp[stair - 3] + score[stair - 1]) + score[stair]
    print(dp[n])


if __name__ == "__main__":
    solve()
