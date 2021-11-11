#answer
def solution(array, commands):
    answer = []
    for i in commands:
        result = array[i[0]-1:i[1]]
        result.sort()
        answer.append(result[i[2]-1])
    return answer

#참고용 만든코드 
arr = list(map(int,input().split()))
commands = list(map(int,input().split()))
result = arr[commands[0]-1:commands[1]]
result.sort()
print(result[commands[2]-1])

#sort 함수는 리스트명.sort( ) 형식으로 "리스트형의 메소드"​​이며 리스트 원본값#을 직접 수정합니다.

#sorted 함수는 sorted( 리스트명 ) 형식으로 "내장 함수"이며 리스트 원본 값은 #그대로이고 정렬 값을 반환합니다.
#결국 이말은 s_result =sorted(result) 처럼 값을 저장해야하며 result.sort()는 result를 아예 정렬하는것이다 .
