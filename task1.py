def morecommon(a, b, n):
    firstdivs = 0
    seconddivs = 0
    for i in a:
        if i % n == 0:
            firstdivs += 1
    for i in b:
        if i % n == 0:
            seconddivs += 1
    if firstdivs > seconddivs:
        return True
    return False

a = (3, 5, 6, 7, 8, 9)
b = (4, 5, 7, 8, 20, 21)
print(morecommon(a, b, 3))