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

for i in list_keys:
 	print(i, ":", d[i])

 	

f.close()
