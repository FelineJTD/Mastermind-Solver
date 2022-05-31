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

def guessPegs(list_of_prev_guesses):
  if (len(list_of_prev_guesses) == 0): # first guess
    guess = generatePegs()
    print ("".join(guess))
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
    print(guess)
    return guess

def checkFeedback(exact, num_of_color, tries):
  if (sum(num_of_color) != 4 and tries <= 6):
    num_of_color[tries-1] += exact



if __name__ == "__main__":
  list_of_prev_guesses = {}
  num_of_pegs = 4
  peg_set = 6

  solution = generatePegs(num_of_pegs, peg_set)
  print("\033[91mSolution code: ", end="")
  for i in range(4):
    print(solution[i], end="")
  print("\033[0m")
  print("-------------------------------------")

  exact = 0
  similar = 0
  num_of_guesses = 0
  set_of_guesses = []
  guess = ""

  num_of_color = [0 for i in range(peg_set)]
  while(exact != num_of_pegs):
    num_of_guesses += 1
    print(f"ATTEMPT #{num_of_guesses}: ", end="")
    guess = guessPegs(list_of_prev_guesses)
    exact, similar = checkPegs(list(guess), solution)
    list_of_prev_guesses[guess] = exact, similar
    print(f"Black pegs (exact matches): {exact}")
    print(f"White pegs (close matches): {similar}")
    print("-------------------------------------")
  cyan = "\033[96m"
  green = "\033[92m"
  b = "\033[1m"
  print(f"{green}{b}Code broken. Total number of guesses: {num_of_guesses}")