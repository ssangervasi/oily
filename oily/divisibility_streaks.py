'''
https://projecteuler.net/problem=601
'''
import functools
import heapq
import logging

logger = logging.getLogger('oily.divisibility_streaks')

def solve() -> int:
	'''
	Sum of the number of streaks of size `i` in range `4^i` for `1 <= i <= 31`.
	'''
	sum(
		(
			number_of_streaks_in_range(streak_size=i, range_end=(4 ** i))
			for i in range(1, 32)
		)
	)

description = solve.__doc__

def number_of_streaks_in_range(streak_size: int, range_end: int) -> int:
	'''
	`number_of_streaks_in_range(streak_size, range_end) = P(s, N)`
		=> The number of integers `n`, where `1 <= n <= N`, for which `streak(n) = s`.
	'''
	logger.debug('number_of_streaks_in_range(%i, %i)', streak_size, range_end)
	result = sum(
		1 if streak(n) == streak_size else 0
		for n in range(1, range_end + 1)
	)
	log_cache_stats()
	return result

def streak_with_cache(maxsize=128):
	n_to_streak = {}
	streak_heap = []
	
	def streak_with_cache_instance(n: int) -> int:
		if n in n_to_streak:
			return n_to_streak[n]
		
		streak_n = streak_without_cache(n)

		n_to_streak[n] = streak_n
		heapq.heappush(streak_heap, (streak_n, n))
		if maxsize < len(heapq):
			_, lowest_priority_n = heapq.heappop(streak_heap)
			del n_to_streak[lowest_priority_n]

		return streak_n

	return streak_with_cache_instance

def streak_without_cache(n: int) -> int:
	'''
	`streak(n) = k = streak_size`
		=> The smallest positive integer `k` such that `n + k` is not divisible by `k + 1`.
	'''
	# This is an upper bound on `k` because `n + (n + 1)` is not divisible by `n + 1`.
	upper_bound = n + 1
	for streak_size in range(1, upper_bound):
		divisor = streak_size + 1
		if is_not_divisble(n + streak_size, divisor):
			break
	return streak_size

streak = streak_with_cache()

def is_not_divisble(dividend: int, divisor: int) -> bool:
	return (dividend % divisor) != 0

def log_cache_stats():
	logger.debug('BEGIN: Cache Stats')
	logger.debug(cache_stats(streak))
	# logger.debug(cache_stats(is_not_divisble))
	logger.debug('END: Cache Stats')

def cache_stats(func):
	info = func.cache_info()
	hit_ratio = info.hits / (info.hits + info.misses)
	fill_ratio = info.currsize / (info.maxsize)
	return f'{func.__name__}: {hit_ratio:%} hits | {fill_ratio:%} full'
