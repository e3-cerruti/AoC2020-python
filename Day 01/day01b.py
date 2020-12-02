def main():
    f = open("input.txt", "r")
    numbers = [int(i) for i in f.readlines()]

    values = [(n1, n2, 2020 - (n1 + n2)) for i1, n1 in enumerate(numbers)
              for i2, n2 in enumerate(numbers[i1 + 1:])
              if 2020 - (n1 + n2) in numbers[i2 + 1:]]

    if len(values) == 1:
        (n1, n2, n3) = values[0]
        print(n1 * n2 * n3)
    else:
        print("Something went wrong.")


if __name__ == '__main__':
    main()
