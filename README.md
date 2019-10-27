# oily
Project Euler solutions

## Setup

**1:** Clone me! `git@github.com:ssangervasi/oily.git`

**2:** Install Python 3.7 and [Pipenv](https://pipenv.readthedocs.io/en/latest/install/#make-sure-you-ve-got-python-pip).
For example, with homebrew:

```sh
brew install pipenv
```

**3:** Use Pipenv in the root directory:
```sh
pipenv install
```

Use `--dev` if you want to run the tests:
```sh
pipenv install --dev
```

## Problem #601 [🔗](https://projecteuler.net/problem=601)

Running the module's main with pipenv:

```sh
pipenv run python -m oily.divisibility_streaks
```

To get some extra debugging information:
```sh
pipenv run python -m oily.divisibility_streaks --info
pipenv run python -m oily.divisibility_streaks --debug
```

### Running the tests

```sh
pipenv run pytest oily/divisibility_streaks_test.py
```
