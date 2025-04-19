from pathlib import Path
import re


def ret_bytestring(path : Path):
    regex = r"b(['\"])(.*)\1\)$"
    with open(path, "r") as k:
        string = k.read()
        match  = re.search(regex, string)
        if match:
            return [ord(b) for b in match.group(2).encode('latin-1').decode('unicode_escape')]

t1 = Path("dist/test.py")
t2 = Path("other/dist/test.py")

str1 = ret_bytestring(t1)
str2 = ret_bytestring(t2)

breakpoint()
print(str1)
print("")
print(str2)

print(len(str1), len(str2))


