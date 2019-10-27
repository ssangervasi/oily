'''
https://projecteuler.net/problem=601
'''
import functools
import logging
import math
import pathlib
import textwrap

logger = logging.getLogger(__spec__.name)

def main(argv):
	setup_logging(argv)
	
	description = textwrap.dedent(solve.__doc__)
	print(description)
	logger.info(description)

	solution = solve()
	
	solution_description = f'Solution: {solution}'
	print(solution_description)
	logger.info(solution_description)

def setup_logging(argv):
	log_level = None
	if '--info' in argv:
		log_level = logging.INFO
	elif '--debug' in argv:
		log_level = logging.DEBUG

	if log_level is not None:
		logging.basicConfig(level=log_level, format='%(levelname)s %(asctime)s %(message)s')
		log_path = pathlib.Path(__file__).parent.parent / 'logs' / f'{__spec__.name}.log'
		logger.addHandler(logging.FileHandler(log_path))

def solve() -> int:
	'''
	Sum of the number of streaks of size `i` in range `4^i` for `1 <= i <= 31`.
	'''
	return sum(
		(
			number_of_streaks_in_range(streak_size=i, range_end=(4 ** i))
			for i in range(1, 32)
		)
	)

def number_of_streaks_in_range(streak_size: int, range_end: int) -> int:
	'''
	`number_of_streaks_in_range(streak_size, range_end) = P(s, N)`
		=> The number of integers `n`, where `1 <= n <= N`, for which `streak(n) = s`.
	'''
	logger.info('number_of_streaks_in_range(streak_size=%i, range_end=%i)', streak_size, range_end)
	result = 0
	first_ending = None

	# All streak ends are at jumps of LCM.
	lcm = least_common_multiple(range(1, streak_size + 1))
	logger.debug('streak_size=%i, lcm=%i', streak_size, lcm)

	for ending_at in range(streak_size, range_end + 1, lcm):
		if is_streak(ending_at=ending_at, streak_size=streak_size):
			first_ending = ending_at
			break
	else:
		# Some streak sizes are impossible, such as 5.
		logger.debug('streak_size=%i => %i', streak_size, result)
		return result

	logger.debug('streak_size=%i, first_ending=%i', streak_size, first_ending)

	for ending_at in range(first_ending, range_end + 1, lcm):
		if is_streak(ending_at=ending_at, streak_size=streak_size):
			result += 1

	logger.info('streak_size=%i => %i', streak_size, result)

	return result

def is_streak(ending_at: int, streak_size: int) -> bool:
	# Streak does not end here if the next number continues the streak.
	if is_divisible(ending_at + 1, streak_size + 1):
		return False

	# Step backwards because higher streaks are less common, which will let
	# us return earlier for high numbers:
	for back_step in range(0, streak_size):
		earlier_streak_number = ending_at - back_step
		earlier_streak_size = streak_size - back_step
		if not is_divisible(earlier_streak_number, earlier_streak_size):
			return False

	return True

def is_divisible(dividend: int, divisor: int) -> bool:
	return (dividend % divisor) == 0

def least_common_multiple(nums: 'List[int]') -> int:
	def lcm_of_pair(a, b):
		return (a * b) // math.gcd(a, b)

	return functools.reduce(lcm_of_pair, nums)

if __name__ == '__main__':
	import sys
	main(sys.argv)
