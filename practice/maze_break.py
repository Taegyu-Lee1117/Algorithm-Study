"""한 번 부수는 미로 (Gold)

0은 빈칸, 1은 벽인 N×M 격자에서 (1, 1)부터 (N, M)까지 이동한다.
벽을 최대 한 번 부술 수 있을 때 지나가는 칸 수의 최솟값을 구한다.
도달할 수 없으면 -1을 출력한다.

입력: N M / 공백 없는 격자 N줄
"""

from collections import deque
import sys


def solve() -> None:
    input = sys.stdin.readline
    n, m = map(int, input().split())
    board = [input().strip() for _ in range(n)]
    distance = [[[-1, -1] for _ in range(m)] for _ in range(n)]
    distance[0][0][0] = 1
    queue = deque([(0, 0, 0)])

    while queue:
        row, col, broken = queue.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = row + dr, col + dc
            if not (0 <= nr < n and 0 <= nc < m):
                continue
            next_broken = broken + (board[nr][nc] == "1")
            if next_broken > 1 or distance[nr][nc][next_broken] != -1:
                continue
            distance[nr][nc][next_broken] = distance[row][col][broken] + 1
            queue.append((nr, nc, next_broken))

    candidates = [d for d in distance[n - 1][m - 1] if d != -1]
    print(min(candidates) if candidates else -1)


if __name__ == "__main__":
    solve()
