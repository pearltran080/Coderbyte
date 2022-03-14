def ArrayChallenge(arr):

  # code goes here
  lstOf2s = []
  for i in range(len(arr)):
    if arr[i] == 2:
      lstOf2s.append(i)
    if arr[i] == 1:
      indexOf1 = i

  if len(lstOf2s) == 0:
    return 0

  closest = None
  for two in lstOf2s:
    if closest == None:
      closest = abs(two-indexOf1)
    if abs(two-indexOf1) < closest:
      closest = abs(two-indexOf1)

  return closest

# keep this function call here 
print(ArrayChallenge(input()))

'''
Left or right, return the distance between 1 and the closest 2 in an array of 1, 0s, and 2s
Score: 10/10
'''