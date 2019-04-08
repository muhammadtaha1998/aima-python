from operator import itemgetter


def gbfs_traversal(graph, start, goal):
    open = [start]
    close = []
    while open:
        current = open.pop(0)
        if current not in close:
            close = close + [current[0]]
        for node in graph[current[0]]:
            if node not in open and node not in close:
                open = open + [node]
                open.sort(key=itemgetter(1))
        if goal in close:
            break

    return close


graph = {'Arad': [['Zerind', 374], ['Timisoara', 329], ['Sibiu', 253]],
         'Zerind': [['Oradea', 380], ['Arad', 366]],
         'Oradea': [['Sibiu', 253]],
         'Sibiu': [['Rimniciu Vilcea', 193], ['Fagaras', 178], ['Arad', 366]],
         'Fagaras': [['Sibiu', 253], ['Bucharest', 0]],
         'Rimniciu Vilcea': [['Pitesti', 98], ['Craiova', 160], ['Sibiu', 253]],
         'Timisoara': [['Lugoj', 244], ['Arad', 366]],
         'Lugoj': [['Mehadia', 241]],
         'Mehadia': [['Lugoj', 244], ['Dorbeta', 242]],
         'Dobreta': [['Mehadia', 241], ['Craiova', 160]],
         'Pitesti': [['Craiova', 160], ['Bucharest', 0]],
         'Craiova': [['Pitesti', 98], ['Dobreta', 242], ['Rimniciu Vilcea', 193]],
         'Bucharest': [['Giurgiu', 77], ['Urziceni', 80], ['Fagaras', 178], ['Pitesti', 98]],
         'Giurgiu': [['Bucharest', 0]],
         'Urziceni': [['Vaslui', 199], ['Hirsova', 151], ['Bucharest', 0]],
         'Vaslui': [['Lasi', 226], ['Urziceni', 80]],
         'Lasi': [['Neamt', 234], ['Vaslui', 199]],
         'Neamt': [['Lasi', 226]],
         'Hirsova': [['Eforie', 161], ['Urziceni', 80]],
         'Eforie': [['Hirsova', 151]],
         }

print('The path from Arad to Bucharest using Greedy Best First Search is:\n')
print(gbfs_traversal(graph, ['Arad', -1],'Bucharest'))
