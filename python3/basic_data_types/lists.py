if __name__ == '__main__':
    list_methods = {
        'insert': lambda lst, index, integer: lst.insert(index, integer),
        'print': lambda lst: print(lst),
        'remove': lambda lst, integer: lst.remove(integer),
        'append': lambda lst, integer: lst.append(integer),
        'sort': lambda lst: lst.sort(),
        'pop': lambda lst: lst.pop(),
        'reverse': lambda lst: lst.reverse()
    }

    def getMethod(command):
        return list_methods[command[0]]

    def getArguments(command):
        return [int(command[i]) for i in range(1, len(command))]

    n = int(input())
    lst = []
    commands = [input().split() for i in range(n)]

    for command in commands:
        method = getMethod(command)
        arguments = getArguments(command)
        method(lst, *arguments)
