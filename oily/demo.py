import logging

from oily import divisibility_streaks

problems = [divisibility_streaks]

if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG)

	for problem in problems:
		print(problem.description)
		solution = problem.solve()
		print(f'solution: {solution}')
