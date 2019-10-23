from oily import risky_moon

solvers = [risky_moon.solve]

if __name__ == '__main__':
    for solve in solvers:
        solution = solve()
        print(solution.description())