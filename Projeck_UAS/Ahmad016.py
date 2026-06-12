def tampilkan (A, nama="matriks"):
    print(f"\n{nama} = ")
    for baris in A: 
        print(" ", baris)

def tambah (A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def kurang (A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def kali_skalar(A, k):
    return [[A[i][j] * k for j in range(len(A[0]))] for i in range(len(A))]

def kali (A, B):
    m, n, p = len(A), len(B[0]), len(B)
    return [[sum(A[i][k] * B[k][j] for k in range(p)) for j in range(n)] for i in range(m)]

def transpose (A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]
