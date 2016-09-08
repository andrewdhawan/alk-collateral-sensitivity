#Andrew Dhawan
#Sept 8 2016
#count_cycles.py
#This code enables the count of unique cycles of a particular length
#implements a DFS on an adjacency matrix for a weighted graph.
#Element (i,j)=1 of the adjacency matrix indicates a directed edge
#from node j to node i.

import numpy as np

def find_path_to_vertex (graph, cur_vert, dest_vert, itera, start, cur_traj):
	global count
	
	if (itera==0 and cur_vert==dest_vert):
		count +=1
	#	print("Cycle found:    " + str(dest_vert)+  cur_traj + str(cur_vert))
		return 0

	if (itera==0):
		return 0
	
	if (cur_vert == dest_vert and start==0):
		return 0

	if (start==0):
		cur_traj += str(cur_vert)
	
	for i in range(len(graph[:,cur_vert])):
		if (graph[i,cur_vert] ==1 and itera>0):
			if (cur_traj.find(str(i))<0):
					find_path_to_vertex(graph, i, dest_vert, itera-1,0,cur_traj)
	return 0


#adjacency matrix for the graph:
#G = np.array([[0,0,0,1],[0,0,0,1],[1,1,0,1],[0,1,0,0]])
G = np.array([[0,	0,	0,	0,	0,	0,	1,	0,	1,	0], [0,	0,	0,	0,	0,	1,	1,	0,	1,	0], [0,	0,	0,	0,	0,	0,	1,	0,	1,	1],[0,	0,	0,	0,	0,	1,	1,	1,	1,	0],[0,	0,	0,	0	,0,	0,	1,	0,	1,	1],[0,	0,	0,	0,	0	,0,	1,	0,	0,	0],[0,	0,	0,	0,	0,	1,	0,	0,	0,	1],[0,	0,	0	,0	,1	,1,	1,	0,	1,	0],[1,	0	,0,	1	,0,	1,	1,	1,	0,	0],[1,	1,	1,	1,	0,	1,	1,	0,	1,	0]])

#find all cycles of length 2
count = 0

for i in range(len(G[:,1])):
	find_path_to_vertex(G, i, i, 2,1,"")

print(count/2)

#find all cycles of length 3
count = 0

for i in range(len(G[:,1])):
	find_path_to_vertex(G, i, i, 3,1,"")

print(count/3)

#find all cycles of length 4
count = 0

for i in range(len(G[:,1])):
	find_path_to_vertex(G, i, i, 4,1,"")

print(count/4)

#find all cycles of length 5
count = 0

for i in range(len(G[:,1])):
	find_path_to_vertex(G, i, i, 5,1,"")

print(count/5)

#find all cycles of length 6
count = 0

for i in range(len(G[:,1])):
	find_path_to_vertex(G, i, i, 6,1,"")

print(count/6)

#find all cycles of length 7
count = 0

for i in range(len(G[:,1])):
	find_path_to_vertex(G, i, i, 7,1,"")

print(count/7)

#find all cycles of length 8
count = 0

for i in range(len(G[:,1])):
	find_path_to_vertex(G, i, i, 8,1,"")

print(count/8)

#find all cycles of length 9
count = 0

for i in range(len(G[:,1])):
	find_path_to_vertex(G, i, i, 9,1,"")

print(count/9)