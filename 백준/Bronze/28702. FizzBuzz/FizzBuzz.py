strings = [input().strip() for _ in range(3)]
 
# 가장 마지막 숫자 찾기 
for i in range(2, -1, -1):
    # 인덱스를 기준으로 세 문자열 다음에 올 숫자 찾기
    if strings[i].isdigit():
        answer = int(strings[i]) + (3-i)
        break      
        
# 조건에 맞추어 출력
if answer % 15 == 0:
    print('FizzBuzz')
elif answer % 3 == 0:
    print('Fizz')
elif answer % 5 == 0:
    print('Buzz')
else:
    print(answer)