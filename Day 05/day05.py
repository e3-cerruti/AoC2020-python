
def main():
    with open("input.txt", "r") as f:
    # with open("test.txt", "r") as f:
        lines = f.read().splitlines()

    highest = 0
    flight = []
    for line in lines:
        row = line[:7]
        seat = line[7:]
        row = row.replace('F', '0').replace('B', '1')
        row = int(row, 2)

        seat = seat.replace('L', '0').replace('R', '1')
        seat = int(seat, 2)

        seat_id = row * 8 + seat
        highest = max(highest, seat_id)
        flight.append(seat_id)


    print(highest)

    previous = None
    my_seat = None
    flight.sort()
    print(flight)
    for seat_id in flight:
        # print(previous, seat_id)
        if previous is None:
            previous = seat_id
            continue
        if seat_id > (previous + 1):
            my_seat = previous + 1
            print(my_seat)
        previous = seat_id


if __name__ == '__main__':
    main()
