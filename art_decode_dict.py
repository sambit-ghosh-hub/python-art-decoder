# For standard font in art library it the third line of the number outpts are all unique
# Therefore it is enough to check only the third line to be able to decode the string.
# The only caveat is with 1 and 0 the identifying string of 1 is a subset ob identifying string of 0
# To get around it we just need to check for a matching 0 first, if it mathces we definately know its not 1 other wise we check for 1
# There is also the case of 4 which has a identifying string length of 8 which is more than the standard for all other numbers except 1
# This file stores the mapping from each identifying string to the number and the reverse mapping too.

standard_num_decode_dic = {
 '| | | |':'0',
 '| |':'1',
 '  __) |':'2',
 '  |_ \ ':'3',
 '| || |_ ':'4',
 '|___ \ ':'5',
 "| '_ \ ":'6',
 '   / / ':'7',
 ' / _ \ ':'8',
 '| (_) |':'9',
}

standard_num_decode_dic_rev = {
 '0':u'| | | |',
 '1':u'| |',
 '2':u'  __) |',
 '3':u'  |_ \ ',
 '4':u'| || |_ ',
 '5':u'|___ \ ',
 '6':u"| '_ \ ",
 '7':u'   / / ',
 '8':u' / _ \ ',
 '9':u'| (_) |',
}
