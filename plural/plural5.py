#coding=utf-8
"""将匹配规则存放在rule.en文件中，
将规则和代码分开维护
"""

import re
import string

def buildRule((pattern,search,replace)):
    return lambda word:re.search(pattern,word) and re.sub(search,replace,word)

def plural(noun,language='en'):
    lines = file('rules.%s' % language).readlines()
    patterns = map(string.split,lines)
    rules = map(buildRule,patterns)
    for rule in rules:
        result = rule(noun)
        if result: return result