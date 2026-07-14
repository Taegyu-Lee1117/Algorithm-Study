"""파이프 옮기기 (Gold)

N×N 집에서 1은 벽, 0은 빈칸이다. 처음 파이프는 (1,1)-(1,2)를 차지한다.
가로·세로·대각선 규칙에 따라 파이프 끝을 (N,N)으로 옮기는 방법 수를 구한다.

입력: N / 집 상태 N줄
"""

import sys


def solve() -> None:
    input = sys.stdin.readline
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
    dp[0][1][0] = 1

    for row in range(n):
        for col in range(2, n):
            if board[row][col] == 1:
                continue
            dp[row][col][0] += dp[row][col - 1][0] + dp[row][col - 1][2]
            if row > 0:
                dp[row][col][1] += dp[row - 1][col][1] + dp[row - 1][col][2]
                if board[row - 1][col] == 0 and board[row][col - 1] == 0:
                    dp[row][col][2] += sum(dp[row - 1][col - 1])
    print(sum(dp[n - 1][n - 1]))


if __name__ == "__main__":
    solve()
