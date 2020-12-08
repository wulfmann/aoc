from os.path import join, dirname
from pathlib import Path

class Graph:
    def __init__(self, graph):
        self.graph = graph

    def count_bags(self, target, minimum=1):
        collector = set()

        queue = [(target, minimum)]
        while len(queue) > 0:
            key, minim = queue.pop(0)

            for node in self.graph:
                if node in collector:
                    continue
                if self.graph[node].get(key, -1) < minim:
                    continue

                collector.add(node)
                queue.append((node, 1))

        return len(collector)

def build_graph_input(raw):
    graph = {}

    def pop_prefix(val, suffix='bags'):
        return val.strip().split(suffix)[0].strip()

    for line in raw:
        # remove periods
        line = line.replace('.', '')

        # split line into outer and inner
        [outer, inner] = line.split(' contain ')
        outer = pop_prefix(outer)

        if not outer in graph:
            graph[outer] = {}

        for bag in inner.split(', '):
            bag = pop_prefix(bag).split(' ')
            count, color = bag[0], ' '.join(bag[1:])
            color = pop_prefix(color, 'bag')

            if color == 'other':
                continue

            count = 0 if count == 'no' else int(count)

            graph[outer][color] = count

    return graph

if __name__ == "__main__":
    from os.path import join, dirname
    data = Path(join(dirname(__file__), './input.txt')).open().read()
    data = build_graph_input(data.splitlines())

    graph = Graph(data)
    answer = graph.count_bags('shiny gold', 1)
    print(answer)
