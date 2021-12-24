from random import choice
def dnk(n, m):
    data = {}
    for _ in range(n):
        s = "".join(choice("cgta") for _ in range(m))
        a = s.count('a') / len(s) * 100
        c = s.count('c') / len(s) * 100
        t = s.count('t') / len(s) * 100
        g = s.count('g') / len(s) * 100
        gc = (s.count('g') + s.count('c')) / len(s) * 100
        a = '{:.2f}'.format(a)
        c = '{:.2f}'.format(c)
        t = '{:.2f}'.format(t)
        g = '{:.2f}'.format(g)
        gc = '{:.2f}'.format(gc)
        data[s] = (f'a - {a}%', f'c - {c}%', f'g - {g}%', f't - {t}%', f'gc - {gc}%')
    return data
