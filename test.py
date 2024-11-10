import re

pattern = r'\W+'

text = 'I like a Banana, do you like apples?'

x = re.findall (pattern, text)

print(x)