import collections
import re


def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    slopes = [(1,1), (3, 1), (5, 1), (7, 1), (1, 2)]
    width = len(lines[0])
    height = len(lines)
    product = 1

    for slope in slopes:
        position = (0, 0)
        trees = 0

        # while position[1] < height:
        #     if lines[position[1]][position[0] % width] == '#':
        #         trees += 1
        #     position = tuple(sum(i) for i in zip(position, slope))

        for y in range(0, height, slope[1]):
            x = (y // slope[1]) * slope[0] % width;
            if lines[y][x] == '#':
                trees += 1

        print(f'Trees: {trees} on slope {slope}')
        product *= trees

    print(f'Product of slopes: {product}')


if __name__ == '__main__':
    main()
