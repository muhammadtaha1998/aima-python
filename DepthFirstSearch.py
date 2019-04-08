def dfs_traversal(graph, start,goal):
    closed = []
    opened = [start]
    while opened:
        node = opened.pop(0)
        if node not in closed and node not in opened:
            closed = closed + [node]
            opened = graph[node] + opened
            if goal in closed:
                print("Reached")
                break
    return closed

cityGraph = {
    'Arad':['Zerind','Sibiu','Timisoara'],
    'Bucharest':['Fagaras','Pitesti','Urziceni','Giurgiu'],
    'Craivoa':['Rimnicu Vilcea','Pitesti','Dobreta'],
    'Dobreta':['Mehadia','Craiova'],
    'Eforie':[],
    'Fagaras':['Sibiu','Bucharest'],
    'Giurgiu':[],
    'Hirsova':['Urziceni','Eforie'],
    'Iasi':['Neamt','Vaslui'],
    'Lugoj':['Timisoara','Mehadia'],
    'Mehadia':['Lugoj','Dobreta'],
    'Neamt':[],
    'Oradea':['Zerind','Sibiu'],
    'Pitesti':['Rimnicu Vilcea','Bucharest','Craiova'],
    'Rimnicu Vilcea':['Sibiu','Pitesti','Craiova'],
    'Sibiu':['Oradea','Arad','Fagaras','Rimnicu Vilcea'],
    'Timisoara':['Arad','Lugoj'],
    'Urziceni':['Vaslui','Hirsova','Bucharest'],
    'Vaslui':['Iasi','Urziceni'],
    'Zerind':['Oradea','Arad']
}
