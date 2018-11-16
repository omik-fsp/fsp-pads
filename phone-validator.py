# Phone Number (US) Validator.

def telephoneCheck(phoneToCheck):
    import re
    
    '''
      Disecting regex:

      (1)?                # Valid US Code (optional)
      ([ -])?             # First separator (optional)
      (\(\d{3}\)|\d{3})   # Area code with or whitout ( )
      ([ -])?             # Second separator (opt)
      (\d{3})             # Three digits
      ([ -])?             # Third separator (opt)
      (\d{4})             # Final four digits
    '''

    myRegex = re.compile(r'^(1)?([ -])?(\(\d{3}\)|\d{3})([ -])?(\d{3})([ -])?(\d{4})$')

    if myRegex.search(phoneToCheck):
        print(phoneToCheck + ': Seems like a phone! OK')
    else:
        print(phoneToCheck + ': Doesn\'t look like anything to me')


telephoneCheck("1 (555) 55-5555")
