#coding=utf-8
import sys,os
sys.path.append(os.path.abspath(os.getcwd()))

"""convert to and from Roman numerals"""
import re
#Define exceptions
class RoamnError(Exception): pass
class OutOfRangeError(RoamnError):pass
class NotIntegerError(RoamnError):pass
class InvalidRomanNumeralError(RoamnError):pass

#Define digit mapping
romanNumeralMap = (
    ('M',1000),
    ('CM',900),
    ('D',500),
    ('CD',400),
    ('C',100),
    ('XC',90),
    ('L',50),
    ('XL',40),
    ('X',10),
    ('IX',9),
    ('V',5),
    ('IV',4),
    ('I',1)
)

def toRoman(n):
    """convert integer to Roman numeral"""
    if not(0<n<5000):
        raise OutOfRangeError,'number out of range, number must be 1...4999'
    if int(n) <>n:
        raise NotIntegerError,'non-integers can not be converted'

    result = ''
    for numeral,integer in romanNumeralMap:
        while n >=integer:
            result +=numeral
            n -=integer
    return result

#Define pattern to detect valid Roman numerals

#romanNumeralPattern = \
#    re.compile('^M?M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$')
#松散正则表达式
romanNumeralPattern = re.compile('''
    ^                  #beginning of string
    M{0,4}             #thousands - 0 to 4 M's
    (CM|CD|D?C?C?C?)  #hundreds - 900(CM),400(CD),0-300(0 to 3C's),
                            #or 500-800(D,followed by 0 to 3 C's)
    (XC|XL|L?X{0,3})  #tens - 90(XC),40(XL),0-30(0 to 3  X's),
                          #  or 50-80(L,followed by 0 to 3 X's)
    (IX|IV|V?I{0,3})  #ones - 9(IX),4(IV),0-3(0 to 3  I's),
                           # or 5-8(V,followed by 0 to 3 I's)
    $                  # end of string
    ''',re.VERBOSE)

def fromRoman(cls):
    """convert Roman numeral to integer"""
    if not cls:
        raise InvalidRomanNumeralError,'Input can not be blank'

    if not romanNumeralPattern.search(cls):
        raise InvalidRomanNumeralError,'Invalid Roman numeral:%s' % cls

    result = 0
    index = 0
    for numeral, integer in romanNumeralMap:
        while cls[index:index+len(numeral)] == numeral:
            result +=integer
            index +=len(numeral)

    return result
