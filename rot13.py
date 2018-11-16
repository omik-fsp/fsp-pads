# CAESARS CIPHER IN PYTHON: MY TWO WAYS


# 1st way: Similar path I followed in FCC JS challenge:
def rot13(strToDecode):

    output = ''

    for charInStr in strToDecode:

        # Lets store the current char Number
        charN = ord(charInStr)

        # Lets add + 13 to the char in each loop
        if charN >= 65:
            charN += 13

        # If we are over 90 then substract 26 (again +13 from original)
        if charN > 90:
            charN -= 26

        output = output + chr(charN)

    print(output)


# 2nd way: With Python codecs lib, easy and for the entire family!
def rot13v2(strToDecode):
    import codecs

    result = codecs.decode(strToDecode, 'rot_13')
    print(result)


rot13("SERR PBQR PNZC")
rot13v2('JVGU YVOF VF GBB RNFL QHHHQR!')
