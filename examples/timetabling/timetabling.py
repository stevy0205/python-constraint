
from constraint import Problem, AllDifferentConstraint

# Check http://www.csc.fi/oppaat/f95/python/talot.py


def solve():
    problem = Problem()
    problem.addVariables(["Maier", "Huber", "Müller", "Schmid"], range(1, 5))
    problem.addVariables(["deutsch", "englisch", "mathe", "physik"], range(1, 5))

    problem.addConstraint(
        AllDifferentConstraint(), ["name%d" % i for i in range(1, 5)]
    )
    problem.addConstraint(
        AllDifferentConstraint(), ["subject%d" % i for i in range(1, 5)]
    )



    # Hint 1 Done

    problem.addConstraint(
        lambda name: name != "Maier",
    )

    # Hint 2
    problem.addConstraint(
        lambda name, subject: name != "Maier" or subject == "deutsch", (f"name{i}", f"subject{i}")
        #lambda name, subject: name != "Maier" or subject == "deutsch",
        #("name%d" % i, "subject%d" % i)
    )

    # Hint 3
    if 1 > i < 4:
        problem.addConstraint(
            lambda namea, nameb, namec:
            namea != "Schmid" or (nameb != "Müller" and namec != "Müller"),
            ("name%d" % i, "name%d" % (i-1), "name%d" % (i+1)),
        )
    elif i == 1:
        problem.addConstraint(
            lambda namea, nameb:
            namea != "Schmid" or nameb != "Müller",
            ("name%d" % i, "name%d" % (i+1)),
        )
    else :
        problem.addConstraint(
            lambda namea, nameb:
            namea != "Schmid" or nameb != "Müller",
            ("name%d" % i, "name%d" % (i-1)),
        )

    # Hint 4
    problem.addConstraint(
        lambda name, subject: name != "Huber" or subject == "Mathe",
        ("name%d" % i, "subject%d" % i),
    )

    # Hint 5
    if i == 4:
        problem.addConstraint(
            lambda subject: subject == "physik",
            ("subject%d" % i),
        )

    # Hint6
    if i == 1:
        problem.addConstraint(
            lambda subjecta, subjectb: subjecta != "deutsch" and subjectb != "englisch",
            ("subject%d" % i, "subject%d" % i),
        )

    solutions = problem.getSolutions()
    return solutions


def showSolution(solution):
    for i in range(1, 5):
        #print("room %d" % i)
        print("--------")
        print("subject: %s" % solution["subject%d" % i])
        print("name: %s" % solution["name%d" % i])
        print("")


def main():
    solutions = solve()
    print("Found %d solution(s)!" % len(solutions))
    print("")
    for solution in solutions:
        showSolution(solution)


if __name__ == "__main__":
    main()
