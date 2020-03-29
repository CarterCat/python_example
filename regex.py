# https://www.programiz.com/python-programming/regex

# \d \w \s .

# * + ? {n} {n,m}

# [0-9a-zA-Z]

# a|b

# ^ $


import re

m = re.match(r'str', 'str')

m = re.split(r'\s+', 'a b  c')

m = re.match(r'(\d+)\D(\d+)', '12f34')

m = re.match(r'(\d+)*', '12f34')

m.groups

m.group(0)

m.group(1)

re.match(r'^(\d+)(0*)$', '102300').groups()

re.match(r'^(\d+?)(0*)$', '102300').groups()

re_phone = re.compile(r'^(\d{3})-(\d{3,8})$')

re_phone.match('010-8086').groups()

