def main():
    with open("input.txt", "r") as f:
        numbers = [int(i) for i in f.readlines()]
    values = [n for i, n in enumerate(numbers) if 2020 - n in numbers[i+1:]]

    if len(values) == 1:
        print(values[0] * (2020 - values[0]))
    else:
        print("Something went wrong.")


if __name__ == '__main__':
    main()