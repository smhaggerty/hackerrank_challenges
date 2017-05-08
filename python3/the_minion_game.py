def minion_game(string):
    # initialize scores and list of values
    vowels = ['A', 'E', 'I', 'O', 'U']
    stuart_score = 0
    kevin_score = 0
    # iterate through string, checking if the current character starts with a
    # vowel or consonant. Then, consider the substring from the current element
    # to the end of the string. Add the length of this substring to the score to
    # account for permutations of the string.
    # Ex: 'CANADA' => 'CANADA', 'CANAD', 'CANA', 'CAN', 'CA', 'C'
    for i in range(len(string)):
        if string[i] in vowels:
            kevin_score += len(string) - i
        else:
            stuart_score += len(string) - i
# compare scores and print the winner
    if stuart_score > kevin_score:
        print('Stuart',stuart_score)
    elif kevin_score > stuart_score:
        print('Kevin',kevin_score)
    else: print('Draw')
