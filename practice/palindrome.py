"""회문 구간 질의 (Gold)

N개의 정수 수열과 M개의 구간 [S, E]가 주어진다. 각 구간이 앞뒤가 같은 수열이면
1, 아니면 0을 출력한다.

입력: N / 수열 / M / M개의 S E (1-indexed)
"""

import sys


def solve() -> None:
    input = sys.stdin.readline
    n = int(input())
    numbers = [0] + list(map(int, input().split()))
    palindrome = [[False] * (n + 1) for _ in range(n + 1)]

    for index in range(1, n + 1):
        palindrome[index][index] = True
    for index in range(1, n):
        palindrome[index][index + 1] = numbers[index] == numbers[index + 1]
    for length in range(3, n + 1):
        for start in range(1, n - length + 2):
            end = start + length - 1
            palindrome[start][end] = numbers[start] == numbers[end] and palindrome[start + 1][end - 1]

    answer = []
    for _ in range(int(input())):
        start, end = map(int, input().split())
        answer.append("1" if palindrome[start][end] else "0")
    print("\n".join(answer))


if __name__ == "__main__":
    solve()
