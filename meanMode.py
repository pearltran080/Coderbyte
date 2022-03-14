def ArrayChallenge(arr):

  # code goes here
  sum = 0
  d = {}
  for i in arr:
    sum += i
    if i not in d:
      d[i] = 1
    else:
      d[i] += 1
  

  #mode = keys[values.index(max(keys))]
  maxKey = None
  maxValue = None
  for key, value in d.items():
    if maxValue == None:
      maxKey = key
      maxValue = value
    elif value > maxValue:
      maxKey = key
      maxValue = value

  mode = maxKey
  mean = sum / len(arr)

  if mode == mean:
    return 1
  else:
    return 0


# keep this function call here 
print(ArrayChallenge(input()))

'''
Given a list of integers, return 1 if the mode and mean are the same. 0 otherwise
Score: 10/10
'''