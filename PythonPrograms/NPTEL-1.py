def count_archipelagos(islands, boat_tours, tours):
    # Create adjacency list
    graph = [[] for _ in range(islands + 1)]
    for u, v in tours:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (islands + 1)

    def dfs(node):
        stack = [node]
        while stack:
            current = stack.pop()
            if not visited[current]:
                visited[current] = True
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
    
    archipelagos = 0
    for i in range(1, islands + 1):
        if not visited[i]:
            dfs(i)
            archipelagos += 1
    
    return archipelagos

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        islands = int(data[index])
        boat_tours = int(data[index + 1])
        index += 2
        
        tours = []
        for _ in range(boat_tours):
            u = int(data[index])
            v = int(data[index + 1])
            tours.append((u, v))
            index += 2
        
        results.append(count_archipelagos(islands, boat_tours, tours))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
