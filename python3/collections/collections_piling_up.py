for case in range(int(input())):
    numOfCubes = int(input())
    blockList = [int(i) for i in input().split()]
    haltIndex = 0
    haltIndexRight = len(blockList)

    while haltIndex < haltIndexRight - 1 and blockList[haltIndex] >= blockList[haltIndex+1]:
        haltIndex += 1
    while haltIndex < haltIndexRight - 1 and blockList[haltIndex] <= blockList[haltIndex + 1]:
        haltIndex += 1

    if haltIndex == haltIndexRight - 1:
        print('Yes')
    else:
        print('No')
