from collections import deque


def shortest_path(maze, start, target):
    R, C = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    queue = deque()
    queue.append(start)
    visited = [[False] * C for _ in range(R)]
    visited[start[0]][start[1]] = True
    distance = [[float("inf")] * C for _ in range(R)]
    distance[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()

        if (x, y) == target:
            return distance[x][y]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                if maze[nx][ny] != 1 and maze[nx][ny] != 2:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                elif maze[nx][ny] == 3:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1

        if sum(row.count(2) for row in maze) > 2:
            break

    return "STUCK"


# Read the input values
R, C = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(R)]
start = tuple(map(int, input().split()))
target = tuple(map(int, input().split()))

# Call the function to find the shortest path
result = shortest_path(maze, start, target)

# Print the result
print(result)
