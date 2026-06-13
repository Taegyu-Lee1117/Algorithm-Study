"""비가 와도 안전한 곳 (Silver)

지역의 높이가 N×N 격자로 주어진다. 비의 높이 이하인 칸은 잠긴다.
가능한 모든 비의 높이에 대해 잠기지 않은 연결 영역 수의 최댓값을 구한다.

입력: N / 높이 격자 N줄
"""

from collections import deque
import sys


def solve() -> None:
    input = sys.stdin.readline
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    answer = 1

    for rain in range(max(map(max, board))):
        visited = [[False] * n for _ in range(n)]
        areas = 0
        for row in range(n):
            for col in range(n):
                if visited[row][col] or board[row][col] <= rain:
                    continue
                areas += 1
                visited[row][col] = True
                queue = deque([(row, col)])
                while queue:
                    cr, cc = queue.popleft()
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and board[nr][nc] > rain:
                            visited[nr][nc] = True
                            queue.append((nr, nc))
        answer = max(answer, areas)
    print(answer)


if __name__ == "__main__":
    solve()
