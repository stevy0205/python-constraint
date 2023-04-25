from constraint import Problem, AllDifferentConstraint, InSetConstraint


def solve():
    problem = Problem()

    rectangles = [
        {'w': 6, 'h': 4},
        {'w': 8, 'h': 1},
        {'w': 4, 'h': 1},
        {'w': 5, 'h': 2},
        {'w': 2, 'h': 2},
        {'w': 3, 'h': 2},
    ]

    container_width = 7
    container_height = 8

    # Add Variables
    problem.addVariable(rectangles[1], {2, 5})
    problem.addVariable(rectangles[2], {0, 8})
    problem.addVariable(rectangles[3], {4, 8})
    problem.addVariable(rectangles[4], {3, 7})
    problem.addVariable(rectangles[5], {6, 7})
    problem.addVariable(rectangles[6], {5, 7})

    # Add Constraints

    problem.addConstraint(

    )

    solutions = problem.getSolutions()
    return solutions

def main():
    solutions = solve()
    print("Found %d solution(s)!" % len(solutions))
    print("")
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
