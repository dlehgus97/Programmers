#정답 
def solution(s):
    center = int(len(s)//2)
    if len(s)%2 == 0:
        return s[center-1:center+1]
    else:
        return s[center]

#참고로 만든코드 
word = input()

if len(word) %2 == 0:
  center = len(word) // 2
  print(word[center-1:center+1])
elif len(word) % 2 != 0:
  center = len(word) // 2
  print(word[center])
