from os.path import join, dirname
from pathlib import Path
from collections import defaultdict

def find_outer(data, minimum, target, collector):
    for color in data:
        if target in data[color] and data[color][target] >= minimum:
            # print(f'{color} bags contain: {data[color][target]} {target} bags')
            collector.add(color)
            find_outer(data, 1, color, collector)
    return collector

def count_bags(data, minimum, target):
    colors = find_outer(data, minimum, target, set())
    return len(colors)

def parse_inner_value(val):
    val = val.split('bags')[0].strip()
    pieces = val.split(' ')
    res = ' '.join(pieces[1:])
    res = res.split('bag')[0].strip()
    return pieces[0].strip(), res

def parse_inner(val):
    res = {}
    for group in val.split(', '):
        count, color = parse_inner_value(group)
        if color in res:
            raise Exception(f'unexpected state')
        if count == 'no':
            count = '0'
        res[color] = int(count)
    return res

def parse_outer(val):
    return val.split('bags')[0].strip()

def construct_input(data):
    table = defaultdict(list)
    for line in data:
        [outer, inner] = line.split(' contain ')
        outer = parse_outer(outer)
        print(outer)
        table[outer] = parse_inner(inner)
    return table

if __name__ == "__main__":
    from os.path import join, dirname
    data = Path(join(dirname(__file__), './input.txt')).open().read()
    data = construct_input(data.split('\n'))
    answer = count_bags(data, 1, 'shiny gold')
    print(answer)
