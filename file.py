file = open('liczby.txt', 'r')
lines = file.readlines()
a = []
c = []

for line in lines:
        line = int(line.replace('\n', ''))
        a.append(line)

def max_value():
    print('makysmalna wartosc:', max(a))
    

def sort_value():
    print('posortowana wartosci:', sorted(a, reverse=True))

def max_value_alg(x):

    if x == 0:
        return 0

    crn_max = x[0]
    for b in x:
        if b > crn_max:
            crn_max = b
    print(crn_max)
    return x

def odd_num(b):
    for x in b:
        if x%2 != 0:
            c.append(x)
    print(c)
    return c

def max_odd_num(m):
    value = odd_num(m)  
    v2 = max_value_alg(value)


    
def main():

    max_odd_num(a)



main()







