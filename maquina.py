import yaml

class Tape:
    def __init__(self, input_string, blank_symbol):
        self.tape = list(input_string)
        self.head_position = 0
        self.blank_symbol = blank_symbol
    def move_head(self, direction):
        if direction == 'R':
            self.head_position += 1
            if self.head_position >= len(self.tape):
                self.tape.append(self.blank_symbol)
        elif direction == 'L':
            self.head_position -= 1
            if self.head_position < 0:
                self.head_position = 0
                self.tape.insert(0, self.blank_symbol)

    def write_symbol(self, symbol):
        self.tape[self.head_position] = symbol

    def read_symbol(self):
        return self.tape[self.head_position]
