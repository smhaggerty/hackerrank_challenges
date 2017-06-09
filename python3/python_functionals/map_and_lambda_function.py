cube = lambda x: x**3 # complete the lambda function
def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    fib_list = [0, 1]
    for next_index in range(2,n):
        fib_list.append(fib_list[next_index-1] + fib_list[next_index-2])
    return fib_list

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
