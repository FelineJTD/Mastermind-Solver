from itertools import product, tee
from random import choice

COLORS = 'red ', 'green', 'blue', 'yellow', 'purple', 'pink'#, 'grey', 'white', 'black', 'orange', 'brown', 'mauve', '-gap-'
HOLES = 4

def random_solution():
    """Generate a random solution."""
    return tuple(choice(COLORS) for i in range(HOLES))

def all_solutions():
    """Generate all possible solutions."""
    for solution in product(*tee(COLORS, HOLES)):
        yield solution

def filter_matching_result(solution_space, guess, result):
    """Filter solutions for matches that produce a specific result for a guess."""
    for solution in solution_space:
        if score(guess, solution) == result:
            yield solution

def score(actual, guess):
    """Calculate score of guess against actual."""
    result = []
    #Black pin for every color at right position
    actual_list = list(actual)
    guess_list = list(guess)
    black_positions = [number for number, pair in enumerate(zip(actual_list, guess_list)) if pair[0] == pair[1]]
    for number in reversed(black_positions):
        del actual_list[number]
        del guess_list[number]
        result.append('black')
    #White pin for every color at wrong position
    for color in guess_list:
        if color in actual_list:
            #Remove the match so we can't score it again for duplicate colors
            actual_list.remove(color)
            result.append('white')
    #Return a tuple, which is suitable as a dictionary key
    return tuple(result)

def minimal_eliminated(solution_space, solution):
    """For solution calculate how many possibilities from S would be eliminated for each possible colored/white score.
    The score of the guess is the least of such values."""
    result_counter = {}
    for option in solution_space:
        result = score(solution, option)
        if result not in result_counter.keys():
            result_counter[result] = 1
        else:
            result_counter[result] += 1
    return len(solution_space) - max(result_counter.values())

def best_move(solution_space):
    """Determine the best move in the solution space, being the one that restricts the number of hits the most."""
    elim_for_solution = dict((minimal_eliminated(solution_space, solution), solution) for solution in solution_space)
    max_elimintated = max(elim_for_solution.keys())
    return elim_for_solution[max_elimintated]

def main(actual = None):
    """Solve a game of mastermind."""
    #Generate random 'hidden' sequence if actual is None
    if actual == None:
        actual = random_solution()

    #Start the game of by choosing n unique colors
    current_guess = COLORS[:HOLES]

    #Initialize solution space to all solutions
    solution_space = all_solutions()
    guesses = 1
    while True:
        #Calculate current score
        current_score = score(actual, current_guess)
        #print '\t'.join(current_guess), '\t->\t', '\t'.join(current_score)
        if current_score == tuple(['black'] * HOLES):
            print (guesses, 'guesses for\t', '\t'.join(actual))
            return guesses

        #Restrict solution space to exactly those hits that have current_score against current_guess
        solution_space = tuple(filter_matching_result(solution_space, current_guess, current_score))

        #Pick the candidate that will limit the search space most
        current_guess = best_move(solution_space)
        guesses += 1

if __name__ == '__main__':
    print (max(main(sol) for sol in all_solutions()))