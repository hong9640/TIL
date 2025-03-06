'''
재귀로 1-10까지 있는 리스트에서 합이 10인 부분집합의 갯수를 구해라.
'''
def sum_subset(idx, num_sum):
    global result

    if num_sum == 10:
        result += 1

    # 백트해킹 // 가지치기
    if num_sum >= 10:
        return
    # if idx == N:
    #     if num_sum == 10:
    #         result += 1
    #     return
    sum_subset(idx + 1, num_sum + arr[idx])
    sum_subset(idx + 1, num_sum)

N = 10
arr = [1,2,3,4,5,6,7,8,9,10]
result = 0
sum_subset(0, 0)
print(result)