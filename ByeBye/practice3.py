# 문제: 연속 출석 보너스

# 학생의 출석 기록이 문자열로 주어진다.

# O : 출석
# X : 결석

# 연속으로 출석한 날이 길수록 점수를 더 받는다.

# 점수 규칙:

# O가 나오면 현재 연속 출석 수만큼 점수 추가
# X가 나오면 연속 출석 수는 0으로 초기화

# ex) records = "OOXOOO"
# 1 + 2 + 0 + 1 + 2 + 3 = 9


def solution(records):
    score = 0
    count = 0

    for r in records:
        if r == "O":
            count += 1
            score += count
        else:
            count = 0

    return score


print(solution("OOXOOO"))  # 9
print(solution("OXOXO"))   # 3
print(solution("OOOO"))    # 10