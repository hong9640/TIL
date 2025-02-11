arr = list(map(int, input().split()))
for i in range(len(arr)-1):
    if arr[i] > arr[i + 1]:
        print("YES")
    elif arr[i] == 0 and arr[i + 1] == 0:
        pass
    elif arr[i] <= arr[i + 1]:
        print("NO")