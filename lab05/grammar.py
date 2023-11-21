class Grammar:
    EPSILON = "epsilon"

    def __init__(self):
        self.N = []
        self.T = []
        self.S = ""
        self.P = {}

    def __processLine(self, line: str):
        return line.strip().split(' ')[2:]

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

    def __str__(self):
        result = "Non-terminal symbols = " + str(self.N) + "\n"
        result += "Terminal symbols = " + str(self.T) + "\n"
        result += "Start symbol = " + str(self.S) + "\n"
        result += "Production rules = " + str(self.P) + "\n"
        return result