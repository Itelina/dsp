# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    """
    if count < 10:
        print 'Number of donuts:' + str(int(count))
    else:
        print 'Number of donuts: many'
    """
    raise NotImplementedError


def both_ends(s):
    """
    if len(str(s)) >= 2:
        newstring = str(s)[:2] + str(s)[-2:]
        print newstring
    else:
        print ""
    """
    raise NotImplementedError


def fix_start(s):
    """
    b = s[0]
    for i in range(1, len(s)):
       if s[i] == s[0]:
           b += '*' 
       else:
           b += s[i]
   print b
   """
    raise NotImplementedError


def mix_up(a, b):
    """
    def mix_up(a, b):
    first = list(a)
    second = list(b)
    x = first[0:2] 
    y = second[0:2]
    first[0:2] = y
    second[0:2] = x
    print ''.join(first) + ' ' + ''.join(second)
    """
    raise NotImplementedError


def verbing(s):
    """
    if len(s) >=3:
        if s[-3:] == 'ing':
            s += 'ly'
        else:
            s += 'ing'
    print s
    """
    raise NotImplementedError


def not_bad(s):
    """
    import re
    if re.search("not.*bad", s):
       print s[0:re.search("not.*bad", s).start()] + "good" + s[(re.search("not.*bad", s).end()):]
    else:
       print s
    """
    raise NotImplementedError


def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    raise NotImplementedError
