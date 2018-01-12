#coding=utf-8
import re

def plural(noun):
    if re.search('[sxz]$',noun):
        return re.sub('$','es',noun)
    elif re.search('[^aeioudgkprt]h$',noun):
        return re.sub('$','es',noun)
    elif re.search('[^aeiou]y$',noun):
        return re.sub('y$','ies',noun)
    else:
        return noun + 's'