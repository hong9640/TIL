# '''
# [1,2,3]집합의 모든 부분집합을 반복문으로 생성
# '''
# selected = [0] * 3
# for i in range(2):
#     selected[0] = i
#     for j in range(2):
#         selected[1] = j
#         for m in range(2):
#             selected[2] = m
#             subset = []
#             for n in range(3):
#                 # 0은 선택안한 것, 1은 선택한 것.
#                 if selected[n] == 1:
#                     subset.append(n + 1)
#             print(subset)

'''
재귀로 풀기
'''
# 3개 사용 위치
def creatue_subset(depth, included):
    if depth == len(input_list):
        cnt_subset = [input_list[i] for i in range(len(input_list)) if included[i]]
        subsets.append(cnt_subset)
        return
    
    included[depth] = False
    creatue_subset(depth + 1, included)

    included[depth] = True
    creatue_subset(depth + 1, included)

input_list = [1, 2, 3]
subsets = []
init_included = [False] * len(input_list)
creatue_subset(0, init_included)
print(subsets)