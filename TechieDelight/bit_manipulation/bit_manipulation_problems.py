

# Check if a given integer is even or odd
# Odd = True
# Even = False
def isOdd(value):
    return 1 if value & 1 else 0


# Detect if two integers have opposite signs or not
def isOpposite(a, b):
    return 1 if (a ^ b) < 0 else 0


# Add 1 to a given integer
def addOne(value):
    # Invert bits and use twos complement
    return -~value


