from collections import Counter

with open('input.txt') as f:
    boxid_list = f.read().splitlines()

double_boxids = 0
triple_boxids = 0

for boxid in boxid_list:
    double_letters = len(list(filter(lambda x:x==2, Counter(boxid).values())))
    triple_letters = len(list(filter(lambda x:x==3, Counter(boxid).values())))
    if double_letters >= 1: double_boxids += 1;
    if triple_letters >= 1: triple_boxids += 1;
    print('boxid',boxid)
    print('doubles',double_letters)
    print('triples',triple_letters)

print('total doubles',double_boxids)
print('total triples',triple_boxids)

checksum = str(double_boxids * triple_boxids)
print('checksum',checksum)

with open('part1.txt','w') as f: f.write(checksum)