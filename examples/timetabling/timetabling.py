

from constraint import Problem, AllDifferentConstraint

# Check http://www.csc.fi/oppaat/f95/python/talot.py


def solve():
    problem = Problem()
    for i in range(1, 4):
        problem.addVariable("name%s" % i, ["Maier", "Huber", "Müller", "Schmid"])
        problem.addVariable("room%d" % i, ["1", "2", "3", "4"])
        problem.addVariable("subjects%d" % i, ["deutsch", "englisch", "mathe", "physik"])


    problem.addConstraint(
        AllDifferentConstraint(), ["color%d" % i for i in range(1, 6)]
    )
    problem.addConstraint(
        AllDifferentConstraint(), ["nationality%d" % i for i in range(1, 6)]
    )
    problem.addConstraint(
        AllDifferentConstraint(), ["drink%d" % i for i in range(1, 6)]
    )
    problem.addConstraint(
        AllDifferentConstraint(), ["smoke%d" % i for i in range(1, 6)]
    )
    problem.addConstraint(AllDifferentConstraint(), ["pet%d" % i for i in range(1, 6)])

    for i in range(1, 6):

        # Hint 1 Done
        problem.addConstraint(
            lambda name, room: name != "Maier" or room != "4",
            ("name%d" % i, "room%d" % i ),
        )

        #Hint 2
        problem.addConstraint(
            lambda name, subject: name != "Maier" or subject == "deutsch",
            ("name%d" %i, "room%d" % i),
        )

        #Hint 3
        if i > i < 5:
            problem.addConstraint(
                lambda namea, nameb, rooma, roomb:
                    (namea != "Schmid" or nameb != "Müller") and
                    (namea != "Müller" or nameb != "SChmid") and
                    abs(rooma - roomb) > 1,
                ("room%d" % (i-1), "room%d" % i, "name%d" % (i-1), "name%d" % i)
            )

        #Hint 4
        problem.addConstraint(
            lambda name, subject: name != "Huber" or subject == "mathe",
            ("name%d" % i, "subject%d" % i),
        )

        #Hint 5
        problem.addConstraint(
            lambda subject, room: subject != "physik" or room == "4",
            ("subject%d" % i, "room%d" % i),
        )

        #Hint6
        problem.addConstraint(
            lambda subjecta, subjectb, room:
                (subjecta != "deutsch" or room != "1") and
                (subjectb != "englisch" or room != "1")
            ("subject%d" % i, "subject%d" % i, "room%d" % i),
        )

    solutions = problem.getSolutions()
    return solutions


def showSolution(solution):
    for i in range(1, 6):
        print("House %d" % i)
        print("--------")
        print("Nationality: %s" % solution["nationality%d" % i])
        print("Color: %s" % solution["color%d" % i])
        print("Drink: %s" % solution["drink%d" % i])
        print("Smoke: %s" % solution["smoke%d" % i])
        print("Pet: %s" % solution["pet%d" % i])
        print("")


def main():
    solutions = solve()
    print("Found %d solution(s)!" % len(solutions))
    print("")
    for solution in solutions:
        showSolution(solution)


if __name__ == "__main__":
    main()
