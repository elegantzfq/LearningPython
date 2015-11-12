

def seq_ops():
    l = [123, 'spam', 1.23]
    print(len(l))


def type_ops():
    l = [123, 'spam', 1.23]
    l.append('NI')
    a = l.pop()
    print(a)
    print(l)


def nest():
    M = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9],
         [8, 9, 10]]
    print('M:\n', M)
    col1 = [row[1] for row in M]
    print(col1)
    col2 = [row[1] for row in M if row[1] % 2 == 0]
    print(col2)
    diag = [M[i][i] for i in [0, 1, 2]]
    print(diag)
    doubles = [c * 2 for c in 'spam']
    print(doubles)
    rg = list(range(4))
    print(rg)
    rg2 = list(range(-6, 7, 2))
    print(rg2)
    g = [sum(row) for row in M]
    print(g)


# type_ops()

nest()
