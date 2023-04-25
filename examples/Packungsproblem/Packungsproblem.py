from array import array

from constraint import Problem, AllDifferentConstraint, InSetConstraint


def solve():
    problem = Problem()

    rectangles = [
        (6, 4),
        (8, 1),
        (4, 1),
        (5, 2),
        (2, 2),
        (3, 2),
    ]

    container_width = 7
    container_height = 8

    j = 1
    for sizes in rectangles:

        rect = compute_value(sizes[0], sizes[1])
        i = 1
        for comb in rect:
            print("j: " + str(j) + " i: " + str(i))
            problem.addVariable("r" + str(j) + "." + str(i), comb)
            i = i + 1

        j = j + 1
    # Add Constraints


    solutions = problem.getSolutions()
    return solutions


def compute_value(width, height):
    a_list = []
    pos = [0, 1, 2, 3]
    for x in range(1, (9 - width)):
        pos[0] = x
        pos[2] = (x + width - 1)
        for y in range(1, (10 - height)):
            pos[1] = y
            pos[3] = (y + height - 1)
            print(pos)
            a_list.append(tuple(pos))

    for x in range(1, (9 - height)):
        pos[0] = x
        pos[2] = (x + height - 1)
        for y in range(1, (10 - width)):
            pos[1] = y
            pos[3] = (y + width - 1)
            a_list.append(tuple(pos))

    print(a_list)
    return a_list


def main():
    solutions = solve()
    print("Found %d solution(s)!" % len(solutions))
    print("")
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
