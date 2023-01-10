from enum import Enum
from typing import Optional, Dict, List, Callable, Any


class MyQueue:
    data: List[Any]

    def __init__(self):
        self.data = []

    def add(self, item: Any) -> None:
        self.data.append(item)

    def pop(self) -> Any:
        return self.data.pop(0) if len(self.data) > 0 else None

    def __len__(self) -> int:
        return len(self.data)


class EdgeType(Enum):
    directed = 0
    undirected = 1


class Vertex:
    data: Any
    index: int

    def __init__(self, data: Any):
        self.data = data


class Edge:
    edge_type: EdgeType
    source: Vertex
    dest: Vertex
    weight: float

    def __init__(self, source: Vertex, dest: Vertex, edge_type: EdgeType, weight: float):
        self.source = source
        self.dest = dest
        self.edge_type = edge_type
        self.weight = weight

    def __repr__(self) -> str:  # debug ?
        return str(self.dest.data)


class Graph:
    adjacents: Dict[Vertex, List[Edge]]

    def __init__(self):
        self.adjacents = {}

    def create_vertex(self, data: Any) -> Vertex:
        vertex = Vertex(data)
        self.adjacents[vertex] = []
        return vertex

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: float = 1.0) -> None:
        self.adjacents[source].append(Edge(source, destination, EdgeType.directed, weight))

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: float = 1.0) -> None:
        self.adjacents[source].append(Edge(source, destination, EdgeType.undirected, weight))
        self.adjacents[destination].append(Edge(destination, source, EdgeType.undirected, weight))

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: float = 1.0) -> None:
        if edge == edge.directed:
            self.add_directed_edge(source, destination, weight)
        else:
            self.add_undirected_edge(source, destination, weight)

    def __first_vertex(self) -> Vertex:
        for key in self.adjacents:
            return key
        return None

    def traversal_breadth_first(self, func: Callable[[Vertex], None]) -> None:
        closed_set = []
        queue = MyQueue()

        vertex = self.__first_vertex()
        func(vertex)
        closed_set.append(vertex)
        queue.add(vertex)

        while len(queue) > 0:
            vertex = queue.pop()

            if vertex not in closed_set:  # why this must be here?
                func(vertex)
                closed_set.append(vertex)

            edges = self.adjacents[vertex]

            for e in edges:
                if e.dest not in closed_set:
                    queue.add(e.dest)


    def print(self) -> None:
        def print_vert(v: Vertex) -> None:
            print(f'{v.data} -> {self.adjacents[v]}')

        self.traversal_breadth_first(print_vert)

    def traversal_deep_first(self, func: Callable[[Vertex], None]) -> None:
        vertex = self.__first_vertex()
        closed_set = []

        self.__tdf(vertex, func, closed_set)

    def __tdf(self, vertex: Vertex, func: Callable[[Vertex], None], closed_set: List[Vertex]) -> None:
        func(vertex)
        closed_set.append(vertex)

        edges = self.adjacents[vertex]

        for e in edges:
            if e.dest not in closed_set:
                self.__tdf(e.dest, func, closed_set)