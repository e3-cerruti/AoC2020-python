class Bag:
    def __init__(self, color):
        self.color = color
        self.comprised_of = {}
        self.contained_by = []

    def list_bags(self, parent, seen):
        for bag in parent.contained_by:
            if not bag in seen:
                seen.append(bag)
                self.list_bags(bag, seen)


def main():
    with open("test.txt", "r") as f:
        rules = f.read().splitlines()

    bags = {}

    for rule in rules:
        color = rule[:rule.find(" bags contain ")]
        if color in bags.keys():
            outside_bag = bags.get(color)
        else:
            outside_bag = Bag(color)
            bags[color] = outside_bag

        for inner_bag_description in rule[rule.find(" bags contain ") + 14:].split(','):
            if inner_bag_description != "no other bags":
                parts = inner_bag_description.split(' ')
                print(parts[0])
                count = int(parts[0])
                inner_bag_color = parts[1:3]

                if inner_bag_color in list(bags.keys()):
                    inner_bag = bags.get(inner_bag_color)
                else:
                    inner_bag = Bag(inner_bag_color)
                    bags[inner_bag_color] = inner_bag

                inner_bag.contained_by.append(outside_bag)
                outside_bag.comprised_of[inner_bag] = count

    shiny_gold = bags["shiny gold"]
    seen = []
    Bag.list_bags(shiny_gold, seen)
    print(len(seen))






if __name__ == '__main__':
    main()
