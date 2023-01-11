from graph import *
from pathfinder import *

gr = Graph()
v_a = gr.create_vertex('a')
v_b = gr.create_vertex('b')
v_c = gr.create_vertex('c')
v_d = gr.create_vertex('d')
v_e = gr.create_vertex('e')
v_f = gr.create_vertex('f')

gr.add_edge(v_a, v_b, 4)
gr.add_edge(v_a, v_c, 1)

gr.add_edge(v_b, v_d, 10)
gr.add_edge(v_b, v_e, 1)

gr.add_edge(v_c, v_d, 1)
gr.add_edge(v_c, v_e, 1)

gr.add_edge(v_d, v_f, 1)
gr.add_edge(v_e, v_f, 10)

pf = Pathfinder(gr)

path = pf.dijkstra(v_a, v_b)

for vertex in path:
    print(vertex.data)