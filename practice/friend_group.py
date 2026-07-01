"""친구 그룹 질의 (Gold)

N명이 처음에는 서로 다른 그룹에 있다. 친구 관계를 합치는 명령과 두 사람이
같은 그룹인지 묻는 명령을 처리한다.

입력: N M / M개의 명령(0 A B는 합치기, 1 A B는 확인)
출력: 확인 명령마다 YES 또는 NO
"""

import sys


def solve() -> None:
    input = sys.stdin.readline
    n, m = map(int, input().split())
    parent = list(range(n + 1))
    size = [1] * (n + 1)

    def find(node: int) -> int:
        while node != parent[node]:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    answer = []
    for _ in range(m):
        command, a, b = map(int, input().split())
        root_a, root_b = find(a), find(b)
        if command == 1:
            answer.append("YES" if root_a == root_b else "NO")
        elif root_a != root_b:
            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a
            parent[root_b] = root_a
            size[root_a] += size[root_b]
    print("\n".join(answer))


if __name__ == "__main__":
    solve()
