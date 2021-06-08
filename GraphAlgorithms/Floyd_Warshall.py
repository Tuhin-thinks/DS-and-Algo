import sys


def print_mat(mat):
    for r in range(len(mat)):
        for c in range(len(mat[0])):
            elem = mat[r][c]
            if elem != sys.maxsize:
                print(elem, end="\t")
            else:
                print("__", end="\t")
        print()


def accept_edges(mat):
    while True:
        print("Enter Edge: (from, to, weight): ", end="")
        inp = input()
        if inp != 'break':
            from_, to_, weight = map(int, inp.split(" "))
            mat[from_ - 1][to_ - 1] = weight  # 0-indexing
        else:
            break
    return mat


def check_shortest_path(mat, u, v, k):
    return min(mat[u][v], mat[u][k] + mat[k][v])


# ask for number of vertices
V = int(input("Number of vertices:"))

# create the matrix & initialize with 0
mat = [[sys.maxsize for _ in range(V)] for _ in range(V)]

# accept edges and weights
mat = accept_edges(mat)

# print entered matrix in tabular form
print_mat(mat)

# run iteration loop
for r in range(V):
    for c in range(V):
        if r == c: continue
        for k in range(V):
            mat[r][c] = check_shortest_path(mat, r, c, k)

# print the final matrix containing the result
print("Final matrix:")
print_mat(mat)
