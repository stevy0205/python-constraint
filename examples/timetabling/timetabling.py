
from constraint import Problem, AllDifferentConstraint

# Check http://www.csc.fi/oppaat/f95/python/talot.py


def solve():
    problem = Problem()
    problem.addVariables(["Maier", "Huber", "Müller", "Schmid"], range(1, 5))
    problem.addVariables(["deutsch", "englisch", "mathe", "physik"], range(1, 5))



    problem.addConstraint(
        AllDifferentConstraint(),["Maier", "Huber", "Müller", "Schmid"]
    )

    problem.addConstraint(
        AllDifferentConstraint(),["deutsch", "englisch", "mathe", "physik"]
    )

    # Hint 1
    problem.addConstraint(
        lambda p: p != 4, ("Maier",)
    )

    # Hint 2
    problem.addConstraint(
        lambda p, f: p == f, ("Müller","deutsch")

    )

    # Hint 3
    problem.addConstraint(
        lambda p1, p2: (abs(p1-p2) > 1), ("Schmid", "Müller")
    )

    # Hint 4
    problem.addConstraint(
        lambda p, f: p == f, ("Huber", "mathe")
    )

    # Hint 5
    problem.addConstraint(
        lambda f: f == 4, ("physik",)
    )

    # Hint6
    problem.addConstraint(
        lambda f1, f2: f1 != 1 and f2 != 1, ("deutsch", "englisch")

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
