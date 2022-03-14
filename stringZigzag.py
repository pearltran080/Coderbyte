def StringChallenge(strArr):

  # code goes here
  rows = int(strArr[1])
  rowsLst = []
  for i in range(rows):
    rowsLst.append([])

  # true = up, false = down
  direction = False
  currentRow = 0

  for letter in strArr[0]:
    if currentRow == rows-1:
      direction = True
    elif currentRow == 0:
      direction = False

    if direction == False:
      rowsLst[currentRow].append(letter)
      currentRow += 1
    if direction == True:
      rowsLst[currentRow].append(letter)
      currentRow -= 1


  result = ''
  for r in rowsLst:
    for l in range(len(r)):
      result += r[l]

  return result

# keep this function call here 
print(StringChallenge(input()))

'''
Zigzag with strArr[1] amount of rows. Return sequence of letters traversing rows from left to right, top to bottom
Score: 9/10

1. For input ["aeettym", "1"] the output was incorrect. The correct output is aeettym

Ex: ["pearleen", "3"]
p   l
 e r e n
  a   e

output: plerenae
'''