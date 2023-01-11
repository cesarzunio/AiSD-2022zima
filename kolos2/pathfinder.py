from graph import *
from typing import List, Dict


class Pathfinder:
    graph: Graph
    costs: Dict[Vertex, float]  # vertex -> cost
    parents: Dict[Vertex, Vertex]  # child -> parent

    def __init__(self, graph: Graph):
        self.graph = graph
        self.costs = {}
        self.parents = {}

    def pop_lowest_cost_edge(self, open_set: List[Edge]) -> Edge:
        lowest_cost = float('inf')
        index_of_lowest_cost = -1

        for i in range(len(open_set)):
            if self.costs[open_set[i].destination] < lowest_cost:
                lowest_cost = self.costs[open_set[i].destination]
                index_of_lowest_cost = i

        return open_set.pop(index_of_lowest_cost)

    def dijkstra(self, start_node: Vertex, end_node: Vertex) -> List[Vertex]:
        open_set = []  # edge
        closed_set = []  # vertex
        graph = self.graph

        self.costs[start_node] = 0.0
        closed_set.append(start_node)

        for edge in graph.adjacents[start_node]:
            open_set.append(edge)

        while True:
            if len(open_set) == 0:
                print('No path found')
                return []

            # update open_set
            for edge in open_set:
                if edge.destination not in self.costs or self.costs[edge.source] + edge.weight < self.costs[edge.destination]:
                    self.costs[edge.destination] = self.costs[edge.source] + edge.weight
                    self.parents[edge.destination] = edge.source

            # pop lowest edge
            lowest_edge = self.pop_lowest_cost_edge(open_set)
            vertex_to_explore = lowest_edge.destination

            if vertex_to_explore is end_node:
                print('Wow, path finded!')
                return self.retrace_path(start_node, end_node)

            # explore given edge
            closed_set.append(vertex_to_explore)

            for edge in graph.adjacents[vertex_to_explore]:
                if edge.destination not in closed_set:
                    open_set.append(edge)

    def retrace_path(self, start_node: Vertex, end_node: Vertex) -> List[Vertex]:
        pointer = end_node
        path = [end_node]

        while pointer is not start_node:
            pointer = self.parents[pointer]
            path.append(pointer)

        path.reverse()
        return path




