import heapq

class Dijkstra:
    def __init__(self, nodes):
        self._nodes = nodes
        self._graph = {node: [] for node in nodes}

    def add_edge(self, n1, n2, distance):
        self._graph[n1].append((n2, distance))
        self._graph[n2].append((n1, distance))

    def remove_edge(self, n1, n2, distance):
        self._graph[n1].remove((n2, distance))
        self._graph[n2].remove((n1, distance))

    def find_distances(self, start_node):
        distances = {}
        for n in self._nodes:
            distances[n] = float("inf")
        distances[start_node] = 0

        queue = []
        heapq.heappush(queue,(0,start_node))
        visited = set()
        while queue:
            node = heapq.heappop(queue)[1]
            if node in visited:
                continue # continue from next in queue if node visited
            visited.add(node)

            for to_node, distance in self._graph[node]:
                new_distance = distances[node] + distance
                if new_distance < distances[to_node]:
                    distances[to_node] = new_distance
                    heapq.heappush(queue, (new_distance, to_node))

        return distances
