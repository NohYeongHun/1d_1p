def solution(n, graph):
    visited = [False for _ in range(n + 1)]
    cnt = 0

    def dfs(node, visited):
        visited[node] = True
        for n in graph[node]:
            if not visited[n]:
                dfs(n, visited)

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, visited)
            cnt += 1
    print(cnt)
    return


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)
    solution(n, graph)
