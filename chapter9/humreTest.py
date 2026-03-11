import re

from humre import *

phone_regex = group(
    optional_group(either(exactly(3,DIGIT), OPEN_PAREN + exactly(3, DIGIT) +
                          CLOSE_PAREN)),
    optional_group(group_either(WHITESPACE, '-',PERIOD)),
    group(exactly(3, DIGIT)),
    group_either(WHITESPACE, '-',PERIOD),
    group(exactly(4, DIGIT)),
    optional_group(zero_or_more(WHITESPACE),
                   group_either('ext','x',r'ext\.'),
                   zero_or_more(WHITESPACE),
                   group(between(2,5, DIGIT))
                   )
    )
print(phone_regex)
pattern = re.compile(phone_regex)
match = pattern.search('My number is 541-555-1212.')
print(match.group())
