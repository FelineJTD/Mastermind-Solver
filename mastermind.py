from ast import Num
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

def guessPegs(exact, similar, num_of_color, set_of_guesses, peg_set, length, tries):
  if (sum(num_of_color) != length and tries <= peg_set):
    print(sum(num_of_color))
    # try to find out which colors make up the solution
    print(str(tries)*length)
    return str(tries)*length

  if (set_of_guesses == []):
    list_of_possible_colors = []
    for i in range(len(num_of_color)):
      for j in range(num_of_color[i]):
        list_of_possible_colors.append(str(i+1))
    set_of_guesses = list(itertools.permutations(list_of_possible_colors, length))
  
  print(set_of_guesses.pop())
  return (str(set_of_guesses.pop()))

def checkFeedback(exact, num_of_color, tries):
  num_of_color[tries-1] += exact




if __name__ == "__main__":
  num_of_pegs = 4
  peg_set = 6

  solution = generatePegs(num_of_pegs, peg_set)
  print(solution)

  exact = 0
  similar = 0
  num_of_guesses = 0
  set_of_guesses = []

  num_of_color = [0 for i in range(peg_set)]
  while(exact != num_of_pegs):
    num_of_guesses += 1
    guess = guessPegs(exact, similar, num_of_color, set_of_guesses, peg_set, num_of_pegs, num_of_guesses)
    exact, similar = checkPegs(list(guess), solution)
    checkFeedback(exact, num_of_color, num_of_guesses)
    print(num_of_color)
    print(f"exact: {exact}")
    print(f"similar: {similar}")
    print(f"number of guesses: {num_of_guesses}")