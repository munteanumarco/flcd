import re
import os

from lab02.symbol_table import SymbolTable

class Scanner:
    def __init__(self):
        self.program = ""
        self.tokens = []
        self.reserved_words = []
        self.symbol_table = SymbolTable()
        self.PIF = []
        self.index = 0
        self.current_line = 1
        self.token_positions = {}
        self.read_tokens()

    def set_program(self, program):
        self.program = program

    def read_tokens(self):
        with open(os.path.join(os.path.dirname(__file__), 'lab01', 'Token.in'), "r") as file:
            lines = file.read().splitlines()
            for i, line in enumerate(lines, start=1):
                token = line.split()[0]
                if token in ['int', 'string', 'input', 'output', 'if', 'else', 'while', 'for', 'true', 'false']:
                    self.reserved_words.append(token)
                else:
                    self.tokens.append(token)
                self.token_positions[token] = i

    def parse_spaces(self):
        while self.index < len(self.program) and self.program[self.index].isspace():
            if self.program[self.index] == '\n':
                self.current_line += 1
            self.index += 1

    def is_string_constant(self):
        regex_for_string_constant = re.compile(r'^"[a-zA-z0-9_ ?:*^+=.!]*"')
        match = regex_for_string_constant.match(self.program[self.index:])
        if not match:
            return False

        string_constant = match.group(0)
        if not self.symbol_table.search(string_constant):
            hash = self.symbol_table.insert(string_constant)
        else:
            hash = self.symbol_table.search(string_constant)

        self.index += len(string_constant)
        self.PIF.append(["const", hash])
        return True
    
    def is_int_constant(self):
        regex_for_int_constant = re.compile(r'^[-+]?(\d+)')
        match = regex_for_int_constant.match(self.program[self.index:])
        if not match:
            return False

        if re.compile(r'^[-+]?(\d+)[a-zA-Z]').match(self.program[self.index:]):
            return False

        int_constant = match.group(0)
        if not self.symbol_table.search(int_constant):
            hash = self.symbol_table.insert(int_constant)
        else:
            hash = self.symbol_table.search(int_constant)

        self.index += len(int_constant)
        self.PIF.append(["const", hash])
        return True
    

    def check_valid_identifier(self, possible_identifier, program_substring):
        if possible_identifier in self.reserved_words:
            return False
        if re.compile(r'^[#]?[A-Za-z_][A-Za-z0-9_]*: (int|string)').search(program_substring):
            return True
        return self.symbol_table.search(possible_identifier)

    def is_identifier(self):
        regex_for_identifier = re.compile(r'^([#]?[a-zA-Z_][a-zA-Z0-9_]*)')
        match = regex_for_identifier.match(self.program[self.index:])
        if not match:
            return False
        identifier = match.group(1)

        if not self.check_valid_identifier(identifier, self.program[self.index:]):
            return False

        if not self.symbol_table.search(identifier):
            hash = self.symbol_table.insert(identifier)
        else:
            hash = self.symbol_table.search(identifier)

        self.index += len(identifier)
        self.PIF.append(["identifier", hash])

        return True


    def is_token(self):
        possible_token = self.program[self.index:].split(" ")[0]

        for reserved_token in self.reserved_words:
            if possible_token.startswith(reserved_token):
                regex = f"^[#]?[a-zA-Z0-9_]*{reserved_token}[a-zA-Z0-9_]+"
                if re.compile(regex).search(possible_token):
                    return False
                self.index += len(reserved_token)
                position = self.token_positions[reserved_token]
                self.PIF.append([position, -1])
                return True

        for token in self.tokens:
            if token == possible_token:
                self.index += len(token)
                position = self.token_positions[token]
                self.PIF.append([position, -1])
                return True
            elif possible_token.startswith(token):
                self.index += len(token)
                position = self.token_positions[token]
                self.PIF.append([position, -1])
                return True

        return False


    def parse_token(self):
        self.parse_spaces()
        
        if self.index >= len(self.program):
            return
        for check in [self.is_identifier, self.is_string_constant, self.is_int_constant, self.is_token]:
            if check():
                return

        end_of_token_index = self.index
        while end_of_token_index < len(self.program) and not self.program[end_of_token_index].isspace() and not self.program[end_of_token_index] in {',', '.', ';', ':', '!', '?', '(', ')', '[', ']', '{', '}'}:
            end_of_token_index += 1

        raise Exception(f"Lexical error: invalid token '{self.program[self.index:end_of_token_index] }' at line {self.current_line}, index {self.index}")


    def scan(self, file_name):
        try:
            file_path = os.path.join(os.path.dirname(__file__), 'lab01', 'problems', file_name)
            with open(file_path, 'r') as f:
                self.program = f.read()
            while self.index < len(self.program):
                self.parse_token()
            pif_path = f"out/PIF{file_name.replace('.txt', '.out')}"
            with open(pif_path, "w") as pif_file:
                for token, position in self.PIF:
                    pif_file.write(f"{token} -> {position}\n")
            st_path = f"out/ST{file_name.replace('.txt', '.out')}"
            with open(st_path, "w") as st_file:
                st_file.write(str(self.symbol_table))
            print("Lexically correct")
        except Exception as e:
            print(f"error: {e}")
scanner = Scanner()
scanner.scan("p1.txt")
