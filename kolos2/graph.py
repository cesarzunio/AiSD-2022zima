from typing import Dict, List, Any, Callable
from enum import Enum


class Vertex:
    data: Any

    def __init__(self, data: Any):
        self.data = data


class EdgeType(Enum):
    directed = 0
    undirected = 1


class Edge:
    source: Vertex
    destination: Vertex
    weight: float

    def __init__(self, source: Vertex, destination: Vertex, weight: float):
        self.source = source
        self.destination = destination
        self.weight = weight

    def __repr__(self):
        return self.destination.data


class Graph:
    adjacents: Dict[Vertex, List[Edge]]

    def __init__(self):
        self.adjacents = {}

    def create_vertex(self, data: Any) -> Vertex:
        vertex = Vertex(data)
        self.adjacents[vertex] = []
        return vertex

    def add_edge(self, source: Vertex, destination: Vertex, weight: float = 1.0) -> None:
        self.adjacents[source].append(Edge(source, destination, weight))
        self.adjacents[destination].append(Edge(destination, source, weight))

    def print_vertex(self, vertex: Vertex) -> None:
        print(f'{vertex.data} -> {self.adjacents[vertex]}')

    def get_first(self) -> Vertex:
        for key in self.adjacents:
            return key

        return None

    def breadth_first_traversal(self, func: Callable[[Vertex], None]) -> None:
        visited = []
        queue = []

        vertex_current = self.get_first()

        if vertex_current is None:
            print('Graph is empty')
            return

        queue.append(vertex_current)
        visited.append(vertex_current)

        while len(queue) > 0:
            vertex_current = queue.pop(0)

            func(vertex_current)

            for edge in self.adjacents[vertex_current]:
                if edge.destination not in visited:
                    visited.append(edge.destination)
                    queue.append(edge.destination)

    def deep_first_traversal(self, func: Callable[[Vertex], None]) -> None:
        visited = []

        vertex_current = self.get_first()

        if vertex_current is None:
            print('Graph is empty')
            return

        visited.append(vertex_current)
        self.__dfs(vertex_current, func, visited)

    def __dfs(self, vertex: Vertex, func: Callable[[Vertex], None], visited: List[Vertex]) -> None:
        func(vertex)

        for edge in self.adjacents[vertex]:
            if edge.destination not in visited:
                visited.append(edge.destination)
                self.__dfs(edge.destination, func, visited)


