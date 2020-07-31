import re


pattern = re.compile(r'hello')
str1 = 'hello world!'
result = pattern.match(str1)
print(result)
