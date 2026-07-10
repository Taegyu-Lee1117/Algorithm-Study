"""가장 긴 증가 수열 (Gold)

N개의 정수 중 일부를 순서대로 골라 엄격히 증가하는 부분 수열을 만든다.
가능한 최대 길이를 구한다.

입력: N / 정수 N개
"""

from bisect import bisect_left
import sys


def solve() -> None:
    input = sys.stdin.readline
    int(input())
    numbers = map(int, input().split())
    tails = []
    for value in numbers:
        index = bisect_left(tails, value)
        if index == len(tails):
            tails.append(value)
        else:
            tails[index] = value
    print(len(tails))


if __name__ == "__main__":
    solve()
