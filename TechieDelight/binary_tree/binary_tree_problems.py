
def isIdentical(a, b):
    if a == None and b == None:
        return True

    if not any([a,b]):
        return False

    return a.getValue() == b.getValue() and (isIdentical(a.getLeft(), b.getLeft()) \
            and isIdentical(a.getRight(), a.getRight()))





  
