from parser.grammar import Grammar
from parser.lr0_parser import Parser
from parser.parser_output import ParserOutput
from parser.test_lr0_parser import run_all_tests

def print_menu():
    menu_options = {
        "0": "Exit",
        "1": "State of the Grammar",
        "2": "Check if CFG",
        "3": "Production Set for a Non-Terminal",
        "4": "Print canonical collection",
        "5": "Run tests for lr0 parser",
        "6": "Create parsing table"
    }

    for key, value in menu_options.items():
        print(f"{key}. {value}")

if __name__ == '__main__':
    g = Grammar()
    g.read_from_file("g1.in")
    g.make_enhanced_grammar()
    parser = Parser(g)
    parser.create_canonical_collection()
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
            for state in parser.canonical_collection:
                print(state)
        if option == '5':
            run_all_tests()
        if option == '6':
            parser.create_parsing_table()
            parser.print_parsing_table()
            output_band = parser.parse_sequence(['a', 'b', 'b', 'c'])
            print(output_band)
            parserOutput = ParserOutput(output_band, g)
            parserOutput.compute_parsing_tree()
            for item in parserOutput.parsing_tree:
                print(item)
            parserOutput.print_to_file("out1.txt")
