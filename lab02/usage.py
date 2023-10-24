from symbol_table import SymbolTable

st = SymbolTable()

def run_tests():
    test_insert()
    test_delete()
    print("Tests passed!")

def test_insert():
    st.insert("variable_name") 
    assert st.search("variable_name") == True

def test_delete():
    st.delete("variable_name")
    assert st.search("variable_name") == False

run_tests()
