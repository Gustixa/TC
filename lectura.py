import yaml

# Ruta al archivo YAML
archivo_yaml = 'prueba.yaml'

# Leer el archivo YAML
with open(archivo_yaml, 'r') as archivo:
    datos = yaml.safe_load(archivo)

# Acceder a los datos necesarios para la simulación
q_states = datos['q_states']
alphabet = datos['alphabet']
tape_alphabet = datos['tape_alphabet']
delta = datos['delta']
simulation_strings = datos['simulation_strings']

# A continuación, puedes implementar la simulación de la máquina de Turing utilizando estos datos.
# Aquí hay un ejemplo muy simplificado de cómo podrías hacerlo:

def simular_maquina_turing(cadena):
    estado_actual = q_states['initial']
    cinta = list(cadena)
    cabeza = 0  # Posición inicial de la cabeza en la cinta

    while estado_actual != q_states['final']:
        simbolo_actual = cinta[cabeza]
        transicion_encontrada = False

        # Buscar una transición que coincida con el estado actual y el símbolo actual en delta
        for transicion in delta:
            if (
                transicion['params']['initial_state'] == estado_actual and
                transicion['params']['tape_input'] == simbolo_actual
            ):
                # Aplicar la transición
                cinta[cabeza] = transicion['params']['output']['mem_cache_value']
                estado_actual = transicion['params']['output']['final_state']

                # Mover la cabeza de la cinta
                if transicion['params']['output']['tape_displacement'] == 'R':
                    cabeza += 1
                elif transicion['params']['output']['tape_displacement'] == 'L':
                    cabeza -= 1

                transicion_encontrada = True
                break

        if not transicion_encontrada:
            # Si no se encontró una transición válida, la máquina de Turing se bloquea
            break

    # Comprobar si la simulación llegó al estado final
    if estado_actual == q_states['final']:
        print("La máquina de Turing ha aceptado la cadena.")
    else:
        print("La máquina de Turing se ha bloqueado o ha rechazado la cadena.")

# Simular la máquina de Turing con las cadenas de simulación
for cadena in simulation_strings:
    print(f"Simulación para la cadena: {cadena}")
    simular_maquina_turing(cadena)
    print("\n")
