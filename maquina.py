import yaml

class Tape:
    def __init__(self, input_string, blank_symbol):
        # Inicializa la cinta con la cadena de entrada y el símbolo en blanco
        self.tape = list(input_string)
        self.head_position = 0
        self.blank_symbol = blank_symbol

    def move_head(self, direction):
        # Mueve la cabeza de la cinta hacia la izquierda o hacia la derecha
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
        # Escribe un símbolo en la posición actual de la cabeza de la cinta
        self.tape[self.head_position] = symbol

    def read_symbol(self):
        # Lee el símbolo en la posición actual de la cabeza
        return self.tape[self.head_position]

class TuringMachine:
    def __init__(self, config_file):
        # Inicializa la Máquina de Turing cargando la configuración desde un archivo YAML
        self.load_configuration(config_file)
        self.current_state = self.initial_state
        self.tape = None

    def load_configuration(self, config_file):
        # Carga la configuración desde el archivo YAML
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

    def load_input(self, input_string):
        # Carga una cadena de entrada en la Máquina de Turing
        self.tape = Tape(input_string, self.blank_symbol)
        self.current_state = self.initial_state

    def step(self):
        # Realiza un paso en la simulación de la Máquina de Turing
        current_symbol = self.tape.read_symbol()
        for rule in self.delta:
            if rule['params']['initial_state'] == self.current_state and rule['params']['tape_input'] == current_symbol:
                new_state = rule['output']['final_state']
                new_symbol = rule['output']['tape_output']
                displacement = rule['output']['tape_displacement']
                self.tape.write_symbol(new_symbol)
                self.tape.move_head(displacement)
                return self.current_state, current_symbol, new_state, new_symbol, displacement
        # Usa una excepción personalizada para manejar transiciones no válidas
        raise Exception("No valid transition found.")

    def get_full_tape_state(self):
        # Obtiene el estado completo de la cinta (estado actual + contenido de la cinta)
        return f"{self.current_state}{''.join(self.tape.tape)}"

    def run(self):
        # Ejecuta la Máquina de Turing hasta que alcanza un estado final
        snapshots = []
        # Agrega el estado inicial y la cinta antes de cualquier transición
        snapshots.append(self.get_full_tape_state())
        while self.current_state not in self.final_states:
            state_before, symbol_read, new_state, symbol_written, movement = self.step()
            # Agrega el estado y la cinta después de cada transición
            snapshots.append(f"{state_before}{''.join(self.tape.tape)} - {new_state}{''.join(self.tape.tape)}")
            self.current_state = new_state
        # Determina si la cadena es aceptada y quita los caracteres de cinta en blanco
        is_accepted = self.current_state in self.accept_state
        final_tape_output = ''.join(self.tape.tape).rstrip(self.blank_symbol)
        return is_accepted, final_tape_output, snapshots

# Ejemplo de uso del código
input_string = 'aaabbaa'
tm = TuringMachine('alteradora.yaml')
tm.load_input(input_string)
result, tape_output, process_steps = tm.run()
print("Cinta de entrada:\n" + input_string)
print("\nPasos de la Máquina de Turing:")
for step in process_steps:
    print(step)
print("\n")
print("Resultado de la Máquina de Turing:\n" + tape_output)
print("\nCadena aceptada: " + ("Sí" if result else "No"))


#cadenas  a probar
#abbbb
#abbabb
#baaaa
#aaabbaa
