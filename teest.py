import itertools

set_of_guesses = list(set(itertools.permutations("1432", 4)))
print(set_of_guesses, len(set_of_guesses))