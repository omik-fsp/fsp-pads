# Palindrome checker using Python's slice notation
# https://stackoverflow.com/questions/509211/understanding-pythons-slice-notation/509295#509295


def palindrome(stringToCheck):

    toCompare = ''

    # casefold() Returns a version of the string suitable for caseless comparisons.
    # strip all non alphanumerics
    for char in stringToCheck.casefold():
        if char.isalnum():
            toCompare = toCompare + char

    # compare to reverse
    if toCompare == toCompare[::-1]:
        print(stringToCheck + ': A palindrome')
    else:
        print(stringToCheck + ': Not a palindrome')


palindrome('RFfeS')
palindrome('amor a roma')
palindrome('Was it a car or a cat I saw?')
