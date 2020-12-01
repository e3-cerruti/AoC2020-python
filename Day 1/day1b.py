def main():
    numbers = []
    f = open("input.txt", "r")
    numbers = [int(i) for i in f.readlines()]

    for n in solve(numbers):
        print(n)


def solve(numbers):
    for i1, n1 in enumerate(numbers):
        if n1 > 2020:
            continue
        for i2, n2 in enumerate(numbers[i1 + 1:]):
            if n1 + n2 > 2020:
                continue
            for n3 in numbers:
                if n1 + n2 + n3 == 2020:
                    print(n1, n2, n3)
                    yield n1 * n2 * n3


if __name__ == '__main__':
    main()