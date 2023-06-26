a = []
a = input()
ab = []
for i in a:
    ab.append(i)
ab.sort()
b = []
b = input()
ba = []
for i in b:
    ba.append(i)
ba.sort()
if len(a) == len(b):
    if ab == ba:
        print('Слова являются анаграммами')
    else:
        print('Слова не являются анаграммами')
else:
    print('Слова не являются анаграммами')

