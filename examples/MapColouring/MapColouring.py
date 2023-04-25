from constraint import Problem, AllDifferentConstraint
from enum import Enum


# Check http://www.csc.fi/oppaat/f95/python/talot.py


BW = "Baden-Württemberg"
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
MVP = "Mecklenburg-Vorpommern"


def solve():
    problem = Problem()
    problem.addVariables(
        [BW, BAY, SARL, RHPF, HES, THU, SAX, SAA, NRW, NS, BER,
         BRAND, BREM, HAM, SLH, MVP], range(1, 4))

    # CEM SARL -NRW
    # STEVE NS -MVP

    # BW
    problem.addConstraint(
        lambda b1, b2, b3, b4: b1 not in [b2, b3, b4], (BW, BAY, HES, RHPF)
    )

    # BAY
    problem.addConstraint(
        lambda b1, b2, b3, b4, b5: b1 not in [b2, b3, b4, b5], (BAY, BW, HES, THU, SAX)
    )

    # SARL
    problem.addConstraint(
        lambda b1, b2: b1 not in [b2], (SARL, RHPF)
    )

    # PHPF
    problem.addConstraint(
        lambda b1, b2, b3, b4, b5: b1 not in [b2, b3, b4, b5], (RHPF, HES, BW, NRW, SARL)
    )

    # HES
    problem.addConstraint(
        lambda b1, b2, b3, b4, b5, b6, b7: b1 not in [b2, b3, b4, b5, b6, b7],
        (HES, RHPF, BW, BAY, THU, NS, NRW)
    )

    # THU
    problem.addConstraint(
        lambda b1, b2, b3, b4, b5, b6: b1 not in [b2, b3, b4, b5, b6],
        (THU, BAY, SAX, SAA, NS, HES)
    )

    # SAX
    problem.addConstraint(
        lambda b1, b2, b3, b4, b5: b1 not in [b2, b3, b4, b5], (SAX, BAY, THU, SAA, BRAND)
    )

    # SAA
    problem.addConstraint(
        lambda b1, b2, b3, b4, b5: b1 not in [b2, b3, b4, b5], (SAA, THU, SAX, BRAND, NS)
    )

    # NRW
    problem.addConstraint(
        lambda b1, b2, b3, b4: b1 not in [b2, b3, b4], (NRW, RHPF, HES, NS)
    )

    # NS
    problem.addConstraint(
        lambda b1, b2, b3, b4, b5, b6, b7, b8, b9, b10: b1 not in [b2, b3, b4, b5, b6, b7, b8, b9, b10],
        (NS, NRW, BREM, HAM, SLH, MVP, BRAND, SAA, THU, HES)
    )
    # BER
    problem.addConstraint(
        lambda b1, b2: b1 not in [b2], (BER, BRAND)
    )
    # BRAND
    problem.addConstraint(
        lambda b1, b2, b3, b4, b5, b6: b1 not in [b2, b3, b4, b5, b6], (BRAND, MVP, NS, SAA, SAX, BER)
    )
    # BREM
    problem.addConstraint(
        lambda b1, b2: b1 not in [b2], (BREM, NS)
    )
    # HAM
    problem.addConstraint(
        lambda b1, b2, b3: b1 not in [b2, b3], (HAM, SLH, NS)
    )
    # SLH
    problem.addConstraint(
        lambda b1, b2, b3, b4: b1 not in [b2, b3, b4], (SLH, HAM, NS, MVP)
    )
    # MVP
    problem.addConstraint(
        lambda b1, b2, b3, b4: b1 not in [b2, b3, b4], (MVP, BRAND, NS, SLH)
    )

    solutions = problem.getSolutions()
    return solutions


def showSolution(solution):
    for i in range(1, 5):
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
