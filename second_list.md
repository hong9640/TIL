### 2차원 배열 ###
1. 배열 선언
- 1차원 리스트를 묶어놓은 리스트
- 세로길이, 가로길이를 필요로 한다.
2. 배열 순회
- 행 우선순회를 가장 먼저 이해해야 한다.
- 기본적으로 행의 개수는 len(arr), 열 개수는 len(arr[0])이다.
- 열의 개수가 저 코드가 나오는 이유는 [0]번 인덱스의 길이가 1,2,3,4 이면 세로로 총 4열이 나오기 때문이다.
- 행 우선순위와 열 우선순위를 바꾸고 싶으면 행과 열의 for문 위치를 서로 바꾸기만 하면 된다. 다만 출력은 그대로 arr[i][j] 이때 i는 N, j 는 M 이다.
- 역-행 우선순회가 있는데 이는 각 행을 끝 인엑스부터 0인덱스까지 역순으로 순회한다.
- for i in range(N):
    - M-1부터 0까지 거꾸로 순회
    for j in range(M - 1, -1, -1):
        print(arr[i][j])
        이런식으로 진행
- 역-열 우선 순회는 열 인덱스를 끝에서 부터 0까지 감소시키며, 행 인덱스를 0부터 N-1까지 증가시키며 순회.
- for j in range(M - 1, -1, -1):  
    - for i in range(N):
        - print(arr[i][j])

- 지그재그 배열은 행은 그대로 두고 두번째 행은 열이 역순으로 가게 작성
- ex) f(array[i][j + (m-1-2*j) * (i%2)])
3. 델타
- 2차원 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법
- 미리 방향 벡터(델타 배열)을 정의해 둔다.  
- 상(`row - 1`, `col`)
- 하(`row + 1`, `col`)
- 좌(`row`, `col - 1`)
- 우(`row`, `col + 1`
- 가운데를 3*3배열에서 정 가운데를 (i,j)로 두고 오른쪽부터 시계방향으로 돌아간다. 다만, 상하좌우로 돌아가도 상관은 없다.

- 십자 방향으로 돈다고 생각하면 된다. 
- 코드를 보다가 if 0 <= N and 0 <=nj<N 이 코드는 벽 체크인데 코드가 인덱스 범위를 벗어나지 않도록 한다.
- 위의 코드에서 < N 이렇게 된 이유는 마지막 인덱스는 (n-1, n-1)이기 때문이다.
- 또한 파이썬은 음수 인덱스를 지원한다. 그래서 오류가 발생하지 않고 자신이 원하지 않는 동작을 할 수 있으므로 벽체크가 필요하다.
- 벽을 넘어서면 무시 
  - if nr < 0 or nr >= N or nc < 0 or nc >= M:
    continue
- 범위 내에서만 실행  
  - if 0 <= nr < N and 0 <= nc < M:
    print(matrix[nr][nc])
- 벽 체크는 무조건 들어간다. 델타 쓰면 무조건 들어감!
- 대각선을 이동할 수 도 있는데 
- 델타의 난이도는 if 문이 많아질 때 높아진다. 
1. 전치행렬
- 3*3행렬이 있을 때 사전을 기준으로 사선은 그대로 두고 양 옆을 서로 자리를 바꾸는 행렬
- 대각선의 원소를 구할 때는 i == j 이렇게
- i<j냐 그 반대냐에 따라 선택되는 영역이 다름.
1. 부분집합 
- 유한 개의 정수로 이루어진 집합이 있을 때, 이 집합의 부분집합 중에서 그 집합의 원소를 모두 더한 값이 0이 되는 경우가 있는 지를 알아내는 문제
  1. 비트연산자
- & : 비트 단위로 and 연산
- | 비트 단위로 or 연산
- << 피연산자의 비트 열을 왼쪽으로 이동시킨다. 
- '>>' 피연산자의 비트 열을 오른쪽으로 이동시킨다.
- 부분집합 -> 만약 1,2,3,4 이렇게 있으면 정수의 개수를 n개라 했을 때 
- n**2 - 1 이렇게.
  
> [정리]  
> 2차원 배열을 생성할 때는 주소 공유 문제에 주의해야 하며, 
파이썬에서는 [[0]*M for _ in range(N)]를 권장한다.