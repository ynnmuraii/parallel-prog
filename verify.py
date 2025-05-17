import numpy as np

def read_matrix(filename):
    with open(filename) as f:
        rows, cols = map(int, f.readline().split())
        data = []
        for _ in range(rows):
            data.append(list(map(float, f.readline().split())))
        return np.array(data)

A = read_matrix('matrixA.txt')
B = read_matrix('matrixB.txt')
C_cpp = read_matrix('matrixC.txt')

C_py = A @ B

if np.allclose(C_cpp, C_py):
    print('Verification successful: results match.')
else:
    print('Error: results do not match!')
    print('C++ result:\n', C_cpp)
    print('Python result:\n', C_py)
