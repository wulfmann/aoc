from os.path import join, dirname
from pathlib import Path

def part_one(data):
    accumulator = 0
    processed = set()

    index = 0
    while index < len(data):
        if index in processed:
            return None

        processed.add(index)
        instruction = data[index]

        operation, argument = instruction.split(' ')
        argument = int(argument)

        if operation == 'jmp':
            index += argument
            continue

        index += 1
        if operation == 'nop':
            continue
        elif operation == 'acc':
            accumulator += argument

    return accumulator

def part_two(data):
    for i, instruction in enumerate(data):
        mutated_data = data.copy()
        operation, argument = instruction.split(' ')

        if operation == 'acc':
            continue

        operation = 'jmp' if operation == 'nop' else 'nop'
        mutated_data[i] = f'{operation} {argument}'

        res = part_one(mutated_data)
        if res is not None:
            return res

if __name__ == "__main__":
    from os.path import join, dirname
    data = Path(join(dirname(__file__), './input.txt')).open().read()
    answer = part_two(data.splitlines())
    print(answer)
