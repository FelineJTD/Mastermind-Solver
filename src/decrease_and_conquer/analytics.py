import itertools
import random
from time import perf_counter

def generatePegs(num_of_pegs=4, peg_set=6):
  pegs = []
  for i in range(num_of_pegs):
    pegs.append(str(random.randint(1,peg_set)))
  return pegs

def checkPegs(guess, pegs):
  exact = 0
  similar = 0
  pegs_copy = pegs.copy()
  for i in range(4):
    if guess[i] == str(pegs_copy[i]):
      exact += 1
      guess[i] = "-1"
      pegs_copy[i] = "0"
  for i in range(4):
    for j in range(4):
      if guess[i] == str(pegs_copy[j]):
        similar += 1
        pegs_copy[j] = "0"
        break
  return exact, similar

def guessPegs(list_of_prev_guesses):
  if (len(list_of_prev_guesses) == 0): # first guess
    guess = generatePegs()
    return "".join(guess)
  else:
    e = -1
    s = -1
    guess = "0000"
    accepted = False
    while (not(accepted)):
      guess = generatePegs()
      accepted = True
      for i in list_of_prev_guesses.keys():
        e, s = checkPegs(list(i), guess)
        if (e != list_of_prev_guesses[i][0] or s != list_of_prev_guesses[i][1]):
          accepted = False
          break

    guess = "".join(guess)
    return guess

def checkFeedback(exact, num_of_color, tries):
  if (sum(num_of_color) != 4 and tries <= 6):
    num_of_color[tries-1] += exact

COLORS = '1', '2', '3', '4', '5', '6'
HOLES = 4

if __name__ == "__main__":
  worst_case = 0
  total = 0
  all_possible_solutions = list(itertools.product(*itertools.tee(COLORS, HOLES)))
  total_tries = len(all_possible_solutions)
  timeStart = perf_counter()

  while(all_possible_solutions != []):

    list_of_prev_guesses = {}
    num_of_pegs = 4
    peg_set = 6

    solution = list(all_possible_solutions.pop())

    exact = 0
    similar = 0
    num_of_guesses = 0
    set_of_guesses = []
    guess = ""

    num_of_color = [0 for i in range(peg_set)]
    while(exact != num_of_pegs):
      num_of_guesses += 1
      guess = guessPegs(list_of_prev_guesses)
      exact, similar = checkPegs(list(guess), solution)
      list_of_prev_guesses[guess] = exact, similar

    if (num_of_guesses > worst_case):
      worst_case = num_of_guesses
    total += num_of_guesses

    print(f"{num_of_guesses} guess(es) for {solution}")
  timerEnd = perf_counter()
  cyan = "\033[96m"
  green = "\033[92m"
  b = "\033[1m"
  print(green, b)
  print(f"Total time to solve all possible solutions: {(timerEnd-timeStart):0.4f} seconds")
  print(f"Average guesses: {total/total_tries:.4f}")
  print(f"Worst case scenario: {worst_case}")