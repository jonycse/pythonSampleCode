'''
example of iterator pattern with generator
'''

def show_chars(n):
    list=['A','B','C','D','E','F','G','H','I','J']
    for data, pos in zip(list, range(n)):
        yield data

chars_set= show_chars(5)
for ch in chars_set:
    print ch