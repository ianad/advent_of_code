from collections import Counter

debug_input = False
debug_rdout = False

if debug_input:
    boxid_list = ['abcde','fghij','klmno','pqrst','fguij','axcye','wvxyz']
else:
    with open('input.txt') as f: boxid_list = f.read().splitlines()
    
double_boxids = 0
triple_boxids = 0

for boxid in boxid_list:
    for other_boxid in boxid_list:
        if boxid is not other_boxid:
            differ = [i for i, j in zip(boxid, other_boxid) if i != j]
            if len(differ) == 1:
                if debug_rdout: print('boxid',boxid)
                common = ''.join([i for i, j in zip(boxid, other_boxid) if i == j])

with open('output.txt','w') as f: f.write(common)