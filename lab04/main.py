from fa import FiniteAutomaton


def run():
    fa = FiniteAutomaton()
    filename = input("Enter the filename: ")
    fa.read_from_file(filename)
    print("The FA is deterministic." if fa.is_deterministic() else "The FA is nondeterministic.")

    while True:
        print("\nMenu")
        print("1. Display FA")
        print("2. Check if a sequence is accepted by the FA")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            fa.display()
        elif choice == '2':
            sequence = input("Enter the sequence: ")
            print("Accepted" if fa.accepts(sequence) else "Not Accepted")
        elif choice == '3':
            break

if __name__ == "__main__":
    run()