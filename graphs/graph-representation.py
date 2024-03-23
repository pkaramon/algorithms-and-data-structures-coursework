# list of edges

class ListOfEdgesGraph:
    def __init__(self, order, edges, vertices_info=None):
        self.edges = edges
        self.order = order
        if vertices_info is None:
            self.vertices_info = [i for i in range(order)]

    def edge_exists(self, edge):
        for ed in self.edges:
            if edge == ed:
                return True
        return False

    def in_degree(self, n):
        result = 0
        for edge in self.edges:
            if edge[1] == n:
                result += 1
        return result

    def out_degree(self, n):
        result = 0
        for edge in self.edges:
            if edge[0] == n:
                result += 1
        return result

    def neighbours(self, n):
        result = set()
        for edge in self.edges:
            if edge[0] == n:
                result.add(edge[1])
            if edge[1] == n:
                result.add(edge[0])
        return result


# matrix

class MatrixGraph:
    def __init__(self, order):
        self.order = order
        self.matrix = [[None for _ in range(order)] for _ in range(order)]

    def set_edge(self, edge, value):
        self.matrix[edge[0]][edge[1]] = value

    def edge_exists(self, edge):
        return self.matrix[edge[0]][edge[1]] is not None


def from_list_of_edges_to_matrix(edges, order):
    matrix = [[False for _ in range(order)] for _ in range(order)]
    for v, u in edges:
        matrix[v][u] = True
    return matrix


def print_graph_matrix(matrix, order):
    order_digits = len(str(order))
    print(" " * (order_digits + 1), end='')
    first_row = [f"{i:{order_digits}}" for i in range(order)]
    print(' '.join(first_row))

    for i in range(order):
        print(f'{i:{order_digits}} ', end='')
        for n in matrix[i]:
            print(' ' * (order_digits - 1), end='')
            print('T' if n else '.', end='')
            print(' ', end='')
        print()


print_graph_matrix(
    from_list_of_edges_to_matrix([(0, 1), (1, 0), (1, 2), (2, 3), (4, 1), (4, 3), (4, 5), (5, 4), (6, 7), (7, 8)], 101),
    101)
