keypadCode = [1, 1, 2, 6]

keyCodeSize = len(keypadCode)
possibleCodes = 10 ** keyCodeSize
countOfCodesTried = 0
codesTried = [False] * possibleCodes

def generateNextGuess(prevGuess, depth):
    if depth > keyCodeSize:
      print('Depth is too large')
      return

    newGuess = [prevGuess[1], prevGuess[2], prevGuess[3]]
    newGuess.append(0)
    print('The new guess is:', newGuess)
    for i in range(10 ** depth):
        iDigits = numberToDigits(i)
        for d in range(1, depth + 1):
          newGuess[keyCodeSize - d] = iDigits[keyCodeSize - d]
        
        newGuessIndex = codeToIndex(newGuess)
        if codesTried[newGuessIndex] == False:
          return newGuess

    print("At the end, the newGuess is: ", newGuess)
    return generateNextGuess([prevGuess[1], prevGuess[2], prevGuess[3], 0] , depth + 1)


def isGuessAMatch(guess):
    return codeToIndex(guess) == codeToIndex(keypadCode)

def recordCodeTries(ct):
    code = codeToIndex(ct)
    print("Code is", code)
    codesTried[code] = True


def codeToIndex(ct):
    index = 0
    for i in range(keyCodeSize):
      index += ct[i] * (10 ** (keyCodeSize - i - 1))
    return index

def numberToDigits(num):
  digits = [0] * keyCodeSize
  for i in range(keyCodeSize):
    digits[keyCodeSize - i - 1] = (num % (10 ** (i + 1))) // (10 ** i)
  return digits

currentCodeGuess = [0] * keyCodeSize

while (countOfCodesTried < possibleCodes):
    print("Trying code: ", currentCodeGuess)
    if isGuessAMatch(currentCodeGuess):
        print('You did it in', countOfCodesTried ,'tries')
        break
    recordCodeTries(currentCodeGuess)
    countOfCodesTried += 1
    currentCodeGuess = generateNextGuess(currentCodeGuess, 1)
