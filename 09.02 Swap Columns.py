def swap_columns(a, i, j):
    for k in range(len(a)):
        a[k][i], a[k][j] = a[k][j], a[k][i]

def print_array(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end =' ')

swap_columns(a, i, j)
print_array(a)