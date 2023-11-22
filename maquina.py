import yaml

class Tape:
    def __init__(self, input_string, blank_symbol):
        self.tape = list(input_string)
        self.head_position = 0
        self.blank_symbol = blank_symbol