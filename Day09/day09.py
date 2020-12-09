def main():
    set_length = 25

    with open("input.txt", "r") as f:
        numbers = [int(n) for n in f.read().splitlines()]

    term = 0
    for i, number in enumerate(numbers[set_length:]):
        found = False
        for j in range(i, i + set_length):
            if number - numbers[j] in numbers[j+1:i + set_length]:
                found = True
                break
        if not found:
            print(number)
            term = number
            break

    start = 0
    end = 1

    while (total := sum(numbers[start: end])) != term:
        end += 1
        if total > term or end > len(numbers):
            start += 1
            end = start + 1

    print(min(numbers[start:end]) + max(numbers[start:end]))


if __name__ == '__main__':
    main()
