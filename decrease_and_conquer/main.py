import itertools
import random

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
    if guess[i] == pegs_copy[i]:
      exact += 1
      guess[i] = "-1"
      pegs_copy[i] = "0"
  for i in range(4):
    for j in range(4):
      if guess[i] == pegs_copy[j]:
        similar += 1
        pegs_copy[j] = "0"
        break
  return exact, similar

def guessPegs(list_of_prev_guesses, prev_guess, exact, similar, tries):
  # print(list_of_prev_guesses)
  if (tries == 1):
    print("1122")
    return "1122"
  else:
    e = -1
    s = -1
    guess = "0000"
    accepted = False
    # print(list_of_prev_guesses)
    while (not(accepted)):
      guess = generatePegs()
      accepted = True
      for i in list_of_prev_guesses.keys():
        e, s = checkPegs(list(i), guess)
        if (e != list_of_prev_guesses[i][0] or s != list_of_prev_guesses[i][1]):
          accepted = False
          break

    guess = "".join(guess)
    # print(e, s)
    # print(list_of_prev_guesses[i][0], list_of_prev_guesses[i][1])
    print(guess)
    return guess
  # if (sum(num_of_color) != length and tries <= peg_set):
  #   # try to find out which colors make up the solution
  #   print(str(tries)*length)
  #   return str(tries)*length, set_of_guesses

  # if (set_of_guesses == []):
  #   list_of_possible_colors = []
  #   for i in range(len(num_of_color)):
  #     for j in range(num_of_color[i]):
  #       list_of_possible_colors.append(str(i+1))
  #   set_of_guesses = list(itertools.permutations(list_of_possible_colors, length))
  
  # next_guess = ""
  # for i in set_of_guesses.pop():
  #   next_guess += i
  # print(next_guess)
  # return (next_guess, set_of_guesses)

def checkFeedback(exact, num_of_color, tries):
  if (sum(num_of_color) != 4 and tries <= 6):
    num_of_color[tries-1] += exact




if __name__ == "__main__":
  list_of_prev_guesses = {}
  num_of_pegs = 4
  peg_set = 6

  solution = generatePegs(num_of_pegs, peg_set)
  print(solution)

  exact = 0
  similar = 0
  num_of_guesses = 0
  set_of_guesses = []
  guess = ""

  num_of_color = [0 for i in range(peg_set)]
  while(exact != num_of_pegs):
    num_of_guesses += 1
    print("GUESS: ", end="")
    guess = guessPegs(list_of_prev_guesses, guess, exact, similar, num_of_guesses)
    exact, similar = checkPegs(list(guess), solution)
    list_of_prev_guesses[guess] = exact, similar
    # checkFeedback(exact, num_of_color, num_of_guesses)
    print(f"exact: {exact}")
    print(f"similar: {similar}")
    print(f"number of guesses: {num_of_guesses}")
    print("-------------------------------------")