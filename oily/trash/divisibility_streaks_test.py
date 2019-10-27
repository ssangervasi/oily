import pytest

from . import divisibility_streaks

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
		result = divisibility_streaks.number_of_streaks_in_range(13, 67108864)
		print(result)		
		assert result == 1


class Test_streak:
	@pytest.mark.parametrize(
		'example', [
			{ 'n': 13, 'expected': 4 },
			{ 'n': 120, 'expected': 1 },
		]
	)
	def test_parametrized_examples(self, example):
		assert divisibility_streaks.streak(example['n']) == example['expected']
