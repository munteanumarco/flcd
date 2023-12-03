import itertools


class State:
    id = itertools.count()

    def __init__(self, closure_items, closure):
        self.id = next(self.id)
        self.closure_items = closure_items
        self.closure = closure

    def get_all_symbols_after_dot(self):
        result = []
        for item in self.closure:
            if item.dotPosition < len(item.rhs):
                result.append(item.rhs[item.dotPosition])
        return result

    def __eq__(self, other):
        return self.closure_items == other.closure_items

    def __str__(self):
        result = "s" + str(self.id) + " = closure({"
        for item in self.closure_items:
            result += str(item) + ", "
        result = result[:-2] + "}) = {"
        for item in self.closure:
            result += str(item) + ", "
        result = result[:-2] + "}"
        return result