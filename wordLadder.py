from collections import deque

from Graph import Graph


def build_graph(wordfile):
    buckets = {}
    G = Graph()
    with open(wordfile, 'r') as f:
        for line in f:
            word = line.strip()
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i + 1:]
                if bucket in buckets:
                    buckets[bucket].append(word)
                else:
                    buckets[bucket] = [word]

    for adj in buckets.values():
        for word1 in adj:
            for word2 in adj:
                if word1 != word2:
                    G.add_edge(word1, word2)

    return G


def BFS(graph, start):
    queue = deque()
    start_vertex = graph.get_vertex(start)
    start_vertex.predecessor = None
    start_vertex.distance = 0
    start_vertex.color = 'gray'
    queue.append(start_vertex)

    while queue:
        current = queue.popleft()
        for adj in current.get_connections():
            if adj.color == 'white':
                adj.color = 'gray'
                adj.predecessor = current
                adj.distance = current.distance + 1
                queue.append(adj)
        current.color = 'black'


def traverse(end):
    while end:
        print(end.key)
        end = end.predecessor


if __name__ == '__main__':
    G = build_graph('word.txt')
    BFS(G, 'fool')
    traverse(G.get_vertex('sage'))
