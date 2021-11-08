def solution(a, b):
    month = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ];
    day = [ "THU", "FRI", "SAT" ,"SUN", "MON","TUE", "WED" ];
    result =b
    for i in range(a-1):
        result +=month[i]
    return day[result%7]
