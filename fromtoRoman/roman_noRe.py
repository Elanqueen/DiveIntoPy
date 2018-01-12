#coding=utf-8
import sys,os
sys.path.append(os.path.abspath(os.getcwd()))

"""convert to and from Roman numerals
    此处，采用romantable取代正则表达式，提升代码运行速度
"""
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

#定义转换最大值
MAX_ROMAN_NUMERAL= 4999
toRomanTable = [None]
fromRomanTable = {}

def toRoman(n):
    """convert integer to Roman numeral"""
    if not(0<n<MAX_ROMAN_NUMERAL+1):
        raise OutOfRangeError,'number out of range, number must less than %s' % MAX_ROMAN_NUMERAL
    if int(n) <>n:
        raise NotIntegerError,'non-integers can not be converted'
    return toRomanTable[n]

def fromRoman(cls):
    """convert Roman numeral to integer"""
    if not cls:
        raise InvalidRomanNumeralError,'Input can not be blank'

    if not fromRomanTable.has_key(cls):
        raise InvalidRomanNumeralError,'Invalid Roman numeral:%s' % cls

    return fromRomanTable[cls]

def toRomanDynamic(n):
    """convert integer to Roman numeral using dynamic programming"""
    result =""
    for numeral, integer in romanNumeralMap:
        if n >= integer:
            result += numeral
            n -= integer
            break
    if n>0:
        result +=toRomanTable[n]
    return result

def fillLookupTables():
    """compute all the possible roman numerals"""
    #Save the values in two global tables to convert to and from integer
    for integer in range(1,MAX_ROMAN_NUMERAL+1):
        romanNumber = toRomanDynamic(integer)
        toRomanTable.append(romanNumber)
        fromRomanTable[romanNumber]=integer

fillLookupTables()
