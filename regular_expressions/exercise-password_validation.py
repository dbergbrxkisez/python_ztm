import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = 'Dbergbrxkisez'
pattern2 = re.compile(r"[A-Za-z0-9$%#@]{8,}\d")
pattern3 = re.compile(r"([A-Za-z0-9$%#@]{7,}[0-9])")
password = 'jhfsdjhf3423%$9'

a = pattern.search(string)
print(a)
check = pattern2.fullmatch(password)
print(check)
checkcheck = pattern3.fullmatch(password)
print(checkcheck)

# At least 8 char long.
# contain any sort letters, numbers $%#@.
# ends with a number.

