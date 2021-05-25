from colorama import Fore, Back, Style

visited = list()


class Graph:
    def __init__(self, g_dict=None) -> None:
        if not g_dict:
            g_dict = {}
        self.g_dict = g_dict

    def add_edge(self, source, dest, weight: int):
        if source in self.g_dict:
            self.g_dict[source].append({dest: weight})
        else:
            self.g_dict[source] = [{dest: weight}]

    def print_graph(self):
        lines = []
        for k, v in self.g_dict.items():
            print(k, " : ", v)
        return "\n".join(lines)

    def adj(self, u):
        return [list(i.keys())[0] for i in self.g_dict[u]]

    def dfs(self, u):
        global visited
        if visited is None:
            visited = list()
        if u not in visited:
            visited.append(u)
            print(u, end=f"{visited} -> ")

        # explore any unvisited node from u
        try:
            adjacent_vertices = self.adj(u)
        except KeyError:
            print(f"{Fore.BLUE}No exiting node from {u}{Style.RESET_ALL}")
            # print(" -> ".join(visited[:-1]), end=f" -> {u}\n")
            print(f"{Fore.RED}[DEL] visited : {visited}{Fore.RESET}")
            visited.clear()
            print(f"{Fore.GREEN}[OVER]{u}, {visited}{Fore.RESET}")
            return

        for V in [i for i in adjacent_vertices if i not in visited]:
            self.dfs(V)
        print(f"{Fore.GREEN}[OVER]{u}, {visited}{Fore.RESET}")


# Edges
# A -> B
# A -> D

# B -> C
# C -> D
# D -> E

# F -> E

graph = Graph()
graph.add_edge('A', 'B', 3)
graph.add_edge('A', 'D', 1)
graph.add_edge('B', 'C', 2)
graph.add_edge('C', 'D', 5)
graph.add_edge('D', 'E', 8)
graph.add_edge('F', 'E', 5)
graph.add_edge('F', 'A', 6)

print("Adjacency list representation:")
graph.print_graph()

print("\n[DFS Search result]")
starting_vertex = 'F'
graph.dfs(starting_vertex)  # start dfs from node 'F'
