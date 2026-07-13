"""행렬 곱셈 순서 (Gold)

순서가 고정된 N개의 행렬이 주어진다. 행렬 곱셈의 결합 순서를 정해 필요한
스칼라 곱셈 횟수의 최솟값을 구한다.

입력: N / 각 행렬의 행 열 N줄
"""

import sys


def solve() -> None:
    input = sys.stdin.readline
    n = int(input())
    matrices = [tuple(map(int, input().split())) for _ in range(n)]
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            dp[start][end] = min(
                dp[start][mid]
                + dp[mid + 1][end]
                + matrices[start][0] * matrices[mid][1] * matrices[end][1]
                for mid in range(start, end)
            )
    print(dp[0][n - 1])


if __name__ == "__main__":
    solve()
