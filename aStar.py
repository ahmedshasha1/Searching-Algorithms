Graph_nodes = {
    'A': [('B', 6), ('F', 3)],
    'B': [('A', 6), ('C', 3), ('D', 2)],
    'C': [('B', 3), ('D', 1), ('E', 5)],
    'D': [('B', 2), ('C', 1), ('E', 8)],
    'E': [('C', 5), ('D', 8), ('I', 5), ('J', 5)],
    'F': [('A', 3), ('G', 1), ('H', 7)],
    'G': [('F', 1), ('I', 3)],
    'H': [('F', 7), ('I', 2)],
    'I': [('E', 5), ('G', 3), ('H', 2), ('J', 3)],
}
h={
    'A':10,
    'B':8,
    'C':5,
    'D':7,
    'E':3,
    'F':6,
    'G':5,
    'H':3,
    'I':1,
    'J':0
}



def path_cost(path):
    gCost=0
    for node,cost in path:
        gCost+=cost
    lastNode=path[-1][0]
    fCost=gCost+h[lastNode]
    return fCost,lastNode



def a_Star_Search(graph,start,goal):
    visitted=[]
    queue=[[(start,0)]]
    
    while queue:
        queue.sort(key=path_cost)  
        path=queue.pop(0)
        node=path[-1][0]
        if node in visitted :
            continue
        
        visitted.append(node)
        if node==goal:
            return path
        else:
            adjnodes=graph.get(node,[])
            for node2,cost in adjnodes:
                newPath=path.copy()
                newPath.append((node2,cost))
                queue.append(newPath)



print(a_Star_Search(graph=Graph_nodes,start='A',goal='J'))
                
