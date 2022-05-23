from cgi import print_arguments
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

def guessPegs(exact, similar, num_of_color, set_of_guesses, peg_set, length, tries):
  if (sum(num_of_color) != length and tries <= peg_set):
    # try to find out which colors make up the solution
    # print(str(tries)*length)
    return str(tries)*length, set_of_guesses

  if (set_of_guesses == []):
    list_of_possible_colors = []
    for i in range(len(num_of_color)):
      for j in range(num_of_color[i]):
        list_of_possible_colors.append(str(i+1))
    set_of_guesses = list(set(itertools.permutations(list_of_possible_colors, length)))
  
  next_guess = ""
  for i in set_of_guesses.pop():
    next_guess += i
  # print(next_guess)
  return (next_guess, set_of_guesses)

def checkFeedback(exact, num_of_color, tries):
  if (sum(num_of_color) != 4 and tries <= 6):
    num_of_color[tries-1] += exact




if __name__ == "__main__":
  COLORS = '1', '2', '3', '4', '5', '6'#, 'grey', 'white', 'black', 'orange', 'brown', 'mauve', '-gap-'
  HOLES = 4
  worst_case = 0
  total = 0
  num_of_pegs = 4
  peg_set = 6
  all_possible_solutions = list(itertools.product(*itertools.tee(COLORS, HOLES)))
  all_possible_solutions_2 = []
  all_possible_solutions_3 = []
  print(len(all_possible_solutions))
  # e, s = checkPegs(list(i), guess)
  count = 0
  for i in range(len(all_possible_solutions)):
    # print(i)
    e, s = checkPegs(["4","3","5","3"], list(all_possible_solutions[i]))
    # print(e, s)
    if ((e == 0 and s == 3)):
      # print(i)
      count += 1
      all_possible_solutions_2.append(all_possible_solutions[i])
  # print(count)
  # print(all_possible_solutions_2)
  # print(len(all_possible_solutions_2))
  # print(len(all_possible_solutions))
  # print(all_possible_solutions)
  # print(len(all_possible_solutions))
  # print(all_possible_solutions)
  count = 0
  for i in range(len(all_possible_solutions_2)):
    # print(i)
    e, s = checkPegs(["3","5","4","6"], list(all_possible_solutions_2[i]))
    # print(e, s)
    if ((e == 3 and s == 0)):
      # print(i)
      count += 1
      all_possible_solutions_3.append(all_possible_solutions_2[i])
  print(count)
  print(all_possible_solutions_3)
  print(len(all_possible_solutions_3))

  # for i in all_possible_solutions:
  #   e, s = checkPegs(["3","5","4","6"], list(i))
  #   e1, s1 = checkPegs(["4","3","5","3"], list(i))
  #   if (e != 3 or s != 0 or e1 != 0 or s1 != 3):
  #     all_possible_solutions.remove(i)
  
  # print(len(all_possible_solutions))
  # print(all_possible_solutions)
  # # total_tries = len(all_possible_solutions)
  # # timeStart = perf_counter()

  # # # guess, set_of_guesses = guessPegs(exact, similar, num_of_color, set_of_guesses, peg_set, num_of_pegs, num_of_guesses)
  # # while(all_possible_solutions != []):
  # #   # list_of_prev_guesses = {}
  # #   num_of_pegs = 4
  # #   peg_set = 6

  # #   solution = list(all_possible_solutions.pop())
  # #   # print(solution)

  #   exact = 0
  #   similar = 0
  #   num_of_guesses = 0
  #   set_of_guesses = []
  #   guess = ""

  #   num_of_color = [0 for i in range(peg_set)]
  #   while(exact != num_of_pegs):
  #     num_of_guesses += 1
  #     guess, set_of_guesses = guessPegs(exact, similar, num_of_color, set_of_guesses, peg_set, num_of_pegs, num_of_guesses)
  #     exact, similar = checkPegs(list(guess), solution)
  #     checkFeedback(exact, num_of_color, num_of_guesses)
  #     # list_of_prev_guesses[guess] = exact, similar
  #     # checkFeedback(exact, num_of_color, num_of_guesses)

  #   if (num_of_guesses > worst_case):
  #     worst_case = num_of_guesses
  #   total += num_of_guesses

  #   print(f"{num_of_guesses} guess(es) for {solution}")
  # timerEnd = perf_counter()
  # cyan = "\033[96m"
  # green = "\033[92m"
  # b = "\033[1m"
  # print(green, b)
  # print(f"Total time to solve all possible solutions: {(timerEnd-timeStart):0.4f} seconds")
  # print(f"Average guesses: {total/total_tries:.4f}")
  # print(f"Worst case scenario: {worst_case}")