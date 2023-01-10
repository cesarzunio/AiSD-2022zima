from typing import Dict, List
from graph import Graph, Vertex, Edge


class Pathfinder:
    cost_set: Dict[Vertex, float]
    parent_set: Dict[Vertex, Vertex]  # child -> parent
    graph: Graph

    def __init__(self, graph: Graph):
        self.cost_set = {}
        self.parent_set = {}
        self.graph = graph

    def dijkstra(self, start_node: Vertex, end_node: Vertex) -> List[Vertex]:
        open_set = []
        closed_set = []

        self.cost_set[start_node] = 0.0
        closed_set.append(start_node)
        for edge in self.graph.adjacents[start_node]:
            open_set.append(edge)
            self.parent_set[edge.dest] = edge.source

        while True:
            # update costs
            for edge in open_set:
                if edge.dest not in self.cost_set or self.cost_set[edge.source] + edge.weight < self.cost_set[edge.dest]:
                    self.parent_set[edge.dest] = edge.source
                    self.cost_set[edge.dest] = self.cost_set[edge.source] + edge.weight

            # pop lowest cost
            edge_to_explore = self.pop_lowest_cost(open_set)
            vertex_to_explore = edge_to_explore.dest

            print(f'from: {edge_to_explore.source.data} to {edge_to_explore.dest.data}')

            if vertex_to_explore is end_node:
                print('Reached end!')
                return self.retrace_path(end_node, start_node)

            # add edges
            closed_set.append(vertex_to_explore)

            for edge in self.graph.adjacents[vertex_to_explore]:
                if edge.dest not in closed_set:
                    open_set.append(edge)

    def pop_lowest_cost(self, open_set: List[Edge]):
        lowest_cost = float('inf')
        index = -1

        for i in range(len(open_set)):
            iedge = open_set[i]
            if self.cost_set[iedge.dest] < lowest_cost:
                lowest_cost = self.cost_set[iedge.dest]
                index = i

        return open_set.pop(index)

    def retrace_path(self, end_node: Vertex, start_node: Vertex) -> List[Vertex]:
        return_list = [end_node]
        pointer = end_node

        while pointer is not start_node:
            pointer = self.parent_set[pointer]
            return_list.append(pointer)

        return_list.reverse()
        return return_list
