
from constraint import Problem, AllDifferentConstraint

# Check http://www.csc.fi/oppaat/f95/python/talot.py


def solve():
    problem = Problem()
    problem.addVariables(["BW","BAY","SARL","RHPF","HES","THU","SAX","SAA","NRW","NS","BER","BRAND","BREM","HAM","SLH","MVP"], range(1, 4))

#CEM SARL -NRW
#STEVE NS -MVP

    #BW
    problem.addConstraint(
       lambda b1,b2,b3,b4: b1 not in [b2,b3,b4], ("BW","BAY","HES","RHPF")
    )

    #BAY
    problem.addConstraint(
        lambda b1,b2,b3,b4,b5: b1 not in[b2,b3,b4,b5], ("BAY","BW","HES","THU","SAX")
    )

    #NS
    problem.addConstraint(
        lambda b1,b2,b3,b4,b5,b6,b7,b8,b9,b10: b1 not in[b2,b3,b4,b5,b6,b7,b8,b9,b10], ("NS","NRW","BREM","HAM","SLH","MVP","BRAND","SAA","THU","HES")
    )
    #BER
    problem.addConstraint(
        lambda b1,b2: b1 not in[b2], ("BER","BRAND")
    )
    #BRAND
    problem.addConstraint(
        lambda b1,b2,b3,b4,b5,b6: b1 not in[b2,b3,b4,b5,b6], ("BRAND","MVP","NS","SAA","SAX","BER")
    )
    #BREM
    problem.addConstraint(
        lambda b1,b2,b3,b4,b5: b1 not in[b2,b3,b4,b5], ("BREM","NS")
    )
    #HAM
    problem.addConstraint(
        lambda b1,b2,b3: b1 not in[b2,b3], ("HAM","SLH","NS")
    )
    #SLH
    problem.addConstraint(
        lambda b1,b2,b3,b4: b1 not in[b2,b3,b4], ("SLH","HAM","NS","MVP")
    )
    #MVP
    problem.addConstraint(
        lambda b1,b2,b3,b4: b1 not in[b2,b3,b4], ("MVP","BRAND","NS","SLH")
    )


    solutions = problem.getSolutions()
    return solutions


def showSolution(solution):
    for i in range(1,5):
        print("Room %d:" % i)
        print("")



def main():
    solutions = solve()
    print("Found %d solution(s)!" % len(solutions))
    print("")
    for solution in solutions:
        print(solution)




if __name__ == "__main__":
    main()
