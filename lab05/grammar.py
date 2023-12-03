class Grammar:
    EPSILON = "epsilon"
    STARTING_SYMBOL = "S'"

    def __init__(self, is_enhanced=False):
        self.N = []
        self.T = []
        self.S = ""
        self.P = {}
        self.duplicated_terminal = False
        self.is_enhanced = is_enhanced

    def check_if_grammar_is_enhanced(self):
        if len(self.P[self.S]) != 1:
            return False
        for production in self.P.values():
            for rhs in production:
                if self.S in rhs:
                    return False
        return True

    def make_enhanced_grammar(self):
        if not self.is_enhanced:
            self.N.append(Grammar.STARTING_SYMBOL)
            self.P[Grammar.STARTING_SYMBOL] = [[self.S]]
            self.S = Grammar.STARTING_SYMBOL
            self.is_enhanced = True

    def __processLine(self, line: str):
        return line.strip().split(' ')[2:]
    
    def check_duplicated_terminal(self):
        exist_list = []
        for non_term in self.P:
            for prods in self.P.get(non_term):
                for value in prods:
                    if value in self.T:
                        if value in exist_list:
                            self.duplicated_terminal = True
                        else:
                            exist_list.append(value)

    def readFromFile(self, file_name: str):
        with open(file_name) as file:
            N = self.__processLine(file.readline())
            T = self.__processLine(file.readline())
            S = self.__processLine(file.readline())[0]

            file.readline()

            P = {}
            for line in file:
                split = line.strip().split('->')
                source = split[0].strip()
                sequence = split[1].lstrip(' ')
                sequence_list = []
                for c in sequence.split(' '):
                    sequence_list.append(c)

                if source in P.keys():
                    P[source].append(sequence_list)
                else:
                    P[source] = [sequence_list]

            self.N = N
            self.T = T
            self.S = S
            self.P = P

    def checkCFG(self):
        self.check_duplicated_terminal()
        if self.duplicated_terminal:
            return False
        
        hasStartingSymbol = False
        for key in self.P.keys():
            if key == self.S:
                hasStartingSymbol = True
            if key not in self.N:
                return False
        if not hasStartingSymbol:
            return False
        for production in self.P.values():
            for rhs in production:
                for value in rhs:
                    if value not in self.N and value not in self.T and value != Grammar.EPSILON:
                        return False
        return True

    def get_production_of_non_terminal(self, non_terminal_key):
        values = ''
        values += str(self.P.get(non_terminal_key))
        return values

    def __str__(self):
        result = "Non-terminal symbols = " + str(self.N) + "\n"
        result += "Terminal symbols = " + str(self.T) + "\n"
        result += "Start symbol = " + str(self.S) + "\n"
        result += "Production rules = " + str(self.P) + "\n"
        return result