from operator import itemgetter


def astarik_traversal(graph, start, goal):
    open = [start]
    close = []
    while open:
        current = open.pop(0)
        if current not in close:
            close = close + [current]
        for node in graph[current[0]]:
            if node not in open and node not in close:
                open = open + [[node[0],close[-1][1]+node[1],node[2]]]
                open.sort(key=lambda element:element[1]+element[2])

        if goalCheck(close,goal):
            break

    return [a[0] for a in close]

def goalCheck(close,goal):
    for element in close:
        if goal in element:
            return True
    return False

graph = {'Arad': [['Zerind', 75, 374], ['Timisoara', 118, 329], ['Sibiu', 140, 253]],
         'Zerind': [['Oradea', 71, 380], ['Arad', 75, 366]],
         'Oradea': [['Zerind', 71, 374], ['Sibiu', 151, 253]],
         'Sibiu': [['Rimniciu Vilcea', 80, 193], ['Fagaras', 99, 176], ['Arad', 140, 366],['Oradea', 151, 380]],
         'Fagaras': [['Sibiu', 99, 253], ['Bucharest', 211, 0]],
         'Rimniciu Vilcea': [['Pitesti', 97, 100], ['Craiova', 146, 160], ['Sibiu', 80, 253]],
         'Timisoara': [['Lugoj', 111, 244], ['Arad', 118, 366]],
         'Lugoj': [['Mehadia', 70, 241], ['Timisoara', 111, 329]],
         'Mehadia': [['Lugoj', 70, 244], ['Dobreta', 75, 242]],
         'Dobreta': [['Mehadia', 75, 241], ['Craiova', 120, 160]],
         'Pitesti': [['Craiova', 138, 160], ['Bucharest', 101, 0]],
         'Craiova': [['Pitesti', 138, 100], ['Dobreta', 120, 242], ['Rimniciu Vilcea', 146, 193]],
         'Bucharest': [['Giurgiu', 90, 77], ['Urziceni', 85, 80], ['Fagaras', 211, 178], ['Pitesti', 101, 100]],
         'Giurgiu': [['Bucharest', 90, 0]],
         'Urziceni': [['Vaslui', 142, 199], ['Hirsova', 98, 151], ['Bucharest', 85, 0]],
         'Vaslui': [['Lasi', 92, 226], ['Urziceni', 142, 80]],
         'Lasi': [['Neamt', 87, 234], ['Vaslui', 92, 199]],
         'Neamt': [['Lasi', 87, 226]],
         'Hirsova': [['Eforie', 86, 161], ['Urziceni', 98, 80]],
         'Eforie': [['Hirsova', 86, 151]], }

print('The sequence of cities visited while searching for path between nodes ''Arad'' and ''Bucharest'' is ')

print(astarik_traversal(graph, ['Arad',0, -1], 'Bucharest'))
