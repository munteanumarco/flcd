from parser.grammar import Grammar
from parser.lr0_parser import Parser
from parser.parser_output import ParserOutput
from parser.test_lr0_parser import run_all_tests

from scanner.language_lexical import LanguageLexical
from scanner.token_identifier import TokenIdentifier

def final_lab_parsing():
    lexical = LanguageLexical()
    token_identifier = TokenIdentifier(lexical)

    print("Analyzing p2...")
    p1_source = open("examples/p1.in", "r")
    token_identifier.read_tokens(p1_source)

    tokens = []
    for item in token_identifier.Pif.Tokens:
        tokens.append(item[0])

    g = Grammar()
    g.read_from_file("g2.in")
    print(g)
    g.make_enhanced_grammar()
    parser = Parser(g)
    parser.create_canonical_collection()
    for state in parser.canonical_collection:
        print(state)

    parser.create_parsing_table()

    print(parser.parsing_table)

    output_band = parser.parse_sequence(tokens)
    print(output_band)

    parserOutput = ParserOutput(output_band, g)
    parserOutput.compute_parsing_tree()
    for item in parserOutput.parsing_tree:
        print(item)

    parserOutput.print_to_file("out2.txt")



def print_menu():
    menu_options = {
        "0": "Exit",
        "1": "State of the Grammar",
        "2": "Check if CFG",
        "3": "Production Set for a Non-Terminal",
        "4": "Print canonical collection",
        "5": "Run tests for lr0 parser",
        "6": "Create parsing table",
        "7": "Final parser run for program",
    }

    for key, value in menu_options.items():
        print(f"{key}. {value}")

if __name__ == '__main__':
    g = Grammar()
    g.read_from_file("g1.in")
    g.make_enhanced_grammar()
    parser = Parser(g)
    while True:
        print_menu()
        option = input("Option is:")
        if option == '0': 
            break
        if option == '1':
            print(str(g))
        if option == '2':
            if g.checkCFG():
                print("The grammar is a CFG")
            else:
                print("The grammar is not a CFG")
        if option == '3':
            key = input("Key is:")
            print(g.get_production_of_non_terminal(key))
        if option == '4':
            parser.create_canonical_collection()
            for state in parser.canonical_collection:
                print(state)
        if option == '5':
            run_all_tests()
        if option == '6':
            parser.create_canonical_collection()
            parser.create_parsing_table()
            parser.print_parsing_table()
            output_band = parser.parse_sequence(['a', 'b', 'b', 'c'])
            print(output_band)
            parserOutput = ParserOutput(output_band, g)
            parserOutput.compute_parsing_tree()
            for item in parserOutput.parsing_tree:
                print(item)
            parserOutput.print_to_file("out1.txt")

        if option == '7':
            final_lab_parsing()