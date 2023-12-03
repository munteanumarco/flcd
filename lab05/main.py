from grammar import Grammar
from lr0_parser import Parser

if __name__ == '__main__':
    g = Grammar()
    g.readFromFile("resources/g1.txt")
    g.make_enhanced_grammar()
    parser = Parser(g)
    parser.create_canonical_collection()
    while True:
        print("0. Exit")
        print("1. State of the Grammar")
        print("2. Check if CFG")
        print("3. Production Set for a Non-Terminal")
        print("4. Print canonical collection")
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