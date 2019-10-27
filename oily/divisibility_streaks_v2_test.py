import pytest

from . import divisibility_streaks_v2 as divisibility_streaks

class Test_number_of_streaks_in_range:
	@pytest.mark.parametrize(
		'example', [
			{ 'streak_size': 3, 'range_end': 14, 'expected': 1 },
			{ 'streak_size': 6, 'range_end': (10 ** 6), 'expected': 14_286 },
		]
	)
	def test_parametrized_examples(self, example):
		assert divisibility_streaks.number_of_streaks_in_range(
			example['streak_size'],
			example['range_end'],
		) == example['expected']

	def test_example_to_optimize(self):
		result = divisibility_streaks.number_of_streaks_in_range(8, (4 ** 8))		
		assert result == 52


class Test_is_streak:
	@pytest.mark.parametrize(
		'example', [
			{ 'ending_at': 2, 'streak_size': 1, 'expected': True },
			{ 'ending_at': 2, 'streak_size': 2, 'expected': False },
			{ 'ending_at': 16, 'streak_size': 4, 'expected': True },
		]
	)
	def test_parametrized_examples(self, example):
		assert divisibility_streaks.is_streak(
			ending_at=example['ending_at'],
			streak_size=example['streak_size'],
		) == example['expected']
