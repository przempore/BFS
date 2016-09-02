def BFS(s, Adj):
  level = {s: 0}
  parent = {s: None}
  i = 1
  frontier = [s]
  while frontier:
    next = []
    for u in frontier:
      for v in Adj[u]:
        if v not in level:
          level[v] = i
          parent[v] = u
          next.append(v)
    frontier = next
    print frontier
    i += 1


def main():
    s = 1
    level = {s: 0}
    adj = [[1], [0, 2], [1, 3], [2, 4, 5], [3, 5, 6], [3, 4, 6, 7], [4, 5, 7], [5, 6]]

    BFS(2, adj)



if __name__ == "__main__":
  main()
