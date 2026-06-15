"""연구실 방어 (Gold)

0은 빈칸, 1은 벽, 2는 바이러스인 N×M 연구실이 주어진다.
빈칸 세 곳에 새 벽을 세운 뒤 바이러스가 퍼지지 않는 칸의 최댓값을 구한다.

입력: N M / 연구실 N줄
"""

from collections import deque
from itertools import combinations
import sys


def solve() -> None:
    input = sys.stdin.readline
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    empty = [(r, c) for r in range(n) for c in range(m) if board[r][c] == 0]
    viruses = [(r, c) for r in range(n) for c in range(m) if board[r][c] == 2]
    answer = 0

    for walls in combinations(empty, 3):
        copied = [row[:] for row in board]
        for row, col in walls:
            copied[row][col] = 1
        queue = deque(viruses)
        while queue:
            row, col = queue.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, col + dc
                if 0 <= nr < n and 0 <= nc < m and copied[nr][nc] == 0:
                    copied[nr][nc] = 2
                    queue.append((nr, nc))
        answer = max(answer, sum(row.count(0) for row in copied))
    print(answer)


if __name__ == "__main__":
    solve()
