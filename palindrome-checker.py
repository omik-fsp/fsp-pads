# Palindrome checker using Python's slice notation
# https://stackoverflow.com/questions/509211/understanding-pythons-slice-notation/509295#509295


def palindrome(str):

    toCompare = ''

    # casefold() Returns a version of the string suitable for caseless comparisons.
    str = str.casefold()

    # strip all non alphanumerics
    for char in str:
        if char.isalnum():
            toCompare = toCompare + char

    # compare to reverse
    if toCompare == toCompare[::-1]:
        print(toCompare + ': A palindrome')
    else:
        print(toCompare + ': Not a palindrome')


palindrome('RFfeS')
palindrome('amor a roma')
palindrome('Was it a car or a cat I saw?')
