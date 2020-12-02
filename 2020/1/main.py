from os.path import join, dirname
from pathlib import Path

def find_sum(data, target):
    table = {}
    for idx, current in enumerate(data):
        difference = target - current
        if difference in table:
            return data[table[difference]] * data[idx]
        else:
            table[current] = idx

if __name__ == "__main__":
    from os.path import join, dirname
    data = Path(join(dirname(__file__), './input.txt')).open().read()
    # convert all the strings to ints
    data = [int(d) for d in data.split('\n')]
    answer = find_sum(data, target=2020)
    print(answer)
