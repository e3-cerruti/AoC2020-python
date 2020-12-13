known_paths = {}

def main():
    with open("test1.txt", "r") as f:
        adapters = [int(i) for i in f.readlines()]

    part1(adapters)
    part2(adapters)


def part1(adapters):
    adapters.sort()
    jolts = 0
    gaps = [0, 0, 0, 1]
    for adapter in adapters:
        gaps[adapter - jolts] += 1
        jolts = adapter

    print(gaps)

    print(gaps[1] * gaps[3])


def part2(adapters):
    adapters.append(0)
    adapters.sort()
    paths = 1

    prev = False
    for adapter in adapters:
        next_adapter = [p for p in range(adapter + 1, adapter + 4) if p in adapters]
        print(paths, adapter, next_adapter)
        if prev:
            paths *= max(1, len(next_adapter) - 1)
        else:
            paths *= max(1, len(next_adapter))
        prev = len(next_adapter) == 3

    print(paths)


def part2r(adapters):
    adapters.append(0)
    adapters.sort()
    tree = {}

    for adapter in adapters:
        possibilities = []
        for next_adapter in range(adapter + 1, adapter + 4):
            if next_adapter in adapters:
                possibilities.append(next_adapter)
        tree[adapter] = possibilities

    print(tree)

    paths = number_of_paths(tree, 0)

    print(paths)


def number_of_paths(tree, node):
    if not tree[node]:
        return 1

    if node in known_paths.keys():
        return known_paths[node]

    paths = 0
    for child in tree[node]:
        paths += number_of_paths(tree, child)

    known_paths[node] = paths
    return paths


if __name__ == '__main__':
    main()
