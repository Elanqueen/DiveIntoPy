#coding=utf-8
"""动态生成匹配函数"""

import  re

def buildMatchAndApplyFunctions((pattern,search,replace)):
    matchFunction = lambda word:re.search(pattern,word)
    applyFunction = lambda word:re.sub(search,replace,word)
    return (matchFunction,applyFunction)

patterns =\
(
    ('[sxz]$','$','es'),
    ('[^aeioudgkprt]h$','$','es'),
    ('[^aeiou]y$','y$','ies'),
    ('$','$','s')
)
rules = map(buildMatchAndApplyFunctions,patterns)

def plural(noun):
    for matchesRule,applyRule in rules:
        if matchesRule(noun):
            return applyRule(noun)
