"""проект отпечаток языка
считаем каких букв в строке/тексте больше
деалем графику"""

from collections import Counter

f = open('fingerprint_language.txt', 'r')
s = f.read()
s1 = s.lower()

d = dict(Counter(s1))

list_keys = list(d.keys())
list_keys.sort()

procent = d[max(d, key=d.get)]

for i in list_keys:
    d[i] = round((d[i] / 100 * procent), 2)
    print(f'{i}, ":", {d[i]}%')

f.close()
