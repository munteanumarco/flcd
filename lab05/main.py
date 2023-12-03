from grammar import Grammar

if __name__ == '__main__':
    g = Grammar()
    g.readFromFile("resources/g1.txt")
    while True:
        print("0. Exit")
        print("1. State of the Grammar")
        print("2.Check if CFG")
        print("3. Production Set for a Non-Terminal")
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