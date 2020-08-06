with open('p079_keylog.txt', 'r') as f:
    unique_bigrams = {i for sl in [(n[:2], n[1:]) for n in f.read().splitlines()] for i in sl}
# split all the numbers into bigrams, and then set comprehension for unique ones

import networkx as nx

DG = nx.DiGraph()
DG.add_edges_from(unique_bigrams)

print(''.join(nx.algorithms.topological_sort(DG)))  # order dependencies by topo sort of DAG!!!

# tried to code this algorithm which got messy and doesn't work...
# pw = ''
# for b in sorted(unique_bigrams):
#     if b[0] in pw and b[1] in pw:
#         if pw.index(b[0]) > pw.index(b[1]):
#             pw = pw[:pw.index(b[1])] + b[0] + pw[pw.index(b[1]):]
#     else:
#         if b[0] not in pw and b[1] not in pw:
#             pw = b[0] + pw + b[1]
#         else:
#             if b[0] not in pw:
#                 pw = pw.split(b[1])[0] + b[0] + b[1] + pw.split(b[1])[1]
#             if b[1] not in pw:
#                 pw = pw.split(b[0])[0] + b[0] + b[1] + pw.split(b[0])[1]
