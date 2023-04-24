
from constraint import Problem, AllDifferentConstraint
from enum import Enum


# Check http://www.csc.fi/oppaat/f95/python/talot.py

class Land(Enum):
    BW = "Baden-Württember"
    BAY = "Bayern"
    SARL = "Saarland"
    RHPF = "Rheinland-Pfalz"
    HES = "Hessen"
    THU = "Thüringen"
    SAX = "Sachsen"
    SAA = "Sachsen-Anhalt"
    NRW = "Nordrhein-Westfalen"
    NS = "Niedersachen"
    BER = "Berlin"
    BRAND = "Brandenburg"
    BREM = "Bremen"
    HAM = "Hamburg"
    SLH = "Schleswig-Holstein"
    MVP= "Mecklenburg-Vorpommern"



def solve():
    problem = Problem()
    problem.addVariables([Land.BW,Land.BAY,Land.SARL,Land.RHPF,Land.HES,Land.THU,Land.SAX,Land.SAA,Land.NRW,Land.NS,Land.BER,Land.BRAND,Land.BREM,Land.HAM,Land.SLH,Land.MVP], range(1, 4))

#CEM SARL -NRW
#STEVE NS -MVP

    #BW
    problem.addConstraint(
       lambda b1,b2,b3,b4: b1 not in [b2,b3,b4], (Land.BW,Land.BAY,Land.HES,Land.RHPF)
    )

    #BAY
    problem.addConstraint(
        lambda b1,b2,b3,b4,b5: b1 not in[b2,b3,b4,b5], (Land.BAY,Land.BW,Land.HES,Land.THU,Land.SAX)
    )

    #SARL
    problem.addConstraint(
        lambda b1,b2: b1 not in[b2], (Land.SARL,Land.RHPF)
    )

    #PHPF
    problem.addConstraint(
        lambda b1,b2,b3,b4,b5: b1 not in[b2,b3,b4,b5], (Land.RHPF,Land.HES,Land.BW,Land.NRW, Land.SARL)
    )

    #HES
    problem.addConstraint(
        lambda b1,b2,b3,b4,b5,b6,b7: b1 not in[b2,b3,b4,b5,b6,b7], (Land.HES,Land.RHPF,Land.BW,Land.BAY,Land.THU,Land.NS,Land.NRW)
    )

    #THU
    problem.addConstraint(
        lambda b1,b2,b3,b4,b5,b6,b7: b1 not in[b2,b3,b4,b5,b6,b7], (Land.THU,Land.BAY,Land.SAX,Land.SAA,Land.NS,Land.HES)
    )
    
    #SAX
    problem.addConstraint(
        lambda b1,b2,b3,b4,b5: b1 not in[b2,b3,b4,b5], (Land.SAX,Land.BAY,Land.THU,Land.SAA,Land.BRAND)
    )

    #SAA
    problem.addConstraint(
        lambda b1,b2,b3,b4,b5: b1 not in[b2,b3,b4,b5], (Land.SAA,Land.THU,Land.SAX,Land.BRAND,Land.NS)
    )

    #NRW
    problem.addConstraint(
        lambda b1,b2,b3,b4: b1 not in[b2,b3,b4], (Land.NRW,Land.RHPF,Land.HES,Land.NS)
    )

    #NS
    problem.addConstraint(
        lambda b1,b2,b3,b4,b5,b6,b7,b8,b9,b10: b1 not in[b2,b3,b4,b5,b6,b7,b8,b9,b10], (Land.NS,Land.NRW,Land.HES,Land.THU,Land.SAA,Land.BRAND,Land.MVP,Land.HAM,Land.SLH, Land.BREM)
    )

    #BER
    problem.addConstraint(
        lambda b1,b2: b1 not in[b2], (Land.BER,Land.BRAND)
    )

    #BRAND
    problem.addConstraint(
        lambda b1,b2,b3,b4,b5,b6: b1 not in[b2,b3,b4,b5,b6], (Land.BRAND,Land.BER,Land.MVP,Land.NS,Land.SAA,Land.SAX)
    )

    #BREM
    problem.addConstraint(
        lambda b1,b2: b1 not in[b2], (Land.BREM,Land.NS)
    )

    #HAM
    problem.addConstraint(
        lambda b1,b2,b3: b1 not in[b2,b3], (Land.HAM,Land.SLH,Land.NS)
    )

    #SLH
    problem.addConstraint(
        lambda b1,b2,b3,b4: b1 not in[b2,b3,b4], (Land.SLH,Land.HAM,Land.MVP,Land.NS)
    )

    #MVP
    problem.addConstraint(
        lambda b1,b2,b3,b4: b1 not in[b2,b3,b4], (Land.MVP,Land.SLH,Land.NS,Land.BRAND)
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
