from tkinter import E


file = open('liczby.txt', 'r')
lines = file.readlines()
a = []
c = []
g = []
for line in lines:
        line = int(line.replace('\n', ''))
        a.append(line)

def max_value():
    print('makysmalna wartosc:', max(a))
    

def sort_value():
    print('posortowana wartosci:', sorted(a, reverse=True))

def cur_max(s):
    cur_max = s[0]
    for x in s :
        if x > cur_max:
            cur_max = x
    print(cur_max)
    return cur_max


def odd(b):
    for x in b:
        if x%2 != 0:
            c.append(x)
    print(c)
    return c

def even(b):
    for x in b:
        if x%2 == 0:
            g.append(x)
    print(g)
    return g

def min_p(f):
    curr_min = f[0]
    for x in f:
        if x < curr_min:
            curr_min = x
    print(curr_min)
    return curr_min

def max_odd(j):
    h = odd(j)
    cur_max(h)

def max_even(t):
    e = even(t)
    cur_max(e)


def main():

    max_odd(a)
    max_even(a)

main()







