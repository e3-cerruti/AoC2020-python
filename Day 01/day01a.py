def main():
    with open("input.txt", "r") as f:
        numbers = [int(i) for i in f.readlines()]
    values = [(n, 2020 - n) for i, n in enumerate(numbers) if 2020 - n in numbers[i+1:]]

    if len(values) == 1:
        (n1, n2) = values[0]
        print(n1 * n2)
    else:
        print("Something went wrong.")


if __name__ == '__main__':
    main()
