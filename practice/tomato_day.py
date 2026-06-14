"""창고 숙성 날짜 (Silver)

M×N 창고에서 1은 익은 토마토, 0은 익지 않은 토마토, -1은 빈칸이다.
익은 토마토는 매일 상하좌우 토마토를 익게 한다. 모두 익는 최소 날짜를 구한다.
불가능하면 -1을 출력한다.

입력: M N / 창고 N줄
"""

from collections import deque
import sys


def solve() -> None:
    input = sys.stdin.readline
    m, n = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(n)]
    queue = deque((r, c) for r in range(n) for c in range(m) if box[r][c] == 1)

    while queue:
        row, col = queue.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = row + dr, col + dc
            if 0 <= nr < n and 0 <= nc < m and box[nr][nc] == 0:
                box[nr][nc] = box[row][col] + 1
                queue.append((nr, nc))

    if any(0 in row for row in box):
        print(-1)
    else:
        print(max(map(max, box)) - 1)


if __name__ == "__main__":
    solve()
