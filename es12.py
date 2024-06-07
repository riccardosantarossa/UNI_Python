from __future__ import print_function

def periodoFrazionarioQuadratico(s):
    n = len(s)
    for length in range(1, n):  #esegue al massimo n iterazioni
        pattern = s[:length]
        quo = n // length
        if pattern * quo + s[:n % length] == s:
            return length
    return 0

def periodoFrazionarioLineare(s):
    n = len(s)
    r = [0] * n
    lunghezzaPeriodo = 0
    i = 1

    while i < n: #attraversa la stringa una sola volta
        if s[i] == s[lunghezzaPeriodo]:
            lunghezzaPeriodo += 1
            r[i] = lunghezzaPeriodo
            i += 1
        else:
            if lunghezzaPeriodo != 0:
                lunghezzaPeriodo = r[lunghezzaPeriodo - 1]
            else:
                r[i] = 0
                i += 1

    periodo = n - r[n - 1]
    return periodo

inputS = input()
print(periodoFrazionarioLineare(inputS))
print(periodoFrazionarioQuadratico(inputS))