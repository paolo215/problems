#Number letter counts

a = {
        0 : "zero",
        1 : "one",
        2 : "two",
        3 : "three",
        4 : "four",
        5 : "five",
        6 : "six",
        7 : "seven",
        8 : "eight",
        9 : "nine",
        10 : "ten",
        11 : "eleven",
        12 : "twelve",
        13 : "thirteen",
        14 : "fourteen",
        15 : "fifteen",
        16 : "sixteen",
        17 : "seventeen",
        18 : "eighteen",
        19 : "nineteen",
        20 : "twenty",
        30 : "thrity",
        40 : "forty",
        50 : "fifty",
        60 : "sixty",
        70 : "seventy",
        80 : "eighty",
        90 : "ninety",
        100 : "hundred",
        1000 : "onethousand"
    }

def tens(n):
    if n <= 20:
        return a[n]
    z = n % 10
    if z != 0:
        return a[n-(n%10)] + a[n%10]
    else:
        return a[n-(n%10)]

def convert(n):
    if n <= 20:
        return tens(n)
    elif n <= 99:
        return tens(n)
    elif n == 100:
        return "one" + a[100]
    elif n <= 999:
        z = n%100
        if z != 0:
            return a[n / 100] + a[100] + "and" + tens(n % 100)
        else:
            return a[n / 100] + a[100]
    elif n == 1000:
        return a[1000]

print sum([len(str(convert(f))) for f in range(1, 1001)])







