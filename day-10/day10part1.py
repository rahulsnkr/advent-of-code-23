import networkx as nx

metal_map = []

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            metal_map.append(line)
        
        rows, cols = len(metal_map), len(metal_map[0])
        graph = nx.Graph()

        for x, line in enumerate(metal_map):
            for y, ch in enumerate(line):
                if ch == 'S':
                    start = (x,y)
                # nort-south edges
                if x > 0 and metal_map[x-1][y] in 'F7|S' and ch in "JL|S":
                    graph.add_edge((x,y), (x-1,y))
                
                # east-west edges
                if y < cols-1 and metal_map[x][y+1] in 'J7-S' and ch in "FL-S":
                    graph.add_edge((x,y), (x,y+1))

        cycle = nx.find_cycle(graph, start)
        print(len(cycle) // 2)
        