import pprint

from colorama import Fore, Back, Style
import queue
import numpy as np
from typing import List, Dict
import sys


def print_table(table):
    rows = []
    for i in table:
        rows.append('\t'.join(map(str, i)).replace(f'{sys.maxsize}', '-'))
    return "\n".join(rows)


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[sys.maxsize for i in range(len(vertices) + 1)] for j in range(len(vertices) + 1)]

    def __setitem__(self, key, value: List):
        self.graph[key][value[0]] = value[1]

    def __getitem__(self, vertex):
        return self.graph[vertex]  # 0 indexed

    def __str__(self):
        return print_table(self.graph)

    def get_connected_vertices(self, from_):
        connections = self.graph[from_]
        return connections

    @staticmethod
    def find_min_edge(edges_list, not_visited):
        print(f"{Fore.YELLOW}edges_list: {edges_list}{Style.RESET_ALL}\n"
              f"{Fore.BLUE}, not visited: {not_visited}{Style.RESET_ALL}")
        min_so_far = sys.maxsize
        min_edge = None
        for edge, edge_weight in enumerate(edges_list):
            if edge_weight < min_so_far and edge in not_visited:
                min_so_far = edge_weight
                min_edge = edge
        return min_edge, min_so_far

    def dijkstra_single_source_shortest_path(self, source_vertex):
        def add_to_matrix(row, at_zero):
            for index, i in enumerate(row):
                adj_mat[row_count][index] = i
            adj_mat[row_count][0] = at_zero
            not_visited.remove(at_zero)
            print(print_table(adj_mat))

        v_pair = {v: sys.maxsize for v in self.V if v != source_vertex}
        not_visited = self.V.copy()
        adj_mat = [[sys.maxsize for i in range(len((self.graph[0])))] for j in range(len(self.graph))]
        row_count = 0
        # start with source vertex
        not_visited.remove(source_vertex)
        connected_vertices = self.get_connected_vertices(source_vertex)
        selected_vertex, edge_weight = self.find_min_edge(connected_vertices, not_visited)

        add_to_matrix(connected_vertices, selected_vertex)  # add a new row to the matrix
        row_count += 1

        connected_vertices = self.get_connected_vertices(selected_vertex)
        selected_vertex, edge_weight = self.find_min_edge(connected_vertices, not_visited)
        add_to_matrix(connected_vertices, selected_vertex)


vert = [1, 2, 3, 4, 5, 6]
edges = [
    [1, 2, 50],
    [1, 3, 45],
    [1, 4, 10],
    [2, 3, 10],
    [2, 4, 15],
    [3, 5, 30],
    [4, 1, 10],
    [4, 5, 15],
    [5, 2, 20],
    [5, 3, 35],
    [6, 5, 3]
]
g = Graph(vert)
for from_vertex, to_vertex, weight in edges:
    g[from_vertex][to_vertex] = weight
print("\t".join(list(map(str, [' '] + g.V))))
print(len(vert) * '----')
print(g)

g.dijkstra_single_source_shortest_path(1)
