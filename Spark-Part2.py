import pandas as pd
import networkx as nx
import csv


df = pd.read_csv("twich.csv")

g = nx.from_pandas_edgelist(df, source='from', target='to', create_using=nx.DiGraph())

# part A) print in_degree and out_degree for graph
in_degree_rows = list()
out_degree_rows = list()
for (node,in_degree) in g.in_degree:
    in_degree_rows.append([node,in_degree])

for (node,out_degree) in g.out_degree:
    out_degree_rows.append([node,out_degree])


#
fields_out_degree = ["node","out_degree"]
fields_in_degree = ["node","in_degree"]


with open('GraphPartTwo/InDegree.csv', 'w' ,newline="") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(fields_in_degree)
    csv_writer.writerows(in_degree_rows)

with open('GraphPartTwo/OutDegree.csv', 'w' ,newline="") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(fields_out_degree)
    csv_writer.writerows(out_degree_rows)


# #part two

fields_ave_neigh = ["node","average_degree_neighbors"]
ave_neigh_rows = list()
for node,ave_neigh in nx.average_neighbor_degree(g).items():
    ave_neigh_rows.append([node,ave_neigh])

with open('GraphPartTwo/averageNeighborsDegree.csv', 'w' ,newline="") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(fields_ave_neigh)
    csv_writer.writerows(ave_neigh_rows)

# part three
diameter = max([max(j.values()) for (i,j) in nx.shortest_path_length(g)])
print("diameter: ", diameter)

#part Four
fields_closeness = ["node","closeness"]
closeness_rows = list()
for node,ave_close in nx.closeness_centrality(g).items():
    closeness_rows.append([node,ave_close])

with open('GraphPartTwo/closenessCentrality.csv', 'w' ,newline="") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(fields_closeness)
    csv_writer.writerows(closeness_rows)

#part Five
fields_pagerank = ["node","PageRank"]
pagerank_rows = list()
for node,pagerank in nx.pagerank(g).items():
    pagerank_rows.append([node,pagerank])

with open('GraphPartTwo/PageRank.csv', 'w',newline="") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(fields_pagerank)
    csv_writer.writerows(pagerank_rows)

#part_six

fields_cc = ["node","ClusteringCoefficient"]
cc_rows = list()
for node,cc in nx.clustering(g).items():
    cc_rows.append([node,cc])

with open('GraphPartTwo/ClusteringCoefficient.csv', 'w' ,newline="") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(fields_cc)
    csv_writer.writerows(cc_rows)


# part seven
scc = [c for c in sorted(nx.strongly_connected_components(g), key=len, reverse=True)]
wcc = [c for c in sorted(nx.weakly_connected_components(g), key=len, reverse=True)]
s = len(scc)
w = len(wcc)
print("scc:", s)
print("wcc:", w)
