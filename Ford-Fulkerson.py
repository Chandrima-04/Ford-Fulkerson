from collections import defaultdict 
class Graph:   
    def __init__(self,graph): 
        self.graph = graph # residual graph 
        self. ROW = len(graph)            
    '''Returns true if there is a path from source 's' to sink 't' in residual graph. Also fills parent[] to store the path '''
    def DFSUtil(self,s,visited, parent): 
        visited[s]= True
        for ind, val in enumerate(self.graph[s]): 
            if visited[ind] == False and val > 0 :
                parent[ind] = s 
                self.DFSUtil(ind, visited, parent)
        return parent
    def DFS(self,s, t, parent): 
        visited = [False]*(len(self.graph)) 
        parent = self.DFSUtil(s,visited,parent) 
        # If we reached sink in DFS starting from source, then return 
        # true, else false 
        return True if visited[t] else False
    # Returns tne maximum flow from s to t in the given graph 
    def FordFulkerson(self, source, sink): 
        final_list = []
        # This array is filled by DFS and to store path 
        parent = [-1]*(self.ROW) 
        max_flow = 0 # There is no flow initially 
        # Augment the flow while there is path from source to sink 
        while self.DFS(source, sink, parent) : 
            # Find minimum residual capacity of the edges along the 
            # path filled by DFS. Or we can say find the maximum flow 
            # through the path found. 
            path_flow = float("Inf") 
            s = sink 
            temp_list = []
            while(s !=  source): 
                path_flow = min (path_flow, self.graph[parent[s]][s]) 
                s = parent[s] 
                if(s!=7 and s!=0):
                    temp_list.append(s)
  
            # Add path flow to overall flow 
            max_flow +=  path_flow 
            # update residual capacities of the edges and reverse edges 
            # along the path 
            v = sink 
            final_list.append(temp_list)
            while(v !=  source): 
                u = parent[v] 
                self.graph[u][v] -= path_flow 
                self.graph[v][u] += path_flow 
                v = parent[v] 
        return max_flow, final_list
        
"Driver code"
import numpy as np
node_count= input ("Input number of nodes in graph")
node_count = int(node_count)
n = 2*(int(node_count))+2
graph =np.zeros((n,n))
"Define input flow"
for j in range(1,node_count+1):
    graph[0][j]=1
"Define output flow"
for i in range(node_count+1, n-1):
    graph[i][n-1] = 1
"Define graph for algorithm"
while True:
    print ("Enter 0 0 to exit")
    a,b = input ("Enter the values of A and B corresponding to line ").split(' ')
    a,b = int(a), int(b)
    graph[a][b+node_count] = 1
    if a == 0 and b==0:
        break       
"print (graph)"
g = Graph(graph)   
source = 0; sink = n-1
flow, edges = g.FordFulkerson(source, sink) 
print ("The maximum possible flow is %d " % flow ) 
for i in edges:
    print (i[0]-int(node_count),i[1])
