from functools import reduce

with open('input.txt') as f:
    list_of_strs = f.read().splitlines()

integerize = lambda x: int(x)
list_of_ints =  list(map(integerize,list_of_strs))

duplicate_freq = False
iter = 0
freq = 0
past_freqs = []

while not duplicate_freq:
    print('Iteration',iter,'...')
    iter += 1
    for i in list_of_ints:
        freq += i
        if freq in past_freqs:
            duplicate_freq = True
            print('Duplicate frequency!',freq)
            break
        past_freqs.append(freq)