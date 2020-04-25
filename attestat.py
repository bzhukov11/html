n = int(input())
a = [['.'] * n for i in range(n)]
for i in range(n):
    a[i][i] = '*'
    a[n // 2][i] = '*'
    a[i][n // 2] = '*'
    a[i][n - i - 1] = '*'
for row in a:
    print(' '.join(row))

print('\n')

a = [['.'] * n for i in range(n)]
for i in range(n):
    a[i][0] = '*'
    a[i][n-1] = '*'
    a[n // 2][i] = '*'
for row in a:
    print(' '.join(row))

print('\n')

a = [['.'] * n for i in range(n)]
for i in range(n):
    a[i][0] = '*'
    a[0][i] = '*'
    if i<n//2:
        a[n//2][i] = '*'
for row in a:
    print(' '.join(row))

print('\n')

a = [['.'] * n for i in range(n)]
for i in range(n):
    a[i][0] = '*'
    a[i][1] = '*'
    a[0][i] = '*'
    a[n//2][i] = '*'
    a[i][n-1] = '*'
    a[n-1][i]='*'
for row in a:
    print(' '.join(row))

print('\n')

a = [['.'] * n for i in range(n)]
for i in range(n):
    
    a[0][n//2] = '*'
    if i>2:
        a[i][n//2
             ] = '*'
    
for row in a:
    print(' '.join(row))

print('\n')

a = [['.'] * n for i in range(n)]
for i in range(n):
    if i>n/2-0.5:
        a[i][0] = '*'
        a[i][n-1] = '*'
    a[n//2][i] = '*'
    if i<n//2+0.5:
        a[i][n - i -1-n//2] = '*'
    if i<n//2+0.5:
        a[i][i-n//2] = '*'
for row in a:
    print(' '.join(row))


