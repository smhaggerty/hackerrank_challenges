if __name__ == '__main__':
    s = input()
    test_dict = {'alnum':[False, lambda x: x.isalnum()],
                 'alpha':[False, lambda x: x.isalpha()],
                 'digit':[False, lambda x: x.isdigit()],
                 'lower':[False, lambda x: x.islower()],
                 'upper':[False, lambda x: x.isupper()]}

    def testChar(char, test):
        if test[1](char):
            test[0] = True
    def hasAttribute(attribute):
        return test_dict[attribute][0]

    for char in s:
        for test in test_dict:
            testChar(char, test_dict[test])

    for attribute in sorted(test_dict):
        print(hasAttribute(attribute))
