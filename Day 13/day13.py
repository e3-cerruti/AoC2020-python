import sys
from functools import reduce


class Bus:
    def __init__(self, identifier, position):
        self.order = position
        self.empty = identifier == 'x'
        if not self.empty:
            self.number = int(identifier)

    def first_departure_after(self, t):
        return self.number, (self.number - t % self.number) % self.number if not self.empty else None

    def departs_in_order_at(self, t):
        return self.number, (t + self.order) % self.number == 0 if not self.empty else None

    def is_empty(self):
        return self.empty

    def __str__(self) -> str:
        return f'Bus: {self.number} at {self.order}'


def main(file):
    with open(file, "r") as f:
        earliest_possible_departure = int(f.readline().strip())
        bus_schedule = f.readline().strip()

    busses = [bus for bus in [Bus(i, p) for (p, i) in enumerate(bus_schedule.split(','))] if not bus.is_empty()]

    departure = min([b.first_departure_after(earliest_possible_departure) for b in busses], key = lambda b: b[1])
    print(f'The earliest departing bus is: {departure[0]} at {departure[1]}.')
    print(f'Result is {departure[0] * departure[1]}.')

    departure = max([bus.number - bus.order for bus in busses])
    depart_in_order = [bus.departs_in_order_at(departure) for bus in busses]
    while not all([depart for number, depart in depart_in_order]):
        step = reduce((lambda x, y: x * y), [number for number, depart in depart_in_order if depart])
        departure += step
        depart_in_order = [bus.departs_in_order_at(departure) for bus in busses]

    print(f'All busses will depart in order at {departure}. {departure == earliest_possible_departure}')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else "test.txt")