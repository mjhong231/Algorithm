import sys
input = sys.stdin.readline


N = int(input())
lst = sorted(list(map(int, input().split())))

three = []

zero = float('inf')  # 숫자값 최소 갱신 변수


for i in range(N-2):  # i는 기준 용액이므로 범위 N-2까지
    mark = lst[i]
    left_mark = i + 1
    right_mark = N - 1

    while left_mark < right_mark:
        sum_v = mark + lst[left_mark] + lst[right_mark]
        if abs(sum_v) <= abs(zero):
            three = [mark, lst[left_mark], lst[right_mark]]  # three 갱신
            zero = sum_v = mark + lst[left_mark] + lst[right_mark]

        if sum_v < 0:  # 합이 0보다 작으면 left 마크 이동
            left_mark += 1

        elif sum_v > 0:  # 합이 0보다 크면 right 마크 이동
            right_mark -= 1

        else:     # 합이 0 이면 정답
            print(*three)
            sys.exit()

print(*three)







