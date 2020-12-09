from HandheldGameConsole.machine import HandheldGameConsole


def swap(instructions, candidate):
    operation, operand = instructions[candidate - 1].split(' ')
    if operation == 'jmp':
        instructions[candidate - 1] = 'nop ' + operand
    elif operation == 'nop':
        instructions[candidate - 1] = 'jmp ' + operand


def main():
    with open("input.txt", "r") as f:
        instructions = f.read().splitlines()

    console = HandheldGameConsole()
    console.load_program(instructions)
    console.run_program()
    print(console.get_accumulator())

    possibly_corrupted = console.get_instructions_run()

    for current_test in possibly_corrupted:
        if instructions[current_test -1][0:3] == "acc":
            continue

        swap(instructions, current_test)
        console.load_program(instructions)
        console.run_program()
        program_counter = console.get_program_counter()
        if program_counter >= len(instructions):
            print(console.get_accumulator())
            break
        swap(instructions, current_test)


if __name__ == '__main__':
    main()