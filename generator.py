import numpy as np

def generate_matrix(rows, cols, min_val=0, max_val=10, filename="matrix.txt"):
    mat = np.random.randint(min_val, max_val + 1, size=(rows, cols))
    with open(filename, "w") as f:
        f.write(f"{rows} {cols}\n")
        for row in mat:
            f.write(" ".join(str(x) for x in row) + "\n")

generate_matrix(3, 2, 1, 10, "matrixA.txt")
generate_matrix(2, 2, 1, 10, "matrixB.txt")
