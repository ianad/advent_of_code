from functools import reduce

with open('input.txt') as f:
    list_of_strs = f.read().splitlines()

integerize = lambda x: int(x)
accumulate = lambda x,y: x+y

list_of_ints =  list(map(integerize,list_of_strs))
sum_of_ints = reduce(accumulate,list_of_ints)

print(sum_of_ints)
input()