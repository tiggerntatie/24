from itertools import permutations, combinations_with_replacement


"""
operators = ['*','/','+','-']

opcombos = set()

for c in combinations_with_replacement(operators, 3): # and every combination of operators
    for o in permutations(c):
        opcombos.add(o)

for o in opcombos:  # RPN N1 N2 O1 N3 O2 N4
    print("((x{0}x){1}x){2}x".format(*o))

for o in opcombos:  # RPN N1 N2 O1 N3 N4 O2 O3
    print("((x{0}x){2}(x{1}x))".format(*o))
    
"""    

type1 = [
    "((x*x)*x)*x",
    "((x*x)+x)*x",
    "((x+x)*x)*x",
    "((x*x)-x)*x",
    "((x/x)+x)*x",
    "((x-x)*x)*x",
    "((x/x)-x)*x",
    "((x+x)+x)*x",
    "((x+x)-x)*x",
    "((x-x)-x)*x",
    "((x*x)*x)/x",
    "((x*x)/x)/x",
    "((x*x)+x)/x",
    "((x+x)*x)/x",
    "((x*x)-x)/x",
    "((x-x)*x)/x",
    "((x/x)/x)/x",
    "((x/x)+x)/x",
    "((x+x)/x)/x",
    "((x/x)-x)/x",
    "((x-x)/x)/x",
    "((x+x)+x)/x",
    "((x+x)-x)/x",
    "((x-x)-x)/x",
    "((x*x)*x)+x",
    "((x*x)/x)+x",
    "((x*x)+x)+x",
    "((x+x)*x)+x",
    "((x-x)*x)+x",
    "((x/x)/x)+x",
    "((x/x)+x)+x",
    "((x+x)/x)+x",
    "((x-x)/x)+x",
    "((x+x)+x)+x",
    "((x*x)*x)-x",
    "((x*x)/x)-x",
    "((x*x)+x)-x",
    "((x+x)*x)-x",
    "((x*x)-x)-x",
    "((x-x)*x)-x",
    "((x/x)/x)-x",
    "((x/x)+x)-x",
    "((x+x)/x)-x",
    "((x/x)-x)-x",
    "((x-x)/x)-x",
    "((x+x)+x)-x",
    "((x+x)-x)-x",
    "((x-x)-x)-x"]

    
"""  Culled by hand for algebraically equivalent or similar operations
((x*x)*x)*x
((x*x)*x)/x
((x*x)*x)+x
((x*x)+x)*x
((x+x)*x)*x
((x*x)*x)-x
((x*x)-x)*x
((x-x)*x)*x
((x*x)/x)/x
((x*x)/x)+x
((x*x)+x)/x
((x/x)+x)*x
((x+x)*x)/x
((x*x)/x)-x
((x*x)-x)/x
((x/x)-x)*x
((x-x)*x)/x
((x*x)+x)+x
((x+x)*x)+x
((x+x)+x)*x
((x*x)+x)-x
((x+x)*x)-x
((x+x)-x)*x
((x-x)*x)+x
((x-x)+x)*x
((x*x)-x)-x
((x-x)*x)-x
((x-x)-x)*x
((x/x)/x)/x
((x/x)/x)+x
((x/x)+x)/x
((x+x)/x)/x
((x/x)/x)-x
((x/x)-x)/x
((x-x)/x)/x
((x/x)+x)+x
((x+x)/x)+x
((x+x)+x)/x
((x/x)+x)-x
((x+x)/x)-x
((x+x)-x)/x
((x-x)/x)+x
((x/x)-x)-x
((x-x)/x)-x
((x-x)-x)/x
((x+x)+x)+x
((x+x)+x)-x
((x+x)-x)-x
((x-x)-x)-x
((x*x)/(x*x))
((x*x)*(x/x))
((x*x)+(x*x))
((x*x)-(x*x))
((x*x)/(x/x))
((x/x)/(x*x))
((x/x)*(x/x))
((x*x)+(x/x))
((x*x)/(x+x))
((x/x)+(x*x))
((x/x)*(x+x))
((x+x)/(x*x))
((x+x)*(x/x))
((x*x)-(x/x))
((x*x)/(x-x))
((x/x)-(x*x))
((x/x)*(x-x))
((x-x)/(x*x))
((x-x)*(x/x))
((x+x)*(x+x))
((x*x)-(x+x))
((x*x)+(x-x))
((x+x)-(x*x))
((x+x)*(x-x))
((x-x)+(x*x))
((x-x)*(x+x))
((x*x)-(x-x))
((x-x)-(x*x))
((x-x)*(x-x))
((x/x)/(x/x))
((x/x)+(x/x))
((x/x)/(x+x))
((x+x)/(x/x))
((x/x)-(x/x))
((x/x)/(x-x))
((x-x)/(x/x))
((x+x)/(x+x))
((x/x)-(x+x))
((x/x)+(x-x))
((x+x)-(x/x))
((x+x)/(x-x))
((x-x)+(x/x))
((x-x)/(x+x))
((x/x)-(x-x))
((x-x)-(x/x))
((x-x)/(x-x))
((x+x)-(x+x))
((x+x)+(x-x))
((x+x)-(x-x))
((x-x)-(x+x))
((x-x)+(x-x))
((x-x)-(x-x))


"""