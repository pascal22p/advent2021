import sys
from collections import Counter

test_input = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

test_large_input = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

expected = """start,HN,dc,HN,end
start,HN,dc,HN,kj,HN,end
start,HN,dc,end
start,HN,dc,kj,HN,end
start,HN,end
start,HN,kj,HN,dc,HN,end
start,HN,kj,HN,dc,end
start,HN,kj,HN,end
start,HN,kj,dc,HN,end
start,HN,kj,dc,end
start,dc,HN,end
start,dc,HN,kj,HN,end
start,dc,end
start,dc,kj,HN,end
start,kj,HN,dc,HN,end
start,kj,HN,dc,end
start,kj,HN,end
start,kj,dc,HN,end
start,kj,dc,end"""

expected_data = []
for line in expected.strip().splitlines():
    expected_data.append(line.split(","))

with open('input') as f:
    input = f.read().rstrip()

def get_edges(input):
    edges = []
    for line in input.strip().splitlines():
        sides = line.split("-")
        edges.append((sides[0], sides[1]))
    return edges

def parse_input(input):
    paths = {}
    for line in input.strip().splitlines():
        sides = line.split("-")
        if sides[0] in paths:
            if sides[1] not in paths[sides[0]]:
                paths[sides[0]].append(sides[1])
        else:
            paths[sides[0]] = [sides[1]]
        if sides[1] in paths:
            if sides[0] not in paths[sides[1]]:
                paths[sides[1]].append(sides[0])
        else:
            paths[sides[1]] = [sides[0]]

    return paths

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in edges:
            if start in self.graph_dict:
                if end not in self.graph_dict[start]:
                    self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
            if end in self.graph_dict:
                if start not in self.graph_dict[end]:
                    self.graph_dict[end].append(start)
            else:
                self.graph_dict[end] = [start]

    def get_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node.upper() == node or node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths

    def get_paths2(self, start, end, path=[]):
        def check_counts(path, node):
            counts = Counter(path)
            if node in counts:
                counts[node] += 1

            if counts[node] == 3:
                return False
            if counts["start"] == 2:
                return False
            if counts["end"] == 2:
                return False

            total = 0
            for item, count in counts.items():
                if item.lower() == item and count > 1:
                    total += 1

            return total < 2


        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node.upper() == node or check_counts(path, node):
                new_paths = self.get_paths2(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths

graph = Graph(get_edges(test_input))
paths = graph.get_paths("start", "end")

for path_expected in expected_data:
    assert path_expected in paths
for path in paths:
    assert path in paths

graph = Graph(get_edges(test_large_input))
paths = graph.get_paths("start", "end")
assert len(paths) == 226, "Number of paths should be 226"

# Part 1
graph = Graph(get_edges(input))
paths = graph.get_paths("start", "end")
print("Part 1 result: %d"%len(paths))
print()
print()

# Part 2
graph = Graph(get_edges(test_large_input))
paths = graph.get_paths2("start", "end")
print("Part 2 Number of paths: %d"%len(paths))
assert len(paths) == 3509, "Number of paths should be 3509"

graph = Graph(get_edges(input))
paths = graph.get_paths2("start", "end")
print("Part 2 result: %d"%len(paths))
