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
class TuringMachine:
    def __init__(self, config_file):
        with open(config_file, 'r') as file:
            self.config = yaml.safe_load(file)
        self.states = self.config['q_states']['q_list']
        self.initial_state = self.config['q_states']['initial']
        self.final_states = self.config['q_states']['final']
        self.accept_state = self.config['q_states']['accept']
        self.alphabet = self.config['alphabet']
        self.tape_alphabet = self.config['tape_alphabet']
        self.blank_symbol = self.config['blank']
        self.delta = self.config['delta']
        self.current_state = self.initial_state
        self.tape = None

    def load_input(self, input_string):
        self.tape = Tape(input_string, self.blank_symbol)
        self.current_state = self.initial_state

    def step(self):
        current_symbol = self.tape.read_symbol()
        for rule in self.delta:
            if rule['params']['initial_state'] == self.current_state and rule['params']['tape_input'] == current_symbol:
                new_state = rule['output']['final_state']
                new_symbol = rule['output']['tape_output']
                displacement = rule['output']['tape_displacement']
                self.tape.write_symbol(new_symbol)
                self.tape.move_head(displacement)
                return self.current_state, current_symbol, new_state, new_symbol, displacement
        raise Exception("No valid transition found.")

