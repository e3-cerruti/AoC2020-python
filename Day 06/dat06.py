def main():
    with open("input.txt", "r") as f:
        groups = f.read().split("\n\n")

    # print(sum([len(set(list(group.replace('\n' ,'')))) for group in groups]))
    result = 0
    for group in groups:
        # print("g->" + str(group))
        persons = [set(list(g)) for g in group.split('\n')]

        print("p->" + str(persons))
        size = len(persons[0].intersection(*persons[1:]))
        print(size)
        result += size
    print(result)

        # print(set(list(persons[0]))
        #       .intersection([set(list(person)) for person in persons[1:]]))
    # print([len(set(list(group.replace('\n' ,'')))) for group in groups])


if __name__ == '__main__':
    main()
