from array import array

from constraint import Problem, AllDifferentConstraint, InSetConstraint


def compute_value(width, height):
    a_list = []
    pos = [0, 1, 2, 3]
    for x in range(1, (9 - width)):
        pos[0] = x
        pos[2] = (x + width - 1)
        for y in range(1, (10 - height)):
            pos[1] = y
            pos[3] = (y + height - 1)

            a_list.append(tuple(pos))

    for x in range(1, (9 - height)):
        pos[0] = x
        pos[2] = (x + height - 1)
        for y in range(1, (10 - width)):
            pos[1] = y
            pos[3] = (y + width - 1)
            a_list.append(tuple(pos))

    return a_list


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

    i = 1
    for rect in rectangles:
        string = "r" + str(i)
        print(string)
        problem.addVariable(string, compute_value(rect[0], rect[1]))
        i = i + 1

    print("hey")

    # Add Constraints
    for i in range(1, 7):
        for j in range(1, 7):
            if j > i:
                problem.addConstraint(
                    lambda r1, r2: no_overlap(r1, r2), ("r%d" % i, "r%d" % j)
                )

    solutions = problem.getSolutions()
    return solutions


def no_overlap(tuple1, tuple2):
    # Calculate bounding boxes of the two rectangles
    x1_min, y1_min, x1_max, y1_max = tuple1
    x2_min, y2_min, x2_max, y2_max = tuple2

    for x in range(x1_min,x1_max+1):
        if (x2_min <= x  <= x2_max):
            for y in range(y1_min,y1_max+1):
                if(y2_min <= y <= y2_max):
                    return False
    return True


def main():
    solutions = solve()
    print("Found %d solution(s)!" % len(solutions))
    print("")
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
