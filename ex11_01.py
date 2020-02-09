import re

# hand = open('regex_sum_test.txt')
# hand = open('regex_sum_42.txt')
hand = open('regex_sum_238923.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    number = re.findall('[0-9]+',line)
    if len(number) == 0: continue
    for num in number:
        n = int(num)
        numlist.append(n)
#        print(n)

print('Sum:', sum(numlist) )
