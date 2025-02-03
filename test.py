import requests

URL = 'https://fakestoreapi.com/carts' #요청주소소
data = requests.get(URL)
# 출력결과 : <Response [200]>
# [200]: 웹의 응답 코드 -> 정상적으로 응답함.
# [404]: 웹의 응답 코드 -> 알 수 없는 주소로 요청했다.
print(data)
