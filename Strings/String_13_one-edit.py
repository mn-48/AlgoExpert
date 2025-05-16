# O(n) Time | O(1) Space
def oneEdit(stringOne, stringTwo):
    lengthOne, lengthTwo = len(stringOne), len(stringTwo)
    if abs(lengthOne - lengthTwo) > 1:
        return False

    madeEdit = False
    idxOne = 0
    idxTwo = 0

    while idxOne < lengthOne and idxTwo < lengthTwo:
        if stringOne[idxOne] != stringTwo[idxTwo]:
            if madeEdit:
                return False
            madeEdit = True
            if lengthOne > lengthTwo:
                idxOne += 1
            elif lengthTwo > lengthOne:
                idxTwo += 1
            else:
                idxOne += 1
                idxTwo += 1
        else:
            idxOne += 1
            idxTwo += 1
    return True
