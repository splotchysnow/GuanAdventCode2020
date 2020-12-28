import fileinput
import re

p1 = 0
p2 = 0

lines = list(fileinput.input())
lines.append("")

for line in lines:
    line = line.strip()
    words = line.split()
    container = words[0] + words[1] + words[2]
    print(words)
print(p1)
print(p2)