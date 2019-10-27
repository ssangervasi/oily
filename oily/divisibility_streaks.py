'''
https://projecteuler.net/problem=601
'''
import functools
import heapq
import logging
import math
import pathlib

logging.basicConfig(level=logging.INFO, format='%(levelname)s %(asctime)s %(message)s')
logger = logging.getLogger('oily.divisibility_streaks_v2')
logger.addHandler(logging.FileHandler(pathlib.Path(__name__).parent.parent / 'logs' / 'oily.divisibility_streaks_v2.log'))


def main():
	logger.info(solve.__doc__)
	solution = solve()
	logger.info(f'solution: {solution}')

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
	first_ending = streak_size

	#	Step by `streak_size` because `(n - 1) + s` must be divisible by `s`.
	for ending_at in range(streak_size, range_end + 1, streak_size):
		if is_streak(ending_at=ending_at, streak_size=streak_size):
			first_ending = ending_at
			break

	# All future streak ends seem to be divisible by LCM
	step_size = least_common_multiple(range(1, streak_size + 1))
	logger.info('streak_size: %i, step_size: %i', streak_size, step_size)
	for ending_at in range(first_ending, range_end + 1, step_size):
		if is_streak(ending_at=ending_at, streak_size=streak_size):
			result += 1

	logger.info('number_of_streaks_in_range(streak_size=%i, range_end=%i) = %i', streak_size, range_end, result)
	return result

def is_streak(ending_at: int, streak_size: int) -> bool:
	logger.debug('is_streak(ending_at=%i, streak_size=%i)', ending_at, streak_size) 

	# Streak does not end here if the next number continues the streak.
	if is_divisible(ending_at + 1, streak_size + 1):
		logger.debug('=> False - next number would continue streak')
		return False

	# Step backwards because higher streaks are less common, which will let
	# us return earlier for high numbers:
	for back_step in range(0, streak_size):
		earlier_streak_number = ending_at - back_step
		earlier_streak_size = streak_size - back_step
		if not is_divisible(earlier_streak_number, earlier_streak_size):
			logger.debug('=> False - %i breaks streak of size %i', earlier_streak_number, earlier_streak_size)
			return False

	logger.debug('=> True')
	return True

def is_divisible(dividend: int, divisor: int) -> bool:
	return (dividend % divisor) == 0

def least_common_multiple(nums):
	def lcm_of_pair(a, b):
		return (a * b) // math.gcd(a, b)

	return functools.reduce(lcm_of_pair, nums)

if __name__ == '__main__':
	main()
