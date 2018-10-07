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
# Culled by hand for algebraically equivalent or similar operations
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



[print("lambda a,b,c,d: ((a{0}b){1}c){2}d,".format(s[3],s[6],s[9])) for s in type1]

type2 = [
    "((x*x)/(x*x))
    "((x*x)*(x/x))
    "((x*x)+(x*x))
    "((x*x)-(x*x))
    "((x*x)/(x/x))
    "((x/x)/(x*x))
    "((x/x)*(x/x))
    "((x*x)+(x/x))
    "((x*x)/(x+x))
    "((x/x)*(x+x))
    "((x+x)/(x*x))
    "((x*x)-(x/x))
    "((x*x)/(x-x))
    "((x/x)-(x*x))
    "((x/x)*(x-x))
    "((x-x)/(x*x))
    "((x+x)*(x+x))
    "((x*x)-(x+x))
    "((x*x)+(x-x))
    "((x+x)-(x*x))
    "((x+x)*(x-x))
    "((x*x)-(x-x))
    "((x-x)-(x*x))
    "((x-x)*(x-x))
    "((x/x)/(x/x))
    "((x/x)+(x/x))
    "((x/x)/(x+x))
    "((x+x)/(x/x))
    "((x/x)-(x/x))
    "((x/x)/(x-x))
    "((x-x)/(x/x))
    "((x+x)/(x+x))
    "((x/x)-(x+x))
    "((x/x)+(x-x))
    "((x+x)-(x/x))
    "((x+x)/(x-x))
    "((x-x)/(x+x))
    "((x/x)-(x-x))
    "((x-x)-(x/x))
    "((x-x)/(x-x))
    "((x+x)-(x+x))
    "((x+x)+(x-x))
    "((x+x)-(x-x))
    "((x-x)-(x+x))
    "((x-x)+(x-x))
    "((x-x)-(x-x))"]    

[print("lambda a,b,c,d: ((a{0}b){1}(c{2}d),".format(s[3],s[6],s[9])) for s in type2]


    
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