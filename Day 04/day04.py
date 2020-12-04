import string


def valid_year(year, first, last):
    if len(year) != 4:
        return False

    try:
        numeric_year = int(year)
    except ValueError:
        return  False

    if not first <= numeric_year <= last:
        return False
    return True


def valid_height(height):
    try:
        numeric_height = int(height[:-2])
    except ValueError:
        return False

    if height[-2:] == 'cm' and 150 <= numeric_height <= 193:
        return True
    elif height[-2:] == 'in' and 59 <= numeric_height <= 76:
        return True
    
    return False


def valid_hair(color):
    print(len(color), color)
    if len(color) != 7 or color[0] != '#' or any([c not in string.hexdigits.lower() for c in color[1:]]):
        return False
    return True


def is_valid(document):
    fields = document.split(' ')
    data = dict(field.split(':') for field in fields)

    if all([k not in ['cid', 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] for k in data.keys()]):
        print('Bad fields')
        return False

    k = data.keys()
    if not 7 <= len(k) <= 8:
        print('Bad num fields')
        return False

    if len(k) == 7 and 'cid' in k:
        print('Missing required fields')
        return False

    if not valid_year(data['byr'], 1920, 2002):
        print('Bad byr', data['byr'])
        return False

    if not valid_year(data['iyr'], 2010, 2020):
        print('Bad iyr', data['iyr'])
        return False

    if not valid_year(data['eyr'], 2020, 2030):
        print('Bad eyr', data['eyr'])
        return False

    if not valid_height(data['hgt']):
        print('Bad hgt')
        return False

    if not valid_hair(data['hcl']):
        print('Bad hcl')
        return False
    
    if data['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        print('Bad ecl')
        return False
    
    if len(data['pid']) != 9 or not data['pid'].isnumeric():
        print('Bad pid')
        return False

    return True


def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    valid = 0
    document = ""

    for line in lines:
        if len(line) == 0:
            print(document)
            if is_valid(document.strip()):
                valid += 1
                print(True)
            document = ""
        else:
            document += " " + line

    print(document)
    if is_valid(document.strip()):
        valid += 1
        print(True)

    print(valid)


if __name__ == '__main__':
    main()
