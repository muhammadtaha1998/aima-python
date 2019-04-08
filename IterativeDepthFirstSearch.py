def idfs_traversal(graph, start, i):
    counter = 0
    dph = i
    closed = []
    opened = [start]

    while opened:

        if counter <= i:
            print ('run if')
            node = opened.pop(0)
            if node not in closed and node not in opened:
                closed = closed + [node]
                depth = graph[node][0][0]
                if depth <= i:
                    if len(graph[node][1]) > 0:
                        for ele in range(len(graph[node][1]) - 1, -1, -1):
                            opened = [graph[node][1][ele]] + opened

            counter = counter + 1

        else:
            print ('run else')
            node = opened.pop(0)
            index = graph[node][0][0]
            if index > i:
                if node not in closed:
                    closed = closed + [node]
            else:
                if len(graph[node][1]) >= 0:
                    closed = closed + [node]
                    for ele in range(len(graph[node][1]) - 1, -1, -1):
                        opened = [graph[node][1][ele]] + opened

    return closed


graph = {'A': [[0], ['B', 'C']],
         'B': [[1], ['D', 'E']],
         'C': [[1], ['F', 'G']],
         'D': [[2], ['H']],
         'E': [[2], []],
         'F': [[2], ['I', 'J']],
         'G': [[2], []],
         'H': [[3], ['K']],
         'I': [[3], ['L', 'M']],
         'J': [[3], ['N']],
         'K': [[4], []],
         'L': [[4], []],
         'M': [[4], []],
         'N': [[4], []]
         }

# IDFS Traversal
print('IDFS Traversal')

for i in range(-1, 4):
    print('\nlimit ---------',i+1)
    print(idfs_traversal(graph, 'A', i))
