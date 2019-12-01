import cvxpy
from cvxpy import log


def solve_problem(matrix):
    """
    Using max sum log because it's Parrto Efficient and without jealousy to distribute m resource to n agents.
    :param matrix: a list of agents, the each agent is a list of his preferences of every resource.
    :return: nothing, Void.
    """
    # -- the number of agents and number of resources
    n = len(matrix)
    m = len(matrix[0])

    # -- the amount of resources every agent gets from every resource (a list of lists of variables)
    resources = [[cvxpy.Variable() for _ in range(m)] for _ in range(n)]

    # -- the constraints
    constraints = []
    # for every agent
    for i in range(n):
        # every amount of resource
        for resource in resources[i]:
            # amount of resource must be >= 0
            constraints.append(0 <= resource)
            # amount of resource must be <= 1
            constraints.append(resource <= 1)
    # the sum of the amount of one resource must be 1
    for i in range(m):
        constraints.append(sum([resources[j][i] for j in range(n)]) == 1)

    # -- the objective function to maximize (sum logs of var*agent's preference for every resource for every agent)
    objective_function = sum([log(sum([matrix[i][j] * resources[i][j] for j in range(m)])) for i in range(n)])

    # -- the problem
    problem = cvxpy.Problem(objective=cvxpy.Maximize(objective_function), constraints=constraints)

    # -- solve the problem
    problem.solve()

    # -- calc the string to print and print it
    for i in range(n):
        to_print = f"Agent #{i+1} gets"
        resource = resources[i]
        for j in range(len(resource)):
            if j == 0:
                to_print += ' '
            else:
                to_print += ", "
            to_print += f'{resource[j].value:.4f} of resource #{j+1}'
        to_print += '.'
        print(to_print)


def test():
    """Test my function with known right solution to problems"""
    # the first problem to test with
    print("Problem #1:\n")
    print("19 0 81")
    print("0 20 80")

    # the right solution
    x = cvxpy.Variable()
    y = cvxpy.Variable()
    prob = cvxpy.Problem(
        cvxpy.Maximize(log(81 * x + 19) + log(80 * (1 - x) + 20)),
        [0 <= x, x <= 1])
    prob.solve()
    print("\nSuppose to be:")
    print(f"Agent #1 gets 1.0000 of resource #1, 0.0000 of resource #2, {x.value:.4f} of resource #3.")
    print(f"Agent #2 gets 0.0000 of resource #1, 1.0000 of resource #2, {1 - x.value:.4f} of resource #3.")
    # my function's solution
    print("\nMy Function:")
    solve_problem([[19, 0, 81], [0, 20, 80]])

    # the seconf problem
    print("\n\nProblem #2:\n")
    print("19 0 0 81")
    print("0 20 0 80")
    print("0 0 40 60")
    x = cvxpy.Variable()
    y = cvxpy.Variable()
    z = cvxpy.Variable()
    prob = cvxpy.Problem(
        objective=cvxpy.Maximize(log(81 * x + 19) + log(80 * y + 20) + log(60 * z + 40)),
        constraints=[0 <= x, x <= 1, 0 <= y, y <= 1, 0 <= z, z <= 1, x + y + z == 1])
    prob.solve()
    print("\nSuppose to be:")
    print(
        f"Agent #1 gets 1.0000 of resource #1, 0.0000 of resource #2, 0.0000 of resource #3, {x.value:.4f} of resource #4.")
    print(
        f"Agent #2 gets 0.0000 of resource #1, 1.0000 of resource #2, 0.0000 of resource #3, {y.value:.4f} of resource #4.")
    print(
        f"Agent #3 gets 0.0000 of resource #1, 0.0000 of resource #2, 1.0000 of resource #3, {z.value:.4f} of resource #4.")
    # my function's solution
    print("\nMy Function:")
    solve_problem([[19, 0, 0, 81], [0, 20, 0, 80], [0, 0, 40, 60]])


def ex1():
    """Solve The Given Problem With My Function"""
    # the problem matrix
    matrix = [[81, 19, 0], [80, 0, 20]]
    # let the function solve the problem
    solve_problem(matrix)


ex1()
