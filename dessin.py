"""
Le programme dessin.py
pour l'article
les différentes versions
"""


def dessin_1():
    print('XXXXXXXXXX')
    print('XXXXXXXXXX')
    print('XXXXXXXXXX')
    print('XXXXXXXXXX')
    print('XXXXXXXXXX')
    print('XXXXXXXXXX')
    print('XXXXXXXXXX')
    print('XXXXXXXXXX')
    print('XXXXXXXXXX')
    print('XXXXXXXXXX')


def dessin_2():
    n = int(input('Donnez la taille de votre carré : '))
    for cpt in range(n):
        print('X' * n)


def dessin_3():
    n = int(input('size : '))
    mid = n//2
    for i in range(mid):
        print('X' * i + 'O' + 'X' * (n - 2*i - 2) + 'O' + 'X' * i)
    if n % 2:
        print('X' * (mid) + 'O' + 'X' * (mid))
        mid = n//2 + 1
    for i in range(mid, n):
        print('X' * (n - i - 1) + 'O' + 'X' * (2*i - n) + 'O' + 'X' * (n - i - 1))

def dessin_4(n, croix, rond):
    def moitie(n, croix, rond):
        l = []
        for i in range(n//2):
            l.append('{0}{1}{2}{1}{0}'.format(croix * i, rond, croix * (n - 2*i - 2)))
        return l

    def milieu(n, croix, rond):
        if n%2:
            return ['{0}{1}{0}'.format(croix * (n//2), rond)]
        else:
            return []

    def dessin(n, croix, rond):
        l1 = moitie(n, croix, rond)
        l2 = l1[::-1]
        lm = milieu(n, croix, rond)
        return '\n'.join(l1+lm+l2) 

    print(dessin(n, croix, rond))





# --
# -- MAIN
# --

dessin_3()    




