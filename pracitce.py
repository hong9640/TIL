cur_pieces = list(map(int, input().split()))
correct_pieces = [1, 1, 2, 2, 2, 8]
result = []
for i in range(6):
    result.append(correct_pieces[i] - cur_pieces[i])
print(*result)