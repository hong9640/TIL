# 패턴 매칭 중 고지식한 알고리즘 for문
# for

# t = 'A pattern matching algorithm'
# p = 'rithm'
#
# M = len(p) # 찾을 패턴의 길이
# N = len(t) # 전체 텍스트의 길이
#
# def brute_force_for(p, t):
#     N = len(t)
#     M = len(p)
#
#     # 시작 위치 컨트롤
#     for i in range(N-M+1):
#         cnt = 0
#         for j in range(M):
#             if t[i+j] == p[j]:
#                 cnt += 1
#             else:
#                 break
#
#         if cnt == M:
#             return i
#     return -1
#
# print(brute_force_for(p, t))

# 패턴 매칭 중 while 문
# while

t = 'A pattern matching algorithm'
p = 'rithm'

M = len(p) # 찾을 패턴의 길이
N = len(t) # 전체 텍스트의 길이

def brute_force_while(p, t):
    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    # i와 j는 전부 범위 내의 인덱스   
    while j < M and i < N:
        # 두개가 서로 다르면
        if t[i] != p[j]:
            # t열의 시작인덱스에서 바로 다음 인덱스로 변경
            i = i - j
            # j는 원점으로
            j = 0
        else:
            i += 1
            j += 1
    #
    if j == M:
        return i - M # 검색 성공
    else:
        return -1 # 검색 실패

print(brute_force_while(p, t))