from grammar import Grammar
from item import Item
from lr0_parser import Parser

def test_closure():
    grammar = Grammar()
    grammar.readFromFile("resources/test.txt")
    grammar.make_enhanced_grammar()
    parser = Parser(grammar)
    initial_item = Item("S'", ["S"], 0)
    closure_state = parser.closure([initial_item])

    expected_items = [
        Item("S'", ["S"], 0),
        Item("S", ["a", "A"], 0),
    ]
    for item in expected_items:
        assert item in closure_state.closure
    print("test_clousure passed")

def test_goto():
    grammar = Grammar()
    grammar.readFromFile("resources/test.txt")
    parser = Parser(grammar)

    initial_item = Item("S", ["a", "A"], 0)
    closure_state = parser.closure([initial_item])
    goto_state_a = parser.goto(closure_state, "a")
    assert Item("S", ["a", "A"], 1) in goto_state_a.closure
    assert Item("A", ["b", "A"], 0) in goto_state_a.closure
    assert Item("A", ["c"], 0) in goto_state_a.closure 
    print("test_goto passed")

def run_all_tests():
    test_closure()
    test_goto()

