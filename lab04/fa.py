class FiniteAutomaton:
    def __init__(self):
        self.states = set()
        self.alphabet = set()
        self.transitions = {}
        self.initial_state = None
        self.final_states = set()
    
    def read_from_file(self, file_name):
        with open(file_name, 'r') as file:
            self.states = set(file.readline().strip().split())
            self.alphabet = set(file.readline().strip().split())

            for line in file:
                parts = line.strip().split()
                if len(parts) == 3:
                    state_from, symbol, state_to = parts
                    if (state_from, symbol) in self.transitions:
                        self.transitions[(state_from, symbol)].add(state_to)
                    else:
                        self.transitions[(state_from, symbol)] = {state_to}
                elif len(parts) == 1 and self.initial_state is None:
                    self.initial_state = parts[0]
                elif len(parts) == 1:
                    self.final_states.add(parts[0])

    def accepts(self, sequence):
        current_state = self.initial_state
        for symbol in sequence:
            if (current_state, symbol) in self.transitions:
                current_state = next(iter(self.transitions[(current_state, symbol)]))
            else:
                return False
        return current_state in self.final_states
    
    def is_deterministic(self):
        for _, value in self.transitions.items():
            if len(value) > 1:
                return False
        return True

    def display(self):
        print("States:", self.states)
        print("Alphabet:", self.alphabet)
        print("Transitions:")
        for key, value in self.transitions.items():
            print(f"  {key[0]} -> {key[1]} -> {value}")
        print("Initial State:", self.initial_state)
        print("Final States:", self.final_states)
