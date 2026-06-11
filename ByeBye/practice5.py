# # 문제: 기능 개발

# 각 기능은 현재 진행률 `progresses`와 하루 개발 속도 `speeds`를 가진다.

# 기능은 앞에 있는 기능부터 순서대로 배포되어야 한다.

# 뒤에 있는 기능이 먼저 완성되더라도, 앞 기능이 완성되지 않으면 함께 배포될 수 없다.

# 각 배포마다 몇 개의 기능이 배포되는지 리스트로 반환하라.

# ## 예시

# ```python
# progresses = [93, 30, 55]
# speeds = [1, 30, 5]


def solution(progresses, speeds):
    answer = []

    days = []

    for p, s in zip(progresses, speeds):
        remain = 100 - p

        if remain % s == 0:
            days.append(remain // s)
        else:
            days.append(remain // s + 1)

    count = 1
    current_day = days[0]

    for i in range(1, len(days)):
        if days[i] <= current_day:
            count += 1
        else:
            answer.append(count)
            count = 1
            current_day = days[i]

    answer.append(count)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
# [2, 1]