#coding=utf-8
import re

#定义匹配规则
rules =\
    (
        (
            lambda word:re.search('[sxz]$',word),
            lambda word:re.sub('$','es',word)
        ),
        (
            lambda word:re.search('[^aeioudgkprt]h$',word),
            lambda word:re.sub('$','es',word)
        ),
        (
            lambda word:re.search('[^aeiou]y$',word),
            lambda word:re.sub('y$','ies',word)
        ),
        (
            lambda word:re.search('$',word),
            lambda word:re.sub('$','s',word)
        )
    )

def plural(noun):
    for matchesRule,applyRule in rules:
        if matchesRule(noun):
            return applyRule(noun)
