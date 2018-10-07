from itertools import permutations, combinations_with_replacement

# list the numbers to use here
numbahs = [2,4,6,8]
# enter the number to calculate here
ansah = 24

numberlist = input("Enter a list of four integers, separated by commas [default: 2,4,6,8]: ")
if numberlist:
    numbahs = [int(n) for n in numberlist.split(',')]
answer = input("Enter a number compute to [default: 24]: ")
if answer:
    ansah = int(answer)

# ways of combining arguments with parenthesis
pgroups = [
    "{0}{1}{2}{3}{4}{5}{6}",
    "({0}{1}{2}){3}{4}{5}{6}",
    "({0}{1}{2}{3}{4}){5}{6}",
    "(({0}{1}{2}){3}{4}){5}{6}",
    "({0}{1}({2}{3}{4})){5}{6}",
    "{0}{1}({2}{3}{4}){5}{6}",
    "{0}{1}({2}{3}({4}{5}{6}))",
    "{0}{1}(({2}{3}{4}){5}{6})",
    "{0}{1}({2}{3}{4}{5}{6})",
    "{0}{1}{2}{3}({4}{5}{6})",
]

operators = ['*','/','+','-']

#for o in combinations_with_replacement(operators, 3):
#    print o

solncount = 0
solnlist = set()
for p in pgroups: # for every combination of parenthesis
    for n in permutations(numbahs):  # and every permutation of numbers
        for c in combinations_with_replacement(operators, 3): # and every combination of operators
            for o in permutations(c):
                s = p.format(n[0],o[0],n[1],o[1],n[2],o[2],n[3]) # construct the expression and...
                # Evaluate, but don't give up and cry when you divide by zero
                try:
                    if eval(s) == ansah:
                        solnlist.add(s)
                except:
                    pass

print ("There were {0} solutions:".format(len(solnlist)))
for s in solnlist:
    print (s)
