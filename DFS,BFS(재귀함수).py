# 반복적으로 구현한 n!

def factorial_iteractive(n):
    result = 1
    # 1부터 n까지의 수를 차례데로 입력하기
    for i in range(1, n+1):
        result *= i
    return result


# 재귀적으로 구현한 n!

def factorial_recursive(n):
    if n <= 1: # n이 1 이하인 경우 1을 반환
        return 1
    # n! = n * (n-1)!를 그대로 코드에 작성하기
    return n * factorial_recursive(n-1)

# 각각의 방식으로 구현한 n! 출력(n=5)
print('반복적으로 구현', factorial_iteractive(5))
print('반복적으로 구현', factorial_recursive(5))
