_, hotelPatronList = input(), input().split()
roomNumbers = set()
patrons = set()
# iterate through the list of patron's room numbers, adding unseen room numbers
# to the set of room numbers for each group. Since there is only one captains
# room, at the end of the traversal the captains room number will be missing
# from the set of patrons.
for patron in hotelPatronList:
    if patron in roomNumbers:
        patrons.add(patron)
    else:
        roomNumbers.add(element)
# print the difference of the two sets, which is the captains room numbers
print(list(roomNumbers.difference(patrons))[0])
