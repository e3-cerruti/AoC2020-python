
class HandheldGameConsole:
    def __init__(self):
        self.instructions_run = []
        self.instructions = None
        self.program_counter = None
        self.accumulator = None
        self.instruction_set = {
            "acc": self.acc,
            "jmp": self.jmp,
            "nop": self.nop
        }

    def acc(self, operands):
        self.accumulator += int(operands[0])
        self.program_counter += 1

    def jmp(self, operands):
        self.program_counter += int(operands[0])

    def nop(self, *_):
        self.program_counter += 1

    def load_program(self, instructions):
        self.instructions = instructions

    def run_program(self):
        self.program_counter = 1
        self.accumulator = 0

        self.instructions_run.clear()

        while True:
            self.instructions_run.append(self.program_counter)
            operation, operands = self.instructions[self.program_counter - 1].split(' ', 1)
            operands = operands.split()

            self.instruction_set[operation](operands)

            if not self.program_counter_valid() or self.program_repeating():
                return

    def program_counter_valid(self):
        return 1 <= self.program_counter <= len(self.instructions)

    def program_repeating(self):
        return self.program_counter in self.instructions_run

    def get_program_counter(self):
        return self.program_counter

    def get_accumulator(self):
        return self.accumulator

    def get_instructions_run(self):
        return self.instructions_run
