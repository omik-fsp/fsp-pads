'''
HOW TO FORM NUMBERS:

- When a symbol appears after a larger (or equal) symbol it is added

VI = V + I = 5 + 1 = 6
LXX = L + X + X = 50 + 10 + 10 = 70

- But if the symbol appears before a larger symbol it is subtracted
IV = V − I = 5 − 1 = 4
IX = X − I = 10 − 1 = 9

- Do not use a symbol more than three times in a row

HOW TO CONVERT TO ROMAN (iex. 1984):

- Break 1984 into 1000, 900, 80 and 4, then do each conversion

1000 = M
900 = CM
80 = LXXX
4 = IV

1000 + 900 + 80 + 4 = 1984, so 1984 = MCMLXXXIV 
'''


def convertToRoman(num):
    romanDict = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100,
                 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    origNum = num
    result = ''

    for i in romanDict:
        while num >= romanDict[i]:
            result = result + i
            num = num - romanDict[i]

    return result


print(convertToRoman(20))
print(convertToRoman(2018))
