import re


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    valid = 0
    for line in lines:
        # parts = line.split(' ', 3)
        # indices = [int(n) - 1 for n in parts[0].split('-', 2)]
        # letter = parts[1][0]
        # password = parts[2]

        x = re.search(r'(\d+)-(\d+)\s(.):\s(.+)', line)
        indices = [int(n) - 1 for n in [x.group(1), x.group(2)]]
        letter = x.group(3)
        password = x.group(4)

        if (password[indices[0]] == letter) != (password[indices[1]] == letter):
            valid += 1
    print(valid)


if __name__ == '__main__':
    main()
