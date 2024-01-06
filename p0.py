import pandas as pd
import json

df=pd.read_json('level0.json')
#print(df.head())
#print(df.tail())
x = df["restaurants"].mode()[0]
#print('x',x['neighbourhood_distance'])
#df["restaurants"].fillna(x, inplace = True) 
df=df.drop('restaurants',axis=1)
df=df.drop('vehicles',axis=1)
df=df.drop('n_neighbourhoods',axis=1)
df=df.drop('n_restaurants',axis=1)
df.dropna(inplace=True)
#print(df.tail())
m=[]
r = x['neighbourhood_distance']
#m.append(x['neighbourhood_distance'])
for i in df['neighbourhoods']:
    m.append(i['distances'])

r.append(0)
#print(r)
m.append(r)
for i in range(len(r)-1):
    m[i].append(r[i])
#print(len(m))
#print(len(m[0]))
#print('m')
#print(m)

def nearest_neighbor(graph, start_node):
    num_nodes = len(graph)
    unvisited_nodes = set(range(num_nodes))
    current_node = start_node
    #path = [current_node]
    path=[]

    while unvisited_nodes:
        nearest_neighbor = min(unvisited_nodes, key=lambda node: graph[current_node][node])
        path.append(nearest_neighbor)
        unvisited_nodes.remove(nearest_neighbor)
        current_node = nearest_neighbor

    path.append(start_node)
    return path

l=len(m)-1
start_node = l
shortest_path = nearest_neighbor(m, start_node)
#print(shortest_path)
for i in range(len(shortest_path)):
    if shortest_path[i]==20:
        shortest_path[i]="r0"
    else:
        shortest_path[i]="n"+str(shortest_path[i])
print(shortest_path)

d={"path":shortest_path}
#print(d)
d1={"v0":d}
#print(d1)

with open("sample.json", "w") as outfile: 
    json.dump(d1, outfile)

#{"v0": {"path": ["r0", "n0", "n1", "n2", "n3", "n4", "n5", "n6", "n7", "n8", "n9", "r0"]}}
    
#{"path": ["r0", "n13", "n8", "n3", "n16", "n1", "n18", "n9", "n14", "n17", "n4", "n15", "n10", "n12", "n6", "n7", "n19", "n5", "n0", "n11", "n2", "r0"]}