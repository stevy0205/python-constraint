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
    problem.addVariable(rectangles[1], [(x, y) for x in range(1, 3) for y in range(1, 6)])
    problem.addVariable(rectangles[2], [(x, y) for x in range(1, 8) for y in range(1, 1)]) #vertikal
    problem.addVariable(rectangles[3], [(x, y) for x in range(1, 5) for y in range(1, 9)])
    problem.addVariable(rectangles[4], [(x, y) for x in range(1, 4) for y in range(1, 8)])
    problem.addVariable(rectangles[5], [(x, y) for x in range(1, 7) for y in range(1, 8)])
    problem.addVariable(rectangles[6], [(x, y) for x in range(1, 6) for y in range(1, 8)])

    problem.addVariable(rectangles[1], [(x, y) for x in range(1, 5) for y in range(1, 4)])
    problem.addVariable(rectangles[3], [(x, y) for x in range(1, 8) for y in range(1, 6)])
    problem.addVariable(rectangles[4], [(x, y) for x in range(1, 7) for y in range(1, 5)])
    problem.addVariable(rectangles[6], [(x, y) for x in range(1, 7) for y in range(1, 7)])

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
