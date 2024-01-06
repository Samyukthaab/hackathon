import pandas as pd
import json

df=pd.read_json('level1a.json')
#print(df.head())
#print(df.tail())
x = df["restaurants"].mode()[0]
y = df["vehicles"].mode()[0]
#print('x',x['neighbourhood_distance'])
#df["restaurants"].fillna(x, inplace = True) 
df=df.drop('restaurants',axis=1)
df=df.drop('vehicles',axis=1)
df=df.drop('n_neighbourhoods',axis=1)
df=df.drop('n_restaurants',axis=1)
df.dropna(inplace=True)
#print('processed')
#print(df.head())
#print(df.tail())
#print(x)
#print(y)

m=[]
order=[]
r = x['neighbourhood_distance']
max_cap = y['capacity']
#m.append(x['neighbourhood_distance'])
for i in df['neighbourhoods']:
    m.append(i['distances'])
    order.append(i['order_quantity'])
r.append(0)
order.append(0)
#print(order)
#print(len(order))
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
    #considered = set(range(num_nodes))
    #print(unvisited_nodes)
    current_node = start_node
    #print(current_node)
    #path = [current_node]
    paths=[]
    cap=0
    path=[]

    while unvisited_nodes:
        considered = unvisited_nodes.copy()
        while(considered):
            #print("while ", unvisited_nodes)
            #print("while ", considered)
            nearest_neighbor = min(considered, key=lambda node: graph[current_node][node])
            #print(nearest_neighbor)
            cap+=order[nearest_neighbor]
            #print(cap)
            if cap<=max_cap:
                path.append(nearest_neighbor)
                considered.remove(nearest_neighbor)
                current_node = nearest_neighbor
            else:
                considered.remove(nearest_neighbor)
        print(path)
        #print(unvisited_nodes)
        for i in path:
            unvisited_nodes.remove(i)
        #print(unvisited_nodes)
        paths.append(path)
        path=[]
        cap=0


    #path.append(start_node)
    return paths

l=len(m)-1
start_node = l
paths = nearest_neighbor(m, start_node)
#print(paths)
for path in paths:
    for j in range(len(path)):
        if path[j]==20:
            path[j]="r0"
        else:
            path[j]="n"+str(path[j])
#print(paths)
d={}
for i in range(len(paths)):
    key="path"+str(i+1)
    d[key]=paths[i]
#print(d)
d1={"v0":d}
print(d1)

with open("sample1.json", "w") as outfile: 
    json.dump(d1, outfile)
