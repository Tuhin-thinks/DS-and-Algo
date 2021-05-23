"""
implementation of kruskals' algorithm using Python
"""
import pprint

adj_mat = {}
mstSet = set()
mstCost = 0

def find_MST(options=None):
    global adj_mat, mstCost, mstSet
    
    if not options:
        min_key = sorted(adj_mat.keys())[0]  # pick the minimum key value
        options = adj_mat[min_key]
        mstSet.add(min_key)
        print(min_key, end="  ")
    else:
        # find option with the lowest edge value, [options: List[dict]]
        for k in list(mstSet):
            k_in_opt = False
            for opts in options:
                if list(opts.keys())[0] == k:
                    options.remove(opts)
                    k_in_opt = True
                    break

    if options:    
        min_option = sorted(options, key=lambda x: list(x.values())[0])[0]
        minOptKey = list(min_option.keys())[0]
        print(minOptKey, end="  ")
        mstSet.add(minOptKey)
        mstCost += list(min_option.values())[0]
        find_MST(options=adj_mat[minOptKey])
    else:
        return



def add_edge(from_edge, to_edge, edge_weight):
    global adj_mat
    if from_edge not in adj_mat:
        adj_mat[from_edge] = []
    if to_edge not in adj_mat:
        adj_mat[to_edge] = []
    adj_mat[from_edge].extend([{to_edge : edge_weight}])
    adj_mat[to_edge].extend([{from_edge : edge_weight}])

def print_adj_matr():
    for k, v in adj_mat.items():
        print(k,' --> ' ,v)

edge_list = [[1,6,10],
            [1,2,28],
            [2,3,16],
            [2,7,14],
            [3,4,12],
            [4,5,22],
            [4,7,18],
            [5,6, 25],
            [5,7,24]]

for from_, to_, weight in edge_list:
    add_edge(from_, to_, weight)

print_adj_matr()

print()
find_MST()

print(f"\nMST cost: {mstCost}")