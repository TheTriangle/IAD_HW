firstalphabet = set()
secondaplhabet = set()

newline = input()
curalph = 1
while newline:
    if curalph == 1:
        firstalphabet.update(set(newline))
        curalph = 2
    else:
        secondaplhabet.update(set(newline))
        curalph = 1
    newline = input()

if len(firstalphabet) > len(secondaplhabet):
    print("Mumbo")
else:
    print("Jumbo")
